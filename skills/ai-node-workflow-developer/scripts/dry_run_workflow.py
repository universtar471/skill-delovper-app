#!/usr/bin/env python3
"""Static node graph dry run. NEVER executes model/API/MCP/CLI or bills money."""
import argparse
import json
from collections import Counter, deque
from pathlib import Path


def validate(graph, registry, allow_mock=False, max_budget=None):
    errors=[]
    warnings=[]
    node_types=registry.get('nodeTypes',{})
    if graph.get('schemaVersion')!=1 or registry.get('schemaVersion')!=1:
        errors.append('Unsupported graph/registry schemaVersion (expected 1)')
    nodes=graph.get('nodes',[])
    edges=graph.get('edges',[])
    if not isinstance(nodes,list) or not isinstance(edges,list) or not isinstance(node_types,dict):
        return {'errors':['nodes, edges and nodeTypes must be list/list/object'],'warnings':[],'order':[],'estimatedCostUsd':None,'static_only':True,'live_execution':False}
    node_by_id={}
    indegree={}
    forward={}
    total_cost=0.0
    for n in nodes:
        if not isinstance(n,dict):errors.append('Non-object node');continue
        nid=n.get('id')
        if not isinstance(nid,str) or not nid.strip():errors.append('Node missing nonempty id');continue
        if nid in node_by_id:errors.append(f'Duplicate node id: {nid}');continue
        node_by_id[nid]=n
        indegree[nid]=0
        forward[nid]=[]
        t=n.get('type')
        desc=node_types.get(t)
        if desc is None:
            errors.append(f'{nid}: unknown node type {t}')
            continue
        if n.get('typeVersion') != desc.get('version'):
            errors.append(f'{nid}: type version mismatch')
        for key in desc.get('requiredParams',[]):
            if not str(n.get('params',{}).get(key,'')).strip():
                errors.append(f'{nid}: missing required parameter {key}')
        status=desc.get('capabilityStatus','LOCAL_VERIFIED')
        if status not in {'LOCAL_VERIFIED','LIVE_E2E_VERIFIED'}:
            if not (allow_mock and status=='MOCK'):
                errors.append(f'{nid}: capability not verified ({status})')
            else:warnings.append(f'{nid}: MOCK capability; not release-ready')
        if desc.get('requiresModel'):
            model=n.get('modelRef')
            chosen=desc.get('models',{}).get(model)
            if not chosen:
                errors.append(f'{nid}: absent/unregistered model')
            else:
                st=chosen.get('status')
                if st!='LIVE_E2E_VERIFIED':
                    if not (allow_mock and st=='MOCK'):
                        errors.append(f'{nid}: model not verified ({st})')
                    else:warnings.append(f'{nid}: MOCK model; not release-ready')
        unit_cost=desc.get('estimatedCostUsd')
        if unit_cost is None:
            warnings.append(f'{nid}: unknown cost estimate')
        elif isinstance(unit_cost,(float,int)) and unit_cost >= 0:
            copies=n.get('params',{}).get('count',1)
            if not isinstance(copies,int) or isinstance(copies,bool) or copies <= 0 or copies > 10000:
                errors.append(f'{nid}: invalid count')
            else:total_cost+=unit_cost*copies
        else:errors.append(f'{nid}: invalid cost estimate')
        if desc.get('isMediaInput'):
            refs=n.get('assetRefs')
            if not refs:
                errors.append(f'{nid}: media references not provided')
            elif not isinstance(refs,list):
                errors.append(f'{nid}: assetRefs must be a list')
            elif any('EXAMPLE' in str(ref).upper() for ref in refs):
                if allow_mock:
                    warnings.append(f'{nid}: placeholder media reference; fixture only')
                else:
                    errors.append(f'{nid}: placeholder media reference not allowed for release')
            else:
                warnings.append(f'{nid}: media references not verified by a file/asset store in static dry run')
    seen_edges=set()
    receiving=Counter()
    for index,e in enumerate(edges):
        if not isinstance(e,dict):errors.append(f'edge[{index}]: not an object');continue
        eid=e.get('id',f'edge[{index}]')
        if eid in seen_edges:errors.append(f'duplicate edge id: {eid}')
        seen_edges.add(eid)
        src,dst=e.get('source'),e.get('target')
        if src not in node_by_id or dst not in node_by_id:
            errors.append(f'{eid}: unknown endpoint')
            continue
        if src==dst:
            errors.append(f'{eid}: self cycle')
        sn,tn=node_by_id[src],node_by_id[dst]
        sd=node_types.get(sn.get('type'))
        td=node_types.get(tn.get('type'))
        if not sd or not td:continue
        op=sd.get('outputs',{}).get(e.get('sourcePort'))
        ip=td.get('inputs',{}).get(e.get('targetPort'))
        if not op or not ip:
            errors.append(f'{eid}: unknown input or output port')
            continue
        if op.get('type') != ip.get('type'):
            errors.append(f'{eid}: incompatible port types {op.get("type")} -> {ip.get("type")}')
        receiving[(dst,e.get('targetPort'))]+=1
        forward[src].append(dst)
        indegree[dst]+=1
    for nid,n in node_by_id.items():
        desc=node_types.get(n.get('type'))
        if not desc:continue
        for pname,p in desc.get('inputs',{}).items():
            number=receiving[(nid,pname)]
            if p.get('required') and number==0:
                errors.append(f'{nid}: unconnected required input {pname}')
            max_connections=p.get('maxConnections',1)
            if max_connections is not None and number>max_connections:
                errors.append(f'{nid}: too many connections to {pname}')
    queue=deque(sorted(n for n,degree in indegree.items() if degree==0))
    order=[]
    while queue:
        nid=queue.popleft()
        order.append(nid)
        for dst in forward[nid]:
            indegree[dst]-=1
            if indegree[dst]==0:queue.append(dst)
    if len(order)!=len(node_by_id):errors.append('Cycle detected: graph must be DAG unless explicit loop engine exists')
    if not node_by_id:errors.append('Empty graph')
    if max_budget is not None and total_cost>max_budget:
        errors.append(f'Estimated cost {total_cost:.4f} exceeds budget {max_budget:.4f}')
    warnings.append('Cost is an estimate from local registry, not a provider quotation')
    return {'nodes':len(nodes),'edges':len(edges),'errors':errors,'warnings':warnings,'order':order,'estimatedCostUsd':round(total_cost,6),'static_only':True,'live_execution':False,'allow_mock':allow_mock}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--workflow',required=True,type=Path)
    ap.add_argument('--registry',required=True,type=Path)
    ap.add_argument('--allow-mock',action='store_true',help='Only for fixture tests; does not certify providers')
    ap.add_argument('--max-budget',type=float,default=None)
    ap.add_argument('--format',choices=['text','json'],default='text')
    a=ap.parse_args()
    try:
        graph=json.loads(a.workflow.read_text(encoding='utf-8'))
        registry=json.loads(a.registry.read_text(encoding='utf-8'))
        report=validate(graph,registry,a.allow_mock,a.max_budget)
    except (OSError,ValueError,TypeError) as exc:ap.error(str(exc))
    if a.format=='json':print(json.dumps(report,indent=2))
    else:
        print(f"DRY RUN: {report['nodes']} nodes, {report['edges']} edges; order: {report['order']}")
        for issue in report['errors']:print('BLOCK:',issue)
        for warning in report['warnings']:print('NOTE:',warning)
        print('No live provider/tool call made. No money spent.')
    raise SystemExit(1 if report['errors'] else 0)
if __name__=='__main__':main()

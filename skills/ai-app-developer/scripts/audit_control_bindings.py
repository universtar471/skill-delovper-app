#!/usr/bin/env python3
"""Static consistency audit of control-to-capability mappings. Not a runtime test."""
import argparse
import csv
import json
from pathlib import Path

def load(path):
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))

def audit(project):
    base=project/'docs' if (project/'docs').is_dir() else project
    reg=load(base/'CAPABILITY_REGISTRY.csv')
    binds=load(base/'CONTROL_BINDINGS.csv')
    tests=load(base/'CONNECTION_TEST_MATRIX.csv')
    caps={r['capability_id'] for r in reg if r.get('capability_id')}
    test_ids={r['test_id'] for r in tests if r.get('test_id')}
    issues=[]
    for r in binds:
        cid=r.get('control_id','(missing)')
        cap=r.get('capability_id','')
        if not cap or cap not in caps: issues.append(f'{cid}: unknown capability {cap}')
        if not r.get('handler') or r.get('handler')=='UNVERIFIED': issues.append(f'{cid}: missing handler')
        if not r.get('adapter') or r.get('adapter')=='UNVERIFIED': issues.append(f'{cid}: missing adapter')
        if r.get('enabled_state','').lower()=='enabled':
            if r.get('mock_only','').lower()=='true': issues.append(f'{cid}: enabled with mock-only integration')
            if r.get('implementation_status')!='E2E_VERIFIED': issues.append(f'{cid}: enabled without E2E_VERIFIED status')
            tid=r.get('e2e_test_id','')
            if not tid or tid not in test_ids: issues.append(f'{cid}: enabled without matching E2E test ID')
            if not r.get('evidence_path'): issues.append(f'{cid}: enabled without evidence path')
    return {'controls':len(binds),'capabilities':len(caps),'tests':len(tests),'issues':issues,'static_audit_only':True}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',type=Path,required=True)
    ap.add_argument('--format',choices=['text','json'],default='text')
    args=ap.parse_args()
    try: data=audit(args.project)
    except (FileNotFoundError,KeyError,ValueError) as error: ap.error(str(error))
    if args.format=='json': print(json.dumps(data,ensure_ascii=False,indent=2))
    else:
        print(f"STATIC BINDINGS: {data['controls']} controls, {data['capabilities']} capabilities, {data['tests']} tests")
        for issue in data['issues']: print('BLOCK:',issue)
        print('NO RUNTIME OR LIVE SERVICE TESTS PERFORMED')
    raise SystemExit(1 if data['issues'] else 0)
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Static run manifest audit. Evidence must be independently reviewed."""
import argparse,json
from pathlib import Path
from audit_acceptance_gates import evidence_file


def audit(path, project):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    errs=[]
    if data.get('status')!='SUCCEEDED':errs.append('run status is not SUCCEEDED')
    if not data.get('runId'):errs.append('missing runId')
    if not data.get('workflowHash'):errs.append('missing workflowHash')
    if not data.get('startedAt') or not data.get('finishedAt'):errs.append('missing timestamps')
    nodes=data.get('nodes')
    if not isinstance(nodes,list) or not nodes:errs.append('missing node results')
    else:
        for n in nodes:
            if n.get('status')!='SUCCEEDED':errs.append('node not succeeded: '+str(n.get('nodeId')))
            if not n.get('nodeId'):errs.append('node id missing')
            if not n.get('adapterVersion'):errs.append('node adapter version missing')
    for out in data.get('outputs',[]):
        path=out.get('filePath')
        if not evidence_file(Path(project).resolve(),path):errs.append('missing output artifact: '+str(path))
        if not out.get('sha256'):errs.append('output hash missing: '+str(path))
    if not data.get('outputs'):errs.append('no output artifacts')
    if not evidence_file(Path(project).resolve(),data.get('logEvidencePath')):errs.append('missing run log evidence')
    if data.get('dryRun') is True or data.get('mockOnly') is True:errs.append('mock or dry run cannot qualify as verified success')
    return {'errors':errs,'static_only':True,'live_run_verified':False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True)
    p.add_argument('--project',type=Path,required=True)
    a=p.parse_args()
    try:r=audit(a.manifest,a.project)
    except (OSError,ValueError,TypeError) as e:p.error(str(e))
    for e in r['errors']:print('BLOCK:',e)
    print('Manifest consistency only; human must inspect actual execution proof.')
    raise SystemExit(1 if r['errors'] else 0)
if __name__=='__main__':main()

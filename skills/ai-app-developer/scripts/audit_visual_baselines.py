#!/usr/bin/env python3
"""Inspect visual baseline review completeness; does not compare pixels."""
import argparse,csv,json
from pathlib import Path
from audit_acceptance_gates import root_dir,evidence_file

COLS=('Screen_ID','Viewport','Zoom','Platform','Priority','Owner_Approval','Waiver_ID','Baseline_Path','Actual_Path','Review_Status','Reviewer','Diff_Evidence','Notes')

def audit(project,require_final=False):
    root,docs=root_dir(project)
    with (docs/'VISUAL_BASELINES.csv').open(encoding='utf-8-sig',newline='') as f:
        rdr=csv.DictReader(f)
        errors=['missing column '+x for x in COLS if x not in (rdr.fieldnames or [])]
        rows=list(rdr)
    if not rows:errors.append('no screenshots planned')
    for n,r in enumerate(rows,2):
        label=(r.get('Screen_ID') or f'row-{n}')+' '+(r.get('Viewport') or '')
        status=(r.get('Review_Status') or '').strip().upper()
        if not (r.get('Viewport') or '').strip() or not (r.get('Platform') or '').strip():
            errors.append(label+': missing platform/viewport')
        if status=='PASS':
            for field in ('Baseline_Path','Actual_Path','Diff_Evidence'):
                if not evidence_file(root,r.get(field)):
                    errors.append(label+': PASS but '+field+' missing')
            if not (r.get('Reviewer') or '').strip():errors.append(label+': PASS but reviewer absent')
        elif require_final and status!='WAIVED':
            errors.append(label+': visual review not closed')
        if status=='WAIVED':
            if (r.get('Priority') or 'P0').upper()=='P0': errors.append(label+': P0 visual waiver prohibited')
            if not (r.get('Notes') or '').strip(): errors.append(label+': waiver has no documented reason')
            if (r.get('Owner_Approval') or '').upper() not in {'YES','APPROVED'}: errors.append(label+': waiver missing owner approval')
            if not (r.get('Waiver_ID') or '').strip(): errors.append(label+': waiver missing ID')
    return {'screenshots':len(rows),'errors':errors,'static_only':True,'pixel_comparison_performed':False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project',required=True,type=Path)
    p.add_argument('--require-final',action='store_true')
    p.add_argument('--format',choices=['text','json'],default='text')
    a=p.parse_args()
    try:r=audit(a.project,a.require_final)
    except (OSError,ValueError,KeyError) as e:p.error(str(e))
    if a.format=='json':print(json.dumps(r,indent=2))
    else:
        print('Visual review rows:',r['screenshots'])
        for e in r['errors']:print('BLOCK:',e)
        print('No screenshot capture or pixel diff performed.')
    raise SystemExit(1 if r['errors'] else 0)
if __name__=='__main__':main()

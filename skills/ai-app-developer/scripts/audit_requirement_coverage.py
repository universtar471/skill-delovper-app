#!/usr/bin/env python3
"""Check frozen requirement coverage records; not proof of behavior."""
import argparse,csv,json
from pathlib import Path
from audit_acceptance_gates import evidence_file,root_dir

COLS=('Requirement_ID','Priority','Approved','Feature_ID','UI_Control_ID','Implementation_File','Test_ID','Test_Status','Test_Evidence','Deviation_ID','Notes')

def audit(project,require_final=False):
    root,docs=root_dir(project)
    with (docs/'REQUIREMENT_COVERAGE.csv').open(encoding='utf-8-sig',newline='') as f:
        rdr=csv.DictReader(f)
        missing=[x for x in COLS if x not in (rdr.fieldnames or [])]
        rows=list(rdr)
    errors=['missing column '+x for x in missing]
    if not rows: errors.append('no requirements')
    seen=set()
    for n,row in enumerate(rows,2):
        rid=(row.get('Requirement_ID') or '').strip()
        pr=(row.get('Priority') or '').strip().upper()
        st=(row.get('Test_Status') or '').strip().upper()
        if not rid or rid in seen: errors.append(f'row {n}: duplicate/missing Requirement_ID')
        seen.add(rid)
        if pr not in {'P0','P1','P2'}: errors.append(f'{rid}: invalid priority')
        if not (row.get('Feature_ID') or '').strip(): errors.append(f'{rid}: no feature mapping')
        if not (row.get('Test_ID') or '').strip(): errors.append(f'{rid}: no test ID')
        if st=='PASS':
            if not evidence_file(root,row.get('Test_Evidence')): errors.append(f'{rid}: PASS but test evidence missing')
            if not evidence_file(root,row.get('Implementation_File')): errors.append(f'{rid}: PASS but code file missing')
        if require_final and pr in {'P0','P1'}:
            if (row.get('Approved') or '').upper() not in {'YES','APPROVED'}:
                errors.append(f'{rid}: not approved')
            if st!='PASS': errors.append(f'{rid}: required test not PASS ({st})')
    return {'requirements':len(rows),'errors':errors,'static_only':True,'runtime_tested':False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project',type=Path,required=True)
    p.add_argument('--require-final',action='store_true')
    p.add_argument('--format',choices=['text','json'],default='text')
    a=p.parse_args()
    try: r=audit(a.project,a.require_final)
    except (OSError,ValueError,KeyError) as e:p.error(str(e))
    if a.format=='json':print(json.dumps(r,indent=2))
    else:
        print('Requirements:',r['requirements'])
        for e in r['errors']:print('BLOCK:',e)
        print('Static file audit only: no application tests run.')
    raise SystemExit(1 if r['errors'] else 0)
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Audit gate records and evidence pointers; never claims runtime tests ran."""
import argparse
import csv
import json
from pathlib import Path

REQUIRED = ('Gate_ID','Requirement_ID','Priority','Description','Status','Evidence_Path','Validation_Command','Verified_At','Owner_Approval','Waiver_ID','Notes')
FINAL = {'PASS', 'WAIVED'}
PENDING = {'NOT_STARTED','IN_PROGRESS','BLOCKED','FAIL'}


def root_dir(project):
    project = Path(project).resolve()
    return project, project/'docs' if (project/'docs').is_dir() else project


def evidence_file(project, value):
    value = (value or '').strip()
    if not value or value.lower() in {'tbd','none','n/a','pending','not_run'}:
        return False
    if Path(value).is_absolute():
        return False
    path = (project / value).resolve()
    try:
        path.relative_to(project)
    except ValueError:
        return False
    return path.is_file() and path.stat().st_size > 0


def audit(project, require_final=False):
    root, docs = root_dir(project)
    path = docs/'ACCEPTANCE_GATES.csv'
    with path.open(newline='',encoding='utf-8-sig') as stream:
        rdr = csv.DictReader(stream)
        fields = rdr.fieldnames or []
        rows = list(rdr)
    errors = ['missing column '+x for x in REQUIRED if x not in fields]
    if not rows: errors.append('no gate rows')
    seen = set()
    for n,row in enumerate(rows,2):
        gid=(row.get('Gate_ID') or '').strip()
        if not gid or gid in seen: errors.append(f'row {n}: missing/duplicate Gate_ID')
        seen.add(gid)
        status=(row.get('Status') or '').strip().upper()
        priority=(row.get('Priority') or '').strip().upper()
        if priority not in {'P0','P1','P2'}: errors.append(f'{gid}: invalid priority')
        if status not in FINAL | PENDING: errors.append(f'{gid}: invalid status {status}')
        if status == 'PASS':
            if not evidence_file(root,row.get('Evidence_Path')):
                errors.append(f'{gid}: PASS without local nonempty evidence file')
            if not (row.get('Verified_At') or '').strip():
                errors.append(f'{gid}: PASS without verification time')
            if gid in {'G0','G1','G6'} and (row.get('Owner_Approval') or '').upper() not in {'YES','APPROVED'}:
                errors.append(f'{gid}: owner approval missing')
        if status=='WAIVED':
            if priority=='P0': errors.append(f'{gid}: P0 waiver prohibited')
            if not (row.get('Waiver_ID') or '').strip(): errors.append(f'{gid}: missing waiver id')
            if (row.get('Owner_Approval') or '').upper() not in {'YES','APPROVED'}:
                errors.append(f'{gid}: unapproved waiver')
        if require_final and priority in {'P0','P1'} and status not in FINAL:
            errors.append(f'{gid}: {priority} not closed ({status})')
    return {'rows':len(rows),'errors':errors,'static_only':True,'runtime_tested':False}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',required=True,type=Path)
    ap.add_argument('--require-final',action='store_true')
    ap.add_argument('--format',choices=['json','text'],default='text')
    a=ap.parse_args()
    try: report=audit(a.project,a.require_final)
    except (OSError,ValueError,KeyError) as e: ap.error(str(e))
    if a.format=='json': print(json.dumps(report,indent=2))
    else:
        print('Static acceptance audit: rows='+str(report['rows']))
        for x in report['errors']:print('BLOCK:',x)
        print('Runtime/API/build/screenshot execution: NOT PERFORMED')
    raise SystemExit(1 if report['errors'] else 0)
if __name__=='__main__': main()

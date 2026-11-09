#!/usr/bin/env python3
"""Validate project documentation readiness; does NOT run or certify the application."""
import argparse
import json
import re
from pathlib import Path

FILES=['PROJECT_BRIEF.md','SPEC.md','ARCHITECTURE.md','TASKS.md','TEST_REPORT.md','PROGRESS.md']
PLACEHOLDERS=('chưa chạy','chưa xác minh','tbd','[điền','[1 câu]')

def check(project):
    base=project/'docs' if (project/'docs').is_dir() else project
    checks=[]
    for name in FILES:
        path=base/name
        exists=path.is_file()
        data=path.read_text(encoding='utf-8') if exists else ''
        meaningful=exists and len(data.strip())>=80
        checks.append({'name':name,'exists':exists,'substantive':bool(meaningful)})
    report=base/'TEST_REPORT.md'
    txt=report.read_text(encoding='utf-8') if report.is_file() else ''
    # Documentation is not test evidence: only literal report rows with PASS markers are potential evidence.
    pass_rows=[line for line in txt.splitlines() if re.search(r'\|\s*PASS\s*\|',line,re.I) and not line.lstrip().startswith('| ---')]
    warnings=[]
    if not pass_rows: warnings.append('No documented PASS test rows; application is NOT verified by this script.')
    if any(w in txt.casefold() for w in PLACEHOLDERS): warnings.append('Test report contains unverified placeholders.')
    if not all(c['exists'] for c in checks): warnings.append('Some required project documents are missing.')
    return {'project':str(project.resolve()),'documents':checks,'document_count':sum(c['exists'] for c in checks),'potential_pass_rows':len(pass_rows),'warnings':warnings,'runtime_tested':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project', type=Path, required=True)
    ap.add_argument('--format',choices=['text','json'],default='text')
    args=ap.parse_args()
    if not args.project.is_dir(): ap.error('Project path must exist and be a directory')
    result=check(args.project)
    if args.format=='json': print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print('DOCUMENT READINESS (not runtime verification)')
        for c in result['documents']:
            print(('OK ' if c['exists'] else 'MISSING ')+c['name'])
        for warning in result['warnings']: print('WARNING:',warning)
        print('Runtime tested: NO (this tool checks documents only)')
    if result['document_count']<len(FILES): raise SystemExit(1)

if __name__=='__main__': main()

#!/usr/bin/env python3
"""Audit IDs and evidence fields in a traceability CSV. NOT an executable app test."""
import argparse,csv,json,re
from pathlib import Path
PREFIX={'REQ_ID':'REQ','FEAT_ID':'FEAT','SCR_ID':'SCR','CMP_ID':'CMP','INT_ID':'INT','TASK_ID':'TASK','TEST_ID':'TEST'}
REQUIRED=list(PREFIX)+['Priority','Reference_ID','Prototype_Evidence','Implementation_Evidence','Status','Owner_Approval']
def audit(path):
    with path.open(newline='',encoding='utf-8-sig') as f:
        rdr=csv.DictReader(f); fields=rdr.fieldnames or []
        missing_columns=[c for c in REQUIRED if c not in fields]
        rows=list(rdr)
    issues=[]
    for i,row in enumerate(rows,2):
        for c,prefix in PREFIX.items():
            v=(row.get(c) or '').strip()
            if not re.fullmatch(prefix+r'-[0-9]+',v): issues.append(f'row {i}: invalid/missing {c}: {v!r}')
        if (row.get('Priority') or '').strip().lower() in ('must','must-have','critical'):
            for col in ['Prototype_Evidence','Implementation_Evidence','Owner_Approval']:
                val=(row.get(col) or '').strip().lower()
                if not val or val in ('pending','tbd','none','n/a'):
                    issues.append(f'row {i}: must-have missing {col}')
    return {'rows':len(rows),'missing_columns':missing_columns,'issues':issues,'runtime_tested':False}
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('csv_file',type=Path);ap.add_argument('--json',action='store_true');a=ap.parse_args()
    report=audit(a.csv_file)
    print(json.dumps(report,indent=2,ensure_ascii=False) if a.json else '\n'.join([f"Rows: {report['rows']}"]+report['missing_columns']+report['issues']+["Runtime tested: NO"]))
    raise SystemExit(1 if report['missing_columns'] or report['issues'] else 0)
if __name__=='__main__':main()

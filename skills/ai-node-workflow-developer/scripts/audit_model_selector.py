#!/usr/bin/env python3
"""Static audit for a production feature-specific model selector (no live API calls)."""
import argparse
import csv
from datetime import datetime, timezone, timedelta
from pathlib import Path

REQUIRED = {"model_id", "provider_id", "feature_id", "task", "operation", "auth_state", "connection_state", "capability_status", "test_status", "test_evidence", "last_verified_utc", "ttl_hours", "enabled_for_feature"}

def audit(path, feature, task, now):
    errors, visible = [], []
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        reader=csv.DictReader(f)
        missing=REQUIRED-set(reader.fieldnames or [])
        if missing:
            return [], ["missing columns: " + ", ".join(sorted(missing))]
        for line, row in enumerate(reader, start=2):
            if row["feature_id"].strip()!=feature or row["task"].strip()!=task:
                continue
            if row["enabled_for_feature"].strip().lower() not in ("yes", "true", "1"):
                continue
            problems=[]
            for field, expected in (("auth_state","authorized"),("connection_state","connected"),("capability_status","verified"),("test_status","passed")):
                if row[field].strip().lower()!=expected:
                    problems.append(field+" must be "+expected)
            for field in ("model_id", "provider_id", "operation", "test_evidence", "last_verified_utc"):
                if not row[field].strip() or row[field].strip().lower() in ("unverified", "unknown", "n/a"):
                    problems.append("missing "+field)
            try:
                verified=datetime.fromisoformat(row["last_verified_utc"].replace("Z", "+00:00"))
                ttl=float(row["ttl_hours"])
                if verified.tzinfo is None or ttl<=0 or verified + timedelta(hours=ttl)<now:
                    problems.append("stale or invalid verification")
            except (ValueError, OverflowError):
                problems.append("invalid last_verified_utc / ttl_hours")
            if problems:
                errors.append("line " + str(line) + " " + row["model_id"] + ": " + "; ".join(problems))
            else:
                visible.append(row["model_id"])
    return visible,errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry",required=True)
    parser.add_argument("--feature", required=True)
    parser.add_argument("--task",required=True)
    args=parser.parse_args()
    visible, errors=audit(args.registry,args.feature,args.task,datetime.now(timezone.utc))
    print("Eligible in static audit:",", ".join(visible) if visible else "none")
    for err in errors: print("ERROR:",err)
    return 1 if errors else 0
if __name__ == "__main__":
    raise SystemExit(main())

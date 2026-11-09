# Requirement Coverage & Deviation Audit

## Requirement matrix
Give every agreed behavior a `REQ-###` and every control or node `CTRL-###` / `NODE-###`. Trace to code path, a runnable TEST ID, test result, execution evidence and approved deviation (if any). Map non-visual requirements (privacy, keyboard, rollback, performance) too.

## Coverage states
- PLANNED: spec exists, implementation not demonstrated.
- IMPLEMENTED: code location provided but no validated runtime proof.
- VERIFIED: successful observed test for the actual build/platform, evidence linked.
- BLOCKED: unavailable provider, hardware, missing requirement detail or reproducible failure.
- REMOVED: authorized scope change with change request and owner approval.
Never describe IMPLEMENTED as VERIFIED.

## Practical steps
1. Freeze spec baseline and calculate all Must requirements before coding.
2. Generate `REQUIREMENT_COVERAGE.csv` with one row per atomic testable requirement.
3. For each vertical slice, update implementation path, test ID, state and evidence location.
4. Find orphaned controls, missing handlers, tests without requirements and requirements without tests.
5. Compare the final snapshot with the baseline; produce a missing-coverage and deviations report.
6. Block release if any Must requirement is not VERIFIED (unless formally removed and approved).

Use `scripts/audit_requirement_coverage.py --project PATH`; this audits records and file pointers, not application behavior.

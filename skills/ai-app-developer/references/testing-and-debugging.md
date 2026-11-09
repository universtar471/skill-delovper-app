# QA and debugging playbook

## Evidence levels
- Proposed: specification only.
- Implemented: source changed, no run proof.
- Built: recorded successful build command on current source.
- Tested: recorded test commands/results or verified manual device tests.
- Released: artifact/location plus deployment/installation confirmation.

## Test pyramid
Feature acceptance criteria → unit logic → integration against boundaries → UI/E2E smoke → device/platform-specific manual QA. Include success, blank input, bad input, permissions denied, offline, slow, interrupted operations and restart.

## Bug triage
Collect expected/actual, reproduction steps, platform/version, logs without secrets, screenshot/video when available, scope/severity. Reproduce; identify root cause; create minimal fix; add regression test; rerun related suites. Classify unresolved or non-reproducible honestly.

## Report
Use `assets/templates/test-report.md` with command, environment, exit code, output summary, timestamp, passed/failed/skipped and artifact hash/path if built. A script that checks docs does NOT validate app runtime behavior. Block release on critical security flaws, data loss, failed core flow or untested build.

## Visual layout regression gate
Apply `layout-qa-and-zoom.md` and store evidence in `assets/templates/layout-test-matrix.csv`. Test UI at narrow/short and wide windows, zoom levels, font scaling, varied strings and all major states; do not equate a screenshot of the default viewport with responsive verification.

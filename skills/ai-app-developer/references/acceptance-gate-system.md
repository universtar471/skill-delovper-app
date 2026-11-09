# Acceptance Gate System (mandatory)

## Purpose and source of truth
Treat an approved specification as a contractual baseline. Every release must have a frozen requirements version, actual implemented behavior, independent test evidence, and owner approval. A screenshot, mock API response, unchecked checkbox, or an agent's statement is NOT proof of runtime behavior.

## Stage gates in order
1. G0 INTAKE: identify feature intent, platform, user, references, constraints and unknowns.
2. G1 SPEC_LOCK: freeze REQ/FEAT/UI/INT IDs, inputs, outputs, failure cases and measurable acceptance criteria; owner reviews.
3. G2 FEASIBILITY: verify libraries, licenses, API/MCP/CLI capabilities, model access, security and actual integration constraints.
4. G3 PROTOTYPE: run interactive critical user flows; compare with approved UX; get owner acceptance before building broadly.
5. G4 IMPLEMENT: link each essential control to real handler/adapter; run unit/integration checks and preserve rollback point.
6. G5 EVIDENCE: execute visual regression, accessibility, responsive, runtime E2E, failure recovery and requirement coverage.
7. G6 RELEASE: clean build, release smoke test, backup/rollback plan, delivery evidence and limitations.

## Gate enforcement
- Maintain `ACCEPTANCE_GATES.csv`, `REQUIREMENT_COVERAGE.csv` and referenced evidence in project docs. Mandatory requirements must have status PASS and evidence before release; a missing dependency remains BLOCKED.
- Only a human-authorized waiver may bypass a noncritical gate. Do not waive missing credentials, broken core action, data-loss risk, critical security, or an unverified live integration in a release.
- Use statuses `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `FAIL`, `PASS`, `WAIVED`. `PASS` means executed and verified, not merely coded.
- Record environment, date/time, tool command, input fixture, actual output, artifact/log paths and reviewer. Redact secrets from logs and screenshot evidence.
- Run `scripts/audit_acceptance_gates.py --project PATH --require-final`; its static audit cannot prove that evidence is authentic or that tests actually ran. Require human review of evidence.
- If verification tools are unavailable, mark `NOT_RUN` in test report and BLOCK release; never fabricate results.

## Example release decision
- G4 implement PASS, G5 live provider E2E BLOCKED -> product is NOT release-ready. Show the exact gap and next action.
- A UI snapshot PASS but an E2E button test FAIL -> NOT release-ready.
- Owner explicitly accepts optional cosmetic variance -> record deviation and approval; critical failures remain blocked.

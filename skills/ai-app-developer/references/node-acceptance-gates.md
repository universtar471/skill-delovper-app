# Node Workflow Acceptance Gates

- G0 input: approved workflow goal; actual source media permission and scope.
- G1 contract: every node type/version, typed ports, preview, prompt edit, model selector and each command has schema and tests.
- G2 preflight: graph/port validation, model availability and capability adapter, estimated cost, permission and security policy.
- G3 visual: zoom/pan, drag, snap, group, icon help, per-node preview, expand viewer, hover and reduced motion; test at high node counts.
- G4 engine: real scheduler, cached/dirty/blocked states, cancellation, timeout, retries, ordered events and resume.
- G5 integration: real API/MCP/CLI evidence and working model output; Dry Run alone is not sufficient.
- G6 persistence: reopen identical graph, model choices and assets; E2E successful run with immutable manifest and usable output.
- G7 release: visual regression, accessibility, performance, secrets audit, build smoke and rollback.

Keep `ACCEPTANCE_GATES.csv`, `WORKFLOW_ACCEPTANCE_GATES.csv`, `REQUIREMENT_COVERAGE.csv`, provider evidence and run snapshots in project docs. Enforce critical gates with `scripts/audit_acceptance_gates.py --require-final`, plus E2E human-reviewable evidence. Never certify a mock-only graph.

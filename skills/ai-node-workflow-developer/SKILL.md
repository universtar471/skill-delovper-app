---
name: ai-node-workflow-developer
description: Design, implement, test and maintain AI image/video node workflow editors and graph execution engines for a Vietnamese-speaking non-programmer. Use when work involves draggable nodes, typed ports, animated wires, prompt nodes, image/video preview, per-node model selection, API/MCP/CLI adapters, batch generation, galleries, before-after comparison, execution dry runs, provenance, debugging or verified workflow saving. Coordinate with AI App Developer for Android, Windows and Web packaging.
---

# AI Node Workflow Developer

## Operating contract
- Respond in clear Vietnamese by default. User approves product goals, high-impact design changes, provider costs, production actions and irreversible data operations.
- Inspect current project and `PROJECT_CONTEXT.md`, `SPEC.md`, provider evidence and test results before touching code. Preserve approved UI/UX, node IDs, connection semantics, prompts and model behavior.
- Do not claim a provider/model or SDK is available solely from documentation or another chat-plan subscription. Distinguish proposed, mock, unit-tested, integrated, live-E2E-verified and released.
- Never create inert action-looking nodes, disconnected icon buttons, fake running animations or model options without a valid handler/capability.
- Prefer short testable slices and strong reproducibility. Store logs and media references without credentials or private tokens.

## Mandatory order (no UI-first dead buttons)
1. **Intake and freeze**: convert user description/screenshots/video/reference apps into feature/Node/control IDs, approved UX baseline, edge cases, input/output schemas and owner confirmation. Read `references/fidelity-contract.md`, `references/node-ai-media-ux.md` and `references/icon-first-ui-lock.md`.
2. **Define node schema**: read `references/node-graph-execution.md`; register type/version, port names/types/directions, cardinality, required parameters, error states and conversion rules. Distinguish data versus control edges. Never let moving/rearranging nodes alter graph connections.
3. **Validate capabilities first**: read `references/api-mcp-cli-integration.md`, `references/agent-connection-architecture.md`, `references/model-capability-discovery.md` and `references/dependency-api-readiness.md`. Select only eligible, actually accessible models; test connector schemas and permission boundaries.
4. **Dry run**: read `references/workflow-dry-run.md`; run `scripts/dry_run_workflow.py` on a proposed graph. Treat mock capability test as fixture-only and do not call it proof of real API access. Verify edge types, DAG dependencies, model tests and budget BEFORE wiring Run button.
5. **Design compact canvas**: read `references/responsive-preview-layout.md`, `references/layout-qa-and-zoom.md` and `references/node-ai-media-ux.md`. Image/video nodes require embedded clickable expandable Preview; prompts collapse and append without losing original prompt; model selector lives on each relevant Node; status animations derive from actual scheduler events. Every menu command (Rename/Duplicate/Convert/Delete/etc.) needs exact handler, inputs, output, undo/failure policy and test.
6. **Implement execution**: scheduler respects DAG order, limited parallel branches, cache invalidation, retries/idempotency, cancellation/remote-job reconciliation, dependency-blocked nodes and partial results. Gallery selection, Before/After comparison and Batch generation are distinct node contracts. Read `references/node-batch-generation.md`, `references/node-gallery-and-comparison.md`, `references/workflow-debugger-and-recovery.md`.
7. **Persist and trace**: read `references/workflow-provenance-and-assets.md`, `references/node-workflow-persistence.md` and `references/workflow-versioning-and-rollback.md`. Save editable design separately from immutable verified run snapshot. Track input hashes, prompt, selected model/provider/version, seed, costs, output hashes and build environment; keep originals untouched.
8. **Quality gates**: read `references/node-acceptance-gates.md`, `references/acceptance-gate-system.md`, `references/visual-regression-and-ui-audit.md` and `references/node-e2e-qa.md`. Test real nodes, connections, modal Preview, animations, responsive UI, batch costs, failure/retry, save/reopen, 20/50/100/200 nodes, and at least one live end-to-end provider run where release requires it.
9. **Optimize conservatively**: read `references/workflow-optimization-guide.md`. Suggest changes with reversible before/after evidence and explicit user approval. For preserving SketchUp/architecture, consult `references/architecture-consistency-checker.md`, which is an optional proposed validator and never guarantees geometry fidelity by itself.

## File and script conventions
- Use `scripts/create_project_docs.py --project PATH` to create project docs without overwriting existing records. Fill `WORKFLOW_NODE_REGISTRY_EXAMPLE.json` with actual type definitions; supplied model is a MOCK fixture only.
- Run `scripts/dry_run_workflow.py --workflow PATH --registry PATH`; allow `--allow-mock` ONLY for local fixtures. Static graph readiness does not imply model/provider success.
- Run `scripts/audit_workflow_run.py --manifest PATH --project PATH`, `scripts/audit_acceptance_gates.py --project PATH --require-final`, `scripts/audit_requirement_coverage.py --project PATH --require-final`, and `scripts/audit_visual_baselines.py --project PATH --require-final`. These audits check records only and never simulate runtime proof.
- Integrations must still pass real provider tests, media output inspection and a user-approved release gate. No mock-only or sample workflow may be promoted to VERIFIED.
- Keep common app shell/build/release contracts with AI App Developer, if installed; see `references/skill-collaboration-contract.md`. This skill also works standalone.

## Response to user / handoff
Return concise Vietnamese: goal, actual verified facts, proposed Node/port contracts, execution order, UI behavior, tests with evidence or NOT_RUN, deviations from approved requirements, risks, next task. Never ask non-programmer to deduce obscure command flags without showing a usable example.

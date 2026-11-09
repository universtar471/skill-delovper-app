# Workflow Dry Run & Preflight Validation

## Non-negotiable definition
Dry Run validates the planned graph without executing a model, CLI process, API call or MCP action. It does not prove performance, model availability or correctness of a generated image. The UI must never call dry run a successful real execution.

## Preflight sequence
1. Load `schemaVersion`, node type registry, typed input/output ports, cardinality, required parameters and model capabilities.
2. Verify unique IDs, known node types and supported versions, graph edges, no missing required input and no invalid type conversions.
3. Compute dependency order, detect cycles, illegal reentrant commands, orphaned data and incompatible versions. Loops require an explicit bounded loop engine, not accidental DAG cycles.
4. Check that configured tool is available in current environment and status `LIVE_E2E_VERIFIED`. A `MOCK` is allowed only for local fixture testing, never release.
5. Estimate jobs, provider quota/concurrency and cost from current authorized pricing records; flag UNKNOWN rather than inventing a number. Block on explicit budget overrun.
6. Emit an ordered execution plan, errors and warnings, without network access. A no-error dry run is only static readiness.
7. Execute integration tests, then a real end-to-end workflow with test data before considering release.

## Script
`python scripts/dry_run_workflow.py --workflow docs/WORKFLOW_DRY_RUN_EXAMPLE.json --registry docs/WORKFLOW_NODE_REGISTRY_EXAMPLE.json --allow-mock`
The example uses MOCK capabilities and is never proof of real provider access. Remove `--allow-mock` for release gating. A failed dry run blocks the Run button with a targeted explanation rather than an indefinite spinner.

## Test cases
Cycle, wrong port type, missing input, node version change, unavailable model, mock-only capability, duplicate ID, illegal fan-in, insufficient budget, missing media path, disconnected provider. Model availability must be rechecked before actual execution.

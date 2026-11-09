# Workflow Debugger, Partial Execution and Recovery

## Debugger panel
Select node -> show stable node ID, declared type/version, input/output schemas, data preview with privacy masking, running status, per-attempt trace, adapter, model, queue time, execution time, cost label, cancellation id and downstream affected nodes.

## Controls
- Inspect: read-only detail, separate from Run.
- Run Selected: calculate needed ancestors; honor cache and dependency policy.
- Retry Failed: require idempotency analysis and budget check before retry; never blindly rerun paid operations or side effects.
- Cancel: request cancellation and reconcile with provider's actual cancellation result; browser closing does not imply remote job stopped.
- Clear Cache: show affected descendants and require confirmation for destructive cache removal.
- Breakpoint/Watch: development-only; redact secrets and personal data.

## Failure handling
- `FAILED` is terminal attempt state, `BLOCKED` for downstream unsatisfied dependency, `SKIPPED` per policy, `CANCELED` only if confirmed, `UNKNOWN` if provider state can't be established.
- Independent branches may finish even when one fails; run manifest records partial success and per-node outputs.
- Checkpoint/resume must use immutable execution attempt IDs and versioned snapshot; avoid duplicate billed jobs after reconnect.
- A completed workflow has actual successful E2E evidence, not just a zero-error Dry Run.

# Graph, execution and animation contract

## Design phases
1. Define node type registry with schema and typed ports, capabilities and adapter IDs before drawing connected nodes.
2. Validate edges, cardinality, mandatory inputs, dependency order, incompatible conversions and cycles (unless explicit loop-control nodes and bounded termination rules exist).
3. Implement graph model with stable node/edge IDs, immutable update transactions, undo/redo and persistence.
4. Implement scheduler with queued -> running -> succeeded/failed/skipped/canceled states; run DAG levels based on satisfied dependencies. Limit concurrency by provider/account/VRAM and budget.
5. Emit ordered structured events (run ID, node ID, attempt ID, edge ID, status, timestamp) and render UI progress from these events; reconcile late/out-of-order events safely.
6. Only after adapter contract tests connect the renderer/toolbar, then test real API/MCP/CLI E2E.

## Execution rules
- Define failure policies per node and edge; a failed branch must not block unrelated branches. Downstream dependent nodes become blocked/skipped with reason.
- Retry uses exponential backoff and explicit caps. Use idempotency keys when supported; never retry side-effecting operations blindly.
- Distinguish `data_edge`, `control_edge`, and `trigger_edge` (if supported). Data edge updates do not imply execution unless scheduler policy says so.
- Cache key includes input asset hashes, merged prompt, model/provider/version, seed, parameters, code/adapter version and relevant environment. Invalidate descendants on effective change, do not rerun independent branches.
- Queue, partial execution, cancellation, checkpoint/resume and reconnect behavior need explicit policy; a stopped browser UI must not imply an already-running remote job has stopped.
- Run manifests contain actual start/end, inputs, outputs, model IDs, costs (actual or estimated labeled), errors, adapter identity, logs and test evidence.

## Layout and interaction requirements
- Pan/zoom independent from node preview content zoom; fit-selection and mini-map. Maintain ports/edge hit targets when zooming. Node previews can simplify to thumbnail/icon at far zoom.
- Moving nodes alters layout only; connections, parameters and execution order cannot change. Group and auto-layout operations must be undoable; reroute edges without detaching.
- Stress test graph at 20/50/100/200 nodes with variable thumbnails; record actual performance, not fixed promised targets.

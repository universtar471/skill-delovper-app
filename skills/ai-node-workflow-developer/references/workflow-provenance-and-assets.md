# Media Asset Provenance, Storage & Execution Snapshots

## Asset contract
- Reference media by immutable asset ID and sha256 digest, not a volatile browser blob URL. Keep original uploads read-only; derivatives refer to their parent(s).
- Store mime type, dimensions, duration, origin, owner/consent context, import time, retention policy and privacy boundary. Video previews must not require loading the original full-resolution file into every node.
- Preserve model ID/provider, API operation/adapter version, positive/negative prompt and merge rule, seed, sampler/ratio/quality, input hashes and output hashes. A prompt or model edit invalidates relevant downstream cache.
- For external assets, keep access tokens out of exported workflow JSON. Export portable reference manifests with explicit missing-file state; do not embed secrets in the graph.

## Two independent saved artifacts
1. Workflow Design Snapshot: editable nodes, edges, node types/versions, parameters, canvas positions, UI groups, model selections and asset references. Saving a draft does not mean it ran.
2. Execution Run Snapshot: immutable graph/config hash and executed node attempts, timestamp, provider/tool IDs, outputs, actual/estimated cost labels, errors, evidence paths, hashes and status per node.

## Replay limitations
Generation is not always bit-for-bit reproducible; model updates, nondeterminism, seed rules, hidden provider revisions and hardware can change output. Retain enough evidence to understand why and show a warning before a paid replay.

## Audit
Use `scripts/audit_workflow_run.py --manifest PATH --project PATH` for structural evidence checks; it does not call providers and cannot establish truth of log statements. Human review plus actual run logs remain required.

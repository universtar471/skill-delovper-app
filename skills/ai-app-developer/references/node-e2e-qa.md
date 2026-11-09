# Node AI workflow UI/engine acceptance suite

Run on actual target platforms, including zoom/narrow viewport and reduced motion. Store screenshot/recording plus event log, graph hash and observed outcomes.

| ID | Test | Expected |
|---|---|---|
| NUI-01 | Upload image/video, click thumbnail | Viewer opens, preserves aspect, supports close/restore focus |
| NUI-02 | Preview in loading/error/expired asset | Useful nonbroken state, retry if feasible |
| NUI-03 | Video player preview | Play, pause, seek without starting workflow |
| NUI-04 | Collapse preset prompt then append custom text | Final merged text correct and saved |
| NUI-05 | Type text while dragging elsewhere | Editing does not move node or trigger canvas shortcuts |
| NUI-06 | Open model picker on generate node | Only compatible/authorized/verified task models visible |
| NUI-07 | Change model with existing downstream nodes | Compatibility and cache invalidation handled; no silent substitution |
| NUI-08 | Execute parallel branches | Only running nodes/edges animate according to actual events |
| NUI-09 | Fail/retry/cancel | No permanent spinner; clear evidence and downstream states |
| NUI-10 | Respect reduced motion | No forced animation; labels still show progress |
| NUI-11 | Duplicate node | Unique new ID; no active job/credential copy; edges policy explicit |
| NUI-12 | Rename/delete/undo/redo | Graph and saved state consistent |
| NUI-13 | Convert node | Eligible targets only, explicit parameter and edge migration |
| NUI-14 | Move multiple nodes, Auto Layout | Only positions change, edge semantics intact |
| NUI-15 | Save draft/validated/verified and reload | Status accurate; media and prompt retained without secrets |
| NUI-16 | 20/50/100/200 nodes at variable zoom | Benchmark UI responsiveness, overlap, previews and edge rendering |
| NUI-17 | Disconnect provider and reopen workflow | No fake success; unavailable models shown appropriately |
| NUI-18 | Run partial branches and reused cache | Unaffected nodes not rerun and data lineage preserved |

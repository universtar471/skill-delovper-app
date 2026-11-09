# Workflow Optimizer (advisory only)

- Do not automatically rewrite an approved pipeline merely to decrease Node count. Show proposed optimization, expected tradeoffs, affected outputs, cost and test plan; obtain owner approval.
- Safe suggestions: remove provably orphaned unused nodes, group presentation-only nodes, cache repeated immutable input loads, reduce duplicated preview thumbnails and schedule independent branches concurrently within limits.
- Risky suggestions requiring approval: changing model/provider, altering prompt order, modifying seed, changing image resolution or cropping, combining separate validation steps, removing checkpoints, reducing batch count.
- Compare before/after run manifests and visual image quality against project acceptance criteria; if outputs differ, prefer preserving the original.
- Keep reversible change requests and rollback snapshot for every optimization.

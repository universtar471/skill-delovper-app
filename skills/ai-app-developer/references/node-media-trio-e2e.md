# E2E acceptance tests — media trio

## Baseline and scope
- Test through the *real* UI/graph engine and adapters where available; structural stubs are only simulation. Capture run ID, screenshot/video, logs, input hashes, output IDs and platform. Never mark integration verified based solely on mocks.

| ID | Scenario | Pass condition |
|---|---|---|
| GAL-01 | Gallery populated | only supported image refs show, count accurate, aspect preserved |
| GAL-02 | Navigate vs select | navigation does not mutate output until explicit select |
| GAL-03 | Selection changes | selected ID propagates to dependent node; no unapproved provider call |
| GAL-04 | Missing asset / reload | error placeholder and repair action; layout, selection persist |
| CMP-01 | Before/after input | distinct typed inputs and provenance preserved |
| CMP-02 | Zoom/pan/slider | aligned, usable at 80–200% app zoom and keyboard/touch |
| CMP-03 | Differing resolution | no silent stretching/crop; mismatch handled as specified |
| CMP-04 | Export/selection | review action doesn't mutate source; explicit output honored |
| BATCH-01 | Planned jobs | Cartesian count computed before any provider request |
| BATCH-02 | Eligible model | unauthorized/incompatible model hidden or disabled |
| BATCH-03 | Rate limit + retry | bounded scheduler; no blind charged duplicates |
| BATCH-04 | Partial failure | distinct per-job states, usable partial result only if policy allows |
| BATCH-05 | Cancel and restart | no unapproved restart or unexpected charge |
| BATCH-06 | Duplicate clicks | idempotent action or second click disabled |
| BATCH-07 | Save/reopen | graph + manifest + selected media ref restored; no secrets |
| BATCH-08 | End-to-end | batch → gallery → comparison → selected output works with evidence |

## Release gate
- A gallery, compare or batch node is **UI prototype** until controls are integrated with real handlers. It is **runtime tested** only with passing outcomes and evidence. If live provider testing not possible, record `NOT_RUN`, block release of that node as verified and describe missing credentials/tools.

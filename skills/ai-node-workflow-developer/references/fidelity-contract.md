# Fidelity contract — prevent spec-to-product drift

## Establish a signed-off baseline
Create an immutable baseline identifier such as `BASELINE-2026-11-09-A` and link approved `PROJECT_BRIEF`, `SPEC`, `UI_SCREEN_SPEC`, user screenshots/videos, design tokens, interaction contracts, test cases, repo commit and prototype snapshot. Retain old baselines for comparison. Record `approved / provisional / rejected`, date and approver in `DECISIONS.md`.

## Traceability chain
`User input + observable reference -> REQ -> FEAT -> SCR -> CMP + INT -> DATA/API -> TASK -> code changes -> TEST -> evidence -> approval`.
- Every interaction gets an ID, including back/undo, drag/drop, long press, confirmation, cancellation, empty/error/loading, permissions, offline and accessibility.
- Every button specifies what happens after press, before any backend exists. Unwired decorative buttons are forbidden in an approved interactive prototype.
- Every business rule includes testable inputs, outputs, constraints, boundary values and negative cases.
- Do not substitute an existing component because it looks similar; record behavioral gaps and reject it if mandatory requirements are unsupported.

## Change management
For deviations create `CHANGE_REQUEST.md` entry: ID, baseline, affected IDs, original behavior, proposed change, why, visual before/after, data/API effects, regression risks, estimated complexity, explicit owner decision. Until approved, preserve baseline. Fixing an implementation bug that restores accepted behavior does not require feature-scope approval.

## Measurable acceptance
- Requirement coverage: all `must-have` REQ map to one or more FEAT and TEST; all shipped interactive CMP map to INT + evidence.
- Functional fidelity: key flows pass on target device/browser, not only a static browser render.
- Visual fidelity: compare same viewport, font, data, OS scaling, theme, DPI. Use image diff or reviewer before/after; define tolerances per project, avoid claiming a universal numeric threshold.
- Contract fidelity: navigation, validation, data persistence, failures, performance, responsiveness, keyboard/touch semantics.
- No stage moves from `approved prototype` to `implemented` without written approval or documented explicit delegation; do not claim to have sign-off based on silence.

## Screen design minimum
For every screen specify: screen ID, purpose, hierarchy, elements, size / spacing tokens, component sources, keyboard and gestures, user actions, transitions, data schema, fake-vs-real data, loading/error/empty/success/permission states, breakpoints, accessibility, analytics only with consent, links to tests.

## Post-implementation comparison
At each completed feature: capture actual app screenshots/video, walk through every contracted action, compare with baseline, list deviations in `DEVIATION_LOG.md`, categorize `blocker/high/low`, fix or seek owner approval. Preserve test evidence and user decision. Do not recast missing behavior as 'future enhancement'.

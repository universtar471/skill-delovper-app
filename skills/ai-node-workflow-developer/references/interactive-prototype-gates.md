# Interactive prototype and quality gates

## Gate A — requirements understood
- For each `REQ` write acceptance criteria, priority, reference, owner decision, assumptions and unknowns. Map screenshots/video frames to observed behavior; mark extrapolation explicitly.
- Demo a user journey map with back, cancellation, errors, empty states and recovery. Require owner sign-off on scope.

## Gate B — functional prototype (before large-scale build)
- Build a clickable or executable prototype using the target framework when feasible. Every visible control in the chosen slice must perform an intentional action or be explicitly marked disabled with reason.
- Use representative data (not all happy-path placeholders), real navigation and deterministic fake services that mimic future backend contracts.
- Capture screen recordings for default, hover/focus, active, loading, error, empty, success, mobile/desktop. Ask owner to review behavior AND appearance.
- Verify a 'vertical slice': navigate -> edit -> validate -> save -> reopen; identify persistence as mock or real.

## Gate C — contract freeze
- Freeze approved screen specs, design tokens, interaction states, component choices, endpoint/data schema and baseline reference ID. Keep source control commit/tag. Produce `traceability-matrix.csv` with tasks/tests.
- Do not proceed to broad implementation if mandatory interaction behavior remains unspecified.

## Gate D — implementation parity
- Build one FEAT at a time. Each pull request must point to IDs, show actual screenshots/video, tests run and deviations. Compare on target viewport and input method; record usability feedback.
- Block merging if a high-severity required behavior is missing or a previously approved flow regresses.

## Gate E — release readiness
- Run unit, component, integration, E2E, smoke, accessibility and responsive checks that are available. Record skipped checks with reason. Confirm installation/build and state migrations on target platform.
- Generate `DEVIATION_LOG`, `TEST_REPORT` and release summary. Ask owner to explicitly accept any known remaining differences.

## Example: video editor
`REQ-001 user trims clip` -> `SCR-003 timeline` -> `CMP-021 trim handle` -> `INT-004 drag left bound, never past right` -> `TASK-017` -> `TEST-032 trim with short clip / empty clip / undo` -> `proof: screen recording on Android`. A pretty timeline with no drag behavior fails Gate B.

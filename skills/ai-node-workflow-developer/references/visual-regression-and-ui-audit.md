# Visual Regression & UI Behavior Audit

## Why it matters
A screen can look correct but contain dead buttons, wrong state transitions or inaccessible controls. Visual matching and functional verification are separate required gates.

## Freeze the baseline
Record approved image/prototype version, pixel dimensions, viewport, zoom, DPR/DPI, theme, font scale, locale, dataset, animation state, expected controls and crop policy. Store approved baselines in versioned project assets; document permitted dynamic regions.

## Automated screenshots when tools exist
- Render actual built app (web browser, Android emulator/device, or Windows runtime). Capture baseline and actual at identical geometry and state.
- Compare images with pixel/perceptual diffs where tools are available; set tolerances per screen, not universal magic numbers. Investigate dynamic content separately.
- Repeat at narrow/short viewport and zoom 80/100/125/150/200% when appropriate to platform. Verify toolbar overflow, text wrapping, `?` help overlays, popovers, panel min sizes and Preview aspect ratio.
- Run click/navigation tests for every visible action and review disabled/loading/error states. Never pass a button just because it exists.
- Review icons and text alternatives (accessible name, tooltip, keyboard focus, contrast, touch target, motion reduction).

## Evidence contract
Each row in `VISUAL_BASELINES.csv` must point to approved baseline, captured actual image, diff/review evidence, and reviewer decision. Treat `PASS` as reviewed evidence, not script truth. The static `scripts/audit_visual_baselines.py` checks file references and review completeness only; it does not produce a screenshot or compute similarity.

## Typical causes of drift
Different design fonts, component defaults, CSS min-width, unrelated responsive breakpoint, untested 150% zoom, placeholder handlers, hidden overflow, reference asset mismatch. Document the root cause before tuning visual styles.

For P0/essential controls, do not allow visual review waivers. For P1/P2 waivers, record a reason, waiver ID and explicit owner approval.

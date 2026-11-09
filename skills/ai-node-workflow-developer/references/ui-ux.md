# UI/UX design-to-implementation contract

**Mandatory:** Read `icon-first-ui-lock.md` and `control-behavior-spec.md` before creating layouts. Use `assets/templates/control-inventory.csv`, `assets/templates/control-contract.md` and `assets/templates/icon-help-policy.md` as the authoritative screen-control inventory. This overrides any default tendency to fill screens with explanatory text or merge unrelated actions for simplicity.


Start with an app flow map and screen inventory. For each screen specify purpose, layout regions, component tree, labels in Vietnamese, click/tap/keyboard behavior, enabled/disabled/loading/empty/success/error states, navigation back behavior and responsive breakpoints.

Define design tokens (hex colors, spacing, radii, typography with licensing and fallback, icon library and sizes), interaction specs (hover, pressed, focus, transitions/durations, reduced motion), contrast, touch targets, keyboard traversal and screen-reader labels. Do not claim a font is installed; include fallback. Record any platform-specific differences.

If a reference image/video was provided, map every visible element to a requirement ID and mark unseen behavior as unknown. Avoid recreating other apps' protected logos and visual assets. Create wireframes first, then UI component implementation and visual QA screenshots only if accessible.

Mandatory UI acceptance: every visible action has intended behavior, error and loading feedback; no decorative inactive buttons disguised as functional controls.

## Responsive panels and preview gate
Read `responsive-preview-layout.md` and `layout-qa-and-zoom.md` for every editor/preview/inspector/resizable app interface. Create a panel layout contract and test matrix before approval. Explicitly distinguish application-window resize, OS/browser zoom, and media-content zoom.

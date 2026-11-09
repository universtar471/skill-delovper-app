# Responsive Preview & Panel Layout Lock

## Goal and trigger
Apply to every app with preview, editor, split pane, adjustable sidebar, floating tools, output gallery, log/review window, inspector or media canvas; also apply to general windows when resizing, device rotation or zoom can change available space. Always consult this document before prototype approval and before UI implementation. "Looks good at default desktop size" is not acceptance.

## Distinguish three types of zoom
1. **Window/viewport resizing**: resizing a desktop application window or browser viewport changes available CSS/device-independent pixels; reflow panels and controls.
2. **Browser/OS text zoom or DPI scaling**: changes layout and text metrics. Support browser 80, 100, 125, 150, 200% where practical and Windows 100, 125, 150, 200% display scaling. Avoid disabling browser pinch/zoom or relying on font scaling of the entire app.
3. **Content zoom** inside a preview: zoom an image/video/canvas/model, *not* the interface. Keep controls usable and preview bounds defined. Provide fit-to-view, reset (100%), bounded zoom, pan, and an explicit zoom indicator when relevant.

## Layout invariants (mandatory)
- Define per-region preferred width, minimum usable width, minimum height, priority, and compact fallback. No fixed full-screen width that prevents window shrinkage.
- The **preview stays usable**; protect minimum readable/actionable area, aspect ratio and never let a sidebar or toolbar cover the primary preview unless deliberately opened as a transient overlay with dismissal and focus management.
- Use flexible tracks: on Web `minmax(0,1fr)`, `min-width:0`, `min-height:0`, `max-width:100%`, `box-sizing:border-box`, and `overflow` on the correct nested scrolling container. For flex siblings that must shrink, set `min-width:0` and `min-height:0` explicitly.
- Image/video/canvas: specify containment policy (`object-fit:contain` or equivalent) and intrinsic aspect ratio; avoid stretching, cropping or clipping unless content intentionally uses crop mode. Canvas pixel backing-store dimensions must update with measured element size/DPR when appropriate; preserve scene state.
- Prefer collapsible panels and responsive modes over tiny unusable columns. If combined panel minimums exceed viewport, automatically switch to compact/single-panel mode. Save/resume splitter sizes where useful, but clamp persisted dimensions after a viewport change.
- Each toolbar defines item priority and collapse order. Overflow moves less-frequent commands into explicit menu(s) with original identities, not merged into a generic command. Do not hide a crucial destructive action under an ambiguous icon; accessible names must remain.
- Text: short button labels may ellipsize with accessible full name/tooltip; input data, crucial validation/errors and user-selected file names must remain discoverable; wrap long text and URLs appropriately. Do not clip user-editable content silently.
- Help text and longer notes stay behind contextual `?` according to icon-first rules; a help popup/sheet must stay within the viewport, be dismissible by Escape/back/tap outside, and work with keyboard and screen readers.
- Ensure splitters cannot leave panes below minimum width; include keyboard-operable resize and reset layout. Avoid horizontal page scrolling unless explicitly justified for an internal canvas/timeline.
- Manage overlays/popovers/modals: compute placement, flip/shift within viewport, account for virtual keyboard/safe areas/mobile browser chrome; retain dismiss and focus behavior.
- On touch devices respect minimum practical tap targets (generally aim for ~44x44 CSS px / platform-equivalent), even when visual icon is smaller; do not overlap hit areas.

## Panel behavior contract
For **every** adjustable pane record: `PANEL-ID`, role, parent, x/y docking, preferred/min/max width and height, resize mode, priority, fallback (`collapse`, `drawer`, `tab`, `stack`, `scroll`), persistence, content zoom handling, accessibility, resize tests. Use `assets/templates/panel-layout-contract.md`.

### Default example for video/image editor (starting point, not universal sizing)
- ≥1280 CSS px: sidebar + large preview + inspector, all resizable with clamps.
- 900–1279 CSS px: collapse or drawer inspector, retain preview + essential tools.
- 600–899 CSS px: stacked preview/workspace; inspector as tab/drawer.
- <600 CSS px: one focus panel at a time; bottom navigation or actionable tabs; preview remains accessible; use no forced three-column layout.
- Height below ~650 CSS px: vertical toolbars/panels scroll independently, preview keeps defined min height or enters compact mode; fullscreen preview if needed.
**Breakpoints are hypotheses**. Compute the actual switch using measured content minimums and verify on target hardware. Do not simply scale everything smaller.

## Explicit zoom interaction for preview
- Wheel+modifier, pinch or +/− controls must have documented precedence; avoid hijacking page scroll unexpectedly.
- Zoom focal point should stay under cursor/touch focus when feasible; pan should be bounded or clearly allow moving beyond the content as specified.
- Fit and 100% are distinct actions. Reset after asset replacement is specified. For video, zoom of displayed frame must not change output-resolution/export settings.
- Record zoom value, initial and max/min limits, input device mappings, preview state persistence, reset condition and output (rendered display transform only vs actual exported crop).

## Failure modes / prohibited shortcuts
- Absolute-position each button across a responsive row; position fixed controls over preview without collision checking; use `transform:scale` to solve window size problems; hide overflow on the root and make essential actions unreachable; cap all text to a single line without recovery; set broad `min-width` on the app shell; remove controls at small sizes without alternate access.
- A UI with no visible overlap but a clipped inaccessible command still **fails**.

## Verification gate
1. Define representative device/viewport and content cases via `assets/templates/layout-test-matrix.csv`.
2. Test all primary screens at portrait/landscape as relevant, narrow and wide windows, browser zoom/DPI/text enlargement, and nested preview zoom; include longest translated text, long project names, slow loading and errors.
3. Use actual browser/device runtime and inspect rendering plus keyboard/touch; take screenshots or recordings and log tested configuration. Use browser automation/visual-diff and DOM bounding rectangles where available, or platform screenshots + manual inspection. Automated bounding-box checks are indicators, **not** proof of usability.
4. Re-test after changes to panel minimums, toolbar contents, global font scale, CSS theme or preview renderer.
5. Approval fails for: overlapping controls, unreachable actions, clipped critical text, impossible panel resizing, unintended horizontal page scroll, preview obscured by a permanent control, floating help outside viewport, broken input focus, or zoom changing exported content unexpectedly.

## Platform notes
- **Web/React**: Grid/Flex with `minmax(0,1fr)`, `min-width:0`, media/container queries as appropriate; use ResizeObserver to size canvas to its actual parent (clean up). Beware `100vh` in mobile browsers; use dynamic viewport units where supported.
- **Android/Compose**: adaptive window size classes/constraints, layout modifiers, scrollable/foldable/orientation tests, fontScale and IME/safe insets. Avoid hardcoded dp widths spanning the screen.
- **Windows**: layout managers or adaptive grids, OS DPI scaling, resize/minimum window limits (documented), dock/splitter persistence with bounds, taskbar and multi-monitor DPI transitions.

## Required handoff
Provide layout diagram by mode, panel specs, toolbar overflow strategy, preview zoom spec, and tested matrix with screenshots/observations and any deviations. Preserve baseline in a signed-off layout contract; change requests required for substantive alteration.

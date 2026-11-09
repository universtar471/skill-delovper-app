# Layout, overflow and zoom QA checklist

## Test dimensions
Test the actual app, not just Figma or image mocks. Record CSS viewport or dp/physical resolution and scaling separately. Suggested browser viewport grid: 360x640, 390x844, 600x800, 768x1024, 1024x768, 1280x720, 1440x900, 1920x1080. Test at browser zoom 80%, 100%, 125%, 150%, 200%. Android: small phone, typical phone, large phone/tablet, rotate and keyboard open, fontScale 1.0 and 1.3+ when supported. Windows: minimum supported window, maximized, nonmaximized, DPI 100%/150%/200%, cross-monitor move.

## Required checks per mode
- [ ] Window can shrink to declared minimum; no pane prevents intended smaller modes.
- [ ] Preview content remains visible; aspect ratio remains correct, with fit/reset and pan/zoom preserved.
- [ ] Toolbar icons never overlap or have conflicting hit targets; overflow alternatives exist and operate.
- [ ] Each control has unambiguous function, action contract, icon name and a reachable help (?) affordance where needed.
- [ ] No horizontal scrollbar on the overall page unless explicitly required; inner timeline/canvas horizontal scrolling is allowed by spec.
- [ ] Long Vietnamese text, filenames, URLs, translated strings, and error messages wrap or offer expand/full text, not vanish.
- [ ] Popovers/dialogs stay within the visible viewport and respect keyboard/safe-area insets.
- [ ] On narrow/short screens, inspector/history/output panels collapse to reachable drawers/tabs; splitters clamp.
- [ ] Scrollbars remain accessible, not obscured by fixed headers/footers.
- [ ] Loading, empty, error, offline and permission-denied content retains valid layout.
- [ ] Touch, keyboard, screen reader focus and Escape/back dismissal function.
- [ ] Content zoom and browser/OS zoom remain independent; output/export not changed unless specifically intended.
- [ ] Persisted layout restored inside current viewport constraints.

## Automation advice
- On Web, use Playwright or equivalent to screenshot viewport variants, evaluate document scroll sizes and bounding rectangles for known critical regions, check visibility and run keyboard flows. Flag suspicious intersections but whitelist intentional popovers/overlays. Always manually review screenshot diffs.
- On Android, use instrumented UI tests/screenshot tests at varied device configurations and font scaling; record emulator/device evidence.
- On Windows, test with real resizable window and OS scaling. Use UI automation plus manual screenshots where framework tooling is insufficient.
- Test main application states and output panels, not only an empty shell. Add a layout regression check to CI where feasible.

## Defect reporting
For each issue record `LAYOUT-XXX`, device/viewport, app zoom and content zoom separately, window state, screenshot path, affected panel/control IDs, steps to reproduce, expected/actual result, severity, fix commit, retest outcome. Never mark layout as "verified" without executed tests and evidence.

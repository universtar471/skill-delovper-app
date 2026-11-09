# Icon-first UI lock: compact, usable, faithful

Apply this contract to EVERY screen and every UI change, on Android, Windows and Web. The product owner's preference is compact, calm, icon-first presentation with minimal permanent explanatory text. This is a **presentation lock**: never add visible instructional paragraphs, decorative labels, redundant headings, or oversized toolbars without documenting the exception and requesting approval. The lock does not excuse inaccessible or ambiguous UI.

## 1. Information hierarchy and text policy
1. Present working surface and primary action first. Cluster tools by task frequency and logical workflow, not arbitrary symmetry. Put advanced and contextual actions in contextual tools/panels; keep discoverability via consistent icons, a nearby `?`, tooltips and discoverable menus.
2. Prefer a recognizable icon for a *clear* single-purpose command; use icon+short label only where icon-only is ambiguous, hazardous, or essential to wayfinding. Keep indispensable data/field labels, values, errors, confirmations, permissions, legal/safety disclosures and screen-reader names. Do not replace these with a hidden `?`.
3. Hide **nonessential long guidance, notes, how-to, parameter definitions and examples** behind an adjacent `?` help trigger. The `?` opens a contextual popover, tooltip, side sheet or modal according to content length and device; preserve user context; do not use as the only place for crucial alerts or validation feedback.
4. Avoid placeholder-only forms; label essential inputs visibly (compact text label where necessary) and provide accessibility names for icon-only controls. Use progressive disclosure without burying primary functionality.
5. Before adding a visible sentence, classify it as: essential functional label, data value, critical status/error, required consent/safety, or optional guidance. Only optional guidance MUST move into `?`. Document justified exceptions.

## 2. Action/control integrity
- Make a separate control for each distinct primary action. NEVER attach unrelated functions to one generic button or create a misleading "magic" button merely to save space.
- Combine actions only if the combination has a coherent, explicitly documented model users expect (e.g. play/pause is a mutually exclusive state toggle; split-button has clear menu affordance and separate choices; context menu items are explicit). Each actionable menu item remains individually named and tested.
- No button may be visually actionable without an implemented, testable outcome; missing functionality is represented as a clearly disabled affordance with explanation if it must be shown, otherwise omit it.
- A single icon should have the same semantics in all screens. Map each icon to one command ID. Do not reuse visually similar icons for opposite operations without clear differentiation.
- Surface command availability in context. Explain disabled reasons in accessible help or tooltip; do not rely on color alone.

## 3. Required control record before coding
Create one row in `assets/templates/control-inventory.csv` **per control, including menu items** and complete the rich description in `assets/templates/control-contract.md` for anything nontrivial:
- Stable `CTRL` ID, feature/requirement ID, screen, location, priority and visibility conditions.
- User goal, icon source/name/license, optional compact text, accessible name, `?` help ID and full help content.
- Explicit event trigger: tap/click, long-press, keyboard shortcut, drag, double-click, hover; distinguish hover discovery from execution; prevent accidental destructive triggers.
- Preconditions, input types, required/default values, validation and range/unit/format.
- Detailed output/effect: UI state change, created/changed data, file/API/job, navigation, confirmation and success response.
- State machine: idle/hover/focus/pressed/active/selected/disabled/loading/success/error, with transitions and cancel/undo behavior.
- Invalid/empty inputs, network failures, concurrent operation, debounce/repeated taps, permissions, offline behavior and recovery.
- Exact target function/module/API or `not yet implemented`, test ID, prototype and implementation evidence.
- Touch target and keyboard focus/accessible label. Check target sizes against relevant platform guidelines; do not blindly enforce one dimension across all platforms.

## 4. Layout rules
- Allocate regions by actual work hierarchy: navigation, primary canvas/content, contextual inspector, utilities, status. Avoid multiple always-expanded sidebars, repeated controls and gratuitous card decoration.
- Define grid, spacing tokens, responsive breakpoints, density options, safe areas, minimum interactive targets, overlays, z-index/focus order and overflow handling.
- Put frequently used actions at top-level; group uncommon actions into predictable expandable panels or menus with **specific** commands; never collapse all unrelated tools behind one undifferentiated icon.
- Prefer icon glyphs from one consistent, properly licensed family, with consistent stroke, optical weight and hitboxes. Document each exception.
- Keep tooltips/help reachable with keyboard and touch, not hover-only; support Escape/close, focus restore and assistive technology. Avoid help icons that block primary canvas or cause layout shift.
- For Android: long-press may reveal command name but `?` still exposes full help; ensure gesture conflicts are resolved. For Windows: tooltips and shortcut hints. For Web: hover/focus/tap accessible controls. Document platform differences.

## 5. Design freeze + quality gates
**Gate A — inventory:** Count functions and actionable controls: every required action has one explicit reachable command; no duplicate, misleading or inert control. Link REQ -> FEAT -> SCR -> CTRL -> INT -> TEST.
**Gate B — icon validation:** Run a 5-second comprehension check and keyboard/screen-reader/touch review; if users misunderstand a critical icon, add a short label rather than sacrificing comprehension.
**Gate C — interaction prototype:** Demonstrate all primary flows, empty/disabled/loading/error/success and contextual `?` overlays. Owner approves screenshots + playable prototype, not just prose.
**Gate D — implementation audit:** Compare approved control inventory and layouts against actual code screenshots and tests. Require tests for each CTRL. Log any changed/added/removed/merged command as a deviation and seek approval.

## 6. Red flags (block completion)
- One generic button advertises multiple unrelated tasks without explicit selection.
- Unimplemented button appears usable; clicking does nothing.
- Help text exposed as permanent explanatory paragraphs without approved exception.
- Important errors, consent, required labels or results hidden in `?`.
- Icon-only controls with no accessible name or undiscoverable meanings.
- Screenshot looks correct but input, output, validation, state and testing evidence are absent.

## Example: video editor timeline
`CTRL-PLAY`: play/pause timeline toggle; input playhead/timebase; output playback state; shortcut Space when focus rules permit; explicit active state.
`CTRL-SPLIT`: separate scissors icon; requires selected clip and valid playhead; output two clips and one undo step; disabled when no clip is selected. Never combine with trim or delete.
`CTRL-TRIM`: dedicated trim handles contextual on selected clip; input handle drag with constraints; output adjusted boundaries; reversible.
`CTRL-HELP-TIMELINE`: `?` opens concise help for zoom, selection, split, trim and shortcuts; its only job is help, not executing an edit.

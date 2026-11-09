# Control behavior specification and evidence

Treat every visible icon/control as a tiny product feature with a concrete contract. Read `icon-first-ui-lock.md` before drafting screens.

## Process
1. Start from feature scenarios. Break each scenario into independent user intents and domain commands. Draw a flow showing what happens when inputs are absent, valid, invalid, slow, cancelled or failed.
2. Invent a stable CTRL ID and use one control per independently meaningful command. Buttons that only open a well-labeled menu are allowed if each menu option has its own CTRL ID and distinct behavior.
3. Select layout and visual hierarchy only AFTER inventory, to prevent the layout from dictating missing functionality. Select icons from inspected real libraries; record source/license/framework compatibility. Reject an icon if its meaning cannot be explained without a long tooltip for routine use.
4. Write each contract using `assets/templates/control-contract.md`. Map to UI component and handler names only once code exists; never invent actual functions.
5. Prototype each mode and test on actual target sizes/input devices. Inspect keyboard navigation, screen reader name, hitbox and accidental touch. User approves location, icon shape and resulting behavior.
6. Implement behavior behind an explicit command handler. Keep loading/disable logic aligned with preconditions. Add tests that verify the promised observable result, not merely a click event.
7. Audit `control-inventory.csv` and code. Fail release if a required control is missing, inert or mapped to unapproved behavior.

## Operational state transition sample
`CTRL-EXPORT`:
- Idle: icon `download`; enabled only if a renderable project exists.
- Trigger: click/tap/Enter/Space when focused.
- Input: export resolution, format, destination; persist only with permission.
- Validation: reject unsupported format, blocked output path, insufficient storage.
- Loading: disable duplicate export, show task progress and cancel when supported.
- Success: output filename and destination; open/save action as available; status stays visible outside `?`.
- Failure: inline actionable error with retry; preserve settings; never hide failure in help.
- `?`: explain formats, approximate disk usage and export settings; do not make `?` initiate export.

## Audit output
For every screen report: number of requirements, number of independent commands, number of documented controls, implemented/tested counts, extra/deleted/merged controls, unresolved ambiguity and exceptions to hidden-help rule. Mark discrepancies explicitly BLOCKED rather than cosmetically simplifying.

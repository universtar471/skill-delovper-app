# Intake and multimedia reference analysis

## Input channels
Accept Vietnamese descriptions, PDFs/specs, screenshots, hand sketches, videos, sample applications, app-store listings, source repositories. Inventory inputs with file/location, accessibility and date. Do not imply an asset has been opened if only mentioned.

## Workflow
1. Summarize the user goal in plain Vietnamese: audience, main job, target platforms, data source, constraints and success definition.
2. For screenshots: note visible layout hierarchy, labels, controls, states and uncertainties. Identify dimensions, fonts and colors as estimates unless inspected/measured. Do not infer hidden workflows from a single state.
3. For videos: create timestamped observation rows (time, action, visual outcome, confidence). Separate **observed** from **hypothesized**. Note keyboard modifiers, touch gestures, animations and error states only if visible.
4. For sample apps: list behavior to emulate versus behavior to avoid; never copy restricted assets, branding or proprietary code.
5. Convert every observable feature into a user story, trigger, inputs, state change, output, edge cases and acceptance criterion.
6. Identify unknowns: ask only blocking questions. Use reversible assumptions for remaining unknowns.

## Example
Input: “Android app, paste a video link, download then edit in a cartoon UI.”
Output: Screen A URL intake; screen B download status/error; screen C timeline editor; local file picker; output destination; legal/permission checks. Do not assume downloads from arbitrary sources are authorized.

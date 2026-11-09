# AI media Node UX contract (mandatory)

Apply this spec for image/video ingest, generation, editing, upscale, prompt and agent/tool nodes. Pair with `node-graph-execution.md`, `node-workflow-persistence.md`, icon-first and responsive rules.

## Common node shell
- Show compact title, distinct type icon, rename affordance, execution status, relevant selected model (if applicable), and a kebab menu for separate actions. Expose exactly typed input/output ports with visible compatible highlights during wiring.
- Default display is compact. Expand by intentional action; preserve node dimensions in workflow metadata and impose minimum/maximum size with internal scrolling rather than clipping.
- Default actions: Rename; Duplicate; Delete; Convert (only eligible and validated targets); Inspect; Help `?`. Separate actions; menu may group commands but must not merge their semantics. Confirm destructive actions if data loss; support Undo/Redo. Duplicate generates a NEW ID and copies settings but not credentials, live jobs, or outgoing connections by default. Document any different wiring policy.
- The entire node is draggable only from header/drag handle. Clicking text fields, sliders, preview, ports or model menu must NEVER start node dragging. Selection, multi-select, keyboard shortcuts, snap-to-grid, z-order and Undo/Redo must be testable.

## Image / video input and output preview
- Provide a compact thumbnail or video poster in the node body by default; preserve content aspect ratio with letterboxing/contain. For unloaded, running, errored and missing media show explicit placeholder or state, not broken images.
- Click preview to open an image lightbox or video viewer: large resizable modal/side inspector with zoom/fit, pan, file details, resolution, source node/job, compare before/after when applicable, next/previous outputs and download/save only if available. Escape/close returns focus to originating node and never changes execution or node positions.
- On video provide play/pause, timeline scrub, duration, mute if relevant, and poster; delay heavy decoding/lazy load offscreen. Keep preview playback separate from workflow execution. Videos may require signed URLs/permissions.
- Treat original media and generated result as separate immutable asset references. Store file references, media metadata and checksums; never embed large base64 images/videos in workflow JSON. Handle expired remote URLs, missing assets, upload progress and failed transfers.
- Preview click target must not conflict with node drag/pan or wire drag, including touch gestures.

## Text / prompt nodes
- Show collapsed prompt preview (1–3 lines or explicit summary) with ellipsis, character/token indication if available; no gigantic default text block.
- Open inline editor/inspector deliberately. Support pasted or typed user additions, multiline text, templates/variables, optional preset + appended prompt, reset-to-preset, copy, clear, save and validation. Explicitly define whether append replaces or adds to preset and show merged final prompt in inspector.
- Provide prompt version/history and preserve unsaved input; distinguish prompt text from confidential keys or tool instructions. Ensure text editing and undo do not move the node or trigger global shortcuts unexpectedly.

## Per-node model selection
- Show chosen model label next to model icon inside applicable nodes. Picker includes ONLY models eligible for that node operation, connected account, input mode and actual verified execution per `model-capability-discovery.md`.
- Changing model must validate its input/output schema, cost, parameters and existing edges; warn before invalidating cached downstream results or expensive rerun. Store model provider, stable model ID, optional version and settings. Never silently swap models; handle disappearance/permission loss by disabled state and resolution guidance.
- For nodes without an AI model (upload, save, merge), do not fake a model picker.

## Execution animation and accessible status
- Idle: neutral. Queued/waiting: understated pulse and label. Running: subtle animated node border/progress and animated corresponding ACTIVE edge, not every wire. Success: static success mark. Failed: red/error icon with details. Cached/skipped/canceled: distinct static status.
- Animate edge direction ONLY while a real event/job is executing or stream is active. Derive state from execution engine events, not a cosmetic timer. Completed edges stop animating; parallel branches animate concurrently; blocked downstream edges remain still.
- Respect reduced motion and battery saver; provide equivalent text/icon status. Throttle animations in big graphs, only animate visible active edges and avoid hundreds of independent timers.
- Expose node progress where provider supports it; otherwise show indeterminate state, elapsed time and cancel/timeout pathways. Never invent percentage.

## Node conversion
- Offer only target node types with declared migration adapter and compatible ports/parameters. Preview affected connections, model settings and lost values BEFORE committing; allow Cancel. Preserve Node ID only when semantic identity is preserved; otherwise remap IDs/edges as a single undoable graph transaction. Invalid connections must be explicitly repaired or disconnected with review, never silently left broken.

## Acceptance checks
- Image and video thumbnails click through to full viewer and close without changing graph state; no distortion at narrow/zoomed canvas.
- Prompt collapses, expands, appends custom text and persists complete final value; entry does not drag node.
- Model switches change eligible options and correctly invalidate dependent caches; a model without access cannot run.
- Delete, duplicate, rename, convert, move, multi-select, undo/redo each have separate E2E proof.
- Only truly running nodes/edges animate; cancel/fail/retry and reduced-motion modes do not misrepresent execution.

# Image Gallery and Before/After Comparison Nodes

## Image Gallery Node — media selection contract
- Implement `IMAGE_GALLERY_V1` with typed input `images: ImageAsset[]` (minimum 1) and optional `metadata: ImageMetadata[]`; outputs `selected_image: ImageAsset`, `selected_index: integer`, optionally `selected_metadata` and `selection_event` (if control flow is modeled separately). Never silently push all images to a single-image output.
- Gallery displays one selected thumbnail with compact count `3/8`; arrows previous/next, thumbnail strip as expandable inspector, explicit select-for-output action, `?` for help. Click opens image lightbox with fit/zoom/pan and metadata. Mark choice visually, persist stable image ID rather than only index, restore selection after reopen.
- Separate *browse* from *select*: moving arrows previews candidate, explicit Select/Use Output updates downstream output; optional auto-select mode requires owner approval. Selection invalidates only affected descendants, never reruns generation automatically without explicit auto-run setting and cost guard.
- Async image loading uses bounded thumbnails and lazy-loading, maintain aspect ratios, load errors, empty list, missing/deleted assets, duplicate IDs and expiring URLs. Preserve original output assets; NEVER overwrite them on selection.
- Typed port metadata includes MIME, dimensions, source job ID, seed/model when available, hash/reference and permissions; use immutable media references rather than base64 in graph JSON.
- Gallery can merge multiple generators via explicit collection/merge node; do not imply multiple edges into single-image input are legal. Define max items and memory policy.
- Test zero/one/hundreds of images; navigation, selection propagation, lightbox, keyboard/touch, reload, absent assets, and no unintended paid reruns.

## Before/After Comparison Node — pixel alignment and provenance
- Implement `IMAGE_COMPARE_V1` with distinct required `before: ImageAsset` and `after: ImageAsset`; optional compare label/mode; output `comparison_metadata` and optionally `selected_image: ImageAsset` ONLY on explicit user choice. Comparison is a review tool and must not create altered pixels unless user requests export of merged comparison image.
- Show synchronized pan/zoom, accessible slider divider, side-by-side option, fit and reset; respect image orientation and aspect ratio. If dimensions differ, declare contain/letterbox policy or user-approved alignment/crop; never secretly stretch, reproject or crop architectural geometry.
- Display provenance and resolution for both sides. Highlight if either input is missing, video is connected to image-only input, or dimensions differ significantly; block or request explicit alignment depending on contract.
- Inspector offers independent full resolution/zoom, overlay if supported; compact node shows before/after split preview and expands on click. Use visible icon for compare and `?` for explanation.
- For high-resolution 2K/4K/8K, load preview pyramids/downsampled proxies where needed; full resolution only on demand. Avoid allocating two full images in every graph thumbnail.
- Test 2 input ports, same/different dimensions, missing input, slider at ends, identical-image baseline, keyboard and touch drag without moving node, and export provenance.

## Shared UI guardrails
- Drag node ONLY from header. Preview interactions do not pan graph, connect wire or initiate node drag.
- Node menu provides separate Rename, Duplicate, Convert, Delete with confirmations and undo rules. Gallery/compare source asset IDs must survive duplication only as authorized references.
- Both nodes display runtime status, errors and cache label; no fabricated processing animation for pure UI-only preview operations.

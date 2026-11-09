# Architecture Consistency Checker Node (proposal until implemented)

## Purpose
Compare a source SketchUp/render/reference image with an AI-generated result to flag possible changes to building geometry, roof edges, doors/windows, structure, materials, lighting, and context. It is an assistant for human review, not a structural truth engine.

## Node contract
- Type ID: `ARCH_CONSISTENCY_V1` with typed ports `original:IMAGE`, `generated:IMAGE`, optional `regions:MASK/ROI`, and `report:JSON` plus optional `overlay:IMAGE`.
- Inputs: original asset ID, candidate asset ID, declared viewpoints/camera transform if available, protected material/geometry regions, sensitivity per category.
- Outputs: categorized observations, region references, severity, confidence with calibration note, heatmap/overlay, reviewer decision, optional downstream gate `APPROVED/REVIEW_REQUIRED`.
- Comparing different camera angles without registration leads to false positives. If viewpoints cannot be registered, flag `INSUFFICIENT_COMPARABILITY` rather than claiming a geometry error.
- Use image alignment plus region/object extraction where supported. Distinguish material or lighting variability from changed architecture; metadata and user annotations override image-only assumptions.
- Human must approve critical geometry decisions. Never alter original design automatically based only on a score.
- No model/provider is pre-approved by the Skill: apply Model Capability Discovery and live access tests.

## Acceptance tests
Same-view geometry preserved; deliberate window position change; missing roof fascia; shadow-only difference; different crop; different camera viewpoint; occluded facade; tiny image; incompatible aspect ratio. Measure false positives/negatives on user-reviewed examples and record actual results.

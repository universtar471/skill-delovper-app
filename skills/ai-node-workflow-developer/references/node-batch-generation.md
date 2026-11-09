# Batch Generation Node — bounded AI jobs

## Node contract
- `IMAGE_BATCH_GENERATE_V1`: typed inputs `prompt: Text` or `prompts: Text[]`, optional `reference_images: ImageAsset[]`, `seed: integer?`, `settings`; typed outputs `results: ImageAsset[]`, `job_manifest: BatchManifest`, `failures: ErrorRecord[]`, `selected_image: ImageAsset?` only on explicit selection.
- Define **batch dimension** (variants, camera, lighting, material, seeds, prompt matrix), total job count as product of dimensions, and exact mapping of each output to prompt/seed/model/settings and reference assets.
- Expose one per-node *verified* model picker filtered by operation, user credentials, reference-image support, permitted output resolution, available quota. Never show text-only models or incompatible API credentials.
- Compact UI: selected model label, number of variants, estimated number of requests/cost (only when grounded), Run/Cancel, queue status, small result strip, link to expanded Gallery. Put advanced dimensions and instructions in inspector or `?`.

## Run safety and sequencing
1. Validate prompts and input assets, explicit limit on combinations and total jobs, accessible service/adapter, model capabilities and quotas.
2. Show computed job count and estimated cost; require user confirmation above budget threshold, when unknown price, or when large batch could create unbounded cost. Do not auto-run when a graph wire is attached.
3. Create immutable batch ID and per-job idempotency key. Dispatch through controlled scheduler with bounded concurrency, provider rate limits, timeout, exponential backoff and only safe retries. Never blindly retry charged or side-effecting jobs.
4. Show each job as queued/running/success/failed/canceled/unknown, plus overall progress based on terminal job counts. Do not invent provider percentages. Cancel queued jobs and request cancellation of active ones where supported; report partial completion and any jobs with uncertain status.
5. Validate media outputs, save results and per-job metadata; return a result array and manifest. A partially failed batch is not automatically a fully verified workflow. Explicit partial-output policy needed to pass downstream results.
6. Keep outputs immutable and cache by job spec with careful handling of random seed and nondeterministic providers. Changing model/seed/prompt invalidates only matching jobs and downstream nodes. Re-run failed items separately with consent and duplicate protection.

## State persistence
- Save workflow definition and batch parameters separately from run results. Store batch run manifest and media asset references outside workflow JSON; no API secrets or embedded large base64 images.
- Restoring a graph must show completed/failed/missing assets honestly and never restart a billed batch without user confirmation. Template verification requires successful E2E evidence for required outputs.

## Test matrix
- Single job, multiple variants, Cartesian explosion prevention, rate-limit 429, 401/403, quota exhausted, 5xx, timeout, payment uncertainty, partial failure, crash/restart, cancellation race, duplicate clicks, offline run, select-result propagation, large image previews, reduced motion and restore.

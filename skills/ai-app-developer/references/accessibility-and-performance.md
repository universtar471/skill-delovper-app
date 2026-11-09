# Accessibility and Performance Guardrails

- Icon-first is not icon-only semantics: each clickable icon needs accessible name, keyboard operability when applicable, clear focus indication, tooltip or contextual `?` and distinguishable states without relying on color alone.
- Keep labels and critical errors visible when necessary. Do not hide essential accessibility instructions, costs or irreversible consequences behind a tooltip.
- Test common viewport sizes, platform font scaling, high DPI, Windows display scale, Android text size and reduced motion. Verify that panel controls remain reachable with keyboard/screen reader/touch.
- Measure startup time, memory, frame time and key action latency in the actual target environment; define app-specific budgets before testing rather than asserting invented universal values.
- For large image/video previews virtualize offscreen content, release unused texture/buffer objects, and avoid loading full-resolution assets into every thumbnail.
- Under resource pressure prefer graceful quality reduction/pagination, never silent data loss or hidden pending operations.
- Record results in `ACCESSIBILITY_TEST_MATRIX.csv` and `PERFORMANCE_BUDGET.csv`.

# ChatGPT ↔ Codex ↔ Claude Code coordination

## Shared source of truth
Use tracked Markdown docs in `docs/`: PROJECT_BRIEF, SPEC, ARCHITECTURE, TASKS, DECISIONS, TEST_REPORT, PROGRESS. The agent must inspect these and `git status` before work.

## Assignment discipline
1. Give a single scoped task with goal, files to inspect/change, forbidden changes, acceptance criteria and commands to run.
2. Reserve a branch/task owner per overlapping file set. Prefer sequential edits. Never merge competing changes without review.
3. Ask coding agent to produce a diff and list test commands and their exact outcomes. A successful command must be observed, not presumed.
4. Review feature acceptance, regressions, dependencies, accessibility and secret leaks before merge.
5. Update docs and a concise handoff entry: changed files, commit/hash if known, tests, failures, next task.

## Copy-ready agent task
```text
Bạn là Coding Agent trong dự án [tên]. Đọc README, docs/SPEC.md, docs/ARCHITECTURE.md, docs/TASKS.md và git status trước khi sửa. Chỉ thực hiện [ID và tên task]. Không thay đổi yêu cầu đã duyệt. Đề xuất cách làm ngắn trước khi sửa. Viết code thật; thêm test cho logic mới; chạy lệnh build/test nếu môi trường cho phép. Báo cáo: file sửa, hành vi, lệnh và kết quả thực tế, lỗi tồn đọng, hướng rollback. Không tuyên bố chạy thành công khi chưa chạy. Nếu thiếu quyền/công cụ, nói rõ.
```

## Platform instructions
ChatGPT may prepare/inspect only through tools it actually has. Codex and Claude Code may operate on files/terminal only when installed, authorized and connected. Treat tool availability as a runtime fact, not a product promise. Do not paste secrets into shared chat prompts.

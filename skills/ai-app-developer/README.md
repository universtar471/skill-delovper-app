# AI App Developer — Skill cài đặt

Skill hỗ trợ người không chuyên lập trình xây dựng ứng dụng Android, Windows, Web qua ChatGPT/Codex/Claude Code. Đầu vào: mô tả tiếng Việt, ảnh/video, app/repo tham khảo. Đầu ra: đặc tả, thiết kế, nhiệm vụ code, quy trình test và bàn giao có bằng chứng.

## Cách sử dụng
1. Cài file `skill.zip` thông qua thư viện Skills của môi trường hỗ trợ.
2. Yêu cầu: “Dùng AI App Developer phân tích ý tưởng [mô tả] và tạo MVP cho Android/Windows/Web.”
3. Khi có repository, cho Agent quyền truy cập repo và công cụ build/test phù hợp. Skill không tự cung cấp IDE, runtime, SDK hay API.
4. Cho Agent xem ảnh/video tham chiếu có quyền sử dụng và hỏi nó phân biệt quan sát/giả định.
5. Dùng `scripts/create_project_docs.py --project <thư_mục>` để khởi tạo tài liệu dự án. Sau khi điền thông tin, kiểm tra bằng `scripts/validate_project.py --project <thư_mục>`.

## Giới hạn
ZIP là bộ hướng dẫn/tiện ích, không phải một ứng dụng đã build. Agent chỉ có thể chạy test, tạo APK/EXE hoặc deploy khi môi trường có công cụ và quyền tương ứng. Các nền tảng có thể có cách cài Skill khác nhau; với môi trường không nhận ZIP trực tiếp, dùng nội dung SKILL.md và references làm hướng dẫn dự án.

## Bản nâng cấp: Fidelity-first UX/UI
Tham khảo `references/ui-reference-catalog.md` (8 kho UI), `references/ui-source-research.md`, `references/fidelity-contract.md`, `references/interactive-prototype-gates.md`. Dùng mẫu `ui-reference-evaluation.md`, `interaction-contract.md`, `traceability-matrix.csv`, `deviation-log.md`, `change-request.md`.
Chạy `python scripts/audit_traceability.py docs/traceability-matrix.csv` để kiểm tra liên kết ID và bằng chứng; script không chạy kiểm thử ứng dụng.

## Quy chuẩn bố trí mới: Icon-first UI Lock
Mọi màn hình mặc định tinh gọn, ưu tiên icon rõ nghĩa và ít chữ; ghi chú/hướng dẫn dài đặt sau dấu `?` gần đối tượng. Các nhãn thiết yếu, lỗi và trạng thái quan trọng vẫn được hiển thị rõ và hỗ trợ tiếp cận. Mỗi thao tác độc lập có CTRL ID, input/output, trạng thái và test riêng; không được gộp các chức năng không liên quan thành nút chung. Tham khảo `references/icon-first-ui-lock.md`, `references/control-behavior-spec.md`, `assets/templates/control-inventory.csv` và `assets/templates/control-contract.md`.

### Quy chuẩn bổ sung: Preview, khung chia, phóng to/thu nhỏ
Đọc `references/responsive-preview-layout.md` và `references/layout-qa-and-zoom.md`. Dùng `assets/templates/panel-layout-contract.md` để khóa kích thước tối thiểu/tối đa và chế độ co gọn của từng khung. Dùng `assets/templates/layout-test-matrix.csv` để ghi kiểm thử resize, zoom giao diện và zoom nội dung riêng biệt. Không chấp nhận nút đè nhau, mất nút, chữ tràn, popup vượt màn hình hoặc Preview không còn sử dụng được.

## Capability-first integration lock
Before creating any enabled action control, verify how its local/API/MCP/CLI capability will execute and how failures will be shown. See `references/api-mcp-cli-integration.md`, `references/agent-connection-architecture.md`, `references/integration-testing.md`; generate control/capability mapping templates and run `scripts/audit_control_bindings.py` for static pre-release audits. Real end-to-end tests remain mandatory.

## Model selector theo chức năng
Không hiển thị toàn bộ model trên thị trường. Agent phải kiểm tra loại tác vụ, API/MCP/CLI thực tế, quyền và kết quả chạy thử trước khi đưa vào danh sách model sẵn sàng. Chi tiết: `references/model-capability-discovery.md`; mẫu tại `assets/templates/model-*`; kiểm tra tĩnh bằng `scripts/audit_model_selector.py`.

### Node workflows for AI image/video
New references cover interactive thumbnails and video viewers, collapsed/appendable prompts, per-node eligible models, animated active wires driven by execution events, separate node actions, movable/auto-layout nodes and verified workflow saving. See `references/node-ai-media-ux.md` and `references/node-e2e-qa.md`.

## Media node trio update
Gallery lựa chọn ảnh, so sánh Before/After và Batch Generate được đặc tả riêng với kiểm thử E2E, bảo toàn ảnh gốc, kiểm soát chi phí và lưu kết quả. Xem `references/node-gallery-and-comparison.md`, `references/node-batch-generation.md`, `references/node-media-trio-e2e.md`.

## Acceptance Gate System and dedicated node skill
The new project templates include ACCEPTANCE_GATES.csv, REQUIREMENT_COVERAGE.csv, VISUAL_BASELINES.csv, DEPENDENCY_API_AUDIT.csv, PROJECT_CONTEXT.md and ROLLBACK_PLAN.md. Run the corresponding stdlib-only `scripts/audit_*.py` checks, then independently verify actual builds and live behaviors. The dedicated `AI Node Workflow Developer` skill can be installed separately for graph-specific design and execution; this app skill retains the existing node documentation for backwards compatibility.

## Dry Run / Provenance / Workflow Debugger
The app skill additionally retains Node workflow guidelines for backwards compatibility. For large Node applications install AI Node Workflow Developer separately and follow `references/skill-collaboration-contract.md`. Check `references/workflow-dry-run.md` and use `scripts/dry_run_workflow.py` with registered node types. Dry run does NOT execute paid model calls or certify connectivity.

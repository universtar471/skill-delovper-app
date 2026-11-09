# AI App Developer + AI Node Workflow Developer

Bộ đôi Skill để phát triển, kiểm toán và nâng cấp ứng dụng Android, Windows, Web và các ứng dụng Node-based tạo ảnh/video AI.

## Hai Skill

| Skill | Mã nguồn (đọc/sửa trên GitHub) | ZIP đầy đủ để tải và cài đặt |
| --- | --- | --- |
| **AI App Developer** | [skills/ai-app-developer](skills/ai-app-developer) | [skill.zip](releases/ai-app-developer/skill.zip) |
| **AI Node Workflow Developer** | [skills/ai-node-workflow-developer](skills/ai-node-workflow-developer) | [skill.zip](releases/ai-node-workflow-developer/skill.zip) |

Mỗi bộ Skill được đặt trong thư mục riêng gồm `SKILL.md`, `agents/`, `references/`, `scripts/`, `assets/` và `tests/`. **Hai ZIP là hai Skill độc lập**, mỗi lần cài đặt chọn một ZIP, không gộp chúng thành một Skill.

### Tính năng chính

- **AI App Developer:** UI/UX icon-first, so sánh với giao diện tham chiếu, code cho Android/Windows/Web, API/MCP/CLI, chọn model khả dụng, kiểm tra repo app, Visual Regression, Requirement Coverage, Acceptance Gate, build và rollback.
- **AI Node Workflow Developer:** Editor Node/dây nối, Workflow Engine, Dry Run, nối đúng loại dữ liệu, Preview ảnh/video ngay trên Node, Prompt thu gọn, chọn model trực tiếp, animation chạy, Image Gallery, Before/After, Batch Generation, Debugger, provenance và nghiệm thu Workflow.

### Cài đặt

1. Tải `skill.zip` của từng bộ trong bảng trên.
2. Mở trang Skills của ChatGPT để thêm từng ZIP riêng; hoặc dùng nội dung `SKILL.md` và tham chiếu trong dự án Codex/Claude Code.
3. Khi kiểm tra repo có sẵn, yêu cầu Agent **chỉ audit/báo cáo trước**, không tự sửa hoặc xóa chức năng mà chưa được duyệt.

### SHA-256 của ZIP gốc

- App Developer: `c8f12a1bd3df8dcaaaa86e61af13eafb47c5cf6bcd47e7f9ede3d70a14e23bd4`
- Node Workflow Developer: `2f63aa91e9ab39825085c9bb9661967949613a0d8bb19b4f8a9847b126a598fe`

> Quy tắc: mock/fixture không phải API thật; phải có bằng chứng test/hoạt động trước khi báo hoàn thành.

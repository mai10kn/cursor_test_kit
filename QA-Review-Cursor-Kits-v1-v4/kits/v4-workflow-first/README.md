# QA Review v4 — Workflow First

Đọc `WORKFLOW.md` đầu tiên: đây là **tài liệu thiết kế v4.0 trước khi cải tiến templates**, được sao chép nguyên nội dung từ Starter Kit trước đó.

## Chạy trong Cursor

1. Mở thư mục `v4-workflow-first` riêng biệt.
2. Agent `/qa-review quick` với `input/requirements.md` + `input/testcases.csv`.
3. Yêu cầu tạo `output/findings.json` theo `EVALUATION_SCHEMA.md`, `output/review-sheet.csv`, `output/input-manifest.md` và summary. Quick tối đa 50 TC/module/batch; không tự nâng lên Full.
4. Sau khi có CSV, tạo Excel dropdown bằng script `scripts/make_review_xlsx.py` (cần Python và `artifact_tool` trên máy chạy) hoặc xem file ví dụ `templates/review-sheet-demo.xlsx`.
5. Với Delta: dùng `input/old-requirement.md`, `input/new-requirement.md` và `input/delta-testcases.csv`; với UAT: `input/uat-requirements.md` + `input/uat-feedback.csv`.
6. Independent Audit: mở một phiên Agent mới, cho `qa-auditor` đọc **raw input và output đã có**, không đưa chain-of-thought/lập luận trước đó.

**Trạng thái:** V4 workflow/Skill là thiết kế + hướng dẫn. Excel demo xác minh tính năng dropdown trên dữ liệu giả lập; việc tự động bảo toàn formatting phức tạp của file dự án thật cần kiểm thử riêng. Chưa chạy các version trong Cursor, không có precision/recall thực tế.

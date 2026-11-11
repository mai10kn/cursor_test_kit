# QA Review V1 — Cursor workspace độc lập

**Bước đầu:** đọc [`WORKFLOW.md`](./WORKFLOW.md) để hiểu thiết kế; không sửa Requirement/Test Case khi đang benchmark.

1. Mở đúng thư mục này bằng Cursor > File > Open Folder.
2. Mở Agent và nhập `/qa-review Review input/requirements.md với input/testcases.csv. Xuất output/findings.json theo schema trong README hoặc WORKFLOW.`
3. Lưu toàn bộ kết quả vào `output/`. Output có thể khác nhau giữa các version; riêng `findings.json` có schema chung được mô tả trong `../../evaluation/SCHEMA.md` ở ZIP tổng (có bản copy tại `EVALUATION_SCHEMA.md` ngay trong thư mục này).
4. Đóng session, chuyển sang workspace phiên bản tiếp theo.

**Chú ý:** `/qa-review` là Cursor Skill, không phải tiện ích CLI chạy trực tiếp từ terminal. Nếu slash không hiển thị, mở `.cursor/skills/qa-review/SKILL.md` và @-mention file trong Agent. Chưa tích hợp Jira/Figma live.

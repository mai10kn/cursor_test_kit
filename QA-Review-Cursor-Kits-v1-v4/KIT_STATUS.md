# Trạng thái và giới hạn bộ kit

| Thành phần | Trạng thái |
|---|---|
| `WORKFLOW.md` bốn version | Đã tạo và kiểm tra file tồn tại |
| `.cursor/skills/qa-review/SKILL.md` bốn version | Đã tạo; frontmatter và cấu trúc được kiểm tra tĩnh |
| v1 legacy command `.cursor/commands/review-testcases.md` | Đã cung cấp để tái hiện v1 |
| Input QA Core chung 10 TC | Đã đồng nhất bytes ở cả bốn workspace |
| Golden labels 7 finding | Có, lưu riêng ngoài workspace để tránh leak |
| Comparator precision/recall/F1 | Có; báo NOT_RUN khi chưa có output AI |
| Fixture Delta và UAT | Có, để thử riêng trên v3/v4 theo phạm vi |
| Excel demo của v4 (dropdown) | Có, đã kiểm tra bên trong `.xlsx` có dataValidation |
| Script chuyển CSV → XLSX | Có; cần `artifact_tool` ở môi trường Python |
| Chạy thật trong Cursor | **Chưa**. Cần mở từng folder và gọi `/qa-review` |
| Kết quả Precision/Recall thực tế | **Chưa**. Không gán điểm giả cho các version |
| Tích hợp Jira, Figma, Google Sheets | **Chưa**. Ngoài scope của bộ thử nghiệm workflow |

**Quan trọng:** Bốn bản mô tả sự tiến hóa thiết kế, không phải mã nguồn của một plugin đã triển khai chức năng tự động hoàn chỉnh. `WORKFLOW.md` của v4 được sao chép từ starter workflow-first trước đó; các phiên bản v1–v3 được tái dựng theo nội dung hội thoại và tài liệu người dùng cung cấp.

# So sánh mục tiêu của 4 workflow

| Tiêu chí | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| REQ ↔ TC | Có | Có | Có | Có |
| VP trung gian | Không | Có | Có | Có |
| Review 9 tiêu chí | Cơ bản | Có | Có | Có |
| Gap theo nguồn bằng chứng | Cơ bản | Có | Có | Có, Input Manifest |
| RBT/Regression | Gợi ý chung | Có | Có | Chạy có điều kiện |
| BA: goal, AC, Q&A | Không | Trọng tâm thấp | Bắt buộc trong Full | Bật theo phạm vi |
| Persona/UAT | Không | Kịch bản E2E kỹ thuật | Có | Có, UAT triggers |
| Delta requirement | Không | Chạy lại vùng thay đổi | Impact analysis | Mode Delta riêng |
| Human approval | Khuyến nghị | Cuối chu trình | Gate theo lớp | Gate A (AC) + Gate B (TC) |
| Golden set & feedback | Không | Có khuyến nghị | Có khuyến nghị | Bắt buộc cho rollout |
| Tester-facing output | Markdown | Report + matrix | CSV/sheet | Excel + dropdown + JSON |
| Khối lượng vận hành | Nhẹ | Trung bình–nặng | Nặng nếu Full | Quick nhẹ, Full khi chọn |

**Cách đọc kết quả:** Một phiên bản nhiều phát hiện hơn chưa chắc tốt hơn: đo TP/FP/FN, việc sử dụng bằng chứng, số phút người review và tính hữu dụng của đầu ra. Bộ dữ liệu QA Core so sánh tất cả v1–v4. Bộ BA/UAT chỉ so v3–v4 vì v1/v2 không được thiết kế cho hai nhiệm vụ này.

## Không trộn rule

Mỗi kit có thư mục `.cursor/` riêng. **Không** copy `.cursor` của cả bốn vào cùng workspace hoặc mở thư mục tổng trong Cursor khi chạy thử. Cùng tên skill `/qa-review` là chủ ý để so sánh công bằng.

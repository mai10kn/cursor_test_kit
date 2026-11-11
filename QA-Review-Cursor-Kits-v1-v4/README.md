# QA Review Cursor Kits — 4 phiên bản độc lập

**Mục tiêu:** Thử nghiệm công bằng bốn workflow QA Review trên cùng Requirement và Test Case, trước khi thay đổi file nghiệp vụ thực tế của dự án.

## Bắt đầu

1. Giải nén ZIP tổng. Chỉ mở **một** thư mục `kits/vX-*` bằng Cursor mỗi lần. Đừng mở thư mục tổng như một workspace để tránh nạp nhiều Rule/Skill cùng lúc.
2. Trong từng workspace, **đọc `WORKFLOW.md` trước**, sau đó mở Cursor Agent và nhập `/qa-review` (thêm `quick`, `full`, `delta` hay `uat` tùy version).
3. Sample đầu vào đã được sao chép vào `input/` của từng bộ và **giống hệt nhau cho QA core**. Không đưa file nhãn `evaluation/ground-truth/` vào ngữ cảnh AI khi chạy.
4. Yêu cầu AI xuất `output/findings.json` theo schema trong `EVALUATION_SCHEMA.md` của từng kit; lưu thêm đầu ra người dùng của version tương ứng.
5. Quay về thư mục tổng và chạy `python evaluation/compare_versions.py` để tính điểm từ findings của cả bốn bộ.

**Dễ bắt đầu nhất:** mở `kits/v1-basic`, nhập `/qa-review Review input/requirements.md với input/testcases.csv và lưu kết quả vào output/`. Sau đó thử tương tự ở v2–v4.

## Các phiên bản

| Thư mục | Thiết kế gốc | Điểm vào trong Cursor | Output chính |
|---|---|---|---|
| `kits/v1-basic` | REQ ↔ TC, 4 bước | `/qa-review` (skill) hoặc `/review-testcases` (command) | `review-report.md` |
| `kits/v2-viewpoint-risk` | REQ → VP → TC, 8 phase nội bộ | `/qa-review` (skill) | `coverage-matrix.md`, `review-report.md` |
| `kits/v3-ba-qa-uat` | 3 lớp, 9 phase; BA/QA/UAT | `/qa-review` (skill), mode `quick/full/uat` | `review-sheet.csv`, BA/UAT artifacts theo mode |
| `kits/v4-workflow-first` | 1 lệnh, 3 lớp bật theo scope; quick cap, delta, audit | `/qa-review` (skill), `quick/full/delta/uat` | `review-sheet.xlsx`, `review-sheet.csv`, manifest |

## File dùng để so sánh

- `VERSION_COMPARISON.md`: phạm vi và điểm mạnh/yếu theo phiên bản.
- `EVALUATION_GUIDE.md`: trình tự thử nghiệm, thước đo, tránh bias.
- `evaluation/SCHEMA.md`: schema `findings.json` chung; bắt buộc để chấm kỹ thuật công bằng.
- `evaluation/compare_versions.py`: tính Precision, Recall, F1 từ kết quả AI thực sự sinh ra; nếu chưa chạy AI sẽ báo thiếu dữ liệu, không bịa số.
- `fixtures/qa-core/`: bộ dữ liệu giả lập dùng cho cả bốn version.
- `fixtures/change-delta/`, `fixtures/uat-feedback/`: bài thử bổ sung, chỉ dùng để so năng lực v3/v4; v1/v2 ghi `N/A`.

## Tài liệu thiết kế và nguồn tham khảo

- v1 phản ánh workflow ban đầu trong hội thoại: trích REQ → map TC → kiểm thiếu → báo cáo.
- v2 kết hợp 7 giai đoạn của tài liệu `Workflow AI verify testcase vs requirement...docx` với các bài học Test Viewpoint, Risk-Based Testing và 9 tiêu chí review.
- v3 dựa trên `Đánh giá và phương án cải tiến workflow v3 tester kiêm BA và kiểm thử người dùng.docx`: BA/QA/UAT, 9 phase.
- v4 giữ nguyên **file WORKFLOW.md v4.0-design đã tạo trước đó**, dùng Skill + Rule + Auditor riêng; có thêm công cụ/template để thử nghiệm công bằng.

**Lưu ý:** Đây là 4 kit thiết kế và prompt đã đóng gói, không phải 4 kết quả AI đã chạy trong Cursor. Không cung cấp kết quả Precision/Recall giả. Không upload dữ liệu khách hàng khi chưa được phép.

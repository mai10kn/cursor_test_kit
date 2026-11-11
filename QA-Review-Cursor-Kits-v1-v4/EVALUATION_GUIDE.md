# Hướng dẫn thử nghiệm và chấm điểm

## A. Điều kiện so sánh

- Cùng model Cursor, cùng thinking effort, cùng ngôn ngữ tiếng Việt, cùng input `input/requirements.md` + `input/testcases.csv`.
- Chạy **từng version trong cửa sổ/phiên Agent mới**, không truyền finding của version khác.
- Không cho Agent đọc `evaluation/ground-truth/` khi chạy, vì sẽ gây rò đáp án.
- Giữ nguyên input, không sửa dữ liệu; lưu lịch sử theo `run ID`, prompt, model, version, reviewer minutes.
- Kiểm tra Input Manifest hoặc danh sách file thực đọc; nếu chỉ đọc một phần thì không đưa vào so sánh coverage tổng.

## B. Quy trình

1. Đọc `WORKFLOW.md` của version.
2. Trong workspace đó, nhập: `/qa-review Review input/requirements.md với input/testcases.csv. Xuất findings theo evaluation schema và output chính của version. Không xem ground truth.`
3. Sau khi Agent hoàn tất, xác nhận `output/findings.json` tồn tại và có cấu trúc đúng; không tự sửa finding để tăng điểm.
4. Tiếp tục version tiếp theo ở phiên mới.
5. Từ thư mục tổng: `python evaluation/compare_versions.py`. Script chỉ đo QA Core; các chỉ số BA/UAT cần chạy bộ test riêng và ghi rõ scope.
6. Tester chấm mức hữu ích 1–5 và số phút thao tác; lưu vào `evaluation/reviewer-notes.csv` (không bịa số nếu chưa ghi).

## C. Thước đo

- Precision = TP/(TP+FP); Recall = TP/(TP+FN); F1 = trung bình điều hòa. Script dùng cặp `(tc_id, code)` để giảm việc AI "nói nhiều" nhưng đánh không đúng.
- Evidence Quality: tỷ lệ finding có nguồn thật, kiểm thủ công; không tự lấy chữ "evidence" trong JSON làm bằng chứng hợp lệ.
- Review Effort: số phút người review thực tế.
- User Utility: tester quyết định liệu nội dung có giúp sửa TC/đặt câu hỏi không.
- "Có báo cáo" hoặc "có nhiều TC mới" không phải thước đo thành công.

## D. Bài thử BA/UAT (v3 và v4)

`fixtures/change-delta/`: old/new requirement, TC affected. Chấm missed/false affected IDs.

`fixtures/uat-feedback/`: Feedback cần phân loại. Không ép đánh giá persona suy đoán. Kết quả phải có căn cứ từ AC/feedback.

## E. Phạm vi công cụ

- Cursor Skills: `.cursor/skills/<name>/SKILL.md`, gọi `/qa-review`; mỗi kit chứa điểm vào như nhau.
- v1 còn giữ legacy command trong `.cursor/commands` để đúng tinh thần ban đầu.
- Script score là công cụ deterministic; chưa thay thế được tester xác minh finding bằng chứng.
- Excel v4 là **bản minh họa với dropdown**; khi review file TC dự án thực tế cần bảo toàn dữ liệu/style/sheet và kiểm tra nhập/xuất riêng.

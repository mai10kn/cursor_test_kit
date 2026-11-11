# Schema so sánh findings (QA Core)

Cả 4 version phải xuất một file `output/findings.json`:

```json
{
  "run_id": "demo-v1-001",
  "version": "v1",
  "input_scope": "qa-core",
  "source_files": ["input/requirements.md", "input/testcases.csv"],
  "issues": [
    {"tc_id":"TC-002", "code":"INCORRECT_EXPECTED", "source":"AC-02", "reason":"Expected trái quy tắc khóa sau 5 lần"}
  ]
}
```

Codes chuẩn hóa để tính điểm:

- `INCORRECT_EXPECTED`: expected trái đặc tả đã xác nhận.
- `BOUNDARY_MISSING`: chỉ test bên trong ngưỡng, thiếu giá trị cạnh biên.
- `PERMISSION_MISSING`: thiếu case quyền truy cập cần thiết.
- `EMAIL_CHECK_MISSING`: thiếu checkpoint email khi AC có mail.
- `DUPLICATE`: test case trùng cần xem xét.
- `UNSUPPORTED_EXPECTED`: expected không có nguồn spec, cần làm rõ thay vì khẳng định.

**Lưu ý:** Không được ép mọi phần chưa được đặc tả thành Confirmed Gap. Nếu cần ghi `POTENTIAL_RISK`/`NEED_CLARIFICATION` trong báo cáo mở rộng, mã chuẩn chỉ dùng cho nhóm issue có nhãn ở benchmark. File `findings.json` có thể thêm các trường phụ, script chỉ dùng `issues[].tc_id` và `issues[].code`.

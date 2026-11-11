# Test Viewpoint Catalog — v2 seed (starter)

| VP type | Áp dụng khi | Ví dụ kiểm tra |
|---|---|---|
| Functional | Có action | Submit đúng nghiệp vụ |
| Input | Field được định nghĩa | Required/format |
| Boundary | Có min/max/threshold | min-1/min/max/max+1 |
| State | Có trạng thái | Chuyển trạng thái hợp lệ và không hợp lệ |
| Permission | Có quyền theo role | Không truy cập dữ liệu của role/store khác |
| Integration | Liên kết email/API/provider | Kết quả bên thứ ba và lỗi tích hợp |
| Data integrity | Thao tác ghi dữ liệu | DB/UI đồng bộ |
| Resilience | Lỗi mạng/retry | Không nhân đôi thao tác |
| Localization | Có locale | Nhật/Anh/Trung theo yêu cầu |

Chỉ áp dụng VP hợp lý với REQ; VP AI đề xuất không phải AC đã phê duyệt. Chủ catalog ở v2 chưa có cơ chế version/owner hoàn chỉnh; đây là chỗ so sánh với v4.

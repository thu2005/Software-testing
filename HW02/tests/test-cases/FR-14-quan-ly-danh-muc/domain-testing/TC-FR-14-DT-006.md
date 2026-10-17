# TC-FR-14-DT-006: Từ chối user thường xóa danh mục qua API

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Role trong token | Điều kiện phân quyền | User, không phải Admin |
| Danh mục mục tiêu | Trạng thái | Tồn tại để kiểm tra dữ liệu không đổi |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-006 | EC-AUTH-I02, EC-ACTION-V03 | DELETE `DM-FR14-BAOVE` bằng token user | EC-RESULT-O05 | Request bị từ chối; danh mục vẫn tồn tại. |

## Điều kiện tiên quyết

- Danh mục `DM-FR14-BAOVE` tồn tại.
- Có JWT hợp lệ của tài khoản user mặc định.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tài khoản lấy token | `test@eshop.com` / `Test1234!` |
| Request | `DELETE /api/categories/:id`, với `:id` lấy từ dòng `DM-FR14-BAOVE` trong danh sách hiện tại |

## Các bước kiểm thử

1. Đăng nhập tài khoản user mặc định để lấy JWT hợp lệ.
2. Gửi DELETE tới ID của `DM-FR14-BAOVE` với token user.
3. Ghi nhận response.
4. Dùng phiên Admin xem lại danh sách.

## Kết quả mong đợi

Request bị từ chối vì role không phải Admin; `DM-FR14-BAOVE` vẫn tồn tại. Requirement không quy định HTTP status hoặc thông báo cụ thể.

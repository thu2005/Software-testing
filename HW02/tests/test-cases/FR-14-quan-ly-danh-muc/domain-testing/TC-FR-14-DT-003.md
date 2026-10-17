# TC-FR-14-DT-003: Từ chối thêm danh mục có tên rỗng

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-14](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud), [FR-22](../../../../requirements/system-requirements.md#fr-22-form-requirements); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR14-003](../../../../bug-reports/BUG-FR14-003.md) ([Issue #13](https://github.com/thu2005/CSC13003_eshop/issues/13)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Tên danh mục | Chuỗi bắt buộc | Rỗng là không hợp lệ |
| Vị trí lỗi | Output UI | Phía trên nút submit |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-003 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-I01 | Tên `""` | EC-RESULT-O03 | Hiển thị lỗi phía trên nút submit; không tạo danh mục. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin và mở mục Danh mục.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên danh mục | Chuỗi rỗng `""` |

## Các bước kiểm thử

1. Để trống trường tên danh mục.
2. Bấm nút thêm danh mục.
3. Quan sát thông báo lỗi và danh sách.

## Kết quả mong đợi

Hệ thống từ chối thao tác, hiển thị lỗi phía trên nút submit và không tạo thêm danh mục. Nội dung chính xác của thông báo chưa được đặc tả.

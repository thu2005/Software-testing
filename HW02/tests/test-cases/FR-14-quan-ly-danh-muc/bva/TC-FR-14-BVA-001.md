# TC-FR-14-BVA-001: Tên danh mục tại cận rỗng 0 ký tự

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [FR-14](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud), [FR-22](../../../../requirements/system-requirements.md#fr-22-form-requirements); [bva-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Độ dài tên `L` | `L > 0` | Cận dưới mở | `0` | `δ = 1` ký tự | `-1` không khả thi | `0` không hợp lệ | `1` hợp lệ |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-14-BVA-001 | BV-NAME-001 | `""`, `L = 0` | ON | Admin hợp lệ; form Danh mục | Từ chối, hiển thị lỗi phía trên nút submit và không tạo danh mục. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin và mở mục quản lý Danh mục.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên danh mục | Chuỗi rỗng `""` |
| Độ dài | `L = 0` ký tự |

## Các bước kiểm thử

1. Để trống trường tên danh mục.
2. Bấm nút thêm danh mục.
3. Quan sát vị trí lỗi và danh sách.

## Kết quả mong đợi

Hệ thống từ chối tên rỗng, hiển thị lỗi phía trên nút submit và không tạo danh mục mới. Nội dung chính xác của thông báo chưa được đặc tả.

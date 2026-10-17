# TC-FR-14-BVA-002: Tên danh mục tại giá trị nhỏ nhất hợp lệ 1 ký tự

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [bva-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Độ dài tên `L` | `L > 0` | Cận dưới mở | `0` | `δ = 1` ký tự | `-1` không khả thi | `0` không hợp lệ | `1` hợp lệ |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-14-BVA-002 | BV-NAME-002 | `A`, `L = 1` | OFF⁺ | Admin hợp lệ; chưa có danh mục tên `A` | Tạo danh mục tên `A`. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin và mở mục quản lý Danh mục.
- Không có danh mục tên `A`.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên danh mục | `A` |
| Độ dài | `L = 1` ký tự |

## Các bước kiểm thử

1. Nhập `A` vào trường tên danh mục.
2. Bấm nút thêm danh mục.
3. Quan sát danh sách.

## Kết quả mong đợi

Danh mục tên `A` được tạo và xuất hiện trong danh sách.

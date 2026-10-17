# TC-FR-14-BVA-003: Tên danh mục tại đại diện bên trong 2 ký tự

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
| COND-FR-14-BVA-003 | BV-NAME-003 | `AB`, `L = 2` | Đại diện bên trong | Admin hợp lệ; chưa có danh mục tên `AB` | Tạo danh mục tên `AB`. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin và mở mục quản lý Danh mục.
- Không có danh mục tên `AB`.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên danh mục | `AB` |
| Độ dài | `L = 2` ký tự |

## Các bước kiểm thử

1. Nhập `AB` vào trường tên danh mục.
2. Bấm nút thêm danh mục.
3. Quan sát danh sách.

## Kết quả mong đợi

Danh mục tên `AB` được tạo và xuất hiện trong danh sách.

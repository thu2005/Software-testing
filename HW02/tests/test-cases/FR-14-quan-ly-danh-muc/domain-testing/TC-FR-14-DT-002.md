# TC-FR-14-DT-002: Thêm danh mục với tên không rỗng

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Pass / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Tên danh mục | Chuỗi bắt buộc | Không rỗng |
| Thao tác | Tập hành động | Thêm |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-002 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-V01 | `DM-FR14-THEM` chưa tồn tại | EC-RESULT-O02 | Danh mục được tạo và xuất hiện trong danh sách. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin.
- Không có danh mục tên `DM-FR14-THEM`.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên danh mục | `DM-FR14-THEM` (12 ký tự) |

## Các bước kiểm thử

1. Mở mục quản lý Danh mục.
2. Nhập `DM-FR14-THEM` vào trường tên.
3. Bấm nút thêm danh mục.
4. Quan sát danh sách danh mục.

## Kết quả mong đợi

Danh mục `DM-FR14-THEM` được tạo và xuất hiện trong danh sách.

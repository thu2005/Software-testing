# TC-FR-14-DT-004: Xóa danh mục hiện có

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
| Thao tác | Tập hành động | Xóa |
| Danh mục mục tiêu | Trạng thái | Phải tồn tại trước thao tác |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-004 | EC-AUTH-V01, EC-ACTION-V03 | `DM-FR14-XOA` tồn tại | EC-RESULT-O04 | Danh mục mục tiêu bị xóa và không còn trong danh sách. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin.
- Danh mục `DM-FR14-XOA` tồn tại và không gắn dữ liệu phụ thuộc.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Danh mục cần xóa | `DM-FR14-XOA` |

## Các bước kiểm thử

1. Mở mục quản lý Danh mục.
2. Tìm dòng `DM-FR14-XOA`.
3. Thực hiện thao tác Xóa trên đúng dòng.
4. Tải lại hoặc làm mới danh sách danh mục.

## Kết quả mong đợi

`DM-FR14-XOA` không còn trong danh sách; các danh mục khác không bị xóa. Requirement không quy định dialog xác nhận hoặc thông báo cụ thể.

# TC-FR-14-DT-007: Chặn user thường truy cập quản lý danh mục

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
| Role người dùng | Điều kiện truy cập | User, không phải Admin |
| Phân hệ | Trạng thái | Web Admin |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-007 | EC-AUTH-I02, EC-ACTION-V01 | User thường mở phân hệ Web Admin | EC-RESULT-O05 | Không được truy cập chức năng quản lý danh mục. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản user mặc định hoặc có phiên user hợp lệ.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tài khoản | `test@eshop.com` / `Test1234!` |
| Đích truy cập | Phân hệ Web Admin, mục Danh mục |

## Các bước kiểm thử

1. Dùng phiên user thường truy cập phân hệ Web Admin.
2. Thử mở chức năng quản lý Danh mục.
3. Quan sát khả năng xem và sử dụng chức năng.

## Kết quả mong đợi

User thường không được truy cập chức năng quản lý danh mục. Cách chặn, redirect và thông báo cụ thể chưa được đặc tả.

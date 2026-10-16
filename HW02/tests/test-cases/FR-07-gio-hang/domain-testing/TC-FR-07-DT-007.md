# TC-FR-07-DT-007: Tiếp tục mua sắm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](../../../../analysis/FR-07-gio-hang/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-NAV-V01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-007 | EC-NAV-V01 | Đang ở trang giỏ hàng | EC-RESULT-O06 | Nút `Tiếp tục mua sắm` đưa người dùng về trang chủ. |

## Điều kiện tiên quyết

- Trang giỏ hàng tải thành công.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Trang ban đầu | Giỏ hàng |
| Thao tác | Tiếp tục mua sắm |

## Các bước kiểm thử

1. Mở trang giỏ hàng.
2. Bấm nút `Tiếp tục mua sắm`.
3. Quan sát trang được mở.

## Kết quả mong đợi

Nút `Tiếp tục mua sắm` đưa người dùng về trang chủ.

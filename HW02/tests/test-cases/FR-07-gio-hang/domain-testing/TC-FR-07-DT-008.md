# TC-FR-07-DT-008: Hiển thị giỏ hàng trống

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
| Lớp mục tiêu | Equivalence class | EC-CART-V02 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-008 | EC-CART-V02 | Giỏ có 0 dòng sản phẩm | EC-RESULT-O08 | Trang giỏ hàng hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống. |

## Điều kiện tiên quyết

- Giỏ không có sản phẩm.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Số dòng sản phẩm | 0 |

## Các bước kiểm thử

1. Mở trang giỏ hàng đang rỗng.
2. Quan sát nội dung empty state.

## Kết quả mong đợi

Trang giỏ hàng hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống.

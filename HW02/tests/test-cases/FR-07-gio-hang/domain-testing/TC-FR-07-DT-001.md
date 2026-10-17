# TC-FR-07-DT-001: Hiển thị giỏ hàng có sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](../../../../analysis/FR-07-gio-hang/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR07-002](../../../../bug-reports/BUG-FR07-002.md) ([Issue #6](https://github.com/thu2005/CSC13003_eshop/issues/6)), [BUG-FR07-003](../../../../bug-reports/BUG-FR07-003.md) ([Issue #7](https://github.com/thu2005/CSC13003_eshop/issues/7)), [BUG-FR07-004](../../../../bug-reports/BUG-FR07-004.md) ([Issue #8](https://github.com/thu2005/CSC13003_eshop/issues/8)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-CART-V01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-001 | EC-CART-V01 | Giỏ có SP-A số lượng 2 và SP-B số lượng 1 | EC-RESULT-O01, EC-RESULT-O07 | Danh sách có hai dòng; mỗi dòng hiển thị Sản phẩm, Đơn giá, Số lượng với nút +/-, Thành tiền và Thao tác; nhãn tổng tiền là `Tổng cộng`, không phải `Tổng tạm tính`. |

## Điều kiện tiên quyết

- Giỏ có SP-A số lượng 2 và SP-B số lượng 1.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Dòng 1 | SP-A — ID FR07-A, tên Áo kiểm thử FR07; số lượng 2 |
| Dòng 2 | SP-B — ID FR07-B, tên Túi kiểm thử FR07; số lượng 1 |

## Các bước kiểm thử

1. Mở trang giỏ hàng đã chuẩn bị.
2. Quan sát tiêu đề cột, từng dòng sản phẩm, nút +/- và khu vực tổng tiền.

## Kết quả mong đợi

Danh sách có hai dòng; mỗi dòng hiển thị Sản phẩm, Đơn giá, Số lượng với nút +/-, Thành tiền và Thao tác; nhãn tổng tiền là `Tổng cộng`, không phải `Tổng tạm tính`.

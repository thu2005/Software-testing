# TC-FR-07-BVA-003: Giỏ hàng có 2 dòng sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [bva-analysis.md](../../../../analysis/FR-07-gio-hang/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR07-002](../../../../bug-reports/BUG-FR07-002.md) ([Issue #6](https://github.com/thu2005/CSC13003_eshop/issues/6)), [BUG-FR07-003](../../../../bug-reports/BUG-FR07-003.md) ([Issue #7](https://github.com/thu2005/CSC13003_eshop/issues/7)), [BUG-FR07-004](../../../../bug-reports/BUG-FR07-004.md) ([Issue #8](https://github.com/thu2005/CSC13003_eshop/issues/8)) |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Số dòng sản phẩm phân biệt | ≥0 | Cận dưới đóng | 0 | 1 dòng | -1, không khả thi | 0 | 1 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-07-BVA-003 | BV-ROWS-003 | 2 dòng SP-A và SP-B, mỗi sản phẩm số lượng 1 | Đại diện bên trong | Không thay đổi số lượng trong mỗi dòng | Hiển thị đúng hai dòng sản phẩm; mỗi dòng có các cột bắt buộc và khu vực tổng tiền mang nhãn `Tổng cộng`. |

## Điều kiện tiên quyết

- Giỏ có đúng hai dòng SP-A và SP-B, mỗi sản phẩm số lượng 1.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Số dòng sản phẩm | 2 |
| Trạng thái cụ thể | 2 dòng SP-A và SP-B, mỗi sản phẩm số lượng 1; SP-A = ID FR07-A, tên Áo kiểm thử FR07; SP-B = ID FR07-B, tên Túi kiểm thử FR07 khi được dùng |

## Các bước kiểm thử

1. Chuẩn bị giỏ đúng trạng thái trong bảng dữ liệu.
2. Mở trang giỏ hàng.
3. Đếm số dòng sản phẩm và quan sát vùng nội dung giỏ.

## Kết quả mong đợi

Hiển thị đúng hai dòng sản phẩm; mỗi dòng có các cột bắt buộc và khu vực tổng tiền mang nhãn `Tổng cộng`.

# TC-FR-07-BVA-002: Giỏ hàng có 1 dòng sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [bva-analysis.md](../../../../analysis/FR-07-gio-hang/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Số dòng sản phẩm phân biệt | ≥0 | Cận dưới đóng | 0 | 1 dòng | -1, không khả thi | 0 | 1 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-07-BVA-002 | BV-ROWS-002 | 1 dòng SP-A, số lượng 1 | OFF⁺ | Không thay đổi số lượng trong mỗi dòng | Hiển thị đúng một dòng SP-A với các cột bắt buộc và nhãn `Tổng cộng`. |

## Điều kiện tiên quyết

- Giỏ có đúng một dòng SP-A, số lượng 1.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Số dòng sản phẩm | 1 |
| Trạng thái cụ thể | 1 dòng SP-A, số lượng 1; SP-A = ID FR07-A, tên Áo kiểm thử FR07; SP-B = ID FR07-B, tên Túi kiểm thử FR07 khi được dùng |

## Các bước kiểm thử

1. Chuẩn bị giỏ đúng trạng thái trong bảng dữ liệu.
2. Mở trang giỏ hàng.
3. Đếm số dòng sản phẩm và quan sát vùng nội dung giỏ.

## Kết quả mong đợi

Hiển thị đúng một dòng SP-A với các cột bắt buộc và nhãn `Tổng cộng`.

# TC-FR-07-DT-002: Thêm lại cùng một sản phẩm

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
| Lớp mục tiêu | Equivalence class | EC-SAME-V01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-002 | EC-SAME-V01 | Giỏ có đúng một dòng SP-A số lượng 1; thêm lại SP-A | EC-RESULT-O02 | Số lượng của SP-A tăng và giỏ vẫn chỉ có một dòng SP-A. |

## Điều kiện tiên quyết

- Giỏ có đúng một dòng SP-A với số lượng 1; có thể mở màn hình thêm SP-A.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | SP-A — ID FR07-A, tên Áo kiểm thử FR07 |
| Số lượng ban đầu | 1 |
| Số dòng SP-A ban đầu | 1 |

## Các bước kiểm thử

1. Xác nhận giỏ đang có đúng một dòng SP-A với số lượng 1.
2. Từ màn hình cho phép thêm sản phẩm, thêm lại SP-A.
3. Mở giỏ và quan sát số lượng cùng số dòng SP-A.

## Kết quả mong đợi

Số lượng của SP-A tăng và giỏ vẫn chỉ có một dòng SP-A.

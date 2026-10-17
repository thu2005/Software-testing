# TC-FR-06-MOBILE-DT-001: Hiển thị đầy đủ chi tiết sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-001](../../../../bug-reports/BUG-FR06-001.md) ([Issue #16](https://github.com/thu2005/CSC13003_eshop/issues/16)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Sản phẩm được chọn | Trạng thái | Fixture tồn tại và có đủ dữ liệu |
| Chi tiết sản phẩm | Output | Ảnh lớn, Tên, Giá, Mô tả, Danh mục |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-001 | EC-PRODUCT-V01, EC-ACTION-V01 | Mở `SP-FR06-MOBILE` | EC-RESULT-O01 | Hiển thị đúng năm thành phần của fixture. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tên | `SP-FR06-MOBILE` |
| Giá nguồn | `1234000` |
| Mô tả | `Sản phẩm dùng kiểm thử FR-06 Mobile` |
| Danh mục | `Điện thoại` |
| Ảnh | URL ảnh hợp lệ của fixture |

## Các bước kiểm thử

1. Khởi chạy ứng dụng Mobile và mở danh sách sản phẩm.
2. Chọn sản phẩm `SP-FR06-MOBILE`.
3. Đối chiếu ảnh lớn, tên, giá, mô tả và danh mục với fixture.

## Kết quả mong đợi

Trang chi tiết hiển thị ảnh lớn và đúng Tên `SP-FR06-MOBILE`, Giá tương ứng `1234000`, Mô tả `Sản phẩm dùng kiểm thử FR-06 Mobile`, Danh mục `Điện thoại`; không thiếu thành phần nào.

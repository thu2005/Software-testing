# TC-FR-06-MOBILE-DT-002: Kiểm tra yêu cầu giao diện áp dụng trên trang chi tiết Mobile

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm), [FR-21 đến FR-24](../../../../requirements/system-requirements.md#fr-21-tiêu-chuẩn-giao-diện-chung); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-002](../../../../bug-reports/BUG-FR06-002.md) ([Issue #17](https://github.com/thu2005/CSC13003_eshop/issues/17)), [BUG-FR06-003](../../../../bug-reports/BUG-FR06-003.md) ([Issue #18](https://github.com/thu2005/CSC13003_eshop/issues/18)), [BUG-FR06-004](../../../../bug-reports/BUG-FR06-004.md) ([Issue #19](https://github.com/thu2005/CSC13003_eshop/issues/19)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Trạng thái trang | Output UI | Trang chi tiết fixture trên Mobile |
| Giao diện / navigation / accessibility | Output | Các yêu cầu FR-21, FR-23, FR-24 áp dụng |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-002 | EC-PRODUCT-V01, EC-PAGE-V01 | Quan sát trang fixture và dùng trình đọc màn hình cho ảnh | EC-RESULT-O02 | Các quy tắc UI/navigation/accessibility áp dụng được đáp ứng. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | `SP-FR06-MOBILE` |
| Giá nguồn | `1234000` |
| Công cụ hỗ trợ | Trình đọc màn hình hoặc accessibility inspector của thiết bị |

## Các bước kiểm thử

1. Mở trang chi tiết `SP-FR06-MOBILE`.
2. Kiểm tra ngôn ngữ, định dạng giá và màu nút `Thêm vào giỏ hàng`.
3. Kiểm tra breadcrumb của trang và badge tại liên kết Giỏ hàng.
4. Dùng công cụ hỗ trợ truy cập để đọc mô tả ảnh sản phẩm.

## Kết quả mong đợi

Nội dung dùng tiếng Việt; giá có phân cách hàng nghìn và ký hiệu `₫`; nút `Thêm vào giỏ hàng` màu xanh dương; trang có breadcrumb; liên kết Giỏ hàng có badge số lượng; ảnh sản phẩm có mô tả hỗ trợ truy cập không rỗng.

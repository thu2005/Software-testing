# TC-FR-06-MOBILE-DT-004: Từ chối số lượng rỗng

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Số lượng | Đầu vào | Thiếu giá trị |
| Kết quả nhập | Output lỗi | Không chấp nhận làm số lượng thêm giỏ |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-004 | EC-PRODUCT-V01, EC-QTY-I01 | Xóa thành chuỗi rỗng `""` | EC-RESULT-O04 | Không dùng giá trị rỗng để thêm sản phẩm. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Trạng thái giỏ ban đầu | Không có `SP-FR06-MOBILE` |
| Số lượng | Chuỗi rỗng `""` |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE`, sau đó mở trang chi tiết fixture.
2. Xóa toàn bộ giá trị trong ô Số lượng.
3. Bấm `Thêm vào giỏ hàng` và quan sát control, validation và phản hồi.

## Kết quả mong đợi

Giá trị rỗng không được dùng để thêm sản phẩm. Control có thể ngăn/xử lý về một số nguyên dương hoặc hệ thống từ chối thao tác; không được báo thêm thành công dựa trên số lượng rỗng. Nội dung lỗi cụ thể chưa được đặc tả.

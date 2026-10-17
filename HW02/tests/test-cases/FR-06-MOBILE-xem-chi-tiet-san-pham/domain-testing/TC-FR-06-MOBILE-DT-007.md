# TC-FR-06-MOBILE-DT-007: Từ chối số lượng không phải số

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-005](../../../../bug-reports/BUG-FR06-005.md) ([Issue #20](https://github.com/thu2005/CSC13003_eshop/issues/20)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Số lượng | Đầu vào | Giá trị không phải số |
| Kết quả nhập | Output lỗi | Từ chối sai kiểu |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-007 | EC-PRODUCT-V01, EC-QTY-I04 | Nhập `abc` | EC-RESULT-O04 | Không chấp nhận giá trị không phải số. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Trạng thái giỏ ban đầu | Không có `SP-FR06-MOBILE` |
| Số lượng | `abc` |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE`, sau đó mở trang chi tiết fixture.
2. Thử nhập hoặc dán `abc` vào ô Số lượng.
3. Bấm `Thêm vào giỏ hàng` nếu control cho phép giữ giá trị và quan sát kết quả.

## Kết quả mong đợi

`abc` không được chấp nhận làm số lượng. Control có thể chặn giá trị hoặc hệ thống từ chối thao tác; sản phẩm không được thêm dựa trên giá trị không phải số. Nội dung lỗi cụ thể chưa được đặc tả.

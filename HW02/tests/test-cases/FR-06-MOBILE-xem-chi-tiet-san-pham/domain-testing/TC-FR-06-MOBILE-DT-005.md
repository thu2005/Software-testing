# TC-FR-06-MOBILE-DT-005: Từ chối số lượng nguyên âm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-005](../../../../bug-reports/BUG-FR06-005.md) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Số lượng | Đầu vào số nguyên | `q ≤ 0` không hợp lệ |
| Kết quả nhập | Output lỗi | Từ chối giá trị ngoài miền dương |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-005 | EC-PRODUCT-V01, EC-QTY-I02 | Nhập `-1` | EC-RESULT-O04 | Không chấp nhận số nguyên âm. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Trạng thái giỏ ban đầu | Không có `SP-FR06-MOBILE` |
| Số lượng | `-1` |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE`, sau đó mở trang chi tiết fixture.
2. Thử nhập hoặc dán `-1` vào ô Số lượng.
3. Bấm `Thêm vào giỏ hàng` nếu control cho phép giữ giá trị và quan sát kết quả.

## Kết quả mong đợi

`-1` không được chấp nhận làm số lượng. Control có thể chặn giá trị hoặc hệ thống từ chối thao tác; sản phẩm không được thêm dựa trên số lượng `-1`. Nội dung lỗi cụ thể chưa được đặc tả.

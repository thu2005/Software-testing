# TC-FR-06-MOBILE-DT-003: Chấp nhận số nguyên dương danh nghĩa

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Pass / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Số lượng | Đầu vào số nguyên | `q ≥ 1` |
| Kết quả nhập | Output | Chấp nhận số nguyên dương |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-003 | EC-PRODUCT-V01, EC-QTY-V01 | Nhập `3` | EC-RESULT-O03 | Control chấp nhận và giữ số lượng `3`. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Số lượng | `3` |

## Các bước kiểm thử

1. Mở trang chi tiết fixture.
2. Chọn toàn bộ giá trị hiện có trong ô Số lượng và nhập `3`.
3. Rời focus khỏi ô rồi quan sát giá trị.

## Kết quả mong đợi

Ô Số lượng chấp nhận và giữ giá trị `3` để có thể dùng cho thao tác thêm giỏ.

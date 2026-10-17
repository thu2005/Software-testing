# TC-FR-06-MOBILE-DT-008: Thêm sản phẩm vào giỏ và nhận phản hồi trực quan

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm), [FR-24](../../../../requirements/system-requirements.md#fr-24-feedback--state-requirements); [domain-testing-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-006](../../../../bug-reports/BUG-FR06-006.md) ([Issue #21](https://github.com/thu2005/CSC13003_eshop/issues/21)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Số lượng | Đầu vào số nguyên | Số nguyên dương |
| Thêm vào giỏ / phản hồi | Output | Thêm sản phẩm và hiển thị toast hoặc badge cập nhật |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-008 | EC-PRODUCT-V01, EC-ACTION-V02, EC-QTY-V01 | Nhập `5`, bấm `Thêm vào giỏ hàng` | EC-RESULT-O05 | Thêm fixture với số lượng `5` và có phản hồi trực quan. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm fixture `SP-FR06-MOBILE` xuất hiện trong danh sách sản phẩm.
- Mở chi tiết fixture từ danh sách, trừ khi bước kiểm thử nêu khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | `SP-FR06-MOBILE` |
| Số lượng | `5` |
| Trạng thái giỏ ban đầu | Không có `SP-FR06-MOBILE` |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE` và mở trang chi tiết fixture.
2. Nhập số lượng `5`.
3. Bấm `Thêm vào giỏ hàng`.
4. Quan sát toast/badge, sau đó mở giỏ để kiểm tra sản phẩm và số lượng.

## Kết quả mong đợi

`SP-FR06-MOBILE` được thêm vào giỏ với số lượng `5`. Ngay sau thao tác có phản hồi trực quan bằng toast notification hoặc badge cập nhật.

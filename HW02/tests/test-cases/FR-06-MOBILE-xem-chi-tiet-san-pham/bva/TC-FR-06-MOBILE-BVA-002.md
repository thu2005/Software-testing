# TC-FR-06-MOBILE-BVA-002: Số lượng tại cận tối thiểu hợp lệ

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm), [FR-24](../../../../requirements/system-requirements.md#fr-24-feedback--state-requirements); [bva-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-006](../../../../bug-reports/BUG-FR06-006.md) ([Issue #21](https://github.com/thu2005/CSC13003_eshop/issues/21)) |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Số lượng `q` | `q ≥ 1` | Cận dưới đóng | `1` | `δ = 1` sản phẩm | `0` không hợp lệ | `1` hợp lệ | `2` hợp lệ |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-06-MOBILE-BVA-002 | BV-QTY-002 | `1` | ON | Fixture hợp lệ; giỏ chưa có fixture | Thêm fixture với số lượng `1` và có toast hoặc badge cập nhật. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm `SP-FR06-MOBILE` tồn tại và đang mở ở trang chi tiết.
- Giỏ chưa có `SP-FR06-MOBILE`.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | `SP-FR06-MOBILE` |
| Số lượng | `1` (ON, Hợp lệ) |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE` và mở trang chi tiết fixture.
2. Nhập số lượng `1`.
3. Bấm `Thêm vào giỏ hàng`.
4. Quan sát phản hồi, sau đó mở giỏ để kiểm tra sản phẩm và số lượng.

## Kết quả mong đợi

`SP-FR06-MOBILE` được thêm vào giỏ với số lượng `1`; có phản hồi trực quan bằng toast notification hoặc badge cập nhật.

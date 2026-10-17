# TC-FR-06-MOBILE-BVA-001: Số lượng ngay dưới cận tối thiểu

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [bva-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Số lượng `q` | `q ≥ 1` | Cận dưới đóng | `1` | `δ = 1` sản phẩm | `0` không hợp lệ | `1` hợp lệ | `2` hợp lệ |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-06-MOBILE-BVA-001 | BV-QTY-001 | `0` | OFF⁻ | Fixture hợp lệ; giỏ chưa có fixture | Không thêm sản phẩm dựa trên số lượng `0`; không hiển thị feedback thành công. |

## Điều kiện tiên quyết

- Backend đang chạy và ứng dụng Mobile kết nối được API.
- Sản phẩm `SP-FR06-MOBILE` tồn tại và đang mở ở trang chi tiết.
- Giỏ chưa có `SP-FR06-MOBILE`.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | `SP-FR06-MOBILE` |
| Số lượng | `0` (OFF⁻, Không hợp lệ) |

## Các bước kiểm thử

1. Bảo đảm giỏ chưa có `SP-FR06-MOBILE` và mở trang chi tiết fixture.
2. Nhập số lượng `0`.
3. Bấm `Thêm vào giỏ hàng`.
4. Quan sát phản hồi, sau đó mở giỏ để kiểm tra sản phẩm và số lượng.

## Kết quả mong đợi

Số lượng `0` không được dùng để thêm sản phẩm. Control có thể chặn/điều chỉnh về giá trị hợp lệ hoặc hệ thống từ chối thao tác; giỏ không được nhận fixture dựa trên số lượng `0` và không có feedback thêm thành công.

# TC-FR-06-MOBILE-BVA-001: Số lượng ngay dưới cận tối thiểu

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Xem chi tiết sản phẩm / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [FR-06](../../../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [bva-analysis.md](../../../../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR06-005](../../../../bug-reports/BUG-FR06-005.md) ([Issue #20](https://github.com/thu2005/CSC13003_eshop/issues/20)) |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Số lượng `q` | `q ≥ 1` | Cận dưới đóng | `1` | `δ = 1` sản phẩm | `0` không hợp lệ | `1` hợp lệ | `2` hợp lệ |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-06-MOBILE-BVA-001 | BV-QTY-001 | `0` | OFF⁻ | Fixture hợp lệ; giỏ chưa có fixture | Không dùng `0` làm số lượng hiệu lực; control từ chối thao tác hoặc chuẩn hóa về số nguyên dương trước khi thêm. |

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

Số lượng hiệu lực không được là `0`. Control có thể chặn/từ chối thao tác hoặc chuẩn hóa về một số nguyên dương trước khi thêm. Nếu giỏ thay đổi, số lượng được thêm phải đúng giá trị hợp lệ đang hiển thị sau khi chuẩn hóa; nội dung lỗi cụ thể chưa được đặc tả.

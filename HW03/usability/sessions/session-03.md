# Session 03 — P03 Bùi Nguyễn Quang Tuấn

## Thông tin session

- **Date/time**: 14/11/2026 21:51:26
- **Profile**: Non-IT; mobile
- **Consent to participate**: Yes
- **Consent to record**: Screen + audio
- **SUT build/browser/device**: `85af3ba`; Safari / iPhone
- **Thời lượng recording**: 06:07
- **Task success**: Success — participant hoàn thành luồng sau khi tự sửa trường tổng tiền
- **Hint của moderator**: Không có leading hint hoặc chỉ dẫn UI

## Ghi chú quan sát

| Thời điểm | Bước | Quan sát |
|---|---|---|
| 01:57 | Sau Add to Cart | “Ủa thêm, rồi làm sao để thanh toán ta”; không thấy chỉ báo rõ để chuyển sang thanh toán. |
| 02:39 | Checkout | Nhận ra sản phẩm 6 triệu nhưng tổng thanh toán là 60 triệu. |
| 03:02 | Checkout | Phát hiện trường tổng tiền có thể chỉnh sửa, đổi thành `60000` và hệ thống báo thanh toán thành công. |

## Custom scale thu bổ sung ngày 15/11/2026

| Clarity | Error recovery | Speed | Trust | Mean |
|---:|---:|---:|---:|---:|
| 4 | 3 | 3 | 3 | 3.25 |

## Trả lời phỏng vấn

- **Clarity:** Sau khi thêm vào giỏ không thấy thông báo hoặc số lượng món hàng để biết cách tiếp tục thanh toán.
- **Giá/voucher/tổng tiền:** Trả lời rằng thông tin không được xử lý đúng.
- **Ý định sử dụng:** Không sử dụng vì chưa rõ liên kết ngân hàng, mô tả sản phẩm thiếu thông tin nổi bật và không có hình.
- **Error recovery:** Participant đọc/nêu lỗi gặp phải cho moderator và vẫn tự tiếp tục thao tác để hoàn thành luồng.
- **Speed:** Participant đánh giá luồng khá dễ hiểu, tương tự các website mua hàng thông thường; không xác định bước nào đặc biệt làm mất thời gian.

## Evidence

- Screen + audio: https://www.youtube.com/watch?v=AI_qtxcTea8
- Defect liên quan: [Issue #49 — tổng tiền có thể chỉnh sửa](https://github.com/thu2005/CSC13003_eshop/issues/49), [#54 — thiếu Cart badge](https://github.com/thu2005/CSC13003_eshop/issues/54), [#60 — Coupon tính sai](https://github.com/thu2005/CSC13003_eshop/issues/60)


# Session 07 — P07 Huỳnh Yến Nhi

## Thông tin session

- **Date/time**: 14/11/2026 21:38:22
- **Profile**: Sinh viên IT, không theo hướng tester; online
- **Consent to participate**: Yes
- **Consent to record**: Screen + audio
- **SUT build/browser/device**: `85af3ba`; Google Chrome
- **Thời lượng recording**: 03:51
- **Task success**: Success — participant hoàn thành toàn bộ luồng
- **Hint của moderator**: Không có leading hint hoặc chỉ dẫn UI

## Ghi chú quan sát

| Thời điểm | Bước | Quan sát |
|---|---|---|
| 01:16 | Product Detail | “Ủa là thêm chưa”; lướt lên/xuống nhiều lần rồi tìm Cart. |
| 01:28 | Cart/Home | Cart vẫn trống nên quay lại Home và thêm từ listing; vào lại Cart thấy đúng một sản phẩm. |
| 01:46 | Checkout | Phản ứng khi giá 6 triệu sau voucher lại thành 60 triệu và không muốn tiếp tục mua. |

## Custom scale thu bổ sung ngày 15/11/2026

| Clarity | Error recovery | Speed | Trust | Mean |
|---:|---:|---:|---:|---:|
| 5 | 4 | 2 | 1 | 3.00 |

## Trả lời phỏng vấn

- **Clarity:** Add to Cart từ Product Detail không có phản hồi và sản phẩm không xuất hiện trong Cart; tổng tiền cũng gây khó hiểu.
- **Giá/voucher/tổng tiền:** Không đúng vì voucher làm giá tăng lên 60 triệu.
- **Ý định sử dụng:** Không dùng vì thiếu phản hồi, voucher sai, giao diện không đáng tin và không có hình sản phẩm.
- **Error recovery:** “Tiếp tục kiểm thử để hoàn thành luồng test.”
- **Speed:** “Không mất thời gian.”

## Evidence

- Screen + audio: https://www.youtube.com/watch?v=5N7qLocEnNw
- Defect liên quan: [Issue #60 — Coupon tính sai](https://github.com/thu2005/CSC13003_eshop/issues/60), [#62 — Add to Cart không phản hồi đúng](https://github.com/thu2005/CSC13003_eshop/issues/62)

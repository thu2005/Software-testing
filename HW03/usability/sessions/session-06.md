# Session 06 — P06 Trần Thị Thuỷ Tiên

## Thông tin session

- **Date/time**: 14/11/2026 21:21:21
- **Profile**: Sinh viên IT, không theo hướng tester; online, mobile
- **Consent to participate**: Yes
- **Consent to record**: Screen + audio
- **SUT build/browser/device**: `85af3ba`; Safari / iPhone
- **Thời lượng recording**: 04:28
- **Task success**: Success — participant hoàn thành toàn bộ luồng
- **Hint của moderator**: Không có leading hint hoặc chỉ dẫn UI

## Ghi chú quan sát

| Thời điểm | Bước | Quan sát |
|---|---|---|
| 01:16 | Product Detail | Nhập quantity `-1`; hệ thống vẫn cho phép thêm vào Cart. |
| 01:43 | Listing/Cart | Nhận ra Add to Cart không có popup; quantity âm làm thành tiền `-6.000.000 ₫`, sau đó xóa sản phẩm. |
| 02:33 | Checkout | Nhận ra giá 6 triệu, giảm 10% nhưng “tiết kiệm” hiển thị 54 triệu và thành tiền 60 triệu. |

## Custom scale thu bổ sung ngày 15/11/2026

Phản hồi lần đầu bị loại theo xác nhận của sinh viên; dùng phản hồi thứ hai lúc
20:16:15.

| Clarity | Error recovery | Speed | Trust | Mean |
|---:|---:|---:|---:|---:|
| 3 | 1 | 4 | 1 | 2.25 |

## Trả lời phỏng vấn

- **Clarity:** Nếu không tính các lỗi đã gặp, participant đánh giá luồng khá dễ hiểu.
- **Giá/voucher/tổng tiền:** Không được xử lý đúng.
- **Ý định sử dụng:** Không dùng vì thiếu hình ảnh trực quan và đánh giá từ khách hàng, làm giảm niềm tin.
- **Error recovery:** “Mình nói lỗi đó cho bạn phỏng vấn, tiếp tục test cho xong luồng.”
- **Speed:** “Mình thấy đơn giản và giống các web khác, không gặp khó khăn gì.”

## Evidence

- Screen + audio: https://www.youtube.com/watch?v=b1zkPGr5dKc
- Defect liên quan: [Issue #50 — validation quantity](https://github.com/thu2005/CSC13003_eshop/issues/50), [#60 — Coupon tính sai](https://github.com/thu2005/CSC13003_eshop/issues/60)


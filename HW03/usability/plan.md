# Kế hoạch Usability Evaluation — Luồng mua hàng EShop

## 1. Phạm vi

- **Luồng:** Search (`FR-05`) → Product Detail (`FR-06`) → Shopping Cart
  (`FR-07`) → Coupon (`FR-09`) → Checkout (`FR-08`).
- **Nền tảng chính:** Google Chrome / Windows.
- **SUT build:** `85af3ba` (`main`).
- **Số session chính:** 7 người thật ngoài lớp.
- **Pilot:** 1 người, không thuộc 7 participant chính.

## 2. Mục tiêu nghiên cứu

1. Xác định người dùng có tự tìm được sản phẩm và hiểu thông tin Product Detail
   mà không cần moderator hướng dẫn hay không.
2. Quan sát các điểm do dự, lỗi và khả năng tự phục hồi trong Cart, Coupon và
   Checkout.
3. Đánh giá thời gian/công sức cảm nhận khi hoàn tất luồng mua hàng.
4. Tìm hiểu mức độ tin tưởng của người dùng vào giá, giảm giá, tổng tiền và xác
   nhận đơn hàng.
5. Đo usability tổng thể bằng SUS và giải thích điểm số bằng observation cùng
   câu trả lời probe.

## 3. Câu hỏi nghiên cứu

- Người dùng có nhận biết được cách tìm sản phẩm và mở đúng sản phẩm không?
- Họ có hiểu quantity, Cart, coupon và tổng tiền trước khi xác nhận không?
- Khi thao tác không cho kết quả như mong đợi, họ nhận biết và phục hồi thế nào?
- Bước nào tạo nhiều hesitation hoặc làm luồng chậm nhất?
- Thông tin nào làm tăng hoặc giảm trust ở Checkout?

## 4. Task scenario

> Bạn muốn mua **iPhone 15 Pro Max** trên EShop. Bạn có mã giảm giá
> **SAVE10**. Hãy hoàn tất việc mua **1 sản phẩm** bằng mã này và dừng lại khi
> bạn thấy hệ thống xác nhận đơn hàng thành công.

Scenario chỉ nêu mục tiêu và dữ liệu cần thiết; không nói người tham gia phải
bấm nút nào hoặc đi theo từng màn hình ra sao.

## 5. Trạng thái bắt đầu và dữ liệu test

- Mở trang chủ EShop trên Chrome ở trạng thái chưa có sản phẩm trong Cart.
- Moderator chuẩn bị một test account hoạt động nhưng không ghi password vào
  repository; chỉ cung cấp khi participant cần đăng nhập.
- Xác minh trước session: sản phẩm `iPhone 15 Pro Max` có thể tìm thấy, coupon
  `SAVE10` tồn tại và backend hoạt động.
- Reset Cart/session về cùng trạng thái trước mỗi lượt.
- Không cho participant xem checklist GUI hoặc danh sách bug đã biết.

## 6. Instrument và lý do chọn

Chọn **System Usability Scale (SUS)** gồm 10 câu, Likert 1–5. SUS phù hợp vì:

- ngắn, có thể hoàn thành ngay sau một task end-to-end;
- tạo một composite score 0–100 để so sánh giữa 7 participant;
- có polarity xen kẽ giúp hạn chế trả lời một chiều;
- được dùng cùng observation và probe, không bị diễn giải như công cụ chẩn
  đoán nguyên nhân.

Survey giữ nguyên wording tiếng Anh chuẩn và đúng thứ tự; bản dịch tiếng Việt
được đặt ngay dưới mỗi câu để hỗ trợ participant. Không đảo câu hoặc đổi
polarity. Nguồn survey: [post-test-survey.md](post-test-survey.md).

### Công thức SUS

- Câu lẻ 1, 3, 5, 7, 9: `contribution = response - 1`.
- Câu chẵn 2, 4, 6, 8, 10: `contribution = 5 - response`.
- `SUS = tổng 10 contribution × 2.5` (0–100).

Chỉ tính điểm sau khi có câu trả lời thật; không điền score trước session.

## 7. Dữ liệu thu thập

| Nhóm dữ liệu | Cách ghi nhận |
|---|---|
| Task success | `Success`, `Partial` hoặc `Failed` theo tiêu chí mục 8 |
| Thời gian | Timestamp bắt đầu, kết thúc và thời lượng task |
| Hành vi | Bước trong flow, error, hesitation, backtrack, recovery, hint |
| Think-aloud | Chỉ ghi câu nói thật, đặt trong dấu ngoặc kép |
| SUS | Raw response 1–5 cho đủ 10 câu và score tính sau session |
| Probe | Clarity, error recovery, speed, trust và ý định sử dụng thật |
| Evidence | Screen recording; audio chỉ khi có consent rõ ràng |

## 8. Tiêu chí task success

- **Success:** participant tự hoàn tất đơn hàng đúng sản phẩm, quantity 1 và đã
  thử áp dụng `SAVE10`, không cần moderator chỉ cách thao tác.
- **Partial:** đi đến Checkout nhưng không thể hoàn tất hoặc cần một hint mang
  tính định hướng chung; ghi rõ điểm dừng và nguyên nhân.
- **Failed:** không đến được Checkout/xác nhận đơn hàng, từ bỏ, hoặc moderator
  phải thực hiện thao tác thay participant.

Không sửa verdict chỉ vì SUT có bug; ghi riêng bug, hành vi participant và khả
năng recovery.

## 9. Probe questions

Hỏi sau SUS, điều chỉnh phần trong ngoặc vuông theo observation thật:

1. **Clarity:** Có thời điểm nào bạn không chắc phải làm gì tiếp theo không?
   [Nhắc đúng khoảnh khắc do dự nếu có.]
2. **Error recovery:** Lúc bạn [gặp lỗi/thao tác lại], bạn đã nghĩ gì và điều gì
   giúp hoặc cản bạn tiếp tục? Nếu không có lỗi, ghi rõ câu này được bỏ qua.
3. **Speed:** Luồng này nhanh hay chậm hơn bạn mong đợi? Bước nào lâu nhất?
4. **Trust:** Ở Checkout, bạn có tin rằng giá, coupon, tổng tiền và đơn hàng
   được xử lý đúng không? Vì sao?
5. **Flow-specific:** Có điều gì trong luồng mua hàng này khiến bạn không muốn
   dùng EShop trong thực tế không?

## 10. Quy trình và vai trò moderator

1. Kiểm tra setup, trạng thái Cart và recording.
2. Giải thích consent, quyền dừng và nguyên tắc “đang test sản phẩm, không test
   người tham gia”.
3. Đọc scenario đúng như script; yêu cầu think aloud.
4. Quan sát trung lập, không gợi ý vị trí/nút. Chỉ can thiệp khi participant
   hoàn toàn bế tắc và phải ghi rõ hint.
5. Kết thúc task, cho participant điền SUS trước khi hỏi probe.
6. Cảm ơn, xác nhận lại phạm vi sử dụng recording và reset SUT.

Script chuẩn: [session-script.md](session-script.md). Cấu trúc ghi chép:
[session-template.md](session-template.md).

## 11. Participant và quyền riêng tư

- Chỉ dùng 7 người thật ngoài lớp; ưu tiên người không học IT/không làm tester.
- Sinh viên tự nhập dữ liệu thật vào [participants.md](participants.md).
- Contact phải che bốn chữ số giữa trước khi commit.
- Không ghi password, token, địa chỉ nhà hoặc dữ liệu thanh toán thật.
- Participant có thể từ chối ghi hình/audio hoặc dừng session bất kỳ lúc nào.

## 12. Pilot và quality gate trước M6

Pilot phải dùng một người ngoài 7 participant chính. Sau pilot, ghi:

- scenario có bị hiểu như hướng dẫn từng bước không;
- wording SUS/probe có gây nhầm không;
- setup, test account, coupon và recording có hoạt động không;
- task có quá dài/ngắn không;
- thay đổi nào được áp dụng trước 7 session.

### Pilot record

- Pilot participant: TODO — sinh viên cung cấp người thật, không thuộc 7 người.
- Ngày/giờ: TODO.
- Consent: TODO.
- Vấn đề phát hiện: TODO — chỉ điền từ pilot thật.
- Thay đổi sau pilot: TODO — chỉ điền từ pilot thật.
- Quyết định sẵn sàng chạy M6: TODO.

## 13. Rủi ro và kiểm soát bias

- Không tuyển bạn cùng lớp HW03.
- Không giải thích UI hoặc nhắc participant về bug đã biết.
- Dùng cùng scenario, trạng thái đầu và moderator script cho mọi session.
- Probe theo observation thật nhưng không đặt câu hỏi dẫn dắt.
- Tách defect của SUT khỏi systemic UX issue khi phân tích M7.
- Không dùng AI để tạo participant, quote, observation, response hoặc score.


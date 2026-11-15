# Kế hoạch Usability Evaluation — Luồng mua hàng EShop

## 1. Phạm vi

- **Luồng:** Search (`FR-05`) → Product Detail (`FR-06`) → Shopping Cart
  (`FR-07`) → Coupon (`FR-09`) → Checkout (`FR-08`).
- **Browser thực tế:** P01–P02 dùng Microsoft Edge trên máy moderator; P03 và
  P06 dùng Safari trên iPhone; P04, P05, P07 dùng Google Chrome.
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
5. Đo bốn khía cạnh cốt lõi bằng custom usability scale ngắn và giải thích
   điểm số bằng observation cùng câu trả lời phỏng vấn.

## 3. Câu hỏi nghiên cứu

- Người dùng có nhận biết được cách tìm sản phẩm và mở đúng sản phẩm không?
- Họ có hiểu quantity, Cart, coupon và tổng tiền trước khi xác nhận không?
- Khi thao tác không cho kết quả như mong đợi, họ nhận biết và phục hồi thế nào?
- Bước nào tạo nhiều hesitation hoặc làm luồng chậm nhất?
- Thông tin nào làm tăng hoặc giảm trust ở Checkout?

## 4. Task scenario

> Bạn muốn mua **AirPods Pro 2** với ngân sách **7.000.000 ₫**. Hãy sử dụng
> EShop để tìm và mua sản phẩm, áp dụng mã **SAVE10** trước khi hoàn tất đơn
> hàng.

Scenario chỉ nêu mục tiêu và dữ liệu cần thiết; không nói người tham gia phải
bấm nút nào hoặc đi theo từng màn hình ra sao.

## 5. Trạng thái bắt đầu và dữ liệu test

- Mở trang chủ EShop trên browser của session ở trạng thái chưa có sản phẩm
  trong Cart.
- Moderator chuẩn bị một test account hoạt động nhưng không ghi password vào
  repository; chỉ cung cấp khi participant cần đăng nhập.
- Xác minh trước session: sản phẩm `AirPods Pro 2` có thể tìm thấy, coupon
  `SAVE10` tồn tại và backend hoạt động.
- Reset Cart/session về cùng trạng thái trước mỗi lượt.
- Không cho participant xem checklist GUI hoặc danh sách bug đã biết.

## 6. Instrument và lý do chọn

Instrument cuối cùng dùng để báo cáo là **custom 4-item usability scale**,
Likert 1–5, đo clarity, error recovery, speed và trust. Scale được tạo và gửi
như follow-up ngày 15/11/2026, sau các session chính; vì vậy không gọi hoặc quy
đổi kết quả thành SUS/UEQ-S và không mô tả scale như đã được pilot-test hay hoàn
thành ngay sau từng session.

1. Tôi luôn biết mình cần làm gì tiếp theo trong luồng mua hàng.
2. Khi gặp vấn đề, tôi có thể nhận biết và tìm cách tiếp tục.
3. Tôi có thể hoàn thành luồng mua hàng nhanh chóng, không có bước thừa.
4. Tôi tin tưởng thông tin sản phẩm, voucher và số tiền thanh toán của EShop.

Mỗi câu dùng `1 — Hoàn toàn không đồng ý` đến `5 — Hoàn toàn đồng ý`. Điểm
mỗi participant là trung bình bốn câu; kết quả nhóm là trung bình theo từng
câu và trung bình của toàn bộ 28 response. Nguồn survey và raw response:
[post-test-survey.md](post-test-survey.md).

## 7. Dữ liệu thu thập

| Nhóm dữ liệu | Cách ghi nhận |
|---|---|
| Task success | `Success`, `Partial` hoặc `Failed` theo tiêu chí mục 8 |
| Thời gian | Timestamp bắt đầu, kết thúc và thời lượng task |
| Hành vi | Bước trong flow, error, hesitation, backtrack, recovery, hint |
| Think-aloud | Chỉ ghi câu nói thật, đặt trong dấu ngoặc kép |
| Custom scale | Raw response 1–5 cho đủ 4 câu; không quy đổi sang SUS |
| Probe | Ba câu trong session về clarity, giá/voucher/tổng tiền và ý định sử dụng; dữ liệu error recovery và speed được tổng hợp từ think-aloud, hành vi quan sát và xác nhận của moderator |
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

Ba câu đã được moderator hỏi trong session:

1. Có thời điểm nào bạn không chắc phải làm gì tiếp theo không?
2. Ở lúc thanh toán, các thông tin như giá, voucher và tổng tiền có được xử lý
   đúng với những gì bạn dự định không?
3. Nếu luồng này được đưa vào thực tế, bạn có sử dụng EShop không? Vì sao?

Câu 1 thu thập clarity; câu 2 và 3 làm rõ trust cùng ý định sử dụng. Dữ liệu
định tính về error recovery và speed được tổng hợp từ think-aloud, hành vi quan
sát trong recording và xác nhận bổ sung của moderator ngày 15/11/2026. Cả bảy
participant đều nêu lỗi gặp phải rồi tự tiếp tục; họ đánh giá luồng khá dễ hiểu,
tương tự website mua hàng thông thường và không xác định bước đặc biệt gây chậm.

## 10. Quy trình và vai trò moderator

1. Kiểm tra setup, trạng thái Cart và recording.
2. Giải thích consent, quyền dừng và nguyên tắc “đang test sản phẩm, không test
   người tham gia”.
3. Đọc scenario đúng như script; yêu cầu think aloud.
4. Quan sát trung lập, không gợi ý vị trí/nút. Chỉ can thiệp khi participant
   hoàn toàn bế tắc và phải ghi rõ hint.
5. Kết thúc task và hỏi ba câu phỏng vấn; custom scale được gửi bổ sung sau
   session vào ngày 15/11/2026.
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
- wording scenario và ba câu phỏng vấn có gây nhầm không;
- setup, test account, coupon và recording có hoạt động không;
- task có quá dài/ngắn không;
- thay đổi nào được áp dụng trước 7 session.

### Pilot record

- Pilot participant: `P00` — Trần Gia Hiển, sinh viên IT không theo hướng
  tester, ngoài lớp HW03; contact mask `2312****@student.hcmus.edu.vn`.
- Thời điểm: 12:30 ngày 14/11/2026, trước 7 session chính.
- Hình thức và consent: Online; đã đồng ý tham gia và ghi màn hình + audio.
- Kết quả: Participant thực hiện được scenario; lỗi của SUT xuất hiện trong
  luồng và có thể quan sát đúng mục tiêu kiểm thử. Không phát hiện wording khó
  hiểu, setup hỏng hoặc vấn đề timing cần chặn study.
- Thay đổi sau pilot: Không thay đổi scenario, ba câu phỏng vấn hoặc procedure
  vì pilot không phát hiện vấn đề thuộc thiết kế buổi test. Defect của SUT được
  giữ nguyên để quan sát trong các session chính, không sửa hoặc giải thích
  trước cho participant. Custom scale chưa tồn tại tại thời điểm pilot nên
  không thuộc phạm vi được pilot xác nhận.
- Quyết định sẵn sàng chạy M6: Sẵn sàng; tiếp tục 7 session chính với cùng
  scenario và quy trình.

Trong các session chính, moderator không đưa leading hint hoặc chỉ dẫn UI.

## 13. Protocol deviations / chronology

- `12:30 14/11/2026`: pilot P00 chạy scenario AirPods Pro 2, ba câu phỏng vấn
  và procedure thực tế; không dùng SUS hoặc custom scale.
- `18:53 14/11/2026`: commit M5 `b991a75` lưu AI preparation draft dùng iPhone
  15 Pro Max và SUS. Đây là draft tài liệu không được dùng làm moderator script
  cho pilot hoặc bảy session chính.
- Sau pilot ngày 14/11/2026: bảy session chính dùng scenario AirPods Pro 2 và
  ba câu phỏng vấn đã ghi trong session records.
- `15/11/2026`: custom 4-item scale được tạo và gửi follow-up. Việc này lệch với
  protocol “scale completed after each session”; scale cũng chưa được pilot-test.
- Không sửa lịch sử hoặc bổ sung câu trả lời hồi tố. Sai lệch trên được công bố
  khi diễn giải kết quả và là giới hạn của study.

## 14. Rủi ro và kiểm soát bias

- Không tuyển bạn cùng lớp HW03.
- Không giải thích UI hoặc nhắc participant về bug đã biết.
- Dùng cùng scenario, trạng thái đầu và moderator script cho mọi session.
- Probe theo observation thật nhưng không đặt câu hỏi dẫn dắt.
- Tách defect của SUT khỏi systemic UX issue khi phân tích M7.
- Không dùng AI để tạo participant, quote, observation, response hoặc score.


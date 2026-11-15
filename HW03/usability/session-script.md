# Moderator Script — EShop Purchase Flow

## 1. Trước khi participant vào session

- Xác minh SUT/API hoạt động, Cart trống và test account đăng nhập được.
- Xác minh sản phẩm `AirPods Pro 2` và coupon `SAVE10`.
- Mở trang chủ, tắt notification không liên quan và chuẩn bị screen recording.
- Mở file session tương ứng nhưng chưa điền observation giả định.

## 2. Chào và consent

> Cảm ơn bạn đã tham gia. Hôm nay mình đang kiểm tra sản phẩm EShop, không phải
> kiểm tra khả năng của bạn. Không có thao tác đúng hay sai từ phía bạn; mọi
> khó khăn đều giúp mình hiểu giao diện cần cải thiện ở đâu.

> Session dự kiến mất khoảng 10 phút. Bạn có thể dừng hoặc bỏ qua câu hỏi bất
> kỳ lúc nào. Mình muốn ghi màn hình [và audio] để xem lại thao tác. Dữ liệu chỉ
> dùng cho bài tập, contact sẽ được che khi lưu vào repository. Bạn có đồng ý
> tiếp tục và đồng ý với phạm vi ghi hình này không?

Moderator ghi riêng `Consent to participate` và `Consent to record`; không tự
suy ra consent từ việc participant tiếp tục nói chuyện.

## 3. Think-aloud practice

> Trong lúc làm, bạn hãy nói thành tiếng điều bạn đang tìm, điều bạn mong đợi
> sẽ xảy ra và bất kỳ chỗ nào khiến bạn phân vân. Mình có thể im lặng để tránh
> ảnh hưởng thao tác của bạn.

Nếu participant chưa quen, dùng một ví dụ không liên quan EShop, chẳng hạn mô
tả cách chọn một cuốn sách trên bàn; không demo giao diện đang test.

## 4. Task scenario

Đọc nguyên văn một lần:

> Bạn muốn mua **AirPods Pro 2** với ngân sách **7.000.000 ₫**. Hãy sử dụng
> EShop để tìm và mua sản phẩm, áp dụng mã **SAVE10** trước khi hoàn tất đơn
> hàng.

> Bạn có thể bắt đầu khi sẵn sàng.

Bắt đầu timer khi participant thực hiện hành động đầu tiên.

## 5. Trong task

- Quan sát trung lập; ghi timestamp, bước flow, hesitation, error, backtrack,
  recovery và câu nói thật.
- Không chỉ vào UI, không gọi tên nút cần bấm, không giải thích bug.
- Khi participant im lặng: “Bạn đang nghĩ gì lúc này?”
- Khi hỏi “Tôi phải bấm đâu?”: “Bạn hãy làm điều bạn sẽ làm nếu đang ở một
  mình.”
- Chỉ khi hoàn toàn bế tắc mới dùng một hint định hướng chung; ghi nguyên văn
  hint và đánh task `Partial` nếu hint ảnh hưởng completion.
- Nếu lỗi SUT chặn task, cho participant mô tả điều họ mong đợi; không tự sửa
  dữ liệu rồi ghi như họ đã hoàn tất.

Dừng timer khi có xác nhận thành công, participant từ bỏ hoặc moderator quyết
định task bị blocker.

## 6. Post-test interview

Ba câu đã hỏi trong session:

1. Có thời điểm nào bạn không chắc phải làm gì tiếp theo không?
2. Ở lúc thanh toán, các thông tin như giá, voucher và tổng tiền có được xử lý
   đúng với những gì bạn dự định không?
3. Nếu với luồng này EShop được đưa vào thực tế, bạn có sử dụng không? Vì sao?

Không tranh luận, bảo vệ thiết kế hoặc xác nhận participant “đã hiểu đúng”.

## 7. Custom scale bổ sung

Sau bảy session, participant nhận form bổ sung gồm bốn item Likert 1–5 về
clarity, error recovery, speed và trust. Nội dung và raw response nằm trong
[post-test-survey.md](post-test-survey.md). Không mô tả đây là SUS và không
quy đổi điểm sang thang 0–100.

Việc thu bổ sung này phải được ghi rõ trong report để không tạo ấn tượng scale
đã được hỏi ngay trong session.

## 8. Kết thúc

> Cảm ơn bạn. Những gì bạn vừa chia sẻ sẽ được dùng để tổng hợp vấn đề
> usability cho bài tập. Nếu sau session bạn muốn rút lại recording, hãy liên
> hệ với mình qua kênh đã dùng để mời tham gia.

- Dừng recording và xác minh file evidence đã lưu.
- Hoàn thiện session notes khi ký ức còn mới nhưng không thêm quote không có
  trong recording/notes.
- Reset Cart, account và browser state trước participant tiếp theo.


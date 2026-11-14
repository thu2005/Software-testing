# Moderator Script — EShop Purchase Flow

## 1. Trước khi participant vào session

- Xác minh SUT/API hoạt động, Cart trống và test account đăng nhập được.
- Xác minh sản phẩm `iPhone 15 Pro Max` và coupon `SAVE10`.
- Mở trang chủ, tắt notification không liên quan và chuẩn bị screen recording.
- Mở file session tương ứng nhưng chưa điền observation giả định.

## 2. Chào và consent

> Cảm ơn bạn đã tham gia. Hôm nay mình đang kiểm tra sản phẩm EShop, không phải
> kiểm tra khả năng của bạn. Không có thao tác đúng hay sai từ phía bạn; mọi
> khó khăn đều giúp mình hiểu giao diện cần cải thiện ở đâu.

> Session dự kiến mất khoảng TODO phút. Bạn có thể dừng hoặc bỏ qua câu hỏi bất
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

> Bạn muốn mua **iPhone 15 Pro Max** trên EShop. Bạn có mã giảm giá
> **SAVE10**. Hãy hoàn tất việc mua **1 sản phẩm** bằng mã này và dừng lại khi
> bạn thấy hệ thống xác nhận đơn hàng thành công.

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

## 6. Post-test SUS

> Bây giờ bạn vui lòng trả lời 10 câu SUS theo cảm nhận đầu tiên về hệ thống.
> Mỗi câu dùng thang 1 đến 5. Các câu có thể nghe hơi giống nhau nhưng xin trả
> lời đầy đủ và theo đúng thứ tự.

Không giải thích câu theo hướng tích cực/tiêu cực. Nếu participant hỏi nghĩa,
đọc lại bản dịch đã chuẩn bị, không diễn giải thêm theo trải nghiệm vừa xảy ra.

## 7. Probe questions

Hỏi sau khi SUS đã submit:

1. Có thời điểm nào bạn không chắc phải làm gì tiếp theo không? [Nhắc đúng
   moment quan sát được nếu có.]
2. Lúc bạn [gặp lỗi/thao tác lại], bạn đã nghĩ gì? Điều gì giúp hoặc cản bạn
   tiếp tục? Nếu không có lỗi, bỏ qua và ghi lý do.
3. Luồng này nhanh hay chậm hơn bạn mong đợi? Bước nào lâu nhất?
4. Ở Checkout, bạn có tin rằng giá, coupon, tổng tiền và đơn hàng được xử lý
   đúng không? Vì sao?
5. Có điều gì trong luồng này khiến bạn không muốn dùng EShop trong thực tế?

Không tranh luận, bảo vệ thiết kế hoặc xác nhận rằng participant “đã hiểu đúng”.

## 8. Kết thúc

> Cảm ơn bạn. Những gì bạn vừa chia sẻ sẽ được dùng để tổng hợp vấn đề
> usability cho bài tập. Nếu sau session bạn muốn rút lại recording, hãy liên
> hệ với mình qua kênh đã dùng để mời tham gia.

- Dừng recording và xác minh file evidence đã lưu.
- Hoàn thiện session notes khi ký ức còn mới nhưng không thêm quote không có
  trong recording/notes.
- Reset Cart, account và browser state trước participant tiếp theo.


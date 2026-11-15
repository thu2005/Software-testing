# Phân tích Usability Evaluation — Luồng mua hàng EShop

## 1. Dữ liệu và giới hạn phân tích

- Luồng: Search → Product Detail → Cart → Coupon → Checkout.
- Scenario: mua AirPods Pro 2 với ngân sách 7.000.000 ₫ và dùng `SAVE10`.
- Bảy session được ghi màn hình + audio ngày 14/11/2026.
- Pilot P00 được thực hiện lúc 12:30 ngày 14/11/2026, trước 7 session chính;
  không cần thay đổi scenario, ba câu phỏng vấn hoặc procedure. Custom scale
  chưa tồn tại tại thời điểm pilot nên không được pilot-test.
- Custom 4-item scale được thu bổ sung ngày 15/11/2026, không phải ngay sau từng
  session như protocol yêu cầu.
- Phản hồi đầu của P06 bị loại theo xác nhận của sinh viên; chỉ dùng lần hai.
- Dữ liệu định tính về error recovery và speed được tổng hợp từ think-aloud,
  observation và xác nhận bổ sung của moderator ngày 15/11/2026; không dựng
  thành trích dẫn nguyên văn của từng participant.
- Sinh viên xác nhận cả 7 participant đều hoàn thành luồng: task success `7/7`
  (`100%`). Success chỉ phản ánh completion; không phủ nhận các defect nghiêm
  trọng mà participant gặp trong quá trình thực hiện.
- Moderator không đưa leading hint hoặc chỉ dẫn UI.
- Sinh viên xác nhận đã mở quyền truy cập cho cả 7 YouTube evidence URL.

### Protocol deviations / chronology

1. `12:30 14/11/2026`: P00 pilot scenario AirPods Pro 2, ba câu phỏng vấn và
   procedure thực tế; không dùng SUS hoặc custom scale.
2. `18:53 14/11/2026`: commit M5 `b991a75` lưu AI draft dùng iPhone 15 Pro Max
   và SUS. Draft này không phải moderator script được dùng trong study.
3. Bảy session chính dùng scenario AirPods Pro 2 và ba câu phỏng vấn thực tế.
4. `15/11/2026`: custom scale được tạo và gửi follow-up; scale chưa được
   pilot-test và không được hoàn thành ngay sau từng session. Moderator đồng
   thời xác nhận phần tổng hợp định tính về error recovery và speed.

Các sai lệch được công bố thay vì sửa lịch sử; phần xác nhận bổ sung được ghi
đúng ngày 15/11/2026 và không dựng thành trích dẫn nguyên văn.

## 2. Kết quả custom scale

| Participant | Clarity | Error recovery | Speed | Trust | Mean |
|---|---:|---:|---:|---:|---:|
| P01 | 4 | 5 | 3 | 1 | 3.25 |
| P02 | 3 | 3 | 3 | 1 | 2.50 |
| P03 | 4 | 3 | 3 | 3 | 3.25 |
| P04 | 1 | 3 | 3 | 1 | 2.00 |
| P05 | 2 | 3 | 2 | 2 | 2.25 |
| P06 | 3 | 1 | 4 | 1 | 2.25 |
| P07 | 5 | 4 | 2 | 1 | 3.00 |
| **Mean** | **3.14** | **3.14** | **2.86** | **1.43** | **2.64** |

Trust là tiêu chí thấp nhất (`1.43/5`) và thấp hơn rõ rệt ba tiêu chí còn lại.
Kết quả này nhất quán với observation: cả bảy participant đều nhận ra tổng tiền
sai, sáu người nói sẽ không dùng EShop ở trạng thái hiện tại và một người không
chắc sẽ dùng. Điểm chung `2.64/5` chỉ là trung bình của custom scale, không phải
SUS score.

Task success cao (`100%`) nhưng trust rất thấp cho thấy luồng cơ bản đủ đơn
giản để hoàn tất, trong khi tính đúng đắn và độ tin cậy của kết quả thanh toán
vẫn không đạt kỳ vọng.

Raw response và quy tắc tính: [post-test-survey.md](post-test-survey.md).
Nguồn phản hồi gốc: [Google Form](https://forms.gle/uCQqeNNAwXurnxqJ6) và
[Response Sheet](https://docs.google.com/spreadsheets/d/1xmAl07vqtPXbZKT35tTrBGa2BUUKQUL_t1Swt0GW-FI/edit?usp=sharing).

## 3. Tổng hợp finding

| ID | Finding | Evidence | Loại | Severity | Liên kết |
|---|---|---|---|---|---|
| U-01 | Coupon làm tổng tiền của sản phẩm 6 triệu thành 60 triệu | 7/7 participant nhận ra; trust mean 1.43/5 | Defect | Major | [Issue #60](https://github.com/thu2005/CSC13003_eshop/issues/60) |
| U-02 | Add to Cart thiếu feedback/badge rõ ràng | P02, P03, P04, P06, P07; P02/P04 thêm lặp tạo nhiều sản phẩm | Defect + UX pattern | Major | [#54](https://github.com/thu2005/CSC13003_eshop/issues/54), [#62](https://github.com/thu2005/CSC13003_eshop/issues/62) |
| U-03 | Tổng tiền Checkout có thể sửa trực tiếp | P03 sửa thành `60000` và hệ thống vẫn xác nhận thanh toán | Defect | Major | [Issue #49](https://github.com/thu2005/CSC13003_eshop/issues/49) |
| U-04 | Quantity âm được thêm vào Cart và tạo thành tiền âm | P06 nhập `-1`, sau đó phải tự xóa để tiếp tục | Defect | Major | [Issue #50](https://github.com/thu2005/CSC13003_eshop/issues/50) |
| U-05 | Ảnh sản phẩm chỉ là placeholder chữ | P01, P03, P05, P06, P07 nhắc đến thiếu hình; FR-05/FR-06 yêu cầu ảnh; dedicated retest xác nhận lỗi ở listing và Product Detail | Requirement-backed defect + UX issue | Major | [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64), [bug report](../bug-reports/BUG-IA-01-PRODUCT-001.md) |
| U-06 | Điều hướng và ngữ cảnh mua sắm chưa rõ | P01 tìm coupon ở Cart; P02 thiếu đường quay lại và mất search context; P03 không biết đi đâu để thanh toán | Systemic UX issue | Minor | Liên quan [#51](https://github.com/thu2005/CSC13003_eshop/issues/51), [#53](https://github.com/thu2005/CSC13003_eshop/issues/53) |

## 4. Defect và systemic UX issue

Các finding `U-01`, `U-03`, `U-04` là defect chức năng có hành vi sai xác định
được và đã có GitHub Issue từ Task 1. `U-02` kết hợp defect (click đầu bị bỏ qua,
tạo dòng trùng, thiếu badge) với pattern UX rộng hơn là không có feedback đủ rõ.
`U-05` được nâng từ nhận xét UX thành defect có requirement backing: FR-05/FR-06
yêu cầu ảnh sản phẩm, trong khi dedicated retest xác nhận cả listing và Product
Detail chỉ hiển thị placeholder; 5/7 participant cho rằng thiếu hình ảnh hữu
ích. Bug report, hai screenshot và [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64)
đã được cross-link. Phần mất ngữ
cảnh trong `U-06` vẫn là systemic UX issue.

`U-01` và `U-03` được xếp `Major`, không phải `Blocker`, vì cả 7 participant vẫn
hoàn thành task. Tuy nhiên completion không đồng nghĩa giao dịch hợp lệ: sai tổng
tiền và khả năng sửa total làm mất tính toàn vẹn của kết quả thanh toán.

## 5. Recovery quan sát được

- Cả 7 participant đều đọc/nêu lỗi gặp phải cho moderator và vẫn tự tiếp tục
  để hoàn thành luồng.
- P04 nhận ra sản phẩm trùng và tự xóa bớt.
- P06 xóa sản phẩm quantity âm để tiếp tục.
- P07 quay về Home và dùng Add to Cart ở listing khi Product Detail không cho
  kết quả như mong đợi.
- P03 sửa trực tiếp tổng tiền để hoàn thành, nhưng đây là khai thác một defect,
  không phải recovery flow hợp lệ mà sản phẩm thiết kế cho người dùng.

Về speed, cả 7 participant đánh giá luồng khá dễ hiểu và tương tự các website
mua hàng thông thường; không ai xác định bước cụ thể nào đặc biệt gây chậm.

## 6. Ưu tiên cải thiện

1. Sửa công thức coupon/tổng tiền và khóa total khỏi chỉnh sửa trước mọi retest.
2. Validation quantity ở cả client và server; từ chối số âm, 0, rỗng và thập phân.
3. Bảo đảm click Add to Cart hoạt động ngay, hợp nhất dòng trùng và hiển thị
   toast + badge đồng bộ.
4. Bổ sung hình ảnh, mô tả và tín hiệu tin cậy trên listing/Product Detail.
5. Giữ search context khi “mua tiếp”, bổ sung đường quay lại/breadcrumb và làm
   bước sang Checkout dễ nhận biết hơn.

## 7. Giới hạn dữ liệu còn lại

- Tổng hợp error recovery và speed là bản tóm tắt nguyên ý do moderator xác nhận,
  không có verbatim response riêng cho từng participant.
- Custom scale được thu vào ngày hôm sau và chưa được pilot-test; kết quả chỉ
  được diễn giải như follow-up rating, không phải post-session standard scale.
- U-05 đã có dedicated retest screenshot, bug report và GitHub Issue #64 với
  hai ảnh được nhúng từ repository public.

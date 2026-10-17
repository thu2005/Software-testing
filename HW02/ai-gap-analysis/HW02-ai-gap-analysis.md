# AI Gap Analysis — HW02

> Phạm vi hiện tại: FR-01 và FR-07. Tài liệu này được dùng chung cho toàn bộ HW02; khi phát hiện gap ở feature khác, bổ sung dòng mới vào bảng bên dưới.

## 1. Mục đích

Tài liệu ghi lại những điểm AI bỏ sót, suy luận quá mức hoặc cần con người hiệu chỉnh sau khi rà soát analysis, test case, test run và bug report. Chỉ ghi nhận gap có căn cứ; nếu không phát hiện gap thì không tạo nội dung riêng cho feature đó.

## 2. Tóm tắt gap

| Feature | Gap / rủi ro từ AI | Vì sao AI bỏ sót hoặc dễ sai | Cách sinh viên đã xử lý |
|---|---|---|---|
| FR-07 | AI ban đầu chỉ tập trung vào yêu cầu chức năng FR-07 và chưa đưa đầy đủ các yêu cầu giao diện dùng chung FR-21, FR-23 vào ma trận coverage của trang Giỏ hàng. | Prompt và traceability ban đầu giới hạn theo mã feature, nên các yêu cầu dùng chung như breadcrumb, badge giỏ hàng, trạng thái active của navbar, màu nút, cấu trúc `<h1>` và Tab Order dễ bị bỏ qua. | Rà soát lại phạm vi với SRS và ghi nhận đây là giới hạn coverage của bộ test FR-07 hiện tại. Không tự kết luận hoặc tạo thêm bug chỉ từ ảnh có sẵn đối với hành vi chưa được kiểm thử trực tiếp. |
| FR-07 | Test case `TC-FR-07-DT-007` kiểm tra `Tiếp tục mua sắm` nhưng không cố định trạng thái giỏ rỗng hay có sản phẩm. Hai trạng thái này hiển thị hai nhánh UI khác nhau. | AI gộp hành vi điều hướng về trang chủ thành một lớp duy nhất và chưa xét sự khác biệt về nhãn liên kết giữa các trạng thái giỏ. | Giới hạn kết luận Pass của lần chạy vào trạng thái giỏ rỗng đã thực thi; không khái quát kết quả đó cho trạng thái giỏ có sản phẩm. |
| FR-07 | AI có thể diễn giải các sai lệch phụ xuất hiện trong screenshot thành bug dù test case không kiểm tra trực tiếp điều kiện đó. | Ảnh tĩnh cho thấy giao diện nhưng không chứng minh được đầy đủ hành vi, cấu trúc DOM hoặc thứ tự focus. | Chỉ sáu defect FR-07 được xác nhận qua test đã thực thi mới được lập bug report và GitHub Issue. Các quan sát ngoài oracle được giữ ở mức giới hạn coverage cho đến khi có test và evidence phù hợp. |

## 3. Feature không có gap được ghi nhận

- **FR-01:** Không phát hiện gap có căn cứ sau khi đối chiếu analysis, test case, execution và bug report. Phân tích FR-01 đã bao gồm các yêu cầu form dùng chung FR-22 ngay từ đầu nên không cần tạo mục gap riêng.

## 4. Nguyên tắc rút ra

AI hỗ trợ tốt việc tạo cấu trúc và gợi ý coverage, nhưng có thể giới hạn phạm vi theo đúng mã feature được nêu trong prompt hoặc suy luận quá mức từ evidence gián tiếp. Khi review, cần đối chiếu cả yêu cầu chức năng và yêu cầu dùng chung, đồng thời phân biệt rõ ba trường hợp: bug đã được test xác nhận, test coverage còn thiếu và quan sát chưa đủ bằng chứng. Chỉ bug đã xác nhận mới được đưa vào bug report; coverage chưa thực hiện phải được mô tả đúng là giới hạn, không được trình bày như kết quả Fail.

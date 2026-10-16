# Đặc tả chức năng — FR-01: Đăng ký tài khoản

## 1. Phạm vi và nguồn

| Field | Value |
|---|---|
| Mã yêu cầu / Nhóm / Nền tảng | FR-01 / A / Web |
| Mã dùng cho tệp | FR-01-dang-ky |
| Tác nhân | Khách truy cập đăng ký tài khoản |
| Nguồn nghiệp vụ | [Bản chụp README của SUT](system-requirements.md), §2 FR-01 và §8 FR-22 áp dụng cho form đăng ký |
| Nguồn API | [Bản chụp đặc tả API](api-specification.md), §1.1 |
| Phiên bản SUT | `85af3ba875c88283615e22cb108f13e2fccaf0e9` của repo `CSC13003-eshop/` |

Hai bản chụp đặc tả giữ nguyên nội dung nguồn, bao gồm thuật ngữ/tiêu đề gốc. Các sản phẩm phân tích dùng nội dung tiếng Việt, tiêu đề cột tiếng Anh. Không dùng mã nguồn triển khai để suy ra quy tắc hay kết quả mong đợi.

## 2. Điều kiện tiên quyết

- Có Web và API EShop đang chạy; mở trang đăng ký qua liên kết “Đăng ký”. URL quan sát khi khảo sát: `/register`.
- Dùng email thử nghiệm riêng cho từng ca. Ca email trùng chuẩn bị tài khoản trước bằng một lần đăng ký hợp lệ và ghi kết quả chuẩn bị.
- Thực thi trên bản sao SUT trong `HW02/.runtime/fr01/`; dữ liệu phát sinh không ghi vào repo gốc. Web dùng cổng `15173` do cổng `5173` bị Windows từ chối; API dùng cổng `3000`.

## 3. Đầu vào, đầu ra và quy tắc

| Rule ID | Input / Output | Type | Rule / Constraint | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|
| R01 | `name` | Chuỗi | Họ tên bắt buộc | Từ chối khi bỏ trống | README FR-01, dòng yêu cầu cung cấp Họ Tên |
| R02 | `email` | Chuỗi | Bắt buộc, định dạng hợp lệ | Từ chối khi trống hoặc sai định dạng rõ ràng | README FR-01 |
| R03 | `email` và dữ liệu tài khoản | Chuỗi/trạng thái | Email duy nhất | Từ chối đăng ký email đã tồn tại | README FR-01 |
| R04 | `password` | Chuỗi | Bắt buộc, ít nhất 8 ký tự | Từ chối chuỗi dưới 8 ký tự | README FR-01 |
| R05 | `password` | Thành phần chuỗi | Có ít nhất 1 chữ hoa | Từ chối khi không có chữ hoa | README FR-01 |
| R06 | `password` | Thành phần chuỗi | Có ít nhất 1 chữ thường | Từ chối khi không có chữ thường | README FR-01 |
| R07 | `password` | Thành phần chuỗi | Có ít nhất 1 chữ số | Từ chối khi không có chữ số | README FR-01 |
| R08 | `password` | Thành phần chuỗi | Có ít nhất 1 ký tự trong `@ $ ! % * ? &` | Từ chối khi không có ký tự thuộc tập này | README FR-01 |
| R09 | Xác nhận mật khẩu | Chuỗi/quan hệ | Form phải có trường xác nhận; từ chối khi không khớp | Cho nhập xác nhận và kiểm tra bằng mật khẩu | README FR-01 |
| R10 | Điều hướng sau thành công | Đầu ra UI | Chuyển tới trang đăng nhập | Đến màn hình đăng nhập khi đăng ký thành công | README FR-01 |
| R11 | Trường bắt buộc trên form | Đầu ra UI | Nhãn trường bắt buộc có `*` | Hiển thị dấu bắt buộc | README FR-22 |
| R12 | Trường Email | Kiểu input UI | `type="email"` | Trình duyệt nhận biết kiểu email | README FR-22 |
| R13 | Trường Mật khẩu | Kiểu input UI | `type="password"` | Không hiển thị rõ mật khẩu | README FR-22 |
| R14 | Vị trí thông báo lỗi | Đầu ra UI | Lỗi xuất hiện trên nút submit | Người dùng thấy lỗi trước nút gửi | README FR-22 |
| R15 | `POST /api/register` | Giao diện API | Body mô tả `name`, `email`, `password`; thành công 200, có `message` và `id` | Phản hồi `User registered successfully`, `id` của tài khoản vừa tạo | API §1.1 |

`id: 1` trong tài liệu API là dữ liệu minh họa, không buộc mọi tài khoản mới có ID 1. Không chốt status HTTP hoặc câu chữ lỗi chưa được đặc tả; ca từ chối kiểm tra không được báo đăng ký thành công/cấp ID mới, đồng thời ghi response thực tế.

## 4. Quan hệ phụ thuộc và phạm vi hai lớp

- Email phải đúng định dạng và chưa tồn tại. Ca email trùng dùng chuỗi đúng định dạng; ca sai định dạng không đồng thời dùng email có sẵn.
- Khi kiểm tra từng nhóm ký tự mật khẩu, giữ độ dài ít nhất 8 và ba nhóm còn lại hợp lệ.
- Mật khẩu trống vi phạm đồng thời độ dài và các nhóm ký tự; tách thành nhánh thiếu dữ liệu bắt buộc, không tuyên bố ca này isolate riêng một quy tắc thành phần.
- API §1.1 không mô tả `confirmPassword`; bộ ca API chỉ gửi ba trường được tài liệu hóa. Kiểm tra trường xác nhận/khớp mật khẩu và điều hướng là ca UI, không suy diễn API đã kiểm tra xác nhận.
- Khi trường xác nhận không tồn tại, ca kiểm tra sự hiện diện có thể Fail; ca cần nhập xác nhận phải ghi Blocked do thiếu điều kiện thao tác. Các ca API vẫn thực thi độc lập.

## 5. Thông tin chưa được đặc tả

| Item | Missing Information / Assumption | Impact | Confirmation Status |
|---|---|---|---|
| Họ tên | Không có min/max độ dài, quy tắc trim, Unicode hoặc ký tự cho phép | Chỉ suy ra rỗng/không rỗng; không tự đặt giới hạn 50/255 | Chưa được đặc tả |
| Email | Không có max độ dài, phân biệt hoa/thường, trim hoặc chuẩn regex chi tiết | Dùng lỗi định dạng rõ ràng; không phán email hiếm/chuỗi whitespace khi thiếu oracle | Chưa được đặc tả |
| Mật khẩu | Không có cận trên, quy tắc Unicode hoặc cho phép cấm thêm ký tự khác | BVA dùng chuỗi ASCII; `#` một mình không thay ký tự trong tập yêu cầu; không kết luận `#` bị cấm khi đã có `!` | Chưa được đặc tả |
| Xác nhận | Không có hợp đồng API xác nhận và thông báo lỗi chính xác | Thử xác nhận trên UI; không thêm field API rồi nhận là giao diện được hỗ trợ | Chưa được đặc tả |
| Giới hạn nhập UI | Không có giới hạn cực đại trong đặc tả | Quan sát thuộc tính DOM để ghi giới hạn thực tế, không đổi nó thành quy tắc nghiệp vụ | Chưa được đặc tả |
| Rà soát sinh viên | Chưa có bằng chứng sinh viên rà soát bộ FR-01 | Agent review không thay human review | Chưa ghi nhận |

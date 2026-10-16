# Phân tích Domain Testing — FR-01: Đăng ký tài khoản

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Nguồn đặc tả | [system-requirements.md](../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); FR-22 trong cùng tài liệu |
| Actor / Preconditions | Người dùng chưa có tài khoản; truy cập form đăng ký; hệ thống hoạt động |
| Input | Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu; trạng thái tồn tại của Email |
| Success condition | Tạo tài khoản và chuyển người dùng tới trang Đăng nhập |
| Error conditions | Thiếu trường bắt buộc; Email sai định dạng hoặc đã tồn tại; Mật khẩu không đủ mạnh; xác nhận không khớp |

## 2. Biến đầu vào, đầu ra và điều kiện hệ thống

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| Họ Tên | Input | Chuỗi | Có | Không rỗng; min/max và quy tắc khoảng trắng chưa được đặc tả | FR-01 |
| Email | Input | Chuỗi/email | Có | Định dạng hợp lệ như user@domain.com | FR-01, FR-22 |
| Trạng thái Email | Điều kiện hệ thống | Boolean | Có | Chưa tồn tại / đã tồn tại | FR-01 |
| Mật khẩu | Input | Chuỗi | Có | Dài ≥ 8; ≥1 chữ hoa, ≥1 chữ thường, ≥1 chữ số, ≥1 ký tự trong @ $ ! % * ? & | FR-01, FR-22 |
| Xác nhận mật khẩu | Input | Chuỗi | Có | Khớp chính xác với Mật khẩu | FR-01, FR-22 |
| Kết quả đăng ký | Output | Trạng thái | Không áp dụng | Thành công hoặc bị từ chối theo từng loại vi phạm | FR-01 |
| Điều hướng | Output | Trang | Không áp dụng | Thành công thì chuyển tới trang Đăng nhập | FR-01 |
| Cấu trúc/hiển thị form | Output | UI | Không áp dụng | Dấu *, input type và vị trí lỗi theo FR-22 | FR-22 |

## 3. Các lớp tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| EC-NAME-V01 | Họ Tên | Chuỗi không rỗng | Hợp lệ | Nguyễn Văn An | Cho phép tiếp tục đánh giá form | FR-01 |
| EC-NAME-I01 | Họ Tên | Không cung cấp giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-EMAIL-V01 | Email | Có định dạng email hợp lệ | Hợp lệ | fr01.dt001@example.com | Cho phép tiếp tục đánh giá form | FR-01 |
| EC-EMAIL-I01 | Email | Không cung cấp giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-EMAIL-I02 | Email | Không có định dạng user@domain.com | Không hợp lệ | user-domain.com | Từ chối đăng ký | FR-01 |
| EC-EMAILSTATE-V01 | Trạng thái Email | Email chưa tồn tại trong hệ thống | Hợp lệ | Email mới | Cho phép đăng ký | FR-01 |
| EC-EMAILSTATE-I01 | Trạng thái Email | Email đã tồn tại trong hệ thống | Không hợp lệ | existing.fr01@example.com | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-V01 | Mật khẩu | Ít nhất 8 ký tự và đủ bốn nhóm ký tự | Hợp lệ | Abcdef1!xy | Cho phép tiếp tục đánh giá form | FR-01 |
| EC-PASSWORD-I01 | Mật khẩu | Không cung cấp giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I02 | Mật khẩu | Có 1–7 ký tự | Không hợp lệ | Aa1!xyz | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I03 | Mật khẩu | Đủ độ dài nhưng không có chữ hoa | Không hợp lệ | abcdef1!xy | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I04 | Mật khẩu | Đủ độ dài nhưng không có chữ thường | Không hợp lệ | ABCDEF1!XY | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I05 | Mật khẩu | Đủ độ dài nhưng không có chữ số | Không hợp lệ | Abcdefg!xy | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I06 | Mật khẩu | Đủ độ dài nhưng không có ký tự thuộc tập @, $, !, %, *, ?, & | Không hợp lệ | Abcdef1#xy | Từ chối đăng ký | FR-01 |
| EC-CONFIRM-V01 | Xác nhận mật khẩu | Có giá trị và khớp Mật khẩu | Hợp lệ | Abcdef1!xy | Cho phép đăng ký | FR-01 |
| EC-CONFIRM-I01 | Xác nhận mật khẩu | Không cung cấp giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-CONFIRM-I02 | Xác nhận mật khẩu | Có giá trị nhưng không khớp Mật khẩu | Không hợp lệ | Abcdef1!xz | Từ chối đăng ký | FR-01 |
| EC-FORM-V01 | Nhãn trường bắt buộc | Cả bốn nhãn có ký hiệu * | Hợp lệ | Quan sát form | Đúng cấu trúc form | FR-22 |
| EC-FORM-V02 | Kiểu trường Email | Email dùng type=email | Hợp lệ | Quan sát DOM | Đúng cấu trúc form | FR-22 |
| EC-FORM-V03 | Kiểu trường mật khẩu | Hai trường mật khẩu dùng type=password | Hợp lệ | Quan sát DOM | Che nội dung nhập | FR-22 |
| EC-FORM-V04 | Vị trí thông báo lỗi | Thông báo lỗi nằm trên nút submit | Hợp lệ | Kích hoạt lỗi | Hiển thị đúng vị trí | FR-22 |
| EC-RESULT-O01 | Kết quả | Đăng ký thành công và chuyển tới trang Đăng nhập | Output | Dữ liệu hợp lệ | Tài khoản được tạo; redirect | FR-01 |
| EC-RESULT-O02 | Kết quả | Từ chối do input thiếu/sai quy tắc | Output | Input không hợp lệ | Không tạo tài khoản; không redirect | FR-01 |
| EC-RESULT-O03 | Kết quả | Từ chối do Email trùng | Output | Email đã tồn tại | Không tạo tài khoản thứ hai | FR-01 |
| EC-RESULT-O04 | Kết quả | Từ chối do mật khẩu không khớp | Output | Hai giá trị khác nhau | Không tạo tài khoản | FR-01 |
| EC-RESULT-O05 | Kết quả | Cấu trúc loại input và nhãn đúng | Output | Quan sát form | Thỏa FR-22 | FR-22 |
| EC-RESULT-O06 | Kết quả | Thông báo lỗi nằm trên nút submit | Output | Input gây lỗi | Thỏa FR-22 | FR-22 |

## 4. Quan hệ phụ thuộc

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| DC-01 | Email và dữ liệu hệ thống | Email hợp lệ chưa tồn tại | Email hợp lệ đã tồn tại | Cô lập bằng dữ liệu tiền điều kiện; giữ các field khác hợp lệ | FR-01 |
| DC-02 | Xác nhận mật khẩu và Mật khẩu | Hai chuỗi khớp | Thiếu xác nhận hoặc hai chuỗi không khớp | Cô lập bằng hai chuỗi cụ thể; riêng Mật khẩu rỗng còn vi phạm trường bắt buộc | FR-01 |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| COND-FR-01-DT-001 | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt001@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O01 | Hợp lệ | Đăng ký được chấp nhận và người dùng được chuyển tới trang Đăng nhập. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-002 | EC-NAME-I01 | Họ Tên=[để trống]; Email=fr01.dt002@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối; không tạo tài khoản và không chuyển tới trang Đăng nhập. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-003 | EC-EMAIL-I01 | Họ Tên=Nguyễn Văn An; Email=[để trống]; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối; không tạo tài khoản và không chuyển tới trang Đăng nhập. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-004 | EC-EMAIL-I02 | Họ Tên=Nguyễn Văn An; Email=user-domain.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Email không có định dạng hợp lệ; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-005 | EC-EMAILSTATE-I01 | Họ Tên=Nguyễn Văn An; Email=existing.fr01@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email đã tồn tại | EC-RESULT-O03 | Không hợp lệ | Đăng ký bị từ chối vì Email không duy nhất; không tạo tài khoản thứ hai. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-006 | EC-PASSWORD-I01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt006@example.com; Mật khẩu=[để trống]; Xác nhận=[để trống]; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối; không tạo tài khoản. Ca này đồng thời không thể thỏa quan hệ xác nhận do Mật khẩu bắt buộc bị thiếu. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-007 | EC-PASSWORD-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt007@example.com; Mật khẩu=Aa1!xyz (7 ký tự); Xác nhận=Aa1!xyz; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu có ít hơn 8 ký tự; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-008 | EC-PASSWORD-I03 | Họ Tên=Nguyễn Văn An; Email=fr01.dt008@example.com; Mật khẩu=abcdef1!xy; Xác nhận=abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu không có chữ hoa; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-009 | EC-PASSWORD-I04 | Họ Tên=Nguyễn Văn An; Email=fr01.dt009@example.com; Mật khẩu=ABCDEF1!XY; Xác nhận=ABCDEF1!XY; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu không có chữ thường; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-010 | EC-PASSWORD-I05 | Họ Tên=Nguyễn Văn An; Email=fr01.dt010@example.com; Mật khẩu=Abcdefg!xy; Xác nhận=Abcdefg!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu không có chữ số; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-011 | EC-PASSWORD-I06 | Họ Tên=Nguyễn Văn An; Email=fr01.dt011@example.com; Mật khẩu=Abcdef1#xy; Xác nhận=Abcdef1#xy; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu không có ký tự thuộc tập @, $, !, %, *, ?, &; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-012 | EC-CONFIRM-I01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt012@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=[để trống]; trạng thái=Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì thiếu Xác nhận mật khẩu; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-013 | EC-CONFIRM-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt013@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xz; trạng thái=Email chưa tồn tại | EC-RESULT-O04 | Không hợp lệ | Đăng ký bị từ chối vì hai trường mật khẩu không khớp; không tạo tài khoản. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-014 | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03 | Họ Tên=Không nhập dữ liệu; Email=Không nhập dữ liệu; Mật khẩu=Không nhập dữ liệu; Xác nhận=Không nhập dữ liệu; trạng thái=Không áp dụng; chỉ quan sát form | EC-RESULT-O05 | Hợp lệ | Nhãn của bốn trường bắt buộc có ký hiệu *; Email dùng type=email; Mật khẩu và Xác nhận mật khẩu dùng type=password. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |
| COND-FR-01-DT-015 | EC-FORM-V04 | Họ Tên=Nguyễn Văn An; Email=user-domain.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; trạng thái=Email chưa tồn tại | EC-RESULT-O06 | Không hợp lệ; kiểm tra cách hiển thị | Đăng ký bị từ chối và thông báo lỗi xuất hiện phía trên nút submit. | Đại diện lớp mục tiêu; các điều kiện khác dùng giá trị danh nghĩa hợp lệ. |

## 6. Quá trình lựa chọn ca kiểm thử

`TC-FR-01-DT-001` gộp toàn bộ lớp hợp lệ tương thích để tạo baseline thành công. Mỗi ca âm từ 002 đến 013 chỉ nhắm một lớp đầu vào không hợp lệ; các field còn lại hợp lệ. Ngoại lệ được ghi rõ ở ca Mật khẩu rỗng: xác nhận rỗng giữ quan hệ bằng nhau nhưng không thể làm Mật khẩu hợp lệ. Các ký tự `@`, `$`, `!`, `%`, `*`, `?`, `&` cùng một lớp vì đặc tả quy định cùng hành vi; `!` là đại diện. Các ca 014–015 kiểm tra quy tắc form FR-22 áp dụng cho form đăng ký. Miền có thứ tự của độ dài và số lượng nhóm ký tự được chuyển sang BVA.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| TC-FR-01-DT-001 | COND-FR-01-DT-001 | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01; EC-RESULT-O01 | DC-01, DC-02 | FR-01 | Đăng ký với toàn bộ dữ liệu hợp lệ |
| TC-FR-01-DT-002 | COND-FR-01-DT-002 | EC-NAME-I01; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối khi Họ Tên để trống |
| TC-FR-01-DT-003 | COND-FR-01-DT-003 | EC-EMAIL-I01; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối khi Email để trống |
| TC-FR-01-DT-004 | COND-FR-01-DT-004 | EC-EMAIL-I02; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Email sai định dạng |
| TC-FR-01-DT-005 | COND-FR-01-DT-005 | EC-EMAILSTATE-I01; EC-RESULT-O03 | DC-01 | FR-01 | Từ chối Email đã tồn tại |
| TC-FR-01-DT-006 | COND-FR-01-DT-006 | EC-PASSWORD-I01; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối khi Mật khẩu để trống |
| TC-FR-01-DT-007 | COND-FR-01-DT-007 | EC-PASSWORD-I02; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu ngắn hơn 8 ký tự |
| TC-FR-01-DT-008 | COND-FR-01-DT-008 | EC-PASSWORD-I03; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu thiếu chữ hoa |
| TC-FR-01-DT-009 | COND-FR-01-DT-009 | EC-PASSWORD-I04; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu thiếu chữ thường |
| TC-FR-01-DT-010 | COND-FR-01-DT-010 | EC-PASSWORD-I05; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu thiếu chữ số |
| TC-FR-01-DT-011 | COND-FR-01-DT-011 | EC-PASSWORD-I06; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu thiếu ký tự đặc biệt cho phép |
| TC-FR-01-DT-012 | COND-FR-01-DT-012 | EC-CONFIRM-I01; EC-RESULT-O02 | DC-02 | FR-01 | Từ chối khi Xác nhận mật khẩu để trống |
| TC-FR-01-DT-013 | COND-FR-01-DT-013 | EC-CONFIRM-I02; EC-RESULT-O04 | DC-02 | FR-01 | Từ chối khi hai mật khẩu không khớp |
| TC-FR-01-DT-014 | COND-FR-01-DT-014 | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03; EC-RESULT-O05 | Không áp dụng | FR-22 | Kiểm tra cấu trúc form đăng ký |
| TC-FR-01-DT-015 | COND-FR-01-DT-015 | EC-FORM-V04; EC-RESULT-O06 | Không áp dụng | FR-22 | Kiểm tra vị trí thông báo lỗi |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào hợp lệ / không hợp lệ | 9 / 11 |
| Số lớp đầu ra / quan hệ phụ thuộc | 6 / 2 |
| Số điều kiện / ca kiểm thử | 15 / 15 |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01, EC-RESULT-O01 | TC-FR-01-DT-001 | Đã bao phủ | Chưa chạy | Không có |
| EC-NAME-I01 | TC-FR-01-DT-002 | Đã bao phủ | Chưa chạy | Không có |
| EC-EMAIL-I01, EC-EMAIL-I02 | TC-FR-01-DT-003, TC-FR-01-DT-004 | Đã bao phủ | Chưa chạy | Không có |
| EC-EMAILSTATE-I01, DC-01, EC-RESULT-O03 | TC-FR-01-DT-005 | Đã bao phủ | Chưa chạy | Cần chuẩn bị Email đã tồn tại |
| EC-PASSWORD-I01 đến EC-PASSWORD-I06 | TC-FR-01-DT-006 đến TC-FR-01-DT-011 | Đã bao phủ | Chưa chạy | Không có |
| EC-CONFIRM-I01, EC-CONFIRM-I02, DC-02, EC-RESULT-O04 | TC-FR-01-DT-012, TC-FR-01-DT-013 | Đã bao phủ | Chưa chạy | Không có |
| EC-RESULT-O02 | TC-FR-01-DT-002 đến 004, 006 đến 012 | Đã bao phủ | Chưa chạy | Không có |
| EC-FORM-V01 đến EC-FORM-V04, EC-RESULT-O05, EC-RESULT-O06 | TC-FR-01-DT-014, TC-FR-01-DT-015 | Đã bao phủ | Chưa chạy | Không có |

## 9. Giả định và thông tin chưa được đặc tả

- Không có độ dài tối đa cho Họ Tên, Email hoặc Mật khẩu; không tạo lớp “quá dài”.
- Cú pháp email đầy đủ, quy tắc trim, phân biệt hoa/thường và Unicode chưa được đặc tả; `user-domain.com` chỉ đại diện chắc chắn cho trường hợp thiếu `@`.
- Đặc tả không cho nội dung thông báo lỗi, nên oracle chỉ yêu cầu bị từ chối và tác động dữ liệu/điều hướng quan sát được.
- “Khớp” được hiểu là hai giá trị nhập giống nhau; quy tắc chuẩn hóa chưa được đặc tả.
- Việc kiểm tra đã thiết kế nhưng chưa thực thi; mọi test case có trạng thái `Not Run`.

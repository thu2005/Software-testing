# Phân tích Domain Testing — FR-01: Đăng ký tài khoản

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Nguồn đặc tả | [system-requirements.md](../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); FR-22 trong cùng tài liệu |
| Input | Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu; trạng thái tồn tại của Email |
| Success condition | Tạo tài khoản và chuyển tới trang Đăng nhập |
| Error conditions | Thiếu trường; Email sai/trùng; Mật khẩu yếu; xác nhận không khớp |

## 2. Biến đầu vào, đầu ra và điều kiện hệ thống

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| Họ Tên | Input | Chuỗi | Có | Không rỗng; không có min/max khác | FR-01 |
| Email | Input | Email | Có | Đúng định dạng và duy nhất | FR-01, FR-22 |
| Mật khẩu | Input | Chuỗi | Có | Dài ≥8; có chữ hoa, chữ thường, số và ký tự trong @ $ ! % * ? & | FR-01, FR-22 |
| Xác nhận mật khẩu | Input | Chuỗi | Có | Khớp Mật khẩu | FR-01, FR-22 |
| Kết quả/điều hướng | Output | Trạng thái/trang | Không áp dụng | Thành công: tạo tài khoản và tới Đăng nhập; lỗi: từ chối | FR-01 |
| Cấu trúc form | Output | UI | Không áp dụng | Dấu *, input type, vị trí lỗi | FR-22 |

## 3. Các lớp tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| EC-NAME-V01 | Họ Tên | Có giá trị | Hợp lệ | Nguyễn Văn An | Tiếp tục đánh giá form | FR-01 |
| EC-NAME-I01 | Họ Tên | Không có giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-EMAIL-V01 | Email | Có định dạng hợp lệ | Hợp lệ | fr01.dt001@example.com | Tiếp tục đánh giá form | FR-01 |
| EC-EMAIL-I01 | Email | Không có giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-EMAIL-I02 | Email | Sai định dạng user@domain.com | Không hợp lệ | user-domain.com | Từ chối đăng ký | FR-01 |
| EC-EMAILSTATE-V01 | Trạng thái Email | Chưa tồn tại | Hợp lệ | Email mới | Cho phép đăng ký | FR-01 |
| EC-EMAILSTATE-I01 | Trạng thái Email | Đã tồn tại | Không hợp lệ | existing.fr01@example.com | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-V01 | Mật khẩu | Dài ≥8 và đủ bốn nhóm ký tự | Hợp lệ | Abcdef1!xy | Tiếp tục đánh giá form | FR-01 |
| EC-PASSWORD-I01 | Mật khẩu | Không có giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-PASSWORD-I02 | Mật khẩu | Không thỏa ít nhất một rule độ dài/thành phần | Không hợp lệ | abcdefgh | Từ chối đăng ký | FR-01 |
| EC-CONFIRM-V01 | Xác nhận mật khẩu | Có giá trị và khớp | Hợp lệ | Abcdef1!xy | Cho phép đăng ký | FR-01 |
| EC-CONFIRM-I01 | Xác nhận mật khẩu | Không có giá trị | Không hợp lệ | Chuỗi rỗng | Từ chối đăng ký | FR-01 |
| EC-CONFIRM-I02 | Xác nhận mật khẩu | Không khớp Mật khẩu | Không hợp lệ | Abcdef1!xz | Từ chối đăng ký | FR-01 |
| EC-FORM-V01 | Nhãn bắt buộc | Bốn nhãn có dấu * | Hợp lệ | Quan sát form | Đúng cấu trúc | FR-22 |
| EC-FORM-V02 | Kiểu Email | type=email | Hợp lệ | Quan sát DOM | Đúng cấu trúc | FR-22 |
| EC-FORM-V03 | Kiểu mật khẩu | Hai trường dùng type=password | Hợp lệ | Quan sát DOM | Che nội dung | FR-22 |
| EC-FORM-V04 | Vị trí lỗi | Lỗi nằm trên nút submit | Hợp lệ | Kích hoạt lỗi | Đúng vị trí | FR-22 |
| EC-RESULT-O01 | Kết quả | Thành công và redirect | Output | Dữ liệu hợp lệ | Tạo tài khoản; tới Đăng nhập | FR-01 |
| EC-RESULT-O02 | Kết quả | Từ chối input không hợp lệ | Output | Input sai/thiếu | Không tạo tài khoản | FR-01 |
| EC-RESULT-O03 | Kết quả | Từ chối Email trùng | Output | Email tồn tại | Không tạo bản ghi thứ hai | FR-01 |
| EC-RESULT-O04 | Kết quả | Từ chối xác nhận không khớp | Output | Hai chuỗi khác nhau | Không tạo tài khoản | FR-01 |
| EC-RESULT-O05 | Kết quả | Form thỏa FR-22 | Output | Quan sát form/lỗi | Đúng loại input, nhãn và vị trí lỗi | FR-22 |

## 4. Quan hệ phụ thuộc

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| DC-01 | Email và dữ liệu hệ thống | Email chưa tồn tại | Email đã tồn tại | Chuẩn bị trước dữ liệu trùng | FR-01 |
| DC-02 | Xác nhận và Mật khẩu | Hai chuỗi giống nhau | Hai chuỗi khác nhau | Dùng hai chuỗi cụ thể | FR-01 |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| COND-FR-01-DT-001 | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt001@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; Email chưa tồn tại | EC-RESULT-O01 | Hợp lệ | Đăng ký được chấp nhận và chuyển tới trang Đăng nhập. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-002 | EC-NAME-I01, EC-EMAIL-I01, EC-PASSWORD-I01, EC-CONFIRM-I01 | Họ Tên=[để trống]; Email=[để trống]; Mật khẩu=[để trống]; Xác nhận=[để trống]; Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối; không tạo tài khoản và không chuyển tới trang Đăng nhập. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-003 | EC-EMAIL-I02 | Họ Tên=Nguyễn Văn An; Email=user-domain.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Email không hợp lệ; không tạo tài khoản. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-004 | EC-EMAILSTATE-I01 | Họ Tên=Nguyễn Văn An; Email=existing.fr01@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; Email đã tồn tại | EC-RESULT-O03 | Không hợp lệ | Đăng ký bị từ chối vì Email không duy nhất; không tạo tài khoản thứ hai. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-005 | EC-PASSWORD-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt005@example.com; Mật khẩu=abcdefgh; Xác nhận=abcdefgh; Email chưa tồn tại | EC-RESULT-O02 | Không hợp lệ | Đăng ký bị từ chối vì Mật khẩu không thỏa đầy đủ các nhóm ký tự bắt buộc; không tạo tài khoản. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-006 | EC-CONFIRM-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt006@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xz; Email chưa tồn tại | EC-RESULT-O04 | Không hợp lệ | Đăng ký bị từ chối vì hai mật khẩu không khớp; không tạo tài khoản. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |
| COND-FR-01-DT-007 | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03, EC-FORM-V04 | Họ Tên=Nguyễn Văn An; Email=user-domain.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy; Email chưa tồn tại | EC-RESULT-O05 | Kiểm tra UI | Bốn nhãn bắt buộc có dấu *; Email dùng type=email; hai trường mật khẩu dùng type=password; lỗi nằm phía trên nút submit. | Đại diện một nhóm hành vi; gộp có chủ đích để giữ bộ ca gọn. |

## 6. Quá trình lựa chọn ca kiểm thử

Bộ rút gọn dùng một baseline hợp lệ và một đại diện cho mỗi nhóm hành vi lỗi khác nhau. Ca 002 gộp bốn lớp bắt buộc rỗng; ca 005 gộp các tổ hợp Mật khẩu yếu vì cùng kết quả từ chối. Việc gộp làm giảm khả năng xác định chính xác field/rule gây lỗi nếu ca thất bại, nhưng từng rule thành phần của Mật khẩu được cô lập ở BVA. Ca 007 gộp các kiểm tra cấu trúc tĩnh và kích hoạt một lỗi để kiểm tra vị trí. Không tạo Cartesian product. Các trường hợp có cùng hành vi nhưng khác dữ liệu được chủ động loại trừ.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| TC-FR-01-DT-001 | COND-FR-01-DT-001 | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01; EC-RESULT-O01 | Không áp dụng | FR-01 | Đăng ký với dữ liệu hợp lệ |
| TC-FR-01-DT-002 | COND-FR-01-DT-002 | EC-NAME-I01, EC-EMAIL-I01, EC-PASSWORD-I01, EC-CONFIRM-I01; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối khi bỏ trống các trường bắt buộc |
| TC-FR-01-DT-003 | COND-FR-01-DT-003 | EC-EMAIL-I02; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Email sai định dạng |
| TC-FR-01-DT-004 | COND-FR-01-DT-004 | EC-EMAILSTATE-I01; EC-RESULT-O03 | DC-01 | FR-01 | Từ chối Email đã tồn tại |
| TC-FR-01-DT-005 | COND-FR-01-DT-005 | EC-PASSWORD-I02; EC-RESULT-O02 | Không áp dụng | FR-01 | Từ chối Mật khẩu không đủ mạnh |
| TC-FR-01-DT-006 | COND-FR-01-DT-006 | EC-CONFIRM-I02; EC-RESULT-O04 | DC-02 | FR-01 | Từ chối khi Xác nhận mật khẩu không khớp |
| TC-FR-01-DT-007 | COND-FR-01-DT-007 | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03, EC-FORM-V04; EC-RESULT-O05 | Không áp dụng | FR-22 | Kiểm tra yêu cầu cấu trúc và vị trí lỗi của form |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào/UI hợp lệ / không hợp lệ | 9 / 8 |
| Số lớp đầu ra / quan hệ phụ thuộc | 5 / 2 |
| Số điều kiện / ca kiểm thử | 7 / 7 |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| Các lớp hợp lệ; EC-RESULT-O01 | TC-FR-01-DT-001 | Đã bao phủ | Chưa chạy | Gộp baseline hợp lệ |
| Các lớp trường bắt buộc rỗng; EC-RESULT-O02 | TC-FR-01-DT-002 | Đã bao phủ theo nhóm | Chưa chạy | Không cô lập từng field để giảm số ca |
| EC-EMAIL-I02 | TC-FR-01-DT-003 | Đã bao phủ | Chưa chạy | Không có |
| EC-EMAILSTATE-I01, DC-01, EC-RESULT-O03 | TC-FR-01-DT-004 | Đã bao phủ | Chưa chạy | Cần Email tồn tại |
| EC-PASSWORD-I02 | TC-FR-01-DT-005 | Đã bao phủ theo nhóm | Chưa chạy | BVA cô lập từng rule thành phần |
| EC-CONFIRM-I02, DC-02, EC-RESULT-O04 | TC-FR-01-DT-006 | Đã bao phủ | Chưa chạy | Không có |
| EC-FORM-V01 đến EC-FORM-V04; EC-RESULT-O05 | TC-FR-01-DT-007 | Đã bao phủ | Chưa chạy | Gộp kiểm tra cùng form |

## 9. Giả định và thông tin chưa được đặc tả

- Không có số test case tối thiểu trong đề; bộ 7 ca DT là lựa chọn tối ưu hóa có giải thích, không phải exhaustive testing.
- Không có độ dài tối đa, quy tắc trim/Unicode, cú pháp email đầy đủ hoặc nội dung lỗi cụ thể.
- Các ca chỉ được thiết kế, chưa thực thi; trạng thái `Not Run`.

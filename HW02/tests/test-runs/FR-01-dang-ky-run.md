# Lần thực thi — FR-01: Đăng ký tài khoản

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Người thực hiện / Thời điểm | Sinh viên; tên chưa được cung cấp / Ngày 2026-10-16, múi giờ +07:00; giờ cụ thể chưa được cung cấp |
| Môi trường | Web; trình duyệt và hệ điều hành chưa được cung cấp |
| URL / Phiên bản ứng dụng / Bản dựng | Chưa được cung cấp |
| Chuẩn bị và khôi phục dữ liệu | Cách chuẩn bị Email mới, Email đã tồn tại và khôi phục dữ liệu chưa được cung cấp |
| Nguồn kết quả | Bảng Actual Result do sinh viên cung cấp trong tương tác AI số 12; chưa có screenshot/video/log hệ thống |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-01-DT-001 | Đăng ký với dữ liệu hợp lệ | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Form có dấu * và đúng input type; đăng ký được chấp nhận và chuyển tới trang Đăng nhập. | Nhãn không có `*`; Email dùng `type=text`; thiếu trường Xác nhận mật khẩu; dữ liệu hợp lệ vẫn bị từ chối. | Fail | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending | Có nhiều sai khác; cần phân tích thành các defect riêng. |
| TC-FR-01-DT-002 | Họ Tên để trống | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-DT-003 | Email để trống | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-DT-004 | Email sai định dạng | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Email không hợp lệ; lỗi nằm phía trên nút submit. | Email sai định dạng không được HTML5 validation vì dùng `type=text`; hệ thống báo lỗi mật khẩu thay vì Email. | Fail | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending | Không có bằng chứng về vị trí lỗi; sai loại input và sai validation đã được quan sát. |
| TC-FR-01-DT-005 | Email đã tồn tại | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Email không duy nhất; không tạo tài khoản thứ hai. | Không kiểm tra được tính duy nhất của Email vì request bị chặn trước bởi validation mật khẩu không đúng. | Blocked | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending blocker | Chuẩn hóa từ Fail sang Blocked vì chưa đạt tới validation Email duy nhất. |
| TC-FR-01-DT-006 | Mật khẩu và Xác nhận để trống | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-DT-007 | Xác nhận mật khẩu để trống | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Không có trường Xác nhận mật khẩu để thực hiện test. | Blocked | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending blocker | Chuẩn hóa từ Fail sang Blocked; không thể nhập test data mục tiêu. |
| TC-FR-01-DT-008 | Xác nhận mật khẩu không khớp | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì hai mật khẩu không khớp; không chuyển tới trang Đăng nhập. | Không có trường Xác nhận mật khẩu để nhập giá trị không khớp. | Blocked | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending blocker | Chuẩn hóa từ Fail sang Blocked; không thể thực hiện quan hệ không khớp. |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-01-BVA-001 | Độ dài Mật khẩu OFF⁻ = 7 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Mật khẩu ngắn hơn 8 ký tự; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu 7 ký tự và không chuyển tới Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-BVA-002 | Độ dài Mật khẩu ON = 8 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Chấp nhận và chuyển tới trang Đăng nhập. | Mật khẩu hợp lệ `Abcdef1!` bị từ chối, không chuyển tới Đăng nhập. | Fail | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending | Sai tại cận dưới hợp lệ. |
| TC-FR-01-BVA-003 | Độ dài Mật khẩu OFF⁺ = 9 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Chấp nhận và chuyển tới trang Đăng nhập. | Mật khẩu hợp lệ `ABCDEF1!a` bị từ chối, không chuyển tới Đăng nhập. | Fail | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | Pending | Sai ngay phía trên cận dưới. |
| TC-FR-01-BVA-004 | Số chữ hoa OFF⁻ = 0 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Mật khẩu thiếu chữ hoa; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ hoa và không chuyển tới Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-BVA-005 | Số chữ thường OFF⁻ = 0 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Mật khẩu thiếu chữ thường; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ thường và không chuyển tới Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-BVA-006 | Số chữ số OFF⁻ = 0 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Mật khẩu thiếu chữ số; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ số và không chuyển tới Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |
| TC-FR-01-BVA-007 | Số ký tự đặc biệt OFF⁻ = 0 | Sinh viên; tên chưa được cung cấp | 2026-10-16 +07:00 / Lần 1; giờ cụ thể chưa được cung cấp | Từ chối vì Mật khẩu thiếu ký tự đặc biệt cho phép; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu ký tự đặc biệt cho phép và không chuyển tới Đăng nhập, đúng expected. | Pass | Kết quả bằng văn bản do sinh viên cung cấp; chưa có ảnh/video | None | Không có. |

## Đối chiếu và chuẩn hóa trạng thái

- Giữ `Pass` cho 8 ca có Actual Result được người thực hiện xác nhận khớp Expected Result.
- Giữ `Fail` cho 4 ca đã đạt tới hành vi mục tiêu nhưng Actual Result khác Expected Result: TC-FR-01-DT-001, TC-FR-01-DT-004, TC-FR-01-BVA-002 và TC-FR-01-BVA-003.
- Chuẩn hóa TC-FR-01-DT-005, TC-FR-01-DT-007 và TC-FR-01-DT-008 từ `Fail` sang `Blocked`: mục tiêu tính duy nhất hoặc quan hệ Xác nhận mật khẩu chưa thể thực hiện/quan sát vì blocker xảy ra trước.
- `Pending` và `Pending blocker` chỉ là trạng thái liên kết; chưa tạo bug report và chưa xác định số defect riêng biệt.

## Tổng kết

| Metric | Count |
|---|---:|
| Ca thiết kế | 15 |
| Đã chạy hoàn tất | 12 |
| Đạt | 8 |
| Không đạt | 4 |
| Bị chặn | 3 |
| Chưa chạy | 0 |
| Chưa thực thi hoàn tất | 3 |
| Bug riêng biệt | 0 |

Đếm theo kết quả gần nhất của từng test case. `Bug riêng biệt = 0` vì chưa có bug analysis/report; nhiều ca Fail và Blocked có thể cùng một nguyên nhân nên không đếm trực tiếp từ số ca.

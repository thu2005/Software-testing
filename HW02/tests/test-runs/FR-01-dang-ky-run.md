# Lần thực thi — FR-01: Đăng ký tài khoản

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Người thực hiện / Thời điểm | Thu / 2026-10-16 20:30:00 +07:00 |
| Môi trường | Web; Google Chrome `155.0.8059.40`; Microsoft Windows NT `10.0.26100.0` |
| URL / Phiên bản ứng dụng / Bản dựng | Frontend `http://127.0.0.1:5174/register`; Backend API `http://localhost:3000`. |
| Chuẩn bị và khôi phục dữ liệu | Email mới: dùng địa chỉ riêng theo từng test case; Email đã tồn tại: `existing.fr01@example.com`. Cách khôi phục/reset database giữa các lần chạy chưa được ghi nhận. |
| Nguồn kết quả | Bảng Actual Result do Thu cung cấp trong tương tác AI số 12 và 15 screenshot cục bộ |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-01-DT-001 | Đăng ký với dữ liệu hợp lệ | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Form có dấu * và đúng input type; đăng ký được chấp nhận và chuyển tới trang Đăng nhập. | Nhãn không có `*`; Email dùng `type=text`; thiếu trường Xác nhận mật khẩu; dữ liệu hợp lệ vẫn bị từ chối. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-DT-001-actual-result.png) | [BUG-FR01-001](../../bug-reports/BUG-FR01-001.md) ([#1](https://github.com/thu2005/CSC13003_eshop/issues/1)), [BUG-FR01-002](../../bug-reports/BUG-FR01-002.md) ([#2](https://github.com/thu2005/CSC13003_eshop/issues/2)), [BUG-FR01-003](../../bug-reports/BUG-FR01-003.md) ([#3](https://github.com/thu2005/CSC13003_eshop/issues/3)), [BUG-FR01-004](../../bug-reports/BUG-FR01-004.md) ([#4](https://github.com/thu2005/CSC13003_eshop/issues/4)) | Một ca quan sát được bốn defect độc lập. |
| TC-FR-01-DT-002 | Họ Tên để trống | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-DT-002-pass.png) | None | Không có. |
| TC-FR-01-DT-003 | Email để trống | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-DT-003-pass.png) | None | Không có. |
| TC-FR-01-DT-004 | Email sai định dạng | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Email không hợp lệ; lỗi nằm phía trên nút submit. | Email sai định dạng không được HTML5 validation vì dùng `type=text`; hệ thống báo lỗi mật khẩu thay vì Email. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-DT-004-actual-result.png) | [BUG-FR01-004](../../bug-reports/BUG-FR01-004.md) ([#4](https://github.com/thu2005/CSC13003_eshop/issues/4)) | Ảnh cho thấy lỗi nằm trên nút submit; phần sai là loại input/validation Email. |
| TC-FR-01-DT-005 | Email đã tồn tại | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Email không duy nhất; không tạo tài khoản thứ hai. | Không kiểm tra được tính duy nhất của Email vì request bị chặn trước bởi validation mật khẩu không đúng. | Blocked | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-DT-005-actual-result.png) | [BUG-FR01-001](../../bug-reports/BUG-FR01-001.md) ([#1](https://github.com/thu2005/CSC13003_eshop/issues/1)) | Chưa đạt tới validation Email duy nhất do bug mật khẩu. |
| TC-FR-01-DT-006 | Mật khẩu và Xác nhận để trống | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Theo người thực hiện, hệ thống từ chối đăng ký và không chuyển tới trang Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-DT-006-pass.png) | None | Không có. |
| TC-FR-01-DT-007 | Xác nhận mật khẩu để trống | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. | Không có trường Xác nhận mật khẩu để thực hiện test. | Blocked | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-DT-007-actual-result.png) | [BUG-FR01-002](../../bug-reports/BUG-FR01-002.md) ([#2](https://github.com/thu2005/CSC13003_eshop/issues/2)) | Không thể nhập test data vì thiếu trường Xác nhận mật khẩu. |
| TC-FR-01-DT-008 | Xác nhận mật khẩu không khớp | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì hai mật khẩu không khớp; không chuyển tới trang Đăng nhập. | Không có trường Xác nhận mật khẩu để nhập giá trị không khớp. | Blocked | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-DT-008-actual-result.png) | [BUG-FR01-002](../../bug-reports/BUG-FR01-002.md) ([#2](https://github.com/thu2005/CSC13003_eshop/issues/2)) | Không thể thực hiện quan hệ không khớp vì thiếu trường. |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-01-BVA-001 | Độ dài Mật khẩu OFF⁻ = 7 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Mật khẩu ngắn hơn 8 ký tự; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu 7 ký tự và không chuyển tới Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-BVA-001-pass.png) | None | Không có. |
| TC-FR-01-BVA-002 | Độ dài Mật khẩu ON = 8 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Chấp nhận và chuyển tới trang Đăng nhập. | Mật khẩu hợp lệ `Abcdef1!` bị từ chối, không chuyển tới Đăng nhập. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-BVA-002-actual-result.png) | [BUG-FR01-001](../../bug-reports/BUG-FR01-001.md) ([#1](https://github.com/thu2005/CSC13003_eshop/issues/1)) | Sai tại cận dưới hợp lệ. |
| TC-FR-01-BVA-003 | Độ dài Mật khẩu OFF⁺ = 9 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Chấp nhận và chuyển tới trang Đăng nhập. | Mật khẩu hợp lệ `ABCDEF1!a` bị từ chối, không chuyển tới Đăng nhập. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-01-BVA-003-actual-result.png) | [BUG-FR01-001](../../bug-reports/BUG-FR01-001.md) ([#1](https://github.com/thu2005/CSC13003_eshop/issues/1)) | Sai ngay phía trên cận dưới. |
| TC-FR-01-BVA-004 | Số chữ hoa OFF⁻ = 0 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Mật khẩu thiếu chữ hoa; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ hoa và không chuyển tới Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-BVA-004-pass.png) | None | Không có. |
| TC-FR-01-BVA-005 | Số chữ thường OFF⁻ = 0 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Mật khẩu thiếu chữ thường; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ thường và không chuyển tới Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-BVA-005-pass.png) | None | Không có. |
| TC-FR-01-BVA-006 | Số chữ số OFF⁻ = 0 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Mật khẩu thiếu chữ số; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu chữ số và không chuyển tới Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-BVA-006-pass.png) | None | Không có. |
| TC-FR-01-BVA-007 | Số ký tự đặc biệt OFF⁻ = 0 | Thu | 2026-10-16 20:30:00 +07:00 / Lần 1 | Từ chối vì Mật khẩu thiếu ký tự đặc biệt cho phép; không chuyển tới trang Đăng nhập. | Hệ thống từ chối Mật khẩu thiếu ký tự đặc biệt cho phép và không chuyển tới Đăng nhập, đúng expected. | Pass | [Ảnh Pass](screenshots/TC-FR-01-BVA-007-pass.png) | None | Không có. |

## Đối chiếu và chuẩn hóa trạng thái

- Giữ `Pass` cho 8 ca có Actual Result được người thực hiện xác nhận khớp Expected Result.
- Giữ `Fail` cho 4 ca đã đạt tới hành vi mục tiêu nhưng Actual Result khác Expected Result: TC-FR-01-DT-001, TC-FR-01-DT-004, TC-FR-01-BVA-002 và TC-FR-01-BVA-003.
- Chuẩn hóa TC-FR-01-DT-005, TC-FR-01-DT-007 và TC-FR-01-DT-008 từ `Fail` sang `Blocked`: mục tiêu tính duy nhất hoặc quan hệ Xác nhận mật khẩu chưa thể thực hiện/quan sát vì blocker xảy ra trước.
- Các ca Fail và Blocked đã được liên kết tới bốn bug report riêng biệt sau khi kiểm tra duplicate và evidence.

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
| Bug riêng biệt | 4 |

Đếm theo kết quả gần nhất của từng test case. Bốn bug được đếm theo hành vi khác nhau, không đếm trực tiếp từ số ca Fail/Blocked.

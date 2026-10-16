# Phân tích giá trị biên — FR-01: Đăng ký tài khoản

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Nguồn đặc tả / Phân tích miền | [system-requirements.md](../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](domain-testing-analysis.md) |
| Điều kiện tiên quyết | Trang đăng ký hoạt động; mỗi Email dùng cho ca hợp lệ chưa tồn tại |
| Điều kiện thành công / lỗi | Dữ liệu hợp lệ: tạo tài khoản và chuyển tới Đăng nhập; vi phạm ngưỡng: từ chối đăng ký |

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| Độ dài Họ Tên | Input | Số ký tự | Bắt buộc | 1 | Chưa được đặc tả | Cận dưới đóng | 1 ký tự | Nguyễn Văn An | FR-01 |
| Độ dài Mật khẩu | Input | Số ký tự | ≥8 | 8 | Chưa được đặc tả | Cận dưới đóng | 1 ký tự | Abcdef1!xy (10 ký tự) | FR-01 |
| Số chữ hoa | Input | Số lần xuất hiện | ≥1 | 1 | Phụ thuộc độ dài; không có cận riêng | Cận dưới đóng | 1 ký tự | 1 | FR-01 |
| Số chữ thường | Input | Số lần xuất hiện | ≥1 | 1 | Phụ thuộc độ dài; không có cận riêng | Cận dưới đóng | 1 ký tự | 7 | FR-01 |
| Số chữ số | Input | Số lần xuất hiện | ≥1 | 1 | Phụ thuộc độ dài; không có cận riêng | Cận dưới đóng | 1 ký tự | 1 | FR-01 |
| Số ký tự trong @ $ ! % * ? & | Input | Số lần xuất hiện | ≥1 | 1 | Phụ thuộc độ dài; không có cận riêng | Cận dưới đóng | 1 ký tự | 1 | FR-01 |

## 3. Phương pháp BVA được sử dụng

- Dùng Robust BVA quanh từng cận dưới: `OFF⁻`, `ON`, `OFF⁺`. Với độ dài và số lần xuất hiện, `δ=1`.
- Mỗi ca chỉ thay đổi biến mục tiêu; Mật khẩu luôn được xác nhận bằng cùng chuỗi để cô lập quan hệ khớp.
- Giới hạn nhập tối đa qua UI và cận trên không được đặc tả, vì vậy không tạo giá trị cận trên giả định.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| Độ dài Họ Tên | 0/1 ký tự | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Biên rỗng/không rỗng; δ=1 ký tự |
| Độ dài Mật khẩu | 8 ký tự | 7 | 8 | 9 | Không hợp lệ / Hợp lệ / Hợp lệ | Cận dưới đóng; δ=1 ký tự |
| Số chữ hoa | 1 ký tự | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Ngưỡng tối thiểu; δ=1 lần xuất hiện |
| Số chữ thường | 1 ký tự | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Ngưỡng tối thiểu; δ=1 lần xuất hiện |
| Số chữ số | 1 ký tự | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Ngưỡng tối thiểu; δ=1 lần xuất hiện |
| Số ký tự đặc biệt cho phép | 1 ký tự | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Tập @ $ ! % * ? &; δ=1 lần xuất hiện |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| BV-NAME-001 | Độ dài Họ Tên | Họ Tên bắt buộc; min length=1 | OFF⁻ | 1−1 | [để trống] (0 ký tự) | Không hợp lệ | Từ chối đăng ký vì Họ Tên bắt buộc. | FR-01 |
| BV-NAME-002 | Độ dài Họ Tên | Họ Tên bắt buộc; min length=1 | ON | 1 | A (1 ký tự) | Hợp lệ | Chấp nhận Họ Tên tại cận dưới; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-NAME-003 | Độ dài Họ Tên | Họ Tên bắt buộc; min length=1 | OFF⁺ | 1+1 | An (2 ký tự) | Hợp lệ | Chấp nhận Họ Tên trên cận dưới một đơn vị; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-PWLEN-001 | Độ dài Mật khẩu | Độ dài Mật khẩu ≥8 | OFF⁻ | 8−1 | Aa1!xyz (7 ký tự) | Không hợp lệ | Từ chối đăng ký vì Mật khẩu ngắn hơn 8 ký tự. | FR-01 |
| BV-PWLEN-002 | Độ dài Mật khẩu | Độ dài Mật khẩu ≥8 | ON | 8 | Aa1!xyzz (8 ký tự) | Hợp lệ | Chấp nhận Mật khẩu tại cận dưới; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-PWLEN-003 | Độ dài Mật khẩu | Độ dài Mật khẩu ≥8 | OFF⁺ | 8+1 | Aa1!xyzzz (9 ký tự) | Hợp lệ | Chấp nhận Mật khẩu trên cận dưới một đơn vị; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-UPPER-001 | Số chữ hoa | Số chữ hoa ≥1 | OFF⁻ | 1−1 | abc123!xyz (0 chữ hoa) | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ hoa. | FR-01 |
| BV-UPPER-002 | Số chữ hoa | Số chữ hoa ≥1 | ON | 1 | Abc123!xyz (1 chữ hoa) | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ hoa; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-UPPER-003 | Số chữ hoa | Số chữ hoa ≥1 | OFF⁺ | 1+1 | ABc123!xyz (2 chữ hoa) | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ hoa; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-LOWER-001 | Số chữ thường | Số chữ thường ≥1 | OFF⁻ | 1−1 | ABC123!XYZ (0 chữ thường) | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ thường. | FR-01 |
| BV-LOWER-002 | Số chữ thường | Số chữ thường ≥1 | ON | 1 | ABc123!XYZ (1 chữ thường) | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ thường; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-LOWER-003 | Số chữ thường | Số chữ thường ≥1 | OFF⁺ | 1+1 | ABcd23!XYZ (2 chữ thường) | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ thường; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-DIGIT-001 | Số chữ số | Số chữ số ≥1 | OFF⁻ | 1−1 | Abcdef!xyz (0 chữ số) | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ số. | FR-01 |
| BV-DIGIT-002 | Số chữ số | Số chữ số ≥1 | ON | 1 | Abcde1!xyz (1 chữ số) | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ số; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-DIGIT-003 | Số chữ số | Số chữ số ≥1 | OFF⁺ | 1+1 | Abcd12!xyz (2 chữ số) | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ số; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-SPECIAL-001 | Số ký tự đặc biệt cho phép | Số ký tự đặc biệt cho phép ≥1 | OFF⁻ | 1−1 | Abcdef1xyz (0 ký tự) | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu ký tự thuộc tập cho phép. | FR-01 |
| BV-SPECIAL-002 | Số ký tự đặc biệt cho phép | Số ký tự đặc biệt cho phép ≥1 | ON | 1 | Abcdef1!yz (1 ký tự) | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 ký tự đặc biệt cho phép; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |
| BV-SPECIAL-003 | Số ký tự đặc biệt cho phép | Số ký tự đặc biệt cho phép ≥1 | OFF⁺ | 1+1 | Abcdef1!@z (2 ký tự) | Hợp lệ | Chấp nhận Mật khẩu có 2 ký tự đặc biệt cho phép; đăng ký thành công và chuyển tới trang Đăng nhập. | FR-01 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Xác nhận mật khẩu phải khớp Mật khẩu trong mọi ca BVA mật khẩu | `(password, confirmPassword)=(p,p)` | Không phát sinh lỗi không khớp; kết quả phản ánh biên mục tiêu | Khả thi bằng cách sao chép nguyên chuỗi mục tiêu sang trường xác nhận |
| DB-02 | Các ngưỡng thành phần phụ thuộc tổng độ dài Mật khẩu | Tổng độ dài luôn 10 ở TC-007 đến TC-018 | Cô lập số lượng nhóm ký tự đang xét | Ký tự thay thế được chọn để các nhóm còn lại vẫn ≥1 |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-01-BVA-001 | Độ dài Họ Tên | BV-NAME-001 | OFF⁻ | Họ Tên=[để trống] (0 ký tự); Email=fr01.bva001@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Họ Tên bắt buộc. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-002 | Độ dài Họ Tên | BV-NAME-002 | ON | Họ Tên=A (1 ký tự); Email=fr01.bva002@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Họ Tên tại cận dưới; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-003 | Độ dài Họ Tên | BV-NAME-003 | OFF⁺ | Họ Tên=An (2 ký tự); Email=fr01.bva003@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Họ Tên trên cận dưới một đơn vị; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-004 | Độ dài Mật khẩu | BV-PWLEN-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva004@example.com; Mật khẩu=Aa1!xyz; Xác nhận=Aa1!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Mật khẩu ngắn hơn 8 ký tự. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-005 | Độ dài Mật khẩu | BV-PWLEN-002 | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva005@example.com; Mật khẩu=Aa1!xyzz; Xác nhận=Aa1!xyzz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu tại cận dưới; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-006 | Độ dài Mật khẩu | BV-PWLEN-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva006@example.com; Mật khẩu=Aa1!xyzzz; Xác nhận=Aa1!xyzzz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu trên cận dưới một đơn vị; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-007 | Số chữ hoa | BV-UPPER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva007@example.com; Mật khẩu=abc123!xyz; Xác nhận=abc123!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ hoa. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-008 | Số chữ hoa | BV-UPPER-002 | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva008@example.com; Mật khẩu=Abc123!xyz; Xác nhận=Abc123!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ hoa; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-009 | Số chữ hoa | BV-UPPER-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva009@example.com; Mật khẩu=ABc123!xyz; Xác nhận=ABc123!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ hoa; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-010 | Số chữ thường | BV-LOWER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva010@example.com; Mật khẩu=ABC123!XYZ; Xác nhận=ABC123!XYZ | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ thường. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-011 | Số chữ thường | BV-LOWER-002 | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva011@example.com; Mật khẩu=ABc123!XYZ; Xác nhận=ABc123!XYZ | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ thường; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-012 | Số chữ thường | BV-LOWER-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva012@example.com; Mật khẩu=ABcd23!XYZ; Xác nhận=ABcd23!XYZ | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ thường; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-013 | Số chữ số | BV-DIGIT-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva013@example.com; Mật khẩu=Abcdef!xyz; Xác nhận=Abcdef!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu chữ số. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-014 | Số chữ số | BV-DIGIT-002 | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva014@example.com; Mật khẩu=Abcde1!xyz; Xác nhận=Abcde1!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 chữ số; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-015 | Số chữ số | BV-DIGIT-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva015@example.com; Mật khẩu=Abcd12!xyz; Xác nhận=Abcd12!xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có 2 chữ số; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-016 | Số ký tự đặc biệt cho phép | BV-SPECIAL-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva016@example.com; Mật khẩu=Abcdef1xyz; Xác nhận=Abcdef1xyz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Không hợp lệ | Từ chối đăng ký vì Mật khẩu thiếu ký tự thuộc tập cho phép. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-017 | Số ký tự đặc biệt cho phép | BV-SPECIAL-002 | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva017@example.com; Mật khẩu=Abcdef1!yz; Xác nhận=Abcdef1!yz | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có đúng 1 ký tự đặc biệt cho phép; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |
| COND-FR-01-BVA-018 | Số ký tự đặc biệt cho phép | BV-SPECIAL-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva018@example.com; Mật khẩu=Abcdef1!@z; Xác nhận=Abcdef1!@z | Email mới; các field khác hợp lệ; Xác nhận mật khẩu khớp Mật khẩu | Hợp lệ | Chấp nhận Mật khẩu có 2 ký tự đặc biệt cho phép; đăng ký thành công và chuyển tới trang Đăng nhập. | Kiểm tra riêng một điểm quanh cận; giá trị khác ở mức danh nghĩa. |

## 8. Quá trình lựa chọn ca kiểm thử

Mỗi cận dưới dùng ba điểm liền kề. Chuỗi cho các ngưỡng thành phần đều dài 10 ký tự, nên không đồng thời vi phạm cận độ dài 8; mỗi chuỗi vẫn thỏa ba nhóm ký tự không phải mục tiêu. Các ca hợp lệ dùng Email mới riêng biệt. Không áp dụng BVA cho định dạng Email, tính duy nhất hoặc quan hệ khớp vì đây là miền phân loại/quan hệ không có thứ tự định lượng trong đặc tả. Không tạo cận trên cho bất kỳ trường nào.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-01-BVA-001 | COND-FR-01-BVA-001 | BV-NAME-001 | OFF⁻ | [để trống] (0 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-002 | COND-FR-01-BVA-002 | BV-NAME-002 | ON | A (1 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-003 | COND-FR-01-BVA-003 | BV-NAME-003 | OFF⁺ | An (2 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-004 | COND-FR-01-BVA-004 | BV-PWLEN-001 | OFF⁻ | Aa1!xyz (7 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-005 | COND-FR-01-BVA-005 | BV-PWLEN-002 | ON | Aa1!xyzz (8 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-006 | COND-FR-01-BVA-006 | BV-PWLEN-003 | OFF⁺ | Aa1!xyzzz (9 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-007 | COND-FR-01-BVA-007 | BV-UPPER-001 | OFF⁻ | abc123!xyz (0 chữ hoa) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-008 | COND-FR-01-BVA-008 | BV-UPPER-002 | ON | Abc123!xyz (1 chữ hoa) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-009 | COND-FR-01-BVA-009 | BV-UPPER-003 | OFF⁺ | ABc123!xyz (2 chữ hoa) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-010 | COND-FR-01-BVA-010 | BV-LOWER-001 | OFF⁻ | ABC123!XYZ (0 chữ thường) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-011 | COND-FR-01-BVA-011 | BV-LOWER-002 | ON | ABc123!XYZ (1 chữ thường) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-012 | COND-FR-01-BVA-012 | BV-LOWER-003 | OFF⁺ | ABcd23!XYZ (2 chữ thường) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-013 | COND-FR-01-BVA-013 | BV-DIGIT-001 | OFF⁻ | Abcdef!xyz (0 chữ số) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-014 | COND-FR-01-BVA-014 | BV-DIGIT-002 | ON | Abcde1!xyz (1 chữ số) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-015 | COND-FR-01-BVA-015 | BV-DIGIT-003 | OFF⁺ | Abcd12!xyz (2 chữ số) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-016 | COND-FR-01-BVA-016 | BV-SPECIAL-001 | OFF⁻ | Abcdef1xyz (0 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-017 | COND-FR-01-BVA-017 | BV-SPECIAL-002 | ON | Abcdef1!yz (1 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-018 | COND-FR-01-BVA-018 | BV-SPECIAL-003 | OFF⁺ | Abcdef1!@z (2 ký tự) | Hợp lệ | FR-01 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 6 / 6 / 0 |
| Số biên phụ thuộc / giá trị biên / ca kiểm thử | 2 / 18 / 18 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-NAME-001 đến BV-NAME-003 | TC-FR-01-BVA-001 đến TC-FR-01-BVA-003 | Đã bao phủ | Chưa chạy | Không có |
| BV-PWLEN-001 đến BV-PWLEN-003 | TC-FR-01-BVA-004 đến TC-FR-01-BVA-006 | Đã bao phủ | Chưa chạy | Không có |
| BV-UPPER-001 đến BV-UPPER-003 | TC-FR-01-BVA-007 đến TC-FR-01-BVA-009 | Đã bao phủ | Chưa chạy | Không có |
| BV-LOWER-001 đến BV-LOWER-003 | TC-FR-01-BVA-010 đến TC-FR-01-BVA-012 | Đã bao phủ | Chưa chạy | Không có |
| BV-DIGIT-001 đến BV-DIGIT-003 | TC-FR-01-BVA-013 đến TC-FR-01-BVA-015 | Đã bao phủ | Chưa chạy | Không có |
| BV-SPECIAL-001 đến BV-SPECIAL-003 | TC-FR-01-BVA-016 đến TC-FR-01-BVA-018 | Đã bao phủ | Chưa chạy | Không có |
| DB-01, DB-02 | TC-FR-01-BVA-004 đến TC-FR-01-BVA-018 | Đã bao phủ | Chưa chạy | Không có |
| Cận trên của Họ Tên, Email, Mật khẩu | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không được đặc tả |

## 11. Giả định và thông tin chưa được đặc tả

- Cách đếm ký tự Unicode, xử lý khoảng trắng và giới hạn nhập tối đa chưa được đặc tả; dữ liệu BVA dùng ASCII khi độ dài là oracle.
- Không có cận trên cho độ dài hoặc số lần xuất hiện từng nhóm ký tự.
- Email bắt buộc nhưng độ dài 1 hoặc 2 không thể đồng thời thỏa định dạng; biên rỗng/không rỗng của Email không được chọn vì không cô lập được khỏi rule định dạng.
- Các ca chỉ được thiết kế, chưa thực thi; trạng thái là `Not Run`.

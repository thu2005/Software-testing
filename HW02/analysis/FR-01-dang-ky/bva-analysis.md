# Phân tích giá trị biên — FR-01: Đăng ký tài khoản

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Nguồn đặc tả / Phân tích miền | [system-requirements.md](../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](domain-testing-analysis.md) |
| Điều kiện thành công / lỗi | Mật khẩu đạt mọi ngưỡng: cho phép đăng ký; vi phạm một ngưỡng: từ chối |

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| Độ dài Mật khẩu | Input | Số ký tự | ≥8 | 8 | Chưa được đặc tả | Cận dưới đóng | 1 ký tự | Aa1!#### | FR-01 |
| Số chữ hoa | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số chữ thường | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số chữ số | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số ký tự trong @ $ ! % * ? & | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |

## 3. Phương pháp BVA được sử dụng

- Giữ `OFF⁻/ON/OFF⁺` cho cận độ dài 8.
- Với bốn ngưỡng thành phần, chọn riêng `OFF⁻=0`; dùng chung `Aa1!####` làm `ON=1` cho cả bốn vì các điều kiện tương thích.
- Chủ động không sinh bốn ca `OFF⁺=2`: khi đã đạt tối thiểu 1, giá trị 2 vẫn thuộc cùng miền hợp lệ và lặp hành vi; đây là tối ưu hóa để giới hạn tổng bộ FR-01 ở 14 ca.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| Độ dài Mật khẩu | 8 | 7 | 8 | 9 | Không hợp lệ / Hợp lệ / Hợp lệ | Chọn đủ ba điểm |
| Số chữ hoa | 1 | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Chọn 0 và ON dùng chung; loại 2 |
| Số chữ thường | 1 | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Chọn 0 và ON dùng chung; loại 2 |
| Số chữ số | 1 | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Chọn 0 và ON dùng chung; loại 2 |
| Số ký tự đặc biệt cho phép | 1 | 0 | 1 | 2 | Không hợp lệ / Hợp lệ / Hợp lệ | Chọn 0 và ON dùng chung; loại 2 |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| BV-PWLEN-001 | Độ dài Mật khẩu | ≥8 | OFF⁻ | 8−1 | Aa1!### (7) | Không hợp lệ | Từ chối | FR-01 |
| BV-PWLEN-002 | Độ dài Mật khẩu | ≥8 | ON | 8 | Aa1!#### (8) | Hợp lệ | Chấp nhận | FR-01 |
| BV-PWLEN-003 | Độ dài Mật khẩu | ≥8 | OFF⁺ | 8+1 | Aa1!##### (9) | Hợp lệ | Chấp nhận | FR-01 |
| BV-UPPER-001 | Số chữ hoa | ≥1 | OFF⁻ | 1−1 | aa1!#### (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-LOWER-001 | Số chữ thường | ≥1 | OFF⁻ | 1−1 | AA1!#### (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-DIGIT-001 | Số chữ số | ≥1 | OFF⁻ | 1−1 | Aaa!#### (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-SPECIAL-001 | Số ký tự đặc biệt cho phép | ≥1 | OFF⁻ | 1−1 | Aa1##### (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-GROUP-ON | Bốn số lượng nhóm ký tự | Mỗi nhóm ≥1 | ON | 1 | Aa1!#### (mỗi nhóm đúng 1) | Hợp lệ | Chấp nhận | FR-01 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Xác nhận khớp Mật khẩu | `(p,p)` trong cả 7 ca | Không phát sinh lỗi không khớp | Sao chép đúng chuỗi mục tiêu |
| DB-02 | Tổng độ dài và bốn nhóm ký tự | Chuỗi dài 8 hoặc 9; chỉ nhóm mục tiêu về 0 | Kết quả phản ánh ngưỡng mục tiêu | Ký tự `#` không được tính vào tập đặc biệt bắt buộc; đặc tả không cấm ký tự bổ sung |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-01-BVA-001 | Độ dài Mật khẩu | BV-PWLEN-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva001@example.com; Mật khẩu=Aa1!###; Xác nhận=Aa1!### | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu ngắn hơn 8 ký tự. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-002 | Độ dài và số lượng từng nhóm ký tự | BV-PWLEN-002, BV-GROUP-ON | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva002@example.com; Mật khẩu=Aa1!####; Xác nhận=Aa1!#### | Email mới; các điều kiện khác hợp lệ | Hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-003 | Độ dài Mật khẩu | BV-PWLEN-003 | OFF⁺ | Họ Tên=Nguyễn Văn An; Email=fr01.bva003@example.com; Mật khẩu=Aa1!#####; Xác nhận=Aa1!##### | Email mới; các điều kiện khác hợp lệ | Hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-004 | Số chữ hoa | BV-UPPER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva004@example.com; Mật khẩu=aa1!####; Xác nhận=aa1!#### | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ hoa. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-005 | Số chữ thường | BV-LOWER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva005@example.com; Mật khẩu=AA1!####; Xác nhận=AA1!#### | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ thường. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-006 | Số chữ số | BV-DIGIT-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva006@example.com; Mật khẩu=Aaa!####; Xác nhận=Aaa!#### | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ số. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-007 | Số ký tự đặc biệt cho phép | BV-SPECIAL-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva007@example.com; Mật khẩu=Aa1#####; Xác nhận=Aa1##### | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu ký tự đặc biệt cho phép. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |

## 8. Quá trình lựa chọn ca kiểm thử

`Aa1!####` dài 8 và có đúng một phần tử của từng nhóm bắt buộc, nên một ca hợp lệ cover đồng thời năm điểm ON. Bốn ca OFF⁻ thay riêng từng nhóm về 0 trong khi các nhóm khác vẫn hợp lệ. Ba ca độ dài cover 7/8/9. Họ Tên bắt buộc đã được cover bằng DT; không tạo BVA riêng vì FR-01 không quy định độ dài tối thiểu bằng số ngoài điều kiện có giá trị. Email, tính duy nhất và quan hệ khớp là miền phân loại, không dùng BVA.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-01-BVA-001 | COND-FR-01-BVA-001 | BV-PWLEN-001 | OFF⁻ | Aa1!### (7 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-002 | COND-FR-01-BVA-002 | BV-PWLEN-002, BV-GROUP-ON | ON | Aa1!#### (8 ký tự; đúng 1 chữ hoa, 1 chữ thường, 1 số, 1 ký tự đặc biệt cho phép) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-003 | COND-FR-01-BVA-003 | BV-PWLEN-003 | OFF⁺ | Aa1!##### (9 ký tự) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-004 | COND-FR-01-BVA-004 | BV-UPPER-001 | OFF⁻ | aa1!#### (0 chữ hoa) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-005 | COND-FR-01-BVA-005 | BV-LOWER-001 | OFF⁻ | AA1!#### (0 chữ thường) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-006 | COND-FR-01-BVA-006 | BV-DIGIT-001 | OFF⁻ | Aaa!#### (0 chữ số) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-007 | COND-FR-01-BVA-007 | BV-SPECIAL-001 | OFF⁻ | Aa1##### (0 ký tự trong @ $ ! % * ? &) | Không hợp lệ | FR-01 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 5 / 5 / 0 |
| Số biên phụ thuộc / giá trị biên được chọn / ca kiểm thử | 2 / 8 / 7 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-PWLEN-001 đến BV-PWLEN-003 | TC-FR-01-BVA-001 đến 003 | Đã bao phủ | Chưa chạy | Không có |
| BV-GROUP-ON | TC-FR-01-BVA-002 | Đã bao phủ | Chưa chạy | Gộp bốn điểm ON |
| BV-UPPER-001, BV-LOWER-001, BV-DIGIT-001, BV-SPECIAL-001 | TC-FR-01-BVA-004 đến 007 | Đã bao phủ | Chưa chạy | Cô lập từng OFF⁻ |
| OFF⁺=2 của bốn nhóm | Chưa có | Chủ động loại trừ | Chưa chạy | Cùng miền/hành vi hợp lệ với ON; giảm ca lặp |
| Cận trên | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không được đặc tả |

## 11. Giả định và thông tin chưa được đặc tả

- Đặc tả yêu cầu có ít nhất một ký tự trong tập cho phép, nhưng không cấm ký tự khác; `#` chỉ là ký tự đệm và không được tính vào nhóm đặc biệt bắt buộc.
- Không có cận trên hoặc quy tắc đếm Unicode. Dữ liệu biên dùng ASCII.
- Bộ 7 ca BVA ưu tiên coverage theo ngưỡng, không phải exhaustive testing; `OFF⁺` bị loại có chủ đích và được ghi rõ.
- Các ca chưa được thực thi; trạng thái `Not Run`.

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
| Độ dài Mật khẩu | Input | Số ký tự | ≥8 | 8 | Chưa được đặc tả | Cận dưới đóng | 1 ký tự | Abcdef1! | FR-01 |
| Số chữ hoa | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số chữ thường | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số chữ số | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |
| Số ký tự trong @ $ ! % * ? & | Input | Số lần | ≥1 | 1 | Không có cận riêng | Cận dưới đóng | 1 | 1 | FR-01 |

## 3. Phương pháp BVA được sử dụng

- Giữ `OFF⁻/ON/OFF⁺` cho cận độ dài 8.
- Với bốn ngưỡng thành phần, chọn riêng `OFF⁻=0`; `Abcdef1!` cover ON của chữ hoa, chữ số và ký tự đặc biệt, còn `ABCDEF1!a` cover ON của chữ thường.
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
| BV-PWLEN-001 | Độ dài Mật khẩu | ≥8 | OFF⁻ | 8−1 | Aa1!xyz (7) | Không hợp lệ | Từ chối | FR-01 |
| BV-PWLEN-002 | Độ dài Mật khẩu | ≥8 | ON | 8 | Abcdef1! (8) | Hợp lệ | Chấp nhận | FR-01 |
| BV-PWLEN-003 | Độ dài Mật khẩu | ≥8 | OFF⁺ | 8+1 | ABCDEF1!a (9) | Hợp lệ | Chấp nhận | FR-01 |
| BV-UPPER-001 | Số chữ hoa | ≥1 | OFF⁻ | 1−1 | abcdef1! (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-LOWER-001 | Số chữ thường | ≥1 | OFF⁻ | 1−1 | ABCDEF1! (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-DIGIT-001 | Số chữ số | ≥1 | OFF⁻ | 1−1 | Abcdefg! (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-SPECIAL-001 | Số ký tự đặc biệt cho phép | ≥1 | OFF⁻ | 1−1 | Abcdef12 (0) | Không hợp lệ | Từ chối | FR-01 |
| BV-UPPER-ON, BV-DIGIT-ON, BV-SPECIAL-ON | Ba số lượng nhóm ký tự | Mỗi nhóm ≥1 | ON | 1 | Abcdef1! | Hợp lệ | Chấp nhận | FR-01 |
| BV-LOWER-ON | Số chữ thường | ≥1 | ON | 1 | ABCDEF1!a | Hợp lệ | Chấp nhận | FR-01 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Xác nhận khớp Mật khẩu | `(p,p)` trong cả 7 ca | Không phát sinh lỗi không khớp | Sao chép đúng chuỗi mục tiêu |
| DB-02 | Tổng độ dài và bốn nhóm ký tự | Chuỗi dài 8 hoặc 9; chỉ nhóm mục tiêu về 0 | Kết quả phản ánh ngưỡng mục tiêu | Chọn chuỗi chỉ gồm chữ, số và ký tự đặc biệt được nêu trong requirement |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-01-BVA-001 | Độ dài Mật khẩu | BV-PWLEN-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva001@example.com; Mật khẩu=Aa1!xyz; Xác nhận=Aa1!xyz | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu ngắn hơn 8 ký tự; không chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-002 | Độ dài Mật khẩu; số chữ hoa, chữ số và ký tự đặc biệt | BV-PWLEN-002, BV-UPPER-ON, BV-DIGIT-ON, BV-SPECIAL-ON | ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva002@example.com; Mật khẩu=Abcdef1!; Xác nhận=Abcdef1! | Email mới; các điều kiện khác hợp lệ | Hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-003 | Độ dài Mật khẩu và số chữ thường | BV-PWLEN-003, BV-LOWER-ON | OFF⁺ / ON | Họ Tên=Nguyễn Văn An; Email=fr01.bva003@example.com; Mật khẩu=ABCDEF1!a; Xác nhận=ABCDEF1!a | Email mới; các điều kiện khác hợp lệ | Hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-004 | Số chữ hoa | BV-UPPER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva004@example.com; Mật khẩu=abcdef1!; Xác nhận=abcdef1! | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ hoa; không chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-005 | Số chữ thường | BV-LOWER-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva005@example.com; Mật khẩu=ABCDEF1!; Xác nhận=ABCDEF1! | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ thường; không chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-006 | Số chữ số | BV-DIGIT-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva006@example.com; Mật khẩu=Abcdefg!; Xác nhận=Abcdefg! | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu chữ số; không chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |
| COND-FR-01-BVA-007 | Số ký tự đặc biệt cho phép | BV-SPECIAL-001 | OFF⁻ | Họ Tên=Nguyễn Văn An; Email=fr01.bva007@example.com; Mật khẩu=Abcdef12; Xác nhận=Abcdef12 | Email mới; các điều kiện khác hợp lệ | Không hợp lệ | Từ chối vì Mật khẩu thiếu ký tự đặc biệt cho phép; không chuyển tới trang Đăng nhập. | Điểm cận đại diện; ca ON gộp các ngưỡng tương thích. |

## 8. Quá trình lựa chọn ca kiểm thử

Hai ca hợp lệ cover các điểm ON của bốn nhóm thành phần mà chỉ dùng những loại ký tự được nêu rõ trong requirement. Bốn ca OFF⁻ thay riêng từng nhóm về 0 trong khi các nhóm khác vẫn hợp lệ. Ba ca độ dài cover 7/8/9. Họ Tên bắt buộc đã được cover bằng DT; không tạo BVA riêng vì FR-01 không quy định độ dài tối thiểu bằng số ngoài điều kiện có giá trị. Email, tính duy nhất và quan hệ khớp là miền phân loại, không dùng BVA.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-01-BVA-001 | COND-FR-01-BVA-001 | BV-PWLEN-001 | OFF⁻ | Aa1!xyz (7 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-002 | COND-FR-01-BVA-002 | BV-PWLEN-002, BV-UPPER-ON, BV-DIGIT-ON, BV-SPECIAL-ON | ON | Abcdef1! (8 ký tự; đúng 1 chữ hoa, 1 số, 1 ký tự đặc biệt cho phép) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-003 | COND-FR-01-BVA-003 | BV-PWLEN-003, BV-LOWER-ON | OFF⁺ / ON | ABCDEF1!a (9 ký tự; đúng 1 chữ thường) | Hợp lệ | FR-01 |
| TC-FR-01-BVA-004 | COND-FR-01-BVA-004 | BV-UPPER-001 | OFF⁻ | abcdef1! (0 chữ hoa; 8 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-005 | COND-FR-01-BVA-005 | BV-LOWER-001 | OFF⁻ | ABCDEF1! (0 chữ thường; 8 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-006 | COND-FR-01-BVA-006 | BV-DIGIT-001 | OFF⁻ | Abcdefg! (0 chữ số; 8 ký tự) | Không hợp lệ | FR-01 |
| TC-FR-01-BVA-007 | COND-FR-01-BVA-007 | BV-SPECIAL-001 | OFF⁻ | Abcdef12 (0 ký tự trong @ $ ! % * ? &; 8 ký tự) | Không hợp lệ | FR-01 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 5 / 5 / 0 |
| Số biên phụ thuộc / giá trị biên được chọn / ca kiểm thử | 2 / 9 / 7 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-PWLEN-001 đến BV-PWLEN-003 | TC-FR-01-BVA-001 đến 003 | Đã bao phủ | 1 Pass, 2 Fail | Hai giá trị hợp lệ 8 và 9 ký tự bị từ chối |
| BV-UPPER-ON, BV-DIGIT-ON, BV-SPECIAL-ON, BV-LOWER-ON | TC-FR-01-BVA-002, TC-FR-01-BVA-003 | Đã bao phủ | 2 Fail | Các điểm ON hợp lệ bị từ chối |
| BV-UPPER-001, BV-LOWER-001, BV-DIGIT-001, BV-SPECIAL-001 | TC-FR-01-BVA-004 đến 007 | Đã bao phủ | 4 Pass | Cô lập từng OFF⁻ |
| OFF⁺=2 của bốn nhóm | Chưa có | Chủ động loại trừ | Không áp dụng | Cùng miền/hành vi hợp lệ với ON; giảm ca lặp |
| Cận trên | Chưa có | Bị chặn do thiếu requirement | Không áp dụng | Không được đặc tả |

## 11. Giả định và thông tin chưa được đặc tả

- Không có cận trên hoặc quy tắc đếm Unicode. Dữ liệu biên dùng ASCII.
- Bộ 7 ca BVA ưu tiên coverage theo ngưỡng, không phải exhaustive testing; `OFF⁺` bị loại có chủ đích và được ghi rõ.
- Kết quả thực thi gần nhất được ghi tại `tests/test-runs/FR-01-dang-ky-run.md`.

# Phân tích giá trị biên — FR-14: Quản lý Danh mục

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Nguồn đặc tả / Phân tích miền | [system-requirements.md](../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [domain-testing-analysis.md](domain-testing-analysis.md) |
| Điều kiện tiên quyết | Admin đã đăng nhập; mở mục quản lý Danh mục |
| Điều kiện thành công / lỗi | Tên danh mục không rỗng được chấp nhận để thêm; tên rỗng bị từ chối và không tạo dữ liệu |

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| Độ dài tên danh mục `L` | Input | Số nguyên không âm | `L > 0` | `0` | Chưa được đặc tả | Cận dưới mở tại 0 | 1 ký tự | 2 ký tự (`AB`) | FR-14 |

Không có biên hợp lệ nào khác có thể suy ra. Số lượng danh mục, độ dài tối đa, bộ ký tự, khoảng trắng và duplicate không được đặc tả.

## 3. Phương pháp BVA được sử dụng

- Phương pháp và lý do: Robust BVA tại cận dưới mở `L = 0`; xét điểm nhỏ hơn, đúng cận, ngay phía trong miền và một đại diện bên trong.
- Điểm khả thi qua UI: `L = 0`, `L = 1`, `L = 2`. `L = -1` không phải độ dài chuỗi khả thi nên chỉ ghi trong phân tích.
- Giới hạn nhập qua UI: chưa xác định; không tạo cận trên giả định.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| Độ dài tên `L` | Cận dưới mở `0` | `-1` | `0` | `1` | Không khả thi / Không hợp lệ / Hợp lệ | Bước `δ = 1` ký tự; miền chuỗi có `L ≥ 0`, requirement yêu cầu `L > 0` |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| BV-NAME-000 | Độ dài tên `L` | `L > 0` | OFF⁻ | `0 - 1` | `L = -1` | Không khả thi | Không thể tạo chuỗi có độ dài âm | FR-14 |
| BV-NAME-001 | Độ dài tên `L` | `L > 0` | ON | `0` | `""` (`L = 0`) | Không hợp lệ | Từ chối và không tạo danh mục | FR-14 |
| BV-NAME-002 | Độ dài tên `L` | `L > 0` | OFF⁺ | `0 + 1` | `A` (`L = 1`) | Hợp lệ | Tạo danh mục tên `A` | FR-14 |
| BV-NAME-003 | Độ dài tên `L` | `L > 0` | Đại diện bên trong | `0 + 2` | `AB` (`L = 2`) | Hợp lệ | Tạo danh mục tên `AB` | FR-14 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Độ dài tên và kết quả thêm | `(0, từ chối)`; `(1 hoặc 2, tạo)` | Không tạo ở cận 0; tạo ngay phía trong miền | Giữ tài khoản Admin và trạng thái trang giống nhau, chỉ đổi tên |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-14-BVA-001 | Độ dài tên | BV-NAME-001 | ON | `""`, `L = 0` | Admin hợp lệ; form Danh mục | Không hợp lệ | Từ chối, hiển thị lỗi phía trên nút submit và không tạo danh mục | Kiểm tra đúng cận mở |
| COND-FR-14-BVA-002 | Độ dài tên | BV-NAME-002 | OFF⁺ | `A`, `L = 1` | Admin hợp lệ; chưa có tên `A` | Hợp lệ | Tạo danh mục tên `A` | Giá trị nhỏ nhất hợp lệ |
| COND-FR-14-BVA-003 | Độ dài tên | BV-NAME-003 | Đại diện bên trong | `AB`, `L = 2` | Admin hợp lệ; chưa có tên `AB` | Hợp lệ | Tạo danh mục tên `AB` | Đại diện ngay trong miền để so với cận |

## 8. Quá trình lựa chọn ca kiểm thử

Biên duy nhất có căn cứ là độ dài tên tại 0 vì FR-14 quy định tên bắt buộc, không được rỗng. Cận này là cận mở: `L = 0` không hợp lệ và `L = 1` là giá trị hợp lệ nhỏ nhất. `L = 2` được giữ làm đại diện bên trong; `L = -1` không khả thi. Ca `L = 0` trùng dữ liệu với DT-003 có chủ đích vì hai kỹ thuật phải thể hiện riêng lập luận lớp không hợp lệ và điểm biên. Không kiểm tra cận trên khi requirement và giới hạn UI không cung cấp.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-14-BVA-001 | COND-FR-14-BVA-001 | BV-NAME-001 | ON tại cận mở 0 | `""`, `L = 0` | Không hợp lệ | FR-14, FR-22 |
| TC-FR-14-BVA-002 | COND-FR-14-BVA-002 | BV-NAME-002 | OFF⁺ | `A`, `L = 1` | Hợp lệ | FR-14 |
| TC-FR-14-BVA-003 | COND-FR-14-BVA-003 | BV-NAME-003 | Đại diện bên trong | `AB`, `L = 2` | Hợp lệ | FR-14 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 1 / 1 / 0 |
| Số biên phụ thuộc / giá trị biên / ca kiểm thử | 1 / 4 / 3 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-NAME-000 | Chưa có | Chủ động loại trừ | Chưa chạy | Độ dài `-1` không khả thi |
| BV-NAME-001 | TC-FR-14-BVA-001 | Đã bao phủ | Chưa chạy | Không có |
| BV-NAME-002 | TC-FR-14-BVA-002 | Đã bao phủ | Chưa chạy | Không có |
| BV-NAME-003 | TC-FR-14-BVA-003 | Đã bao phủ | Chưa chạy | Đại diện bên trong |
| Cận trên độ dài; số lượng danh mục | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không tự đặt giới hạn |

## 11. Giả định và thông tin chưa được đặc tả

- Không có độ dài tối đa hoặc giới hạn nhập của UI.
- Không có quy tắc cho tên chỉ gồm khoảng trắng, trim, ký tự hợp lệ, duplicate hoặc phân biệt hoa thường.
- Không có cận số lượng danh mục và không có quy tắc khi xóa danh mục đang được tham chiếu.
- Test data `A` và `AB` phải chưa tồn tại trước từng ca; việc khôi phục dữ liệu do tester thực hiện và review.

# Phân tích giá trị biên — FR-06-MOBILE: Xem chi tiết sản phẩm

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile (mã tệp `FR-06-MOBILE`) |
| Nguồn đặc tả / Phân tích miền | [system-requirements.md](../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm); [domain-testing-analysis.md](domain-testing-analysis.md) |
| Điều kiện tiên quyết | Ứng dụng Mobile kết nối Backend; sản phẩm `SP-FR06-MOBILE` tồn tại; giỏ được đưa về trạng thái xác định trước mỗi ca |
| Điều kiện thành công / lỗi | Số lượng là số nguyên dương, tối thiểu 1; giá trị hợp lệ dùng được để thêm giỏ, giá trị dưới cận bị từ chối |

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| Số lượng `q` | Input | Số nguyên | `q ≥ 1` | `1` | Chưa được đặc tả | Cận dưới đóng | 1 sản phẩm | `5` | FR-06 |

Không có biên có căn cứ cho giá, số lượng tồn kho, kích thước ảnh hoặc độ dài dữ liệu hiển thị trong FR-06.

## 3. Phương pháp BVA được sử dụng

- Phương pháp và lý do: Robust BVA tại cận dưới đóng `q = 1`, dùng điểm ngay dưới cận `0`, đúng cận `1` và ngay trên cận `2`. Giá trị nominal `5` đã được dùng trong Domain Testing nên không tạo thêm ca BVA trùng mục đích.
- Giới hạn nhập qua UI: số lượng tối đa và giới hạn thực tế của control chưa được đặc tả; không tạo cận trên hoặc giá trị cực đại giả định.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| Số lượng `q` | Cận dưới đóng `1` | `0` | `1` | `2` | Không hợp lệ / Hợp lệ / Hợp lệ | `δ = 1` sản phẩm; miền là số nguyên |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| BV-QTY-001 | Số lượng `q` | `q ≥ 1` | OFF⁻ | `1 - 1` | `0` | Không hợp lệ | Không dùng `0` làm số lượng hiệu lực; control từ chối hoặc chuẩn hóa về giá trị hợp lệ trước thao tác | FR-06 |
| BV-QTY-002 | Số lượng `q` | `q ≥ 1` | ON | `1` | `1` | Hợp lệ | Chấp nhận và thêm 1 sản phẩm | FR-06 |
| BV-QTY-003 | Số lượng `q` | `q ≥ 1` | OFF⁺ | `1 + 1` | `2` | Hợp lệ | Chấp nhận và thêm 2 sản phẩm | FR-06 |
| BV-QTY-004 | Số lượng `q` | `q ≥ 1` | Đại diện bên trong | `1 + 4` | `5` | Hợp lệ | Chấp nhận và thêm 5 sản phẩm | FR-06 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Số lượng và kết quả thêm giỏ | `(0, từ chối)`; `(1, thêm 1)`; `(2, thêm 2)` | Chỉ số nguyên tại hoặc trên cận 1 được dùng để thêm | Giữ cùng fixture; đưa giỏ về trạng thái không có fixture trước mỗi ca |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-06-MOBILE-BVA-001 | Số lượng `q` | BV-QTY-001 | OFF⁻ | `0` | Fixture hợp lệ; giỏ chưa có fixture | Không hợp lệ | Không dùng `0` làm số lượng hiệu lực; control từ chối thao tác hoặc chuẩn hóa về số nguyên dương trước khi thêm. | Kiểm tra ngay dưới cận. |
| COND-FR-06-MOBILE-BVA-002 | Số lượng `q` | BV-QTY-002 | ON | `1` | Fixture hợp lệ; giỏ chưa có fixture | Hợp lệ | Thêm fixture với số lượng `1` và có toast hoặc badge cập nhật. | Kiểm tra đúng cận nhỏ nhất hợp lệ. |
| COND-FR-06-MOBILE-BVA-003 | Số lượng `q` | BV-QTY-003 | OFF⁺ | `2` | Fixture hợp lệ; giỏ chưa có fixture | Hợp lệ | Thêm fixture với số lượng `2` và có toast hoặc badge cập nhật. | Kiểm tra ngay phía trong miền. |

## 8. Quá trình lựa chọn ca kiểm thử

Ba ca chỉ thay đổi số lượng `0/1/2`, còn sản phẩm và trạng thái giỏ được giữ giống nhau. Giá trị `5` là đại diện bên trong đã có ở DT-008 nên được ghi trong phân tích nhưng chủ động không tạo thêm ca BVA. Không kiểm tra cận trên khi requirement và giới hạn UI không cung cấp.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-06-MOBILE-BVA-001 | COND-FR-06-MOBILE-BVA-001 | BV-QTY-001 | OFF⁻ dưới cận 1 | `0` | Không hợp lệ | FR-06 |
| TC-FR-06-MOBILE-BVA-002 | COND-FR-06-MOBILE-BVA-002 | BV-QTY-002 | ON tại cận 1 | `1` | Hợp lệ | FR-06, FR-24 |
| TC-FR-06-MOBILE-BVA-003 | COND-FR-06-MOBILE-BVA-003 | BV-QTY-003 | OFF⁺ trên cận 1 | `2` | Hợp lệ | FR-06, FR-24 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 1 / 1 / 0 |
| Số biên phụ thuộc / giá trị biên / ca kiểm thử | 1 / 4 / 3 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-QTY-001 | TC-FR-06-MOBILE-BVA-001 | Đã bao phủ | Fail | Không có |
| BV-QTY-002 | TC-FR-06-MOBILE-BVA-002 | Đã bao phủ | Fail | Không có |
| BV-QTY-003 | TC-FR-06-MOBILE-BVA-003 | Đã bao phủ | Fail | Không có |
| BV-QTY-004 | TC-FR-06-MOBILE-DT-008 | Chủ động loại trừ khỏi BVA | Fail | Giá trị nominal đã được Domain Testing bao phủ |
| Cận trên số lượng / tồn kho | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không tự đặt giới hạn |

## 11. Giả định và thông tin chưa được đặc tả

- Không có số lượng tối đa, quy tắc tồn kho, giới hạn control hoặc hành vi khi vượt khả năng lưu trữ.
- Cách UI xử lý `0` và nội dung lỗi chưa được quy định; oracle chấp nhận việc từ chối hoặc chuẩn hóa về một số nguyên dương trước thao tác, nhưng không chấp nhận dùng `0` làm số lượng hiệu lực.
- Fixture và trạng thái giỏ phải được tester chuẩn bị độc lập; việc khôi phục dữ liệu do tester thực hiện và review.

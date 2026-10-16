# Phân tích giá trị biên — FR-07: Giỏ hàng

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Nguồn đặc tả / Phân tích miền | [system-requirements.md](../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](domain-testing-analysis.md) |
| Điều kiện tiên quyết | Có thể chuẩn bị giỏ với 0, 1 hoặc 2 dòng sản phẩm phân biệt |
| Điều kiện thành công / lỗi | 0 dòng hiển thị empty state; giỏ có dữ liệu hiển thị danh sách và nhãn `Tổng cộng` |

Quy ước dữ liệu kiểm thử: `SP-A` là fixture có ID `FR07-A`, tên `Áo kiểm thử FR07`; `SP-B` là fixture có ID `FR07-B`, tên `Túi kiểm thử FR07`.

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| Số dòng sản phẩm phân biệt trong giỏ | Trạng thái đầu vào | Số nguyên | ≥ 0; FR-07 mô tả riêng trạng thái rỗng | 0 | Chưa được đặc tả | Cận dưới đóng | 1 dòng | 2 dòng | FR-07 |

`Số lượng` không được đưa vào BVA vì FR-07 không quy định cận dưới, cận trên, bước thay đổi chính xác hoặc hành vi ở cận. Nút +/- được kiểm tra như hai lớp thao tác trong Domain Testing.

## 3. Phương pháp BVA được sử dụng

- Phương pháp và lý do: kiểm tra cận dưới đóng `0`, điểm ngay phía trong miền `1`, và đại diện bên trong `2` cho số dòng sản phẩm.
- Giới hạn nhập qua UI: trạng thái `-1 dòng` không thể tạo; cận trên số dòng chưa được đặc tả.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| Số dòng sản phẩm | 0 | -1, không khả thi | 0 | 1 | -1: không khả thi; 0 và 1: hợp lệ | Bước 1 dòng; 2 là đại diện bên trong |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| BV-ROWS-000 | Số dòng sản phẩm | ≥0 | OFF⁻ | 0−1 | -1 dòng | Không khả thi | Không thể chuẩn bị trạng thái giỏ có số dòng âm | FR-07 |
| BV-ROWS-001 | Số dòng sản phẩm | ≥0 | ON | 0 | 0 dòng | Hợp lệ | Hiển thị hình minh họa và thông báo empty state | FR-07 |
| BV-ROWS-002 | Số dòng sản phẩm | ≥0 | OFF⁺ | 0+1 | 1 dòng SP-A | Hợp lệ | Hiển thị một dòng với các cột bắt buộc và nhãn `Tổng cộng` | FR-07 |
| BV-ROWS-003 | Số dòng sản phẩm | ≥0 | Đại diện bên trong | 0+2 | 2 dòng SP-A, SP-B | Hợp lệ | Hiển thị hai dòng với các cột bắt buộc và nhãn `Tổng cộng` | FR-07 |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| DB-01 | Số dòng quyết định empty state hay danh sách | `(0, empty state)`; `(1 hoặc 2, danh sách)` | UI tương ứng với trạng thái giỏ | Chuẩn bị từng trạng thái độc lập; không thay đổi số lượng trong mỗi dòng |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| COND-FR-07-BVA-001 | Số dòng sản phẩm | BV-ROWS-001 | ON | 0 dòng | Giỏ đã được làm rỗng | Hợp lệ | Hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống. | Cận dưới đóng và trạng thái empty state được đặc tả riêng |
| COND-FR-07-BVA-002 | Số dòng sản phẩm | BV-ROWS-002 | OFF⁺ | 1 dòng SP-A, số lượng 1 | SP-A là sản phẩm phân biệt duy nhất | Hợp lệ | Hiển thị đúng một dòng SP-A với các cột bắt buộc và nhãn `Tổng cộng`. | Điểm ngay phía trong miền không rỗng |
| COND-FR-07-BVA-003 | Số dòng sản phẩm | BV-ROWS-003 | Đại diện bên trong | 2 dòng SP-A và SP-B, mỗi sản phẩm số lượng 1 | Hai sản phẩm phân biệt | Hợp lệ | Hiển thị đúng hai dòng sản phẩm; mỗi dòng có các cột bắt buộc và khu vực tổng tiền mang nhãn `Tổng cộng`. | Đại diện bên trong miền không rỗng |

## 8. Quá trình lựa chọn ca kiểm thử

Biên duy nhất có căn cứ là số dòng bằng `0`, do FR-07 quy định riêng giỏ hàng trống. Giá trị `1` kiểm tra chuyển tiếp sang giỏ không rỗng và `2` là đại diện bên trong. `-1` không phải trạng thái có thể chuẩn bị qua hệ thống nên chỉ ghi trong phân tích, không sinh test case. Các ca BVA 0 và 1 trùng trạng thái với DT-008 và DT-001 có chủ đích vì chúng chứng minh riêng biên của collection; không gộp hai kỹ thuật vào một file.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| TC-FR-07-BVA-001 | COND-FR-07-BVA-001 | BV-ROWS-001 | ON | 0 dòng | Hợp lệ | FR-07 |
| TC-FR-07-BVA-002 | COND-FR-07-BVA-002 | BV-ROWS-002 | OFF⁺ | 1 dòng | Hợp lệ | FR-07 |
| TC-FR-07-BVA-003 | COND-FR-07-BVA-003 | BV-ROWS-003 | Đại diện bên trong | 2 dòng | Hợp lệ | FR-07 |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | 1 / 1 / 0 |
| Số biên phụ thuộc / giá trị biên / ca kiểm thử | 1 / 4 / 3 |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| BV-ROWS-000 | Chưa có | Chủ động loại trừ | Chưa chạy | -1 dòng không phải trạng thái khả thi |
| BV-ROWS-001 | TC-FR-07-BVA-001 | Đã bao phủ | Chưa chạy | Không có |
| BV-ROWS-002 | TC-FR-07-BVA-002 | Đã bao phủ | Chưa chạy | Không có |
| BV-ROWS-003 | TC-FR-07-BVA-003 | Đã bao phủ | Chưa chạy | Đại diện bên trong |
| Cận trên số dòng; biên Số lượng | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không tự đặt giới hạn hoặc hành vi |

## 11. Giả định và thông tin chưa được đặc tả

- Không có cận trên số dòng sản phẩm hoặc số lượng của một sản phẩm.
- Không có cận dưới `Số lượng`; không suy ra `1` chỉ từ việc giao diện có nút +/-.
- Không có giới hạn UI cho số dòng; không tạo thêm điểm cực đại thực tế.
- Các ca chưa được thực thi; trạng thái ban đầu là `Not Run / None`.

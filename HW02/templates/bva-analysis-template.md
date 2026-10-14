# Phân tích giá trị biên — <FEATURE-ID>: <Tên chức năng>

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | <FR-ID> / <Nền tảng> |
| Nguồn đặc tả / Phân tích miền | <Tệp và mục liên quan> |
| Điều kiện tiên quyết | <Trạng thái và dữ liệu cần có> |
| Điều kiện thành công / lỗi | <Hành vi theo đặc tả> |

## 2. Các biến có biên

| Variable / Expression | Input / Output | Type | Constraint | Lower Boundary | Upper Boundary | Inclusive / Exclusive | Unit / Step | Nominal Value | Requirement Reference |
|---|---|---|---|---|---|---|---|---|---|
| <Biến/biểu thức> | <Đầu vào/đầu ra> | <Kiểu> | <Điều kiện> | <Cận hoặc chưa đặc tả> | <Cận hoặc chưa đặc tả> | <Đóng/mở> | <Đơn vị và bước dữ liệu> | <Giá trị hợp lệ> | <Nguồn> |

## 3. Phương pháp BVA được sử dụng

- Phương pháp và lý do: <Cách kiểm tra cận, điểm lân cận và đại diện bên trong>.
- Giới hạn nhập qua UI: <Giới hạn thực tế đã biết hoặc chưa xác định>.

## 4. Xác định ON, OFF- và OFF+

| Variable / Expression | Boundary | OFF- | ON | OFF+ | Validity at Each Point | Notes |
|---|---|---|---|---|---|---|
| <Biến/biểu thức> | <Ngưỡng cụ thể> | <b - δ> | <b> | <b + δ> | <Đánh giá theo dấu bất đẳng thức> | <Đơn vị và căn cứ chọn δ> |

## 5. Suy ra giá trị biên

| Boundary Value ID | Variable / Expression | Constraint | Point | Formula | Test Value | Validity | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|---|---|
| <BV-ID> | <Biến/biểu thức> | <Quy tắc> | <LB/UB/ON/OFF-/OFF+/Đại diện/Giới hạn UI> | <Công thức> | <Dữ liệu cụ thể> | <Hợp lệ/Không hợp lệ> | <Hành vi theo đặc tả> | <Nguồn> |

## 6. Biên phụ thuộc

| Dependency ID | Relationship | Boundary Values / Input Tuple | Expected Behavior | Isolation / Feasibility |
|---|---|---|---|---|
| <DB-ID> | <Quan hệ> | <Bộ giá trị cụ thể tại biên và hai phía> | <Hành vi> | <Các ràng buộc còn lại> |

## 7. Ma trận kiểm thử biên

| Test Condition ID | Target Variable | Boundary Value ID | Point | Test Data | Other Constraints | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|---|---|
| <COND-ID> | <Biến mục tiêu> | <BV-ID> | <Điểm biên> | <Dữ liệu cụ thể> | <Giá trị danh nghĩa hợp lệ> | <Hợp lệ/Không hợp lệ> | <Kết quả quan sát được> | <Lý do> |

## 8. Quá trình lựa chọn ca kiểm thử

<Giải thích cách tách biến mục tiêu, chọn giá trị danh nghĩa, gộp điểm trùng và xử lý điểm không nhập được hoặc không khả thi>.

## 9. Ma trận truy vết

| Test Case ID | Test Condition ID | Boundary Value ID | Boundary | Test Value | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|---|
| <TC-ID> | <COND-ID> | <BV-ID> | <Biên> | <Giá trị> | <Tính hợp lệ> | <Nguồn> |

## 10. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số biến có biên / biên dưới / biên trên | <Số đếm> / <Số đếm> / <Số đếm> |
| Số biên phụ thuộc / giá trị biên / ca kiểm thử | <Số đếm> / <Số đếm> / <Số đếm> |

| Boundary / Value ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| <Mọi biên và điểm đã xác định> | <TC-ID hoặc chưa có> | <Đã bao phủ/Chưa bao phủ> | <Kết quả thực thi hoặc chưa chạy> | <Lý do thực tế> |

## 11. Giả định và thông tin chưa được đặc tả

- <Ngưỡng, độ chính xác, giới hạn UI hoặc quy tắc còn thiếu; hoặc không có>.

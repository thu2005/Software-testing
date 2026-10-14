# Phân tích kiểm thử miền — <FEATURE-ID>: <Tên chức năng>

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | <FR-ID> / <Nền tảng> |
| Nguồn đặc tả | <Tệp và mục> |
| Tác nhân / Điều kiện tiên quyết | <Thông tin theo đặc tả> |
| Điều kiện thành công / lỗi | <Hành vi theo đặc tả> |

## 2. Biến đầu vào, đầu ra và ràng buộc

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| <Tên biến/điều kiện> | <Đầu vào/đầu ra> | <Kiểu> | <Có/Không/Chưa đặc tả> | <Miền và ràng buộc> | <Nguồn> |

## 3. Phân vùng tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| <EC-ID> | <Biến/điều kiện> | <Điều kiện của lớp> | <Hợp lệ/Không hợp lệ/Loại đầu ra> | <Giá trị cụ thể> | <Hành vi theo đặc tả> | <Nguồn> |

<Giải thích cách chia khoảng/tập/điều kiện bắt buộc; vì sao cần tách lớp và phạm vi bao phủ>.

## 4. Quan hệ phụ thuộc giữa đầu vào và trạng thái

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| <DC-ID> | <Quan hệ> | <Điều kiện hợp lệ> | <Điều kiện không hợp lệ> | <Khả năng tách riêng lỗi> | <Nguồn> |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| <COND-ID> | <EC-ID đầu vào> | <Dữ liệu và trạng thái cụ thể> | <EC-ID đầu ra> | <Hợp lệ/Không hợp lệ> | <Kết quả quan sát được> | <Lý do chọn> |

## 6. Quá trình lựa chọn ca kiểm thử

<Giải thích chọn đại diện mỗi lớp, gộp lớp hợp lệ tương thích, tách từng lớp đầu vào không hợp lệ và loại bỏ ca trùng. Nêu các lớp có thứ tự cần xét BVA>.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| <TC-ID> | <COND-ID> | <EC-ID> | <DC-ID hoặc không áp dụng> | <Nguồn> | <Lý do> |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào hợp lệ / không hợp lệ | <Số đếm> / <Số đếm> |
| Số lớp đầu ra / quan hệ phụ thuộc | <Số đếm> / <Số đếm> |
| Số điều kiện / ca kiểm thử | <Số đếm> / <Số đếm> |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| <Mọi lớp và quan hệ đã xác định> | <TC-ID hoặc chưa có> | <Đã bao phủ/Chưa bao phủ> | <Kết quả thực thi hoặc chưa chạy> | <Lý do thực tế> |

## 9. Giả định và thông tin chưa được đặc tả

- <Thông tin thiếu, giả định cần xác nhận và ảnh hưởng; hoặc không có>.

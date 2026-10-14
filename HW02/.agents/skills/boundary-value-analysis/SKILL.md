---
name: boundary-value-analysis
description: Phân tích requirement bằng Boundary Value Analysis, xác định ON, OFF-, OFF+, xây dựng ma trận giá trị biên và sinh test case có khả năng truy vết. Sử dụng khi requirement có giới hạn min, max, độ dài, số lượng, ngày giờ, kích thước hoặc ngưỡng.
---

# Kỹ năng phân tích giá trị biên

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục và nội dung dùng tiếng Việt có dấu. Giữ nguyên mã định danh và tên trường thực tế.


## 1. Mục đích

Áp dụng Boundary Value Analysis (BVA) một cách có hệ thống và thể hiện rõ cách từng giá trị biên được suy ra từ requirement.

Skill phải tạo cả analysis và test case, không chỉ sinh danh sách test case.

## 2. Quy tắc ngôn ngữ

Viết bài làm bằng tiếng Việt có dấu. Giữ thuật ngữ kiểm thử khi cần; giữ nguyên ID, tên biến, URL, route, dữ liệu test và thông báo thực tế.

## 3. Nguyên tắc bắt buộc

1. Xem hệ thống như một black-box.
2. Không dựa vào source code trừ khi người dùng yêu cầu.
3. Không tự bịa min, max, length, range hoặc validation rule.
4. Khi thiếu dữ liệu, ghi:
   - `Chưa được đặc tả`, hoặc
   - `Giả định cần xác nhận`.
5. Chỉ áp dụng BVA khi tồn tại miền có thứ tự hoặc ngưỡng có ý nghĩa.
6. Không áp dụng BVA máy móc cho dữ liệu categorical không có thứ tự.
7. Mỗi test case phải chỉ rõ boundary point được cover.
8. Input không phải mục tiêu phải dùng giá trị valid nominal.
9. File analysis và test case phải tách riêng.
10. Không tự tạo bug report khi chưa có actual result.

## 4. Các loại biên cần xem xét

- Giá trị nhỏ nhất
- Giá trị lớn nhất
- Độ dài tối thiểu
- Độ dài tối đa
- Độ dài chính xác
- Numeric range
- Date/time range
- Quantity limit
- File size limit
- Số lần thử
- Pagination limit
- Collection size
- Inclusive boundary
- Exclusive boundary
- Empty / non-empty
- State threshold
- Dependent boundary giữa nhiều input

## 5. Quy trình thực hiện

### Bước 1: Đọc và tóm tắt requirement

Trích xuất: Requirement ID; Feature name; Input; Validation rules; Business rules; Preconditions; Success condition; Error condition.

### Bước 2: Xác định biến có biên

Xuất phát từ phân vùng DT; xem xét biên đầu vào và đầu ra có ý nghĩa theo đặc tả. Nếu biên đầu ra không đạt tới được bằng đầu vào hợp lệ, ghi lý do.

Với mỗi biến: Tên biến; Kiểu dữ liệu; Lower boundary; Upper boundary; Inclusive hoặc Exclusive; Đơn vị; Nominal value; Requirement source; Thông tin còn thiếu.

Không coi mọi field đều có biên.

### Bước 3: Chọn phương pháp BVA

Ưu tiên slide 36–37: kiểm tra cận dưới/trên và ngay hai phía mỗi cận, kèm đại diện bên trong. Với khoảng đóng và bước dữ liệu 1, tương ứng Robust BVA bên dưới; không chỉ dùng Normal BVA rồi bỏ hết điểm ngoài miền.

Slide 36 thêm giá trị nhỏ nhất/lớn nhất **thực sự nhập được qua UI**, thành tối đa 9 điểm ứng viên cho khoảng minh họa. Chỉ thêm khi biết giới hạn UI; không nhập vô cực hoặc ép mọi biến có đúng 9 ca. Gộp điểm trùng nhưng giữ mọi liên kết biên.

Ghi rõ phương pháp, các điểm được chọn và điểm chưa kiểm tra được.

#### Normal BVA

Với valid range `[min, max]`:

- `min`
- `min + 1`
- nominal
- `max - 1`
- `max`

#### Robust BVA

Với valid range `[min, max]`:

- `min - 1`
- `min`
- `min + 1`
- nominal
- `max - 1`
- `max`
- `max + 1`

#### ON / OFF convention

Với minimum boundary:

- `OFF⁻ = min - 1`
- `ON = min`
- `OFF⁺ = min + 1`

Với maximum boundary:

- `OFF⁻ = max - 1`
- `ON = max`
- `OFF⁺ = max + 1`

`OFF⁻/OFF⁺` chỉ hướng nhỏ hơn/lớn hơn, không đồng nghĩa invalid/valid. Với dữ liệu khác số nguyên, thay `1` bằng bước `δ` có căn cứ (độ chính xác tiền, thời gian…). Với biên mở, `ON` có thể invalid; đánh giá theo đúng dấu bất đẳng thức. Không tự đặt epsilon hoặc ngưỡng thiếu trong đặc tả.

### Bước 4: Suy ra giá trị biên

Mỗi boundary value phải có: Boundary Value ID; Input; Constraint; Boundary type; Boundary point; Công thức suy ra; Giá trị cụ thể; Valid hoặc Invalid; Expected behavior; Requirement reference.

Dùng ID:

- `BV-<INPUT>-001`

Với string length, phải ghi:

- Độ dài số học
- Chuỗi test cụ thể có đúng độ dài đó

Với date/time, phải ghi ngày giờ cụ thể.

Với file size hoặc quantity, phải ghi đơn vị.

### Bước 5: Isolate biến kiểm thử

Khi kiểm thử một boundary:

- Chỉ thay đổi biến mục tiêu.
- Các điều kiện khác phải hợp lệ.
- Phải giải thích nominal values đang dùng.
- Nếu không isolate được, ghi rõ dependency.

### Bước 6: Phân tích dependent boundary

Ví dụ:

- End date bằng start date
- End date sớm hơn start date một ngày
- Quantity bằng available stock
- Tổng file size bằng đúng giới hạn

Dùng ID:

- `DB-01`
- `DB-02`

### Bước 7: Xây dựng BVA Test Matrix

Mỗi dòng gồm: Test condition ID; Target variable; Boundary Value ID; Boundary point; Test value; Các ràng buộc khác; Expected validity; Expected behavior; Lý do lựa chọn.

Dùng ID:

- `COND-FRXX-BVA-001`

Không tạo Cartesian product cho mọi biến trừ khi có lý do rõ ràng.

### Bước 8: Sinh test case

Mỗi boundary condition được chọn tạo thành một test case riêng.

Dùng ID:

- `TC-FRXX-BVA-001`

Mỗi file chỉ chứa một test case.

Chèn phần phân tích biên liên quan trực tiếp vào từng file test case theo mẫu.

### Bước 9: Tổng kết coverage

Báo cáo: Tổng biến có biên; Tổng lower boundaries; Tổng upper boundaries; Tổng dependent boundaries; Phương pháp BVA; Tổng boundary values; Tổng test cases; Boundary đã cover; Boundary chưa cover; Lý do loại trừ; Requirement gap.

Mỗi boundary phải có trạng thái:

- `Đã cover`
- `Chủ động loại trừ`
- `Bị chặn do thiếu requirement`

## 6. Mẫu và tệp đầu ra

Khi tạo file, đọc mẫu tương ứng trong `templates/` và điền nội dung tiếng Việt; không giữ placeholder trong sản phẩm hoàn chỉnh. Mỗi test case chỉ trích phần phân tích liên quan, ma trận đầy đủ nằm ở analysis.

| Template | Output Path |
|---|---|
| [Mẫu phân tích](../../../templates/bva-analysis-template.md) | `analysis/<FEATURE-ID>-<feature-name>/bva-analysis.md` |
| [Mẫu ca kiểm thử](../../../templates/bva-test-case-template.md) | `tests/test-cases/<FEATURE-ID>-<feature-name>/bva/TC-<FEATURE-ID>-BVA-<NNN>.md` |

## 7. Quy tắc chất lượng

1. Test value phải cụ thể.
2. Với length boundary, dữ liệu phải đúng số ký tự đã ghi.
3. Phải kiểm tra lại bằng cách đếm ký tự trước khi xuất.
4. Expected result phải nêu rõ accepted/rejected behavior.
5. Không dùng `hoạt động đúng` hoặc `hiển thị lỗi` một cách chung chung.
6. Mỗi test case chỉ cover một boundary point chính.
7. Các biến khác sử dụng valid nominal value.
8. Không ghi actual result khi chưa chạy test.
9. Tính lại oracle: slide 37 có lỗi dấu (`-99 + 9 = -90`, không phải `90`). Nếu UI chặn dữ liệu ngoài miền, ghi hành vi UI; không suy diễn backend đã nhận và từ chối.

## 8. Traceability bắt buộc

Analysis phải có bảng:

| Test Case ID | Boundary Value ID | Boundary | Test Data | Expected Validity | Requirement Reference |
|---|---|---|---|---|---|


Liệt kê cả điểm chưa bao phủ và lý do; phân biệt bao phủ thiết kế với thực thi.

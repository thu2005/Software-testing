---
name: domain-testing
description: Phân tích yêu cầu chức năng bằng Domain Testing, xây dựng phân vùng tương đương, ma trận miền dữ liệu và sinh test case có khả năng truy vết. Sử dụng khi người dùng yêu cầu áp dụng Domain Testing, Equivalence Partitioning, phân tích miền đầu vào hoặc tạo test case từ requirement.
---

# Kỹ năng kiểm thử miền

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục và nội dung dùng tiếng Việt có dấu. Giữ nguyên mã định danh và tên trường thực tế.


## 1. Mục đích

Áp dụng Domain Testing một cách có hệ thống cho một functional requirement.

Skill phải thể hiện đầy đủ quá trình từ requirement đến test case, không chỉ sinh danh sách test case cuối cùng.

## 2. Quy tắc ngôn ngữ

Viết bài làm bằng tiếng Việt có dấu. Giữ thuật ngữ kiểm thử khi cần; giữ nguyên ID, tên biến, URL, route, dữ liệu test và thông báo thực tế.

## 3. Nguyên tắc bắt buộc

1. Xem hệ thống như một black-box.
2. Không dựa vào source code của hệ thống trừ khi người dùng yêu cầu rõ ràng.
3. Không tự bịa requirement, validation rule hoặc business rule.
4. Khi thiếu thông tin, phải ghi rõ:
   - `Chưa được đặc tả`, hoặc
   - `Giả định cần xác nhận`.
5. Phân biệt rõ:
   - Thông tin có trong requirement
   - Giả định
   - Điều kiện kiểm thử suy ra
6. Mỗi test case phải truy vết được đến ít nhất một equivalence class hoặc dependent condition.
7. Phải xem xét cả valid domain và invalid domain.
8. Hạn chế test case trùng lặp; nếu giữ lại phải giải thích lý do.
9. Theo slide 31, mỗi ca invalid cơ sở chỉ vi phạm một lớp đầu vào invalid; các điều kiện khác hợp lệ. Nếu không thể isolate do dependency, ghi rõ. Ca nhiều lỗi chỉ là bổ sung có mục đích, không thay bộ cơ sở.
10. File analysis và file test case phải tách riêng.

## 4. Đầu vào mong đợi

Có thể nhận một hoặc nhiều đầu vào sau:

- Functional requirement
- User story
- Acceptance criteria
- Validation rules
- Mô tả giao diện
- Test case template
- Cấu trúc thư mục project
- Đường dẫn output mong muốn

Nếu không có đủ dữ liệu để kết luận, vẫn tiếp tục phân tích phần có thể xác định và ghi phần còn thiếu vào mục `Giả định và thông tin chưa được đặc tả`.

## 5. Quy trình thực hiện

### Bước 1: Đọc và tóm tắt requirement

Trích xuất: Requirement ID; Tên chức năng; Actor; Preconditions; Input; Output; Business rules; Validation rules; Dependency; Error conditions; Success conditions.

Tạo bảng tóm tắt requirement.

### Bước 2: Xác định biến đầu vào, đầu ra và điều kiện hệ thống

Xác định cả output theo slide 13–17: giá trị tính toán, dữ liệu trả về, thành công và các loại lỗi theo đặc tả. Không chỉ nhắc tới output trong tóm tắt rồi bỏ qua khi phân lớp.

Không chỉ phân tích field trên giao diện.

Cần xem xét:

- Giá trị người dùng nhập
- Trạng thái đăng nhập
- User role
- Dữ liệu đã tồn tại hoặc chưa tồn tại
- Quan hệ giữa nhiều input
- Trạng thái hệ thống hoặc external service nếu requirement có đề cập

Với mỗi biến hoặc điều kiện, xác định: Tên biến; Kiểu dữ liệu; Bắt buộc hay không; Format; Range; Valid conditions; Invalid conditions; Dependency; Nguồn requirement.

### Bước 3: Phân vùng tương đương

Chia các điều kiện **đầu vào và đầu ra** thành equivalence class. Theo slide 18–21:

- Khoảng giá trị: lớp trong khoảng, dưới cận, trên cận; phân biệt đóng/mở.
- Tập giá trị: tách phần tử được xử lý khác nhau, thêm lớp ngoài tập.
- Điều kiện “must be”: lớp thỏa mãn và không thỏa mãn.
- Tách lớp nếu các phần tử có hành vi xử lý khác nhau theo đặc tả.

Cùng lớp là cùng kiểu hành vi mong đợi, không nhất thiết cùng kết quả số; tính oracle cụ thể cho từng dữ liệu test.

Mỗi class phải có: Class ID; Input hoặc điều kiện; Mô tả class; Valid hoặc Invalid; Giá trị đại diện; Requirement reference; Ghi chú hoặc giả định.

Quy tắc ID:

- `EC-<INPUT>-V01` cho valid class
- `EC-<INPUT>-I01` cho invalid class
- `EC-<OUTPUT>-O01` cho lớp đầu ra; liên kết tới test case tạo ra đầu ra đó.

Ví dụ:

- `EC-EMAIL-V01`
- `EC-EMAIL-I01`
- `EC-PASSWORD-I02`

### Bước 4: Phân tích quan hệ phụ thuộc

Xác định các điều kiện phụ thuộc giữa input hoặc giữa input và system state.

Ví dụ:

- `confirmPassword` phải khớp `password`
- Email đúng format nhưng đã tồn tại
- End date phải sau start date
- Một field chỉ bắt buộc khi chọn một option khác

Dùng ID:

- `DC-01`
- `DC-02`

### Bước 5: Xây dựng Domain Matrix

Tạo Domain Matrix thể hiện các tổ hợp điều kiện dự kiến kiểm thử.

Mỗi dòng phải có: Test condition ID; Các class được bao phủ; Giá trị hoặc trạng thái đại diện; Expected validity; Expected behavior; Lý do chọn.

Quy tắc:

- Giữ input không phải mục tiêu ở trạng thái valid nominal.
- Chọn ít nhất một đại diện mỗi lớp khả thi và giải thích lựa chọn.
- Gộp các lớp valid tương thích để bao phủ hết với ít ca trùng lặp (slide 31–33).
- Mỗi ca invalid cơ sở chỉ vi phạm một lớp đầu vào invalid; vẫn truy vết tới lớp lỗi đầu ra tương ứng.
- Không tạo Cartesian product một cách máy móc.

Dùng ID:

- `COND-FRXX-DT-001`

### Bước 6: Sinh test case

Mỗi test condition được chọn phải tạo thành một test case riêng.

Dùng ID:

- `TC-FRXX-DT-001`

Mỗi file chỉ chứa một test case.

Chèn phần phân tích miền liên quan trực tiếp vào từng file test case theo mẫu.

### Bước 7: Tổng kết coverage

Báo cáo: Tổng số input/condition đã phân tích; Tổng valid equivalence class; Tổng invalid equivalence class; Tổng dependent condition; Tổng test condition; Tổng test case; Class đã cover; Class chưa cover; Lý do loại trừ; Requirement gap.

Tính cả lớp đầu ra và các lớp chưa được đưa vào matrix; không chỉ tổng kết phần đã chọn. Phân biệt bao phủ thiết kế và thực thi. Chỉ ra lớp có thứ tự cần chuyển sang BVA, tương ứng bước 4 của slide 13, 34–37.

Mỗi class phải có một trạng thái:

- `Đã cover`
- `Chủ động loại trừ`
- `Bị chặn do thiếu requirement`

## 6. Mẫu và tệp đầu ra

Khi tạo file, đọc mẫu tương ứng trong `templates/` và điền nội dung tiếng Việt; không giữ placeholder trong sản phẩm hoàn chỉnh. Mỗi test case chỉ trích phần phân tích liên quan, ma trận đầy đủ nằm ở analysis.

| Template | Output Path |
|---|---|
| [Mẫu phân tích](../../../templates/domain-testing-analysis-template.md) | `analysis/<FEATURE-ID>-<feature-name>/domain-testing-analysis.md` |
| [Mẫu ca kiểm thử](../../../templates/domain-testing-test-case-template.md) | `tests/test-cases/<FEATURE-ID>-<feature-name>/domain-testing/TC-<FEATURE-ID>-DT-<NNN>.md` |

## 7. Quy tắc chất lượng test case

1. Test data phải là dữ liệu cụ thể, không chỉ ghi `Valid` hoặc `Invalid`.
2. Test steps phải có thể thực thi.
3. Expected result phải quan sát được.
4. Không dùng mô tả mơ hồ như:
   - `Hoạt động đúng`
   - `Validation thành công`
   - `Hiển thị lỗi`
5. Với hành vi có trong đặc tả, nêu rõ (không tự đặt thông báo, redirect hay side effect chưa được quy định):
   - Hành động được chấp nhận hay bị từ chối
   - Thông báo hoặc validation behavior mong đợi
   - Có tạo hoặc thay đổi dữ liệu hay không
   - Có redirect hay không
6. Không ghi actual result hoặc tạo bug report khi test chưa được chạy.

## 8. Traceability bắt buộc

Analysis phải có bảng:

| Test Case ID | Test Condition | Covered Input / Output Classes | Requirement Reference | Selection Reason |
|---|---|---|---|---|

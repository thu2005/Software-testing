---
name: test-case-review
description: Review QA analysis and generated test case files for black-box testing assignments. Use when Codex must audit Domain Testing or Boundary Value Analysis outputs for concrete test data, observable expected results, traceability, duplicates, invented constraints, Vietnamese format, and readiness before execution.
---

# Kỹ năng rà soát ca kiểm thử

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục và nội dung dùng tiếng Việt có dấu. Giữ nguyên mã định danh và tên trường thực tế.

## 1. Mục đích

Review test case đã tạo trước khi execution. Skill này không mặc định sinh test case mới; chỉ phân tích lỗi, đề xuất sửa, và chỉ sửa file khi người dùng yêu cầu rõ ràng hoặc task đang yêu cầu hoàn thiện artifact.

## 2. Quy tắc ngôn ngữ

Viết bài làm bằng tiếng Việt có dấu. Giữ thuật ngữ kiểm thử khi cần; giữ nguyên ID, tên biến, URL, route, dữ liệu test, thông báo thực tế và đường dẫn evidence. Đường dẫn output tính từ `Software-testing/HW02/`.

## 3. Nguyên tắc review

1. Xem hệ thống như black-box.
2. Không đọc source code để suy ra expected result trừ khi người dùng yêu cầu.
3. Không bịa constraint, validation rule, business rule hoặc thông báo lỗi.
4. Nếu requirement thiếu thông tin, ghi `Chưa được đặc tả` hoặc `Giả định cần xác nhận`.
5. Phân biệt lỗi nghiêm trọng cần sửa với gợi ý cải thiện.
6. Không biến một test case thành nhiều mục tiêu kiểm thử chính.
7. Không gán Pass/Fail khi chưa có Actual Result.

## 4. Checklist review

Review từng analysis file và test case file theo các điểm sau:

- Requirement reference có đúng và đầy đủ không.
- DT có cả input/output classes, quy tắc phân lớp và chọn đại diện theo slide 13–33 không.
- BVA có biên đóng/mở, bước dữ liệu, điểm ngay ngoài miền và giới hạn UI khi biết không (slide 36–37).
- Technique có đúng với nội dung không: Domain Testing hay BVA.
- Test case ID, condition ID, equivalence class ID hoặc boundary value ID có nhất quán không.
- Test data có giá trị cụ thể, không chỉ ghi `valid`, `invalid`, `empty`, `too long`.
- Expected Result có quan sát được không: accepted/rejected, validation message nếu requirement có nêu, redirect, data created/updated/not changed.
- Test steps có thực thi được theo UI/API được mô tả không.
- Preconditions có đủ để chạy test không.
- Invalid case có isolate một điều kiện chính không.
- Các input khác có dùng valid nominal value không.
- BVA string length đã đếm đúng số ký tự chưa.
- Domain Matrix hoặc BVA Matrix có nằm trong analysis, không lặp lại đầy đủ trong từng test case.
- Test case có duplicate mục tiêu, duplicate data hoặc duplicate coverage không.
- Status ban đầu phải là `Not Run / None` nếu chưa execution.
- Nội dung có đúng tiếng Việt có dấu, tiêu đề cột tiếng Anh và đúng mẫu trong `templates/` không.

## 5. Cách review

### Bước 1: Thu thập ngữ cảnh

Đọc các file liên quan:

- `requirements/<FEATURE-ID>-<feature-name>.md`
- `analysis/<FEATURE-ID>-<feature-name>/*.md`
- `tests/test-cases/<FEATURE-ID>-<feature-name>/**/*.md`
- Template trong `templates/` nếu cần đối chiếu format.

### Bước 2: Lập danh sách phát hiện

Mỗi finding nên có:

- Mã finding: `REV-<FEATURE-ID>-<NNN>`
- Mức độ: `Critical`, `Major`, `Minor`
- File và dòng nếu có thể xác định
- Mô tả vấn đề
- Ảnh hưởng đến test quality
- Đề xuất sửa cụ thể

### Bước 3: Kiểm tra traceability

Lập bảng:

| Test Case ID | Requirement | Analysis Condition | Class / Boundary | Status | Notes |
|---|---|---|---|---|---|

Trạng thái gồm:

- `Hợp lệ`
- `Thiếu liên kết`
- `Sai liên kết`
- `Cần xác nhận`

### Bước 4: Kiểm tra coverage và duplicate

Lập bảng ngắn:

| Coverage Item | Covering Test Cases | Status | Notes |
|---|---|---|---|

Không yêu cầu tạo Cartesian product. Đánh dấu cả lớp đầu vào/đầu ra, biên hoặc dependency bị bỏ sót khi đối chiếu đặc tả, không chỉ phần AI đã chọn trong analysis.

### Bước 5: Kết luận sẵn sàng execution

Kết luận một trong các trạng thái:

- `Sẵn sàng execution`
- `Cần sửa trước execution`
- `Bị chặn do thiếu requirement`

## 6. Output mặc định

Nếu người dùng không chỉ định file output, tạo review tại:

`reviews/<FEATURE-ID>-<feature-name>/<technique>-review.md`

Đọc [mẫu rà soát](../../../templates/test-case-review-template.md) khi tạo review; điền phát hiện, truy vết, độ bao phủ và trạng thái rà soát thực tế.

## 7. Khi được yêu cầu sửa file

Ghi rõ trạng thái rà soát thực tế của sinh viên; agent review không thay human review (§2 đề). Các thiếu sót của AI có bằng chứng phải được chuyển sang `ai-gap-analysis/` qua `$qa-workflow`.

1. Sửa tối thiểu để khắc phục finding.
2. Giữ ID đã có nếu không bắt buộc đổi.
3. Không tạo expected result mới vượt quá requirement.
4. Cập nhật review để ghi rõ finding nào đã được xử lý.

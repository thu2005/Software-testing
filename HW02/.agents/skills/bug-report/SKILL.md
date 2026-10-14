---
name: bug-report
description: Create or review defect reports from failed QA test executions. Use when a test case has Fail status, Actual Result, Expected Result, environment, and evidence; generate BUG-FRxx-nnn.md files, check reproducibility, severity/priority, duplicates, and links back to test cases.
---

# Kỹ năng báo lỗi

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục và nội dung dùng tiếng Việt có dấu. Giữ nguyên mã định danh và tên trường thực tế.

## 1. Mục đích

Tạo bug report có thể reproduce từ test case bị Fail. Skill này không tạo bug khi test chưa chạy, khi status là Pass/Blocked/Not Run, hoặc khi chưa có Actual Result đủ rõ.

## 2. Quy tắc ngôn ngữ

Viết bài làm bằng tiếng Việt có dấu. Giữ thuật ngữ kiểm thử khi cần; giữ nguyên ID, tên biến, URL, route, dữ liệu test, thông báo thực tế và đường dẫn evidence. Đường dẫn output tính từ `Software-testing/HW02/`.

## 3. Điều kiện trước khi tạo bug

Chỉ tạo bug khi có đủ:

- Test Case ID và file test case.
- Status `Fail`.
- Expected Result.
- Actual Result quan sát được.
- Steps reproduce cụ thể.
- Environment hoặc thông tin build tối thiểu.
- Evidence nếu có.

Nếu thiếu một phần, tạo mục `Thông tin cần bổ sung` thay vì viết bug như đã xác nhận.

## 4. Quy trình tạo bug

### Bước 1: Đối chiếu expected và actual

Xác định sự khác biệt:

| Test Case ID | Expected Result | Actual Result | Difference | Defect? |
|---|---|---|---|---|

Nếu actual khác vì expected result sai hoặc requirement mơ hồ, ghi `Cần review test case/requirement` thay vì tạo bug chắc chắn.

### Bước 2: Kiểm tra duplicate

Tìm trong:

- `bug-reports/*.md`
- `tests/test-runs/*.md`
- Related bugs trong test case file

Không tạo bug mới nếu cùng root cause và cùng behavior đã được report. Nếu là duplicate, cập nhật liên kết đến bug đã có.

### Bước 3: Gán ID bug

Dùng format:

`BUG-FRXX-NNN.md`

Trong đó `NNN` là số tiếp theo trong `bug-reports/` cho feature đó.

### Bước 4: Đánh giá severity và priority

Severity theo tác động:

| Severity | When to Use |
|---|---|
| Critical | Chặn luồng chính, crash, mất dữ liệu, rủi ro bảo mật nghiêm trọng |
| High | Chức năng chính sai, không có workaround hợp lý |
| Medium | Chức năng phụ sai hoặc có workaround chấp nhận được |
| Low | Lỗi nhỏ về UI/text/validation không chặn luồng chính |

Priority theo mức độ cần sửa:

| Priority | When to Use |
|---|---|
| P1 | Cần sửa ngay để tiếp tục test/release |
| P2 | Nên sửa trong vòng hiện tại |
| P3 | Có thể lên lịch sau |

Ghi lý do ngắn cho severity và priority.

### Bước 5: Tạo file bug report

Tạo tại:

`bug-reports/BUG-FRXX-NNN.md`

Đọc [mẫu báo lỗi](../../../templates/bug-report-template.md) khi tạo báo cáo; điền kết quả và bằng chứng thực tế.

## 5. Quy tắc chất lượng

1. Summary phải mô tả symptom, không viết chung chung như `Login bị lỗi`.
2. Steps phải đủ để người khác reproduce.
3. Expected và Actual phải thực sự khác nhau.
4. Evidence phải là đường dẫn file, link, response, log, hoặc mô tả người dùng cung cấp.
5. Không chèn nhiều defect khác nhau vào một bug nếu khác root cause.
6. Không sửa requirement để làm bug hợp lệ.

## 6. GitHub Issues theo HW02 (§6, §14)

- Mọi bug phát hiện phải có báo cáo Markdown **và** issue trên GitHub của nhóm, đính kèm screenshot lỗi. Repository SUT không tự động là repository nhóm.
- Khi nhiệm vụ có đăng issue, dùng đúng repository và quyền truy cập đã có; chuẩn bị title/body và ảnh trước. Đường dẫn ảnh local không phải ảnh đính kèm trên GitHub.
- Ghi URL issue thật và trạng thái đăng. Nếu thiếu ảnh, quyền truy cập hoặc công cụ upload, giữ bản nháp và ghi phần còn thiếu; không bịa issue/link hoặc coi là hoàn tất.
- Bài nộp còn cần screenshot bug trên trang GitHub Issues. Không tạo ảnh minh họa để thay bằng chứng thực tế.

## 7. Cập nhật liên kết

Sau khi tạo bug:

- Cập nhật `tests/test-runs/<FEATURE>-run.md` cột Related Bug nếu file tồn tại.
- Cập nhật `Status / Related bugs` trong test case file nếu workflow yêu cầu đồng bộ.
- Không cập nhật status của test case thành Pass.

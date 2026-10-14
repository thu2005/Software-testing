---
name: qa-workflow
description: Điều phối kiểm thử black-box HW02 cho FR01, FR07, FR14 và FR06 trên Mobile, từ phân tích DT/BVA đến rà soát, thực thi và báo cáo.
---

# Quy trình kiểm thử HW02

Viết bài làm và tiêu đề mục bằng tiếng Việt; tiêu đề cột bảng bằng tiếng Anh. Giữ nguyên ID, tên trường, dữ liệu và thông báo thực tế. Đường dẫn bên dưới tính từ `Software-testing/HW02/`.

## Phạm vi

| Pool | Requirement ID | Feature | Platform |
|---|---|---|---|
| A | FR-01 | Đăng ký tài khoản | Web |
| B | FR-07 | Giỏ hàng | Web |
| C | FR-14 | Quản lý danh mục | Web Admin |
| D | FR-06 | Xem chi tiết sản phẩm | Mobile |

Phạm vi đã chọn được lưu trong [chức năng kiểm thử](../../../requirements/selected-features.md). Đọc đặc tả chức năng để xác định quy tắc nghiệp vụ và kết quả mong đợi; không suy ra chúng từ tên chức năng hoặc mã nguồn. Thiếu quy tắc thì ghi `Chưa được đặc tả` hoặc `Giả định cần xác nhận`.

## Các bước

1. **Đọc yêu cầu:** xác định đầu vào, đầu ra, trạng thái, ràng buộc và quan hệ phụ thuộc của chức năng.
2. **Phân tích và thiết kế:** áp dụng cả `$domain-testing` và `$boundary-value-analysis` cho mỗi chức năng, trình bày cách suy ra lớp, biên và dữ liệu kiểm thử. Biến không có biên có ý nghĩa thì ghi rõ.
3. **Rà soát:** dùng `$test-case-review`, sửa lỗi thiết kế khi trong phạm vi công việc. Ghi nhận phần sinh viên thực sự rà soát/chỉnh sửa; không coi agent review là human review.
4. **Thực thi:** dùng `$test-execution` khi nhiệm vụ yêu cầu chạy kiểm thử. Ghi kết quả quan sát được và bằng chứng; không đoán Pass/Fail. Yêu cầu chỉ phân tích/thiết kế/rà soát kết thúc ở bước tương ứng.
5. **Báo lỗi:** dùng `$bug-report` cho ca Fail có kết quả thực tế. Mọi bug phát hiện cần báo cáo Markdown và GitHub Issue của nhóm kèm ảnh lỗi; ghi rõ phần chưa đăng nếu thiếu quyền truy cập.
6. **Phân tích thiếu sót AI:** nếu có, ghi bằng chứng đầu ra ban đầu, ca/bug bị bỏ sót, nguyên nhân có căn cứ và phần bổ sung vào `ai-gap-analysis/<FEATURE-ID>-<feature-name>.md`.
7. **Lưu quá trình:** sau mỗi tương tác hoàn tất, dùng `$prompt-log` ghi công cụ, ngày giờ, prompt và output vào `reports/prompt_log.md`. Khi thực hiện bài tập và việc commit nằm trong phạm vi được giao, mỗi bước kiểm thử của mỗi chức năng cần một Git commit riêng.

Chỉ đọc skill cần cho bước hiện tại. Tách analysis và test case; mỗi test case một file, ban đầu `Not Run / None`.

## Mẫu và tệp đầu ra

Tra loại file và đường dẫn đầu ra tại [danh mục mẫu](../../../templates/README.md); chỉ đọc mẫu cần cho bước hiện tại. Các skill chuyên biệt liên kết trực tiếp tới mẫu của mình.

Nếu cần ghi nhận đặc tả chức năng, dùng [mẫu yêu cầu](../../../templates/requirement-template.md). Khi phân tích thiếu sót AI, dùng [mẫu AI gap](../../../templates/ai-gap-analysis-template.md).

## Tra cứu yêu cầu và tổng hợp báo cáo

Đề đã chuyển sang [Markdown](../../../requirements/hw02-assignment.md). Chỉ đọc mục cần dùng: §6 yêu cầu kiểm thử, §§9–10 báo cáo AI, §12 lịch sử Git, §§14–15 bài nộp và điểm. Không cần đọc PDF.

Khi chuẩn bị nộp, dùng [checklist](references/hw02-checklist.md). Khi kết thúc công việc, nêu tệp đã tạo/sửa, số ca, kết quả rà soát/thực thi và phần còn thiếu.

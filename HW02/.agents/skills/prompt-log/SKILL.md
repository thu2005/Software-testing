---
name: prompt-log
description: Append a verbatim, unedited transcript of the completed Codex prompt session or available conversation context to prompt_log.md. Use when the user asks to log prompts, save the chat, copy the full conversation exactly after a prompt finishes, preserve AI interaction evidence, or maintain a prompt log for assignment submission.
---

# Kỹ năng ghi nhật ký AI

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục và nội dung dùng tiếng Việt có dấu. Giữ nguyên mã định danh và tên trường thực tế.

## 1. Mục đích

Ghi lại nguyên văn toàn bộ đoạn chat hoặc phần hội thoại khả dụng vào `prompt_log.md` sau khi một prompt/task đã hoàn thành. Skill này dùng để lưu evidence về cách đã dùng AI trong bài tập, nên độ trung thực của transcript quan trọng hơn độ gọn đẹp.

## 2. Nguyên tắc bắt buộc

1. Ghi log sau khi hoàn thành việc chính của prompt. Trong quá trình làm bài HW02, lưu mỗi tương tác AI theo §§2, 9, không chỉ phiên cuối hoặc khi được nhắc.
2. Không thay thế nội dung cũ trong `prompt_log.md`; luôn append thêm entry mới.
3. Nếu không truy cập được toàn bộ lịch sử hội thoại, ghi rõ phạm vi log là `conversation context khả dụng`.
4. Copy nguyên văn câu chữ, thứ tự, lỗi chính tả, cách viết tắt, dấu câu và ngôn ngữ của từng message trong context.
5. Không tóm tắt, không diễn giải, không sửa văn phong, không dịch, không chuẩn hóa câu chữ.
6. Không bịa lại nội dung chat không có trong context.
7. Chỉ được thay đổi nội dung khi cần che bí mật như token, password, key hoặc credential; thay đúng phần bí mật bằng `[REDACTED]`.
8. Nếu có tool output quá dài không còn đầy đủ trong context, ghi nguyên văn phần còn thấy được và ghi chú rõ phần bị thiếu.
9. Ghi tên công cụ AI, ngày giờ và múi giờ cho từng tương tác; model/version chỉ khi biết. Không bịa thời điểm gốc: nếu thiếu, ghi rõ và tách thời điểm lưu log.
10. Chỉ log hội thoại/output hiển thị; không đưa system/developer instructions hoặc suy luận riêng tư vào transcript; khi call đến skill, chỉ ghi tên skill, không log lại toàn bộ nội dung skill. Không ghi trước một câu trả lời chưa được gửi.


## 3. File output

Ghi tại `Software-testing/HW02/reports/prompt_log.md`. Nếu đã có log ở vị trí khác, giữ nội dung cũ và tham chiếu/chuyển theo yêu cầu, không tạo hai bản mâu thuẫn.

Nếu file chưa tồn tại, tạo file mới.

## 4. Format entry

Mỗi lần ghi log, nối một entry theo [mẫu tương tác AI](../../../templates/prompt-log-entry-template.md). Giữ nguyên transcript, quy tắc Model/Timestamp và chỉ log tool call khi người dùng yêu cầu; không chép nội dung skill vào transcript.

## 5. Khi người dùng yêu cầu "toàn bộ đoạn chat"

1. Ghi transcript đầy đủ nhất có trong context hiện tại.
2. Phân vai rõ `User`, `Assistant`, `Tool`, hoặc `System note` nếu cần.
3. Nếu context đã bị compact hoặc thiếu đoạn cũ, ghi chú: `Một phần hội thoại trước đó không còn trong context, chỉ log phần khả dụng`.
4. Không tự tạo lại nguyên văn những đoạn không còn nhìn thấy.
5. Không thay một đoạn chat bằng summary. Nếu đoạn nào không thể copy nguyên văn, bỏ đoạn đó và ghi rõ lý do trong `Notes`.

## 6. Khi dùng cùng skill khác

Các heading/ghi chú audit viết tiếng Việt; prompt và output nguyên văn giữ ngôn ngữ gốc. Log là bằng chứng cho AI Audit Report, không thay phụ lục bắt buộc: khi tổng hợp báo cáo, thêm khai báo công cụ/tác vụ và chỉ mục tới từng tương tác.

Nếu prompt chính dùng `$qa-workflow`, `$domain-testing`, `$boundary-value-analysis`, `$test-case-review`, `$test-execution`, hoặc `$bug-report`, hoàn thành skill chính trước. Sau đó mới dùng `$prompt-log` để append entry vào `prompt_log.md`.

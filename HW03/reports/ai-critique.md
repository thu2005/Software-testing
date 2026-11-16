# Phản biện việc sử dụng AI

AI hữu ích khi chuyển yêu cầu thành artifact có cấu trúc và nối traceability
giữa checklist, kết quả, screenshot, bug report và GitHub Issue. Công cụ còn hỗ
trợ 195 lượt kiểm tra cross-platform và tổng hợp bảy usability session. Tuy
nhiên, các output ban đầu không thể dùng nguyên trạng.

Sai sót rõ nhất nằm ở checklist tại Entry #4. AI tạo 48 mục nhưng ghép nhiều
oracle và bỏ sót ngôn ngữ toàn cục, keyboard Checkout, nội dung dài, session
expiry cùng phục hồi lỗi mạng. Human review phải tách và bổ sung thành 65 mục.
AI còn kết luận Chrome headless không xuất được DOM/screenshot; thực tế profile
mặc định bị từ chối quyền và script đọc DOM trước khi React tải xong. Dùng
profile tạm và chờ API đã giải quyết vấn đề.

Ở Entry #10, AI soạn SUS và scenario iPhone không khớp protocol thực tế; sinh
viên phải công bố chronology, dùng scenario AirPods, custom scale và participant
thật. AI từng xem việc thiếu ảnh chỉ là vấn đề UX, nhưng retest theo FR-05/FR-06
xác nhận đây là defect và cần Issue #64. Ở Entry #11, tổng hợp M8 ban đầu giữ số
liệu chưa chốt và evidence chưa đủ rõ cho một số kiểm tra runtime. Human review
và lần chạy lại ở Entry #12 đã sửa thành 94 Passed, 101 Failed, đồng thời xác
nhận chỉ GUI-029 khác verdict giữa Firefox và Chrome.

Bài học là AI phù hợp để tạo draft, tự động hoá việc lặp lại và gợi ý gap, nhưng
không thay thế oracle, execution evidence hay human review. Mỗi kết luận phải
được đối chiếu requirement; số liệu, link và screenshot phải được kiểm đếm độc
lập trước khi chốt.

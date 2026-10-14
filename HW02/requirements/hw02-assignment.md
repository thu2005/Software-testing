# HW02 – Domain Testing trên EShop

> Bản chuyển nội dung sang Markdown và dịch tiếng Việt từ đề “2026.HW02.Domain Testing_En.pdf” (7 trang). Giữ đủ 17 mục; bỏ đầu/chân trang lặp, chuẩn hóa ký hiệu bị lỗi khi trích xuất. Dùng tài liệu này để tra cứu yêu cầu, không cần kèm PDF gốc. Phạm vi sinh viên chọn được ghi riêng trong [selected-features.md](selected-features.md), không phải nội dung đề gốc.

## 1. Thông tin chung

| Field | Content |
|---|---|
| Mã bài tập | HW02-AI |
| Thời lượng | 10 giờ |
| Hạn nộp | Xem liên kết nộp bài trên Moodle |
| Hình thức | Bài tập cá nhân |
| Nơi nộp | Moodle (báo cáo) |
| Giảng viên và trợ giảng | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| Liên hệ | lqvu@fit.hcmus.edu.vn / tdhoang@fit.hcmus.edu.vn / ttbhanh@fit.hcmus.edu.vn / tploc@fit.hcmus.edu.vn / hthanh@fit.hcmus.edu.vn |
| Chính sách AI | Mở; bắt buộc khai báo và đính kèm AI Audit Report |
| Mức Bloom-AI | G9.1 → G9.6 tùy bài tập, xem ánh xạ chuẩn đầu ra; mức cụ thể của HW02 ở §8 |

## 2. Nguyên tắc thực hiện

Các nguyên tắc này áp dụng xuyên suốt chuỗi bài tập và được dùng để đánh giá bài nộp.

**Chiến lược AI-first.** Phải áp dụng AI vào các kỹ thuật kiểm thử đã học. Không chỉ đưa một prompt chung như “sinh test case và tìm bug trong chức năng này”. Phải hướng dẫn AI qua từng bước của kỹ thuật như trên lớp, sử dụng AI như một trợ lý có kỷ luật.

**Rà soát của con người.** Sinh viên phải kiểm tra cẩn thận mọi kết quả AI tạo ra và chịu trách nhiệm về tính đúng đắn. Phải sửa và tinh chỉnh khi cần; không nộp nguyên đầu ra AI chưa được rà soát.

**AI Audit Report.** Toàn bộ quá trình dùng AI phải có log đầy đủ. Khuyến khích xây dựng Agent Skills tự động áp dụng kỹ thuật vào bài tương tự. Nếu không dùng AI vẫn phải khai báo rõ.

**Tài liệu hóa.** Ghi lại toàn bộ quá trình làm việc bằng định dạng văn bản, chẳng hạn Markdown.

**Chất lượng sản phẩm.** Đánh giá không chỉ dựa vào hoàn thành hay chưa, mà còn số lượng và chất lượng báo cáo tổng quát, báo cáo test case, báo cáo bug, báo cáo tổng kết kiểm thử, script, ảnh chụp, video và liên kết tham khảo.

## 3. Kết quả học tập

- Áp dụng Domain Testing và Boundary Value Analysis vào một hệ thống thực tế.
- Thể hiện năng lực Bloom-AI ở G9.2 (Áp dụng) và G9.3 (Phân tích).

## 4. Hệ thống được kiểm thử

**SUT:** EShop, ứng dụng thương mại điện tử demo bằng tiếng Việt phục vụ thực hành kiểm thử.

**Kho mã nguồn:** <https://github.com/ttbhanh/eshop-sut>.

### Nhóm A – Xác thực, danh mục và sản phẩm

| Requirement ID | Feature |
|---|---|
| FR-01 | Đăng ký tài khoản |
| FR-02 | Đăng nhập và khóa tài khoản |
| FR-03 | Quên mật khẩu và đặt lại mật khẩu (hai bước) |
| FR-04 | Quản lý hồ sơ cá nhân |
| FR-05 | Danh sách và tìm kiếm sản phẩm |
| FR-06 | Xem chi tiết sản phẩm |

### Nhóm B – Giỏ hàng và thanh toán

| Requirement ID | Feature |
|---|---|
| FR-07 | Giỏ hàng |
| FR-08 | Thanh toán |
| FR-09 | Mã giảm giá |
| FR-10 | Máy trạng thái đơn hàng |
| FR-11 | Xem lịch sử đơn hàng của người dùng |

### Nhóm C – Quản trị Web

| Requirement ID | Feature |
|---|---|
| FR-12 | Kiểm soát truy cập |
| FR-13 | Bảng điều khiển |
| FR-14 | Quản lý danh mục (CRUD) |
| FR-15 | Quản lý sản phẩm (CRUD) |
| FR-16 | Nhập sản phẩm từ CSV |
| FR-17 | Quản lý mã giảm giá (CRUD) |
| FR-18 | Quản lý đơn hàng của quản trị viên |
| FR-19 | Quản lý người dùng của quản trị viên |

### Nhóm D – Ứng dụng Mobile

Đề gốc ghi “Mobile App”, không liệt kê riêng các mã chức năng trong nhóm này.

## 5. Lựa chọn chức năng

Trong mỗi nhóm sinh viên, mỗi người chọn **4 chức năng**, mỗi nhóm chức năng A/B/C/D chọn một chức năng. Bảo đảm các thành viên trong nhóm sinh viên không chọn trùng chức năng.

## 6. Yêu cầu thực hiện

Với **mỗi chức năng đã chọn**, thực hiện:

1. **Domain Testing:** với sự hỗ trợ của AI, áp dụng kỹ thuật kiểm thử miền để thiết kế bộ test case đầy đủ. Khuyến khích bổ sung ca khi cần để tăng độ bao phủ. Giải thích chi tiết từng bước áp dụng kỹ thuật; xem lại bài giảng trước khi làm.
2. **Boundary Value Analysis:** tương tự, áp dụng phân tích giá trị biên để thiết kế bộ test case đầy đủ, bổ sung khi cần. Giải thích chi tiết từng bước áp dụng kỹ thuật; xem lại bài giảng trước khi làm.
3. **AI gap analysis:** nếu công cụ AI bỏ sót test case hoặc bug, phải báo cáo và giải thích nguyên nhân, chẳng hạn chất lượng prompt, giới hạn của công cụ hoặc độ phức tạp của chức năng.
4. **Báo lỗi:** báo cáo mọi bug phát hiện trong báo cáo Markdown và trên GitHub Issues của nhóm sinh viên. Đính kèm ảnh chụp bug cho từng issue.

## 7. Agent Skill

Khuyến khích xây dựng Agent Skills áp dụng Domain Testing và Boundary Value Analysis để tái sử dụng cho các chức năng khác.

Nộp skills kèm video minh họa (liên kết YouTube), thể hiện từ đầu đến cuối cách dùng skills trên một chức năng hoàn chỉnh.

## 8. Công cụ được phép và mức Bloom-AI

Được dùng các công cụ sau và phải khai báo trong AI Audit Report:

- Công cụ AI tùy chọn, ví dụ ChatGPT, Claude, Gemini, Copilot, Cursor.
- Công cụ AI sinh test, ví dụ Diffblue, để kiểm tra chéo (không bắt buộc).

Mức yêu cầu của HW02 là **G9.2 (Áp dụng)** và **G9.3 (Phân tích)**.

## 9. AI Audit Report – Phụ lục bắt buộc

Đính kèm báo cáo kiểm toán việc dùng AI làm phụ lục. Có thể dùng nội dung AI Templates được cung cấp nếu cần.

- Nếu không dùng AI, khai báo “Tôi không sử dụng bất kỳ sự hỗ trợ AI nào trong bài tập này”. Câu trong đề gốc: “I do not use any AI help in this exercise.”
- Nếu dùng AI, khai báo “Tôi sử dụng công cụ AI cho các tác vụ sau”. Câu trong đề gốc: “I use AI tools for the following tasks,”.

Với **mỗi tương tác**, ghi:

1. Tên công cụ AI.
2. Ngày và giờ.
3. Prompt của sinh viên.
4. Đầu ra của AI.

Khuyến khích tạo skill hoặc rule tự động trích xuất các thông tin này sau mỗi phiên AI để đơn giản hóa việc ghi nhận.

## 10. AI Critique – Bắt buộc, 200–300 từ

Viết **một đoạn văn 200–300 từ** phản biện AI, trả lời:

- AI sai, thiên lệch hoặc chưa đầy đủ ở đâu?
- Vì sao AI không phát hiện vấn đề đó?
- Sinh viên học được nguyên tắc gì khi cộng tác với AI trong bài tập?

Có thể dùng nội dung AI Templates được cung cấp nếu cần.

## 11. Ràng buộc chống gian lận bằng AI

Không có.

## 12. Lịch sử Git commit

Tạo **một Git commit mới cho mỗi bước của quy trình kiểm thử của mỗi chức năng**.

Cung cấp lịch sử Git commit dưới dạng tệp văn bản.

## 13. Vấn đáp

30% sinh viên được chọn ngẫu nhiên có thể được mời vấn đáp trong tuần sau hạn nộp. Thời lượng 5–7 phút để giải thích cách hoàn thành bài tập.

## 14. Quy định nộp bài

Tên tệp:

```text
<StudentID>_HW02_AI_DomainTesting_<SelfAssessedGrade>.zip
```

`SelfAssessedGrade` là số có **3 chữ số**, nằm trong **[000, 100]**.

Ví dụ: `25127001_HW02_AI_DomainTesting_090.zip`.

Các nội dung bắt buộc trong ZIP:

- Báo cáo chính (**Markdown + PDF**), bao gồm báo cáo Domain Testing và Boundary Value Analysis.
- Báo cáo bug, kèm ảnh chụp bug trên trang GitHub Issues.
- AI Critique và AI Audit Report (**Markdown + PDF**).
- Lịch sử Git commit (tệp văn bản).
- `README.md` gồm bảng tự đánh giá ở §15 và báo cáo tổng kết kiểm thử: số chức năng; số test case đã thiết kế, đã thực thi, đạt, không đạt và chưa thực thi; số bug; video minh họa.
- Các tài liệu hỗ trợ khác.

Nộp lên Moodle. Hạn nộp xem tại liên kết nộp bài.

## 15. Bảng tự đánh giá

| No. | Criterion | Maximum Score | Self-Assessed Score |
|---|---|---:|---|
| 1 | Chức năng A – Kiểm thử miền và giá trị biên | 25 | |
| 2 | Chức năng B – Kiểm thử miền và giá trị biên | 25 | |
| 3 | Chức năng C – Kiểm thử miền và giá trị biên | 25 | |
| 4 | Chức năng D – Mobile, kiểm thử miền và giá trị biên | 15 | |
| 5 | Agent Skills | 10 | |
| | Tổng | 100 | |

## 16. Tài liệu tham khảo

- ISTQB Foundation Level Syllabus (phiên bản mới nhất).
- Hardman, P. (2025). *A Post-AI Learning Taxonomy*.
- Fuster Rabella, M. (2025). *OECD Education Working Paper No. 338*.
- Anthropic (2025). *Building Reliable AI Test Agents* – bài viết kỹ thuật.
- Tài liệu DeepEval và Promptfoo – các framework kiểm thử LLM.

## 17. Quy định khác

- Không cho phép nộp trễ.
- Thiếu bất kỳ tài liệu bắt buộc nào sẽ bị 0 điểm.
- Sao chép giữa sinh viên, **kể cả prompt**, khiến cả hai bên bị 0 điểm.

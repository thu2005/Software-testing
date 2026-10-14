# Mẫu tài liệu HW02

Tiêu đề cột bảng dùng tiếng Anh; tiêu đề mục, giải thích và nội dung điền dùng tiếng Việt có dấu. Giữ nguyên ID, tên trường, dữ liệu, thông báo hệ thống và transcript gốc.

Chỉ đọc mẫu cần cho loại tệp đang tạo. Thay các phần `<...>` bằng thông tin thật; nếu thiếu thì ghi rõ, không điền kết quả giả. Chỉnh số cột đầu vào theo chức năng nhưng giữ tiêu đề cột tiếng Anh.

Mọi đường dẫn đầu ra dưới đây tính từ `HW02/`. Với FR-06 trên Mobile, dùng mã tệp `FR-06-MOBILE` và truy vết về FR-06 trong đặc tả.

| Artifact | Template | Skill / Stage | Output |
|---|---|---|---|
| Đặc tả chức năng | [requirement-template.md](requirement-template.md) | Đọc và ghi nhận yêu cầu | `requirements/<FEATURE-ID>-<feature-name>.md` |
| Phân tích miền | [domain-testing-analysis-template.md](domain-testing-analysis-template.md) | `$domain-testing` | `analysis/<FEATURE-ID>-<feature-name>/domain-testing-analysis.md` |
| Ca kiểm thử miền | [domain-testing-test-case-template.md](domain-testing-test-case-template.md) | `$domain-testing` | `tests/test-cases/<FEATURE-ID>-<feature-name>/domain-testing/TC-<FEATURE-ID>-DT-<NNN>.md` |
| Phân tích biên | [bva-analysis-template.md](bva-analysis-template.md) | `$boundary-value-analysis` | `analysis/<FEATURE-ID>-<feature-name>/bva-analysis.md` |
| Ca kiểm thử biên | [bva-test-case-template.md](bva-test-case-template.md) | `$boundary-value-analysis` | `tests/test-cases/<FEATURE-ID>-<feature-name>/bva/TC-<FEATURE-ID>-BVA-<NNN>.md` |
| Rà soát ca kiểm thử | [test-case-review-template.md](test-case-review-template.md) | `$test-case-review` | `reviews/<FEATURE-ID>-<feature-name>/<technique>-review.md` |
| Lần thực thi | [test-run-template.md](test-run-template.md) | `$test-execution` | `tests/test-runs/<FEATURE-ID>-<feature-name>-run.md` |
| Báo lỗi | [bug-report-template.md](bug-report-template.md) | `$bug-report` | `bug-reports/BUG-<FEATURE-ID>-<NNN>.md` |
| Thiếu sót AI | [ai-gap-analysis-template.md](ai-gap-analysis-template.md) | `$qa-workflow` khi có bằng chứng | `ai-gap-analysis/<FEATURE-ID>-<feature-name>.md` |
| Tương tác AI | [prompt-log-entry-template.md](prompt-log-entry-template.md) | `$prompt-log` | Nối vào `reports/prompt_log.md` |
| Báo cáo chính | [report-template.md](report-template.md) | Tổng hợp báo cáo | `reports/report.md` |
| Báo cáo kiểm toán AI | [ai-audit-report-template.md](ai-audit-report-template.md) | Tổng hợp phụ lục AI | `reports/ai-audit-report.md` |
| Đoạn phản biện AI | [ai-critique-template.md](ai-critique-template.md) | Tổng hợp báo cáo | `reports/ai-critique.md` |
| Tự đánh giá và tổng kết | [readme-template.md](readme-template.md) | Chuẩn bị bài nộp | `README.md` |
| Video minh họa | [demo-videos-template.md](demo-videos-template.md) | Chuẩn bị bài nộp | `reports/demo-videos.md` |

PDF được xuất từ báo cáo Markdown đã điền; không cần mẫu PDF riêng. Git log xuất trực tiếp từ lịch sử thật vào `reports/git_log.txt`. Ảnh, video và URL issue phải lấy từ thực tế, không sinh từ mẫu.

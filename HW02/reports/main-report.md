# Báo cáo tổng kết HW02 — AI-Assisted Domain Testing

## 1. Thông tin bài làm

- Sinh viên: Nguyễn Đoàn Xuân Thu
- MSSV: 23120170
- Repository bài làm và evidence: `thu2005/Software-testing`
- Repository SUT và GitHub Issues: `thu2005/CSC13003_eshop`
- Build/commit SUT được kiểm thử: `85af3ba875c88283615e22cb108f13e2fccaf0e9`
- Test basis: [`system-requirements.md`](../requirements/system-requirements.md), [`api-specification.md`](../requirements/api-specification.md) và [`hw02-assignment.md`](../requirements/hw02-assignment.md)

## 2. Phạm vi và phương pháp

Bài làm chọn một chức năng từ mỗi pool:

| Pool | Feature | Nền tảng |
|---|---|---|
| A | FR-01 — Đăng ký | Web |
| B | FR-07 — Giỏ hàng | Web |
| C | FR-14 — Quản lý danh mục | Web Admin |
| D | FR-06 — Xem chi tiết sản phẩm | Mobile |

Quy trình áp dụng cho mỗi feature gồm: đọc test basis, xác định input domain và equivalence partitions, chọn boundary values, tạo test case đại diện, review DT/BVA, thực thi trên SUT, lưu evidence, nhóm các lỗi cùng nguyên nhân vào bug report và phân tích gap của phần do AI hỗ trợ. AI được dùng để tạo draft và cấu trúc; sinh viên kiểm tra oracle, quyết định verdict và yêu cầu hiệu chỉnh khi đầu ra chưa phù hợp.

## 3. Tổng quan kết quả

| Feature | DT | BVA | Tổng thiết kế | Pass | Fail | Blocked | Bug riêng biệt |
|---|---:|---:|---:|---:|---:|---:|---:|
| FR-01 Web | 8 | 7 | 15 | 8 | 4 | 3 | 4 |
| FR-07 Web | 8 | 3 | 11 | 1 | 10 | 0 | 6 |
| FR-14 Web Admin | 8 | 3 | 11 | 6 | 5 | 0 | 5 |
| FR-06 Mobile | 8 | 3 | 11 | 1 | 10 | 0 | 6 |
| **Tổng** | **32** | **16** | **48** | **16** | **29** | **3** | **21** |

Cả 48 test case đều được đưa vào test run; 45 ca có verdict Pass/Fail và 3 ca FR-01 bị Blocked do giao diện thiếu trường xác nhận mật khẩu cần thiết cho oracle tương ứng.

## 4. FR-01 — Đăng ký Web

- Phân tích: [`domain-testing-analysis.md`](../analysis/FR-01-dang-ky/domain-testing-analysis.md), [`bva-analysis.md`](../analysis/FR-01-dang-ky/bva-analysis.md)
- Test case: [`tests/test-cases/FR-01-dang-ky/`](../tests/test-cases/FR-01-dang-ky/)
- Review: [`dt-bva-review.md`](../reviews/FR-01-dang-ky/dt-bva-review.md)
- Kết quả: [`FR-01-dang-ky-run.md`](../tests/test-runs/FR-01-dang-ky-run.md)
- Bug report: [`BUG-FR01-001.md`](../bug-reports/BUG-FR01-001.md) đến [`BUG-FR01-004.md`](../bug-reports/BUG-FR01-004.md)

Các miền chính gồm họ tên, email, mật khẩu, xác nhận mật khẩu và trạng thái form. BVA tập trung vào độ dài mật khẩu 7/8/9 và số lượng thành phần xác nhận mật khẩu 0/1. Kết quả là 8 Pass, 4 Fail và 3 Blocked. Các defect chính liên quan đến validation mật khẩu hợp lệ, thiếu trường xác nhận mật khẩu, dấu bắt buộc và kiểu input email. Bộ 33 ca ban đầu đã được human review, loại kết hợp dư thừa và rút còn 15 ca đại diện.

Môi trường: Chrome `155.0.8059.40`, Windows `10.0.26100.0`, frontend `http://127.0.0.1:5174/register`, API `http://localhost:3000`.

## 5. FR-07 — Giỏ hàng Web

- Phân tích: [`domain-testing-analysis.md`](../analysis/FR-07-gio-hang/domain-testing-analysis.md), [`bva-analysis.md`](../analysis/FR-07-gio-hang/bva-analysis.md)
- Test case: [`tests/test-cases/FR-07-gio-hang/`](../tests/test-cases/FR-07-gio-hang/)
- Review: [`dt-bva-review.md`](../reviews/FR-07-gio-hang/dt-bva-review.md)
- Kết quả: [`FR-07-gio-hang-run.md`](../tests/test-runs/FR-07-gio-hang-run.md)
- Bug report: [`BUG-FR07-001.md`](../bug-reports/BUG-FR07-001.md) đến [`BUG-FR07-006.md`](../bug-reports/BUG-FR07-006.md)

Bộ test bao phủ cấu trúc giỏ hàng, thêm trùng sản phẩm, điều khiển tăng/giảm, xóa và hộp thoại xác nhận, tiếp tục mua hàng và trạng thái giỏ trống. BVA kiểm tra số dòng giỏ hàng 0/1/2. Kết quả là 1 Pass và 10 Fail, được nhóm thành 6 defect. Gap analysis xác định bộ ban đầu chưa nối đầy đủ yêu cầu giao diện dùng chung FR-21/FR-23 và TC-FR-07-DT-007 chưa cố định trạng thái giỏ; các điểm này được công khai như coverage gap, không bị biến thành defect khi chưa có execution oracle.

Môi trường: Chrome `155.0.8059.40`, Windows, frontend `http://127.0.0.1:5174`, SUT commit `85af3ba875c88283615e22cb108f13e2fccaf0e9`.

## 6. FR-14 — Quản lý danh mục Web Admin

- Phân tích: [`domain-testing-analysis.md`](../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md), [`bva-analysis.md`](../analysis/FR-14-quan-ly-danh-muc/bva-analysis.md)
- Test case: [`tests/test-cases/FR-14-quan-ly-danh-muc/`](../tests/test-cases/FR-14-quan-ly-danh-muc/)
- Review: [`dt-bva-review.md`](../reviews/FR-14-quan-ly-danh-muc/dt-bva-review.md)
- Kết quả: [`FR-14-quan-ly-danh-muc-run.md`](../tests/test-runs/FR-14-quan-ly-danh-muc-run.md)
- Bug report: [`BUG-FR14-001.md`](../bug-reports/BUG-FR14-001.md) đến [`BUG-FR14-005.md`](../bug-reports/BUG-FR14-005.md)

Bộ test bao phủ thêm, xem và xóa danh mục, vai trò truy cập, yêu cầu UI/tiếng Việt, Tab Order và biên độ dài tên 0/1/2. Kết quả là 6 Pass và 5 Fail, tương ứng 5 defect. Rủi ro nổi bật là tài khoản user thường vẫn có thể gọi API xóa danh mục và nhận HTTP 200. Gap analysis còn phát hiện chuỗi `Admin Login`/`Login` trên evidence của ca chặn truy cập; biểu hiện này được bổ sung vào defect ngôn ngữ, trong khi verdict Pass của oracle phân quyền được giữ nguyên.

Môi trường: Chrome `155.0.8059.80`, Windows `10.0.26100.0`, viewport `1440 × 1000`, Playwright `1.64.0`, frontend `http://127.0.0.1:5174`, API `http://127.0.0.1:3000`.

## 7. FR-06 — Xem chi tiết sản phẩm Mobile

- Phân tích: [`domain-testing-analysis.md`](../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md), [`bva-analysis.md`](../analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/bva-analysis.md)
- Test case: [`tests/test-cases/FR-06-MOBILE-xem-chi-tiet-san-pham/`](../tests/test-cases/FR-06-MOBILE-xem-chi-tiet-san-pham/)
- Review: [`dt-bva-review.md`](../reviews/FR-06-MOBILE-xem-chi-tiet-san-pham/dt-bva-review.md)
- Kết quả: [`FR-06-MOBILE-xem-chi-tiet-san-pham-run.md`](../tests/test-runs/FR-06-MOBILE-xem-chi-tiet-san-pham-run.md)
- Bug report: [`BUG-FR06-001.md`](../bug-reports/BUG-FR06-001.md) đến [`BUG-FR06-006.md`](../bug-reports/BUG-FR06-006.md)

Bộ test bao phủ dữ liệu chi tiết sản phẩm, UI/accessibility, trường số lượng, phản hồi thêm vào giỏ và biên số lượng 0/1/2. Kết quả là 1 Pass và 10 Fail, được nhóm thành 6 defect. Gap analysis sau thực thi không xác nhận thêm coverage gap có căn cứ; các quan sát ngoài oracle như safe area không được tự động ghi thành bug.

Môi trường: Android Emulator Pixel 4a (`sdk_gphone64_x86_64`), Android 13 API 33, độ phân giải `1080 × 2340`, Expo Go/SDK 54.

## 8. Review và mức sẵn sàng

| Feature | Kết quả review trước chạy | Điều chỉnh/ghi nhận sau chạy |
|---|---|---|
| FR-01 | Bộ test ban đầu quá lớn | Rút từ 33 xuống 15 ca đại diện |
| FR-07 | Bao phủ nghiệp vụ giỏ hàng | Ghi nhận thiếu liên kết FR-21/FR-23 và state ambiguity ở DT-007 |
| FR-14 | Bao phủ CRUD, phân quyền và UI | Bổ sung biểu hiện ngôn ngữ vào BUG-FR14-002 |
| FR-06 Mobile | Bộ 11 ca có thể thực thi | Không có gap mới đủ căn cứ |

Các review đều có file riêng và dùng requirement làm oracle. Evidence Pass nằm trong [`tests/test-runs/screenshots/`](../tests/test-runs/screenshots/); evidence Fail và ảnh GitHub issue nằm trong [`bug-reports/screenshots/`](../bug-reports/screenshots/).

## 9. Traceability

| Feature | Requirement | Analysis | Test design | Execution | Defect |
|---|---|---|---|---|---|
| FR-01 | FR-01 và yêu cầu UI liên quan | 2 analysis | 15 test case | 15 dòng kết quả | 4 bug / Issues #1–#4 |
| FR-07 | FR-07; gap tham chiếu FR-21/FR-23 | 2 analysis | 11 test case | 11 dòng kết quả | 6 bug / Issues #5–#10 |
| FR-14 | FR-14 và yêu cầu UI/ngôn ngữ | 2 analysis | 11 test case | 11 dòng kết quả | 5 bug / Issues #11–#15 |
| FR-06 Mobile | FR-06 Mobile | 2 analysis | 11 test case | 11 dòng kết quả | 6 bug / Issues #16–#21 |

Mỗi bug report liên kết test case liên quan, actual result, screenshot và GitHub issue. Các issue dùng nhãn `bug` và evidence được trỏ tới repository public để có thể kiểm chứng độc lập.

## 10. AI gap analysis và phản biện

Gap analysis hợp nhất nằm tại [`HW02-ai-gap-analysis.md`](../ai-gap-analysis/HW02-ai-gap-analysis.md). Kết quả chính là: FR-01 và FR-06 không có gap mới đủ căn cứ; FR-07 có thiếu coverage đối với yêu cầu giao diện dùng chung và ambiguity về state; FR-14 bỏ sót một biểu hiện ngôn ngữ nhưng không làm đổi oracle phân quyền của test Pass.

Phần đánh giá việc sử dụng AI được trình bày tại [`ai-audit-report.md`](ai-audit-report.md) và [`ai-critique.md`](ai-critique.md). Prompt đầy đủ được giữ trong [`prompt_log.md`](prompt_log.md); audit chỉ tính những lần AI sinh nguyên artifact, không tính lượt chỉ sửa.

## 11. Requirement gap và giới hạn

- Một số tiêu chí UI/accessibility chưa có metric hoặc công cụ đo định lượng trong test basis; kết luận chỉ được đưa ra khi expected result đủ rõ và có evidence trực tiếp.
- Trạng thái dữ liệu cần được cố định rõ hơn trong các ca phụ thuộc giỏ hàng, đặc biệt TC-FR-07-DT-007.
- Các trường hợp bị Blocked không được đổi thành Fail nếu thành phần cần kiểm thử không tồn tại để thực hiện đúng oracle.
## 12. Kết luận

Bài làm đã hoàn thành thiết kế và thực thi 48 test case cho bốn pool, thu được 16 Pass, 29 Fail và 3 Blocked; 29 ca Fail được quản lý trong 21 defect không trùng lặp. Mỗi feature có analysis, test case, review, test run và evidence; mọi defect có bug report và GitHub issue. Human review đã phát hiện và kiểm soát các hạn chế quan trọng của đầu ra AI, gồm over-generation, bỏ sót requirement dùng chung, ambiguity của trạng thái test và nguy cơ suy diễn ngoài oracle.

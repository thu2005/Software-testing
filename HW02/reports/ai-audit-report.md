# Báo cáo kiểm toán nội dung do AI tạo

## 1. Thông tin

- Sinh viên: Nguyễn Đoàn Xuân Thu
- MSSV: 23120170
- Nguồn kiểm toán: [`prompt_log.md`](prompt_log.md)
- Phạm vi: chỉ các lần AI tạo mới nguyên artifact và có ghi nhận trong prompt log.
- Loại trừ: các lượt chỉ review, sửa, rút gọn, bổ sung evidence, cập nhật issue hoặc phân tích gap. Những lượt này được nêu ở mục “Hiệu chỉnh của sinh viên” khi cần, nhưng không được tính là một artifact AI-generated riêng.

## 2. Phương pháp đánh giá

Mỗi artifact được đối chiếu với đặc tả, yêu cầu bài tập, test basis và bằng chứng thực thi. Verdict được dùng như sau:

- **VALID**: đầu ra phù hợp mục tiêu và không có thiếu sót trọng yếu đã biết.
- **INCOMPLETE**: có phần dùng được nhưng cần con người sửa hoặc bổ sung trước khi nộp.
- **INVALID**: không thể dùng vì sai test basis, sai kết luận hoặc không đáp ứng mục tiêu.

Mỗi liên kết tương tác bên dưới trỏ tới bản ghi nguồn trong [`prompt_log.md`](prompt_log.md), nơi lưu tên công cụ/model, ngày giờ khả dụng, prompt của sinh viên và output của AI. Báo cáo này chỉ đánh giá artifact, không sao chép lại transcript.

## 3. Kết quả kiểm toán

### A01 — Bộ kỹ năng hỗ trợ HW02

1. **Bản ghi nguồn:** [Tương tác 01](prompt_log.md#tương-tác-ai---session-hiện-tại--01) yêu cầu tạo các skill phục vụ quy trình HW02 từ requirement đến test design, execution, review và báo cáo; công cụ AI tạo file trong `.agents/skills/`.
2. **AI output:** Bộ skill ban đầu gồm chín skill và các tệp hướng dẫn liên quan.
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Bộ ban đầu có ích nhưng còn phân mảnh và chưa bám hoàn toàn cấu trúc artifact cuối cùng. Các skill sau đó phải được chuẩn hóa và gom lại để quy trình nhất quán hơn.
5. **Hiệu chỉnh của sinh viên:** Ở các tương tác 02–03, sinh viên yêu cầu chỉnh sửa, rút còn bảy skill và bổ sung checklist/template routing. Các lượt này là sửa artifact nên không được audit thành mục độc lập.

### A02 — Đặc tả yêu cầu bài tập

1. **Bản ghi nguồn:** [Tương tác 04](prompt_log.md#tương-tác-ai---session-hiện-tại--04) yêu cầu đọc đề, xác định phạm vi bốn pool và tạo requirement Markdown dùng làm test basis.
2. **AI output:** [`requirements/hw02-assignment.md`](../requirements/hw02-assignment.md).
3. **Verdict:** **VALID**.
4. **Lý do:** Tài liệu thể hiện đúng các deliverable chính, quy tắc chọn một feature mỗi pool, yêu cầu test design, execution, review, AI gap analysis và báo cáo cuối.
5. **Hiệu chỉnh của sinh viên:** Sinh viên kiểm tra lại phạm vi và dùng các tài liệu này làm nguồn điều phối; không phát hiện sai lệch trọng yếu.

### A03 — Bộ template HW02

1. **Bản ghi nguồn:** [Tương tác 05](prompt_log.md#tương-tác-ai---session-hiện-tại--05) yêu cầu sinh toàn bộ template còn thiếu cho analysis, test case, review, test run, bug report và báo cáo.
2. **AI output:** Mười lăm template trong [`templates/`](../templates/).
3. **Verdict:** **VALID**.
4. **Lý do:** Các template tạo cấu trúc thống nhất cho input domain, equivalence partition, boundary, expected result, traceability, evidence và defect reporting; phù hợp mục đích kiểm soát chất lượng artifact.
5. **Hiệu chỉnh của sinh viên:** Không có sửa chữa nội dung trọng yếu được ghi nhận cho chính bộ template.

### A04 — Kế hoạch thực hiện

1. **Bản ghi nguồn:** [Tương tác 07](prompt_log.md#tương-tác-ai---session-hiện-tại--07) yêu cầu tạo work plan cho toàn bộ bài HW02.
2. **AI output:** [`work-plan.md`](work-plan.md).
3. **Verdict:** **VALID**.
4. **Lý do:** Kế hoạch bao quát bốn feature, các bước phân tích miền, BVA, review, execution, bug reporting, gap analysis và final reporting; thứ tự công việc hỗ trợ traceability từ requirement đến evidence.
5. **Hiệu chỉnh của sinh viên:** Việc thực thi thực tế được cập nhật theo từng feature, không làm thay đổi mục tiêu cốt lõi của kế hoạch.

### A05 — Thiết kế kiểm thử ban đầu cho FR-01

1. **Bản ghi nguồn:** [Tương tác 08](prompt_log.md#tương-tác-ai---session-hiện-tại--08) yêu cầu phân tích Domain Testing/BVA và sinh test case cho FR-01 Đăng ký Web.
2. **AI output:** Hai file analysis và bộ 33 test case ban đầu.
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Test basis và các miền dữ liệu chính được nhận diện, nhưng số ca bị phình do kết hợp nhiều điều kiện, gần với kiểm thử tổ hợp hơn là chọn đại diện lớp tương đương và biên. Điều này làm giảm tính tối thiểu và khả thi của bộ test.
5. **Hiệu chỉnh của sinh viên:** [Tương tác 09](prompt_log.md#tương-tác-ai---session-hiện-tại--09) và [Tương tác 10](prompt_log.md#tương-tác-ai---session-hiện-tại--10) yêu cầu rút gọn và review; bộ cuối còn 15 test case, gồm 8 DT và 7 BVA.

### A06 — Review DT/BVA cho FR-01

1. **Bản ghi nguồn:** [Tương tác 10](prompt_log.md#tương-tác-ai---session-hiện-tại--10) yêu cầu review bộ FR-01 sau khi rút gọn.
2. **AI output:** [`reviews/FR-01-dang-ky/dt-bva-review.md`](../reviews/FR-01-dang-ky/dt-bva-review.md).
3. **Verdict:** **VALID**.
4. **Lý do:** Review kiểm tra coverage, overlap, expected result và tính thực thi của bộ đã tinh gọn; kết quả phù hợp với cấu trúc 8 DT + 7 BVA cuối cùng.
5. **Hiệu chỉnh của sinh viên:** Không ghi nhận lỗi trọng yếu sau review.

### A07 — Test run FR-01

1. **Bản ghi nguồn:** [Tương tác 12](prompt_log.md#tương-tác-ai---session-hiện-tại--12) cung cấp bảng kết quả thực thi và yêu cầu tạo test-run cho FR-01.
2. **AI output:** [`tests/test-runs/FR-01-dang-ky-run.md`](../tests/test-runs/FR-01-dang-ky-run.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** AI tổng hợp đúng Pass/Fail/Blocked từ dữ liệu người dùng cung cấp, nhưng bản tạo đầu chưa có đầy đủ browser, OS, URL, build và evidence theo yêu cầu nộp bài.
5. **Hiệu chỉnh của sinh viên:** Các lượt sau bổ sung môi trường, ảnh Pass/Fail và liên kết issue. Kết quả cuối là 8 Pass, 4 Fail, 3 Blocked.

### A08 — Bốn bug report FR-01

1. **Bản ghi nguồn:** [Tương tác 13](prompt_log.md#tương-tác-ai---session-hiện-tại--13) yêu cầu tạo bug report từ các lỗi đã xác nhận khi chạy FR-01.
2. **AI output:** [`BUG-FR01-001.md`](../bug-reports/BUG-FR01-001.md) đến [`BUG-FR01-004.md`](../bug-reports/BUG-FR01-004.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Các ca có cùng nguyên nhân/triệu chứng được nhóm hợp lý thành bốn defect và report có bước tái hiện, expected/actual cùng evidence. Tuy nhiên, bản tạo đầu vẫn thiếu browser/OS/URL/build và GitHub issue URL theo yêu cầu nộp bài.
5. **Hiệu chỉnh của sinh viên:** Bổ sung môi trường thực thi, URL và ảnh chụp GitHub Issues #1–#4 sau khi kết nối tài khoản `thu2005`.

### A09 — Thiết kế và review FR-07

1. **Bản ghi nguồn:** [Tương tác 17](prompt_log.md#tương-tác-ai---session-hiện-tại--17) yêu cầu tạo analysis, test case và review cho FR-07 Giỏ hàng Web.
2. **AI output:** Hai file analysis, 11 test case và [`reviews/FR-07-gio-hang/dt-bva-review.md`](../reviews/FR-07-gio-hang/dt-bva-review.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Bộ test bao phủ hành vi giỏ hàng cốt lõi và biên số dòng 0/1/2, nhưng AI thu hẹp theo FR-07 nên chưa chủ động nối các yêu cầu giao diện dùng chung FR-21/FR-23. Ngoài ra, TC-DT-007 chưa cố định rõ trạng thái giỏ hàng, nên bằng chứng Pass chỉ chứng minh nhánh giỏ trống.
5. **Hiệu chỉnh của sinh viên:** Gap được ghi tại [`ai-gap-analysis/HW02-ai-gap-analysis.md`](../ai-gap-analysis/HW02-ai-gap-analysis.md); không đổi kết quả đã chạy và không suy diễn thêm defect từ ảnh ngoài oracle.

### A10 — Test run và sáu bug report FR-07

1. **Bản ghi nguồn:** [Tương tác 18](prompt_log.md#tương-tác-ai---session-hiện-tại--18) yêu cầu thực thi/tổng hợp FR-07, lưu evidence và tạo bug report cho lỗi đã quan sát.
2. **AI output:** [`tests/test-runs/FR-07-gio-hang-run.md`](../tests/test-runs/FR-07-gio-hang-run.md) và [`BUG-FR07-001.md`](../bug-reports/BUG-FR07-001.md) đến [`BUG-FR07-006.md`](../bug-reports/BUG-FR07-006.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Nội dung local phản ánh đúng 1 Pass và 10 Fail, nhưng tại thời điểm tạo, GitHub issue/evidence trang issue chưa hoàn tất do chưa có kết nối phù hợp.
5. **Hiệu chỉnh của sinh viên:** Sau khi kết nối GitHub, sinh viên yêu cầu tạo Issues #5–#10, gắn nhãn `bug`, lưu screenshot và cập nhật evidence.

### A11 — Thiết kế và review FR-14

1. **Bản ghi nguồn:** [Tương tác 21](prompt_log.md#tương-tác-ai---session-hiện-tại--21) yêu cầu tạo analysis, test case và review cho FR-14 Quản lý danh mục Web Admin.
2. **AI output:** Hai file analysis, 11 test case và [`reviews/FR-14-quan-ly-danh-muc/dt-bva-review.md`](../reviews/FR-14-quan-ly-danh-muc/dt-bva-review.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Bộ test bao phủ CRUD, phân quyền, UI và biên độ dài tên 0/1/2, nhưng review ban đầu bỏ sót biểu hiện ngôn ngữ tiếng Anh `Admin Login`/`Login` trên trạng thái đầu ra của ca kiểm soát truy cập.
5. **Hiệu chỉnh của sinh viên:** [Tương tác 23](prompt_log.md#tương-tác-ai---session-hiện-tại--23) mở rộng BUG-FR14-002/Issue #12 để ghi nhận biểu hiện này; verdict chức năng của TC-FR-14-DT-007 vẫn là Pass vì oracle chính là chặn truy cập.

### A12 — Test run và năm bug report FR-14

1. **Bản ghi nguồn:** [Tương tác 22](prompt_log.md#tương-tác-ai---session-hiện-tại--22) yêu cầu tổng hợp kết quả thực thi FR-14 và tạo bug report.
2. **AI output:** [`tests/test-runs/FR-14-quan-ly-danh-muc-run.md`](../tests/test-runs/FR-14-quan-ly-danh-muc-run.md) và [`BUG-FR14-001.md`](../bug-reports/BUG-FR14-001.md) đến [`BUG-FR14-005.md`](../bug-reports/BUG-FR14-005.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Kết quả 6 Pass/5 Fail và năm defect được tổng hợp đúng, nhưng BUG-FR14-002 ban đầu chưa mô tả hết các chuỗi tiếng Anh có trong evidence; thông tin môi trường và issue evidence cũng được hoàn thiện ở lượt sau.
5. **Hiệu chỉnh của sinh viên:** Bổ sung môi trường thực thi, cập nhật BUG-FR14-002 và Issues #11–#15 cùng ảnh trang issue.

### A13 — Thiết kế và review FR-06 Mobile

1. **Bản ghi nguồn:** [Tương tác 24](prompt_log.md#tương-tác-ai---session-hiện-tại--24) yêu cầu tạo analysis, test case và review cho FR-06 Xem chi tiết sản phẩm trên Mobile.
2. **AI output:** Hai file analysis, 11 test case và [`reviews/FR-06-MOBILE-xem-chi-tiet-san-pham/dt-bva-review.md`](../reviews/FR-06-MOBILE-xem-chi-tiet-san-pham/dt-bva-review.md).
3. **Verdict:** **VALID**.
4. **Lý do:** Bộ test bao phủ dữ liệu chi tiết sản phẩm, trạng thái UI, accessibility, nhập số lượng, phản hồi thêm giỏ hàng và biên số lượng 0/1/2. Phân tích gap sau thực thi không xác nhận thiếu sót có căn cứ nào cần bổ sung.
5. **Hiệu chỉnh của sinh viên:** Không bổ sung test case sau gap analysis; các quan sát không có oracle trực tiếp như safe area không bị tự động nâng thành defect.

### A14 — Test run và sáu bug report FR-06 Mobile

1. **Bản ghi nguồn:** [Tương tác 25](prompt_log.md#tương-tác-ai---session-hiện-tại--25) yêu cầu chạy/tổng hợp Mobile test, chụp evidence và tạo bug report cho lỗi được xác nhận.
2. **AI output:** [`tests/test-runs/FR-06-MOBILE-xem-chi-tiet-san-pham-run.md`](../tests/test-runs/FR-06-MOBILE-xem-chi-tiet-san-pham-run.md) và [`BUG-FR06-001.md`](../bug-reports/BUG-FR06-001.md) đến [`BUG-FR06-006.md`](../bug-reports/BUG-FR06-006.md).
3. **Verdict:** **INCOMPLETE**.
4. **Lý do:** Kết quả local và evidence phản ánh đúng 1 Pass/10 Fail, nhưng bản tạo đầu chưa có GitHub issue URL và screenshot trang issue.
5. **Hiệu chỉnh của sinh viên:** Tạo Issues #16–#21 với nhãn `bug`, liên kết ảnh evidence từ repository public và bổ sung screenshot trang issue vào các report.

## 4. Tổng hợp độ chính xác

| Verdict | Số artifact | Tỷ lệ |
|---|---:|---:|
| VALID | 5 | 35,7% |
| INCOMPLETE | 9 | 64,3% |
| INVALID | 0 | 0% |
| **Tổng** | **14** | **100%** |

Tỷ lệ trên đánh giá đầu ra tại thời điểm AI tạo mới, không đánh giá lại bản cuối sau khi sinh viên sửa. Vì vậy, `INCOMPLETE` không đồng nghĩa artifact cuối đang sai; nó cho thấy cần human review hoặc bằng chứng bổ sung trước khi dùng.

## 5. Kết luận

AI tạo được khung tài liệu và phần lớn nội dung kỹ thuật có thể sử dụng, nhưng thường cần con người kiểm soát độ tối thiểu của bộ test, phạm vi requirement dùng chung, giới hạn của oracle và độ đầy đủ của environment/evidence. Không có artifact nào bị xác định hoàn toàn `INVALID`; các thiếu sót đã biết đều được sửa hoặc được ghi nhận minh bạch trong gap analysis.

## 6. Công bố sử dụng AI

AI được dùng để tạo draft cho requirement nội bộ, template, kế hoạch, phân tích DT/BVA, test case, review, test-run summary và bug report. Sinh viên quyết định phạm vi, cung cấp hoặc xác nhận dữ liệu thực thi, review đầu ra, yêu cầu sửa các thiếu sót và chịu trách nhiệm về artifact cuối. Báo cáo này không tính các lượt chỉ chỉnh sửa là nội dung AI-generated độc lập.

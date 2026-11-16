# Báo cáo tổng kết HW03 — GUI & Usability Testing

## 1. Thông tin bài làm

- Sinh viên: Nguyễn Đoàn Xuân Thu
- MSSV: 23120170
- Lớp / Khoá: CQ2023/31
- Course repository: `thu2005/Software-testing`
- SUT repository và GitHub Issues: `thu2005/CSC13003_eshop`
- Build SUT được kiểm thử: `85af3ba` (`main`)

## 2. Task 1 — GUI Checklist

### 2.1. Phạm vi và phương pháp

Checklist bao phủ Product Detail (`FR-06`), Shopping Cart (`FR-07`), Checkout
(`FR-08`) và các yêu cầu GUI dùng chung `FR-21`–`FR-24`. Bốn khía cạnh được
kiểm tra là `IA-01` (general UI), `IA-02` (forms), `IA-03` (navigation) và
`IA-04` (feedback/state).

Bộ ban đầu do AI hỗ trợ thiết kế được human review, tách các item chưa nguyên
tử và bổ sung 10 gap item có giải thích. Toàn bộ 65 item sau review được thực
thi trên Google Chrome `157.0.8103.50` / Windows; chỉ item Failed có screenshot.
Các failure cùng nguyên nhân được gom thành một bug để tránh tạo issue trùng.

Artifact chi tiết:

- [GUI checklist Markdown](../checklist/gui-checklist.md)
- [GUI checklist Excel](../checklist/gui-checklist.xlsx)
- [Human gap analysis](../ai-gap-analysis/gui-checklist-gaps.md)
- [Bug reports](../bug-reports/)

### 2.2. Tổng quan kết quả

| Chỉ số | Kết quả |
|---|---:|
| Designed | 65 |
| Executed | 65 / 65 (100%) |
| Passed | 31 (47.69%) |
| Failed | 34 (52.31%) |
| Nguồn AI | 55 |
| Nguồn Human | 10 |
| Bug riêng biệt | 20 |
| GitHub Issues | 20 (`#44`–`#63`) |

### 2.3. Kết quả theo IA

| IA | Designed | Executed | Passed | Failed |
|---|---:|---:|---:|---:|
| IA-01 | 20 | 20 | 14 | 6 |
| IA-02 | 10 | 10 | 4 | 6 |
| IA-03 | 18 | 18 | 7 | 11 |
| IA-04 | 17 | 17 | 6 | 11 |
| **Tổng** | **65** | **65** | **31** | **34** |

`IA-03` và `IA-04` có tỷ lệ Failed cao nhất (cùng 11 item), tập trung ở
breadcrumb/navbar, keyboard focus, route protection, trạng thái lỗi và đồng bộ
cart/checkout.

### 2.4. Kết quả theo screen/scope

| Screen/scope ghi trong checklist | Designed | Executed | Passed | Failed |
|---|---:|---:|---:|---:|
| Product Detail | 20 | 20 | 11 | 9 |
| Shopping Cart | 18 | 18 | 4 | 14 |
| Checkout | 21 | 21 | 13 | 8 |
| Product Detail / Shopping Cart / Checkout | 4 | 4 | 2 | 2 |
| Shopping Cart / Checkout | 2 | 2 | 1 | 1 |
| **Tổng** | **65** | **65** | **31** | **34** |

Shopping Cart có tỷ lệ Failed cao nhất (14/18). Nguyên nhân nổi bật là thiếu
điều khiển tăng/giảm số lượng, thiếu focus indicator, thiếu breadcrumb và các
feedback/state bắt buộc.

### 2.5. Bug traceability

| Bug | Found by Test Case | Severity / Priority | GitHub Issue |
|---|---|---|---|
| BUG-IA-01-CART-001: Cột Đơn giá trong Cart bị ghi thành Giá | GUI-022 | Trivial / P3 | [#44](https://github.com/thu2005/CSC13003_eshop/issues/44) |
| BUG-IA-01-CART-002: Các điều khiển Cart không đạt touch target tối thiểu | GUI-061 | Minor / P2 | [#45](https://github.com/thu2005/CSC13003_eshop/issues/45) |
| BUG-IA-01-CROSS-001: Cart và Checkout không có tiêu đề h1 | GUI-021, GUI-038 | Minor / P2 | [#46](https://github.com/thu2005/CSC13003_eshop/issues/46) |
| BUG-IA-01-CROSS-002: Màu action sai chuẩn và contrast chữ trắng không đạt | GUI-056, GUI-058 | Minor / P2 | [#47](https://github.com/thu2005/CSC13003_eshop/issues/47) |
| BUG-IA-02-CART-001: Cart thiếu điều khiển tăng giảm số lượng | GUI-026, GUI-027, GUI-028, GUI-059 | Major / P1 | [#48](https://github.com/thu2005/CSC13003_eshop/issues/48) |
| BUG-IA-02-CHECKOUT-001: Tổng tiền Checkout cho phép người dùng chỉnh sửa | GUI-042 | Major / P1 | [#49](https://github.com/thu2005/CSC13003_eshop/issues/49) |
| BUG-IA-02-PRODUCT-001: Ô số lượng chấp nhận số âm, 0, số thập phân và giá trị rỗng | GUI-007, GUI-008; P06 | Major / P1 | [#50](https://github.com/thu2005/CSC13003_eshop/issues/50) |
| BUG-IA-03-CART-001: Link Tiếp tục mua sắm dùng sai nhãn | GUI-032 | Minor / P2 | [#51](https://github.com/thu2005/CSC13003_eshop/issues/51) |
| BUG-IA-03-CROSS-001: Điều khiển Product Detail và Cart không có focus indicator nhìn thấy | GUI-010, GUI-029 | Minor / P2 | [#52](https://github.com/thu2005/CSC13003_eshop/issues/52) |
| BUG-IA-03-CROSS-002: Ba trang con không có breadcrumb bắt buộc | GUI-011, GUI-030, GUI-046 | Minor / P2 | [#53](https://github.com/thu2005/CSC13003_eshop/issues/53) |
| BUG-IA-03-CROSS-003: Link Giỏ hàng không hiển thị badge số lượng | GUI-014, GUI-037 | Minor / P2 | [#54](https://github.com/thu2005/CSC13003_eshop/issues/54) |
| BUG-IA-03-CROSS-004: Navbar không highlight Cart hoặc Checkout hiện tại | GUI-031, GUI-047 | Minor / P2 | [#55](https://github.com/thu2005/CSC13003_eshop/issues/55) |
| BUG-IA-04-CART-001: Empty state của Cart không có icon hoặc hình minh họa | GUI-034 | Minor / P2 | [#56](https://github.com/thu2005/CSC13003_eshop/issues/56) |
| BUG-IA-04-CART-002: Xóa sản phẩm khỏi Cart không yêu cầu xác nhận | GUI-035 | Major / P1 | [#57](https://github.com/thu2005/CSC13003_eshop/issues/57) |
| BUG-IA-04-CART-003: Cart dùng nhãn Tổng tạm tính thay vì Tổng cộng | GUI-036 | Minor / P2 | [#58](https://github.com/thu2005/CSC13003_eshop/issues/58) |
| BUG-IA-04-CHECKOUT-001: Checkout không bảo vệ route và không xử lý session hết hạn | GUI-049, GUI-064 | Major / P1 | [#59](https://github.com/thu2005/CSC13003_eshop/issues/59) |
| BUG-IA-04-CHECKOUT-002: Coupon phần trăm tính sai số tiền giảm và thành tiền | GUI-050 | Major / P1 | [#60](https://github.com/thu2005/CSC13003_eshop/issues/60) |
| BUG-IA-04-CHECKOUT-003: Checkout thành công không xóa giỏ hàng | GUI-054 | Major / P1 | [#61](https://github.com/thu2005/CSC13003_eshop/issues/61) |
| BUG-IA-04-PRODUCT-001: Thêm vào giỏ bỏ qua click đầu và tạo dòng trùng khi thêm lại | GUI-017, GUI-018 | Major / P1 | [#62](https://github.com/thu2005/CSC13003_eshop/issues/62) |
| BUG-IA-04-PRODUCT-002: Product Detail thiếu trạng thái phục hồi cho 404 và lỗi mạng | GUI-019, GUI-020 | Minor / P2 | [#63](https://github.com/thu2005/CSC13003_eshop/issues/63) |

### 2.6. Nhận định Task 1

Tất cả item đã được execute và có traceability từ checklist đến screenshot,
Markdown bug report và GitHub Issue. Các defect Major/P1 cần ưu tiên trước khi
đánh giá lại luồng mua hàng, đặc biệt là validation số lượng, cập nhật Cart,
coupon, route protection và việc xóa Cart sau checkout.

## 3. Task 2 — Usability Evaluation

### 3.1. Phạm vi và phương pháp

Bảy participant thực hiện luồng Search (`FR-05`) → Product Detail (`FR-06`) →
Cart (`FR-07`) → Coupon (`FR-09`) → Checkout (`FR-08`) với scenario mua
AirPods Pro 2 trong ngân sách 7.000.000 ₫ và dùng `SAVE10`. Các session ngày
14/11/2026 có screen recording + audio; custom 4-item scale được thu bổ sung
ngày 15/11/2026.

Lúc 12:30 ngày 14/11/2026, trước các session chính, P00 Trần Gia Hiển — một
người riêng ngoài lớp HW03 — đã chạy pilot online. Pilot xác nhận scenario có
thể thực hiện và lỗi SUT xuất hiện đúng phạm vi cần quan sát; không phát hiện
vấn đề wording, setup hoặc timing nên scenario, ba câu phỏng vấn và procedure
không thay đổi. Custom scale chưa tồn tại tại thời điểm pilot nên không được
pilot-test. Pilot không được tính vào dữ liệu của 7 participant chính.

Instrument dùng thang 1–5 cho clarity, error recovery, speed và trust. Scale
được thiết kế ngắn do thời lượng session hạn chế; không phải SUS/UEQ-S và không
quy đổi sang thang 0–100. Ba câu phỏng vấn session thu thập clarity, nhận xét về
giá/voucher/tổng tiền và ý định sử dụng. Hai câu mở follow-up về error recovery
và speed có response riêng của P01–P07 cùng timestamp trong Response Sheet ngày
15/11/2026.

### 3.2. Protocol deviations / chronology

- `12:30 14/11/2026`: P00 pilot scenario AirPods Pro 2, ba câu phỏng vấn và
  procedure thực tế; không dùng SUS/custom scale.
- `18:53 14/11/2026`: commit M5 `b991a75` lưu AI preparation draft dùng iPhone
  15 Pro Max và SUS. Draft này không được dùng làm moderator script cho study.
- Bảy session chính dùng scenario AirPods Pro 2 và ba câu phỏng vấn thực tế.
- `15/11/2026`: custom scale và hai câu mở follow-up về error recovery/speed
  được thu theo từng participant trong Google Form, thay vì hoàn thành ngay sau
  session; instrument chưa được pilot-test.

Đây là protocol deviation không thể sửa lịch sử. Báo cáo giữ disclosure rõ,
ghi phần xác nhận đúng ngày 15/11/2026 và không dựng trích dẫn nguyên văn.

Artifact:

- [Kế hoạch usability](../usability/plan.md)
- [Danh sách participant](../usability/participants.md)
- [Bảy session record](../usability/sessions/)
- [Raw scale response](../usability/post-test-survey.md)
- [Phân tích đầy đủ](../usability/analysis.md)
- [Google Form](https://forms.gle/uCQqeNNAwXurnxqJ6)
- [Response Sheet](https://docs.google.com/spreadsheets/d/1xmAl07vqtPXbZKT35tTrBGa2BUUKQUL_t1Swt0GW-FI/edit?usp=sharing)

### 3.3. Kết quả custom scale

| Clarity | Error recovery | Speed | Trust | Mean chung |
|---:|---:|---:|---:|---:|
| 3.14 | 3.14 | 2.86 | 1.43 | 2.64 / 5 |

Task success là `7/7` (`100%`) theo xác nhận của moderator. Completion cao cho
thấy luồng cơ bản dễ hoàn tất, nhưng không đồng nghĩa trải nghiệm đúng hoặc an
toàn: trust chỉ đạt `1.43/5` và mọi participant đều gặp lỗi tổng tiền.

Trust thấp nhất và nhất quán với dữ liệu định tính: cả 7 participant đều nhận
ra lỗi tổng tiền, 6 người nói sẽ không dùng sản phẩm ở trạng thái hiện tại và
1 người không chắc sẽ dùng.

### 3.4. Finding ưu tiên

| Finding | Tần suất/evidence | Severity | Traceability |
|---|---|---|---|
| Coupon biến tổng 6 triệu thành 60 triệu | 7/7 | Major | [Issue #60](https://github.com/thu2005/CSC13003_eshop/issues/60) |
| Add to Cart thiếu feedback/badge | 5/7; hai người tạo sản phẩm trùng | Major | [#54](https://github.com/thu2005/CSC13003_eshop/issues/54), [#62](https://github.com/thu2005/CSC13003_eshop/issues/62) |
| Tổng Checkout cho phép chỉnh sửa | P03 sửa total và vẫn thanh toán thành công | Major | [Issue #49](https://github.com/thu2005/CSC13003_eshop/issues/49) |
| Quantity âm được thêm vào Cart | P06 | Major | [Issue #50](https://github.com/thu2005/CSC13003_eshop/issues/50) |
| Ảnh sản phẩm chỉ là placeholder chữ | 5/7 nhắc đến; FR-05/FR-06 yêu cầu ảnh; dedicated retest xác nhận ở listing và Product Detail | Major defect + UX issue | [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64), [bug report](../bug-reports/BUG-IA-01-PRODUCT-001.md) |

Mặc dù task success là `7/7`, sai tổng tiền và editable total vẫn là lỗi tính
toàn vẹn giao dịch nghiêm trọng. Hai finding được xếp `Major` thay vì `Blocker`
vì chúng không ngăn participant hoàn tất luồng.

### 3.5. Giới hạn

Cả 7 participant đã được xác nhận ở ngoài lớp HW03 và đều hoàn thành task.
Moderator không đưa leading hint hoặc chỉ dẫn UI. Browser được ghi ở mức cần
thiết theo session, không yêu cầu exact version. Sinh viên xác nhận bảy YouTube
evidence URL đã được mở quyền truy cập.

Hai câu mở về error recovery và speed có response riêng cùng timestamp của cả
7 participant trong Response Sheet. Phản hồi cho thấy participant nêu lỗi hoặc
tiếp tục hoàn thành luồng; về speed, họ nhìn chung đánh giá luồng nhanh, đơn giản
hoặc tương tự website mua hàng khác và không nêu bước cụ thể gây chậm. Form được
thu vào ngày hôm sau và instrument chưa được pilot-test; chronology này vẫn
được công bố.
U-05 đã có dedicated retest screenshot, bug report và GitHub Issue #64; hai ảnh
được nhúng từ repository public.

## 4. Task 3 — Cross-browser / Cross-platform

### 4.1. Platform matrix và kết quả

Toàn bộ 65 item Task 1 được chạy lại trên từng target; không dùng subset. Mỗi
failure có screenshot stamp `23120170@student.hcmus.edu.vn`, họ tên, browser/
OS/device và URL. Kết quả chi tiết nằm trong
[cross-platform report](../cross-platform/report.md).

| Platform | Executed | Passed | Failed |
|---|---:|---:|---:|
| Chrome `157.0.8103.50` / Windows | 65 | 31 | 34 |
| Firefox `160.0` / Windows | 65 | 32 | 33 |
| Chrome `109.0.5414.123` / Android 13 / Pixel_4a emulator | 65 | 31 | 34 |
| **Tổng lượt kiểm tra** | **195** | **94** | **101** |

### 4.2. Khác biệt giữa platform

Có 33 item Failed trên cả ba target và dùng lại bug report/Issue hiện có. Chỉ
một item tạo ra khác biệt:

- `GUI-029`: Firefox Passed vì browser hiển thị focus outline `3px`; Chrome
  Windows và Android Failed. Kết quả liên kết với
  [Issue #52](https://github.com/thu2005/CSC13003_eshop/issues/52).
- `GUI-002` Failed trên cả ba target với `naturalWidth=0`; đây là defect ảnh sản
  phẩm đã được liên kết với
  [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64), không phải
  một defect tương thích Android mới.

Không phát hiện defect cross-platform mới đủ cơ sở tạo GitHub Issue. Kết quả
cho thấy phần lớn failure tái hiện nhất quán, không phụ thuộc một browser duy
nhất. Android Chrome 109 là phiên bản trong AVD và không đại diện cho mọi thiết
bị/phiên bản Android.

## 5. AI usage và human review

Xem [AI Audit Report](ai-audit-report.md), [Prompt Log](prompt-log.md) và
[AI gap analysis](../ai-gap-analysis/gui-checklist-gaps.md).

## 6. Kết luận

HW03 đã hoàn thành cả ba task. Task 1 thiết kế và thực thi 65 checklist item trên
ba màn hình, đạt 31 Passed và 34 Failed; 21 defect có Markdown report, screenshot
và GitHub Issue. Task 2 thực hiện một pilot và bảy session thật; cả bảy người
hoàn thành luồng, nhưng custom scale chỉ đạt `2.64/5` và trust thấp nhất
`1.43/5`, nhất quán với lỗi nghiêm trọng về tổng tiền, coupon và feedback giỏ
hàng. Protocol deviation về thời điểm thu scale/probe được công bố thay vì sửa
lịch sử.

Task 3 chạy lại đủ 65 item trên ba target, tổng cộng 195 lượt với 94 Passed và
101 Failed. Có 33 failure chung; khác biệt duy nhất là focus outline của
`GUI-029` trên Firefox. Kết quả cho thấy các defect chính tái hiện nhất quán,
không chỉ là hiện tượng của một browser. AI được dùng để tạo draft, tự động hoá
execution và tổng hợp, nhưng mọi artifact quan trọng đều được human-review,
đối chiếu lại requirement/evidence và ghi trong AI Audit Report.

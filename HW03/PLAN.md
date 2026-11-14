# Kế hoạch thực hiện HW03 — GUI & Usability

## 1. Scope đã chốt

| Hạng mục | Phạm vi |
|---|---|
| Task 1 — GUI Checklist | Product Detail (`FR-06`), Shopping Cart (`FR-07`), Checkout (`FR-08`) |
| Primary GUI screen | Product Detail (`FR-06`) |
| Task 2 — Usability flow | Search (`FR-05`) → Product Detail (`FR-06`) → Cart (`FR-07`) → Coupon (`FR-09`) → Checkout (`FR-08`) |
| Task 3 — Cross-platform | Chạy lại toàn bộ checklist Task 1 trên ít nhất 3 platform |
| Requirement source | `../../CSC13003-eshop/README.md` (`FR-01`–`FR-24`) |

Sinh viên cần xác nhận primary screen và usability flow không trùng với thành
viên khác trong nhóm trước khi execution chính thức.

## 2. Nguyên tắc làm bài

- Một prompt giải quyết một deliverable hoặc một công việc lớn; không tách thành
  các prompt nhỏ chỉ để sửa tiêu đề, format hoặc một vài dòng.
- Checklist AI được tạo theo **3 prompt lớn, mỗi màn hình một prompt**, thay vì
  chia thành 12 prompt theo từng cặp screen × IA.
- Mọi output AI phải được sinh viên review trước khi dùng. Không tự tạo dữ liệu
  participant, observation, result, quote, screenshot hoặc bug.
- Prompt log/AI audit chỉ ghi cho những prompt thực sự tạo hoặc phân tích artifact
  chính thức của bài. Chat môi trường và chỉnh sửa nhỏ không tạo artifact không
  cần tách thành entry riêng.
- Chỉ commit theo milestone có ý nghĩa và khi sinh viên yêu cầu; không commit sau
  từng thao tác nhỏ hoặc tự động commit.
- Bug được ghi nhận ngay trong lúc execution để giữ liên kết giữa checklist item,
  screenshot, Markdown report và GitHub Issue.

## 3. Skill dùng trong bài

| Công việc | Skill chính |
|---|---|
| Thiết kế/review/execute GUI checklist | `$gui-checklist` |
| Thiết kế và phân tích usability evaluation | `$usability-evaluation` |
| Chạy lại checklist trên nhiều platform | `$cross-platform-testing` |
| Ghi nhận bug thật | `$bug-report` |
| Audit một artifact AI quan trọng | `$ai-audit-log` |

Không cần lặp danh sách skill trong từng bước dưới đây.

## 4. Trạng thái chuẩn bị

**Task 1 đã được gỡ blocker.** SUT frontend/backend trả HTTP `200`; Chrome,
Firefox, Node/npm, Python, Pillow và công cụ đọc PDF đã sẵn sàng. GitHub plugin
đã kết nối và có thể dùng để tạo Issue; GitHub CLI là phương án tùy chọn. Android
SDK có các AVD nhưng chưa khởi động device, chỉ cần xử lý trước Task 3.

Thông tin môi trường chi tiết nằm trong [README.md](README.md).

## 5. Task 1 — GUI Checklist

### M1 — Tạo initial checklist bằng AI

**Trạng thái: Hoàn thành nhưng cần sửa qua M2 — initial draft có 48 item AI và
đạt coverage, nhưng human review phát hiện item chưa nguyên tử, reclassification
và 10 gap. Audit verdict của M1: `INCOMPLETE`.**

Thực hiện 3 prompt lớn:

1. Product Detail: phân tích `FR-06` và các IA, quan sát SUT, tạo item cho
   IA-01–IA-04.
2. Shopping Cart: phân tích `FR-07` và các IA, quan sát SUT, tạo item cho
   IA-01–IA-04.
3. Checkout: phân tích `FR-08` và các IA, quan sát SUT, tạo item cho
   IA-01–IA-04.

Mỗi item phải nguyên tử, kiểm tra được, có expected result rõ ràng và
`Source=AI`. Chưa execute ở bước này; tất cả result để `Not Run`.

**Output:** `checklist/gui-checklist.md` với hơn 40 item không lặp, bao phủ đủ
IA-01–IA-04 và cả ba màn hình.

### M2 — Human review, gap analysis và quality gate

**Trạng thái: Hoàn thành — checklist có 65 item (`55 AI + 10 Human`), ID liên
tục `GUI-001`–`GUI-065`, đủ ba screen/IA và tất cả vẫn `Not Run`. Audit verdict
của M2: `VALID`.**

Review toàn bộ checklist trong một lượt lớn:

- Loại item trùng, mơ hồ, không phù hợp SUT hoặc không thể kiểm tra.
- Bổ sung item AI bỏ sót với `Source=Human`.
- Ghi lý do bỏ sót theo prompt scope, giới hạn model hoặc đặc điểm EShop.
- Xem xét accessibility, keyboard/focus, responsive, Vietnamese text, currency,
  loading/error/empty state, destructive action, RTL và dark mode khi phù hợp.

**Output:** checklist hoàn chỉnh và
`ai-gap-analysis/gui-checklist-gaps.md`.

**Gate trước execution:** hơn 40 item; ID liên tục; đủ Screen/IA/Source;
expected result kiểm tra được; tất cả còn `Not Run`.

### M3 — Baseline execution và bugs

**Trạng thái: Hoàn tất. Đã execute 65/65 item trên Chrome 157 / Windows —
31 Passed, 34 Failed; tạo 34 screenshot, 20 Markdown bug report và 20 GitHub
Issue (#44–#63), có liên kết ngược từ checklist/report.**

Chạy toàn bộ checklist trên Chrome/Windows theo thứ tự Product Detail → Shopping
Cart → Checkout.

- Mỗi item phải được thao tác thật trên SUT và đánh `Passed` hoặc `Failed`.
- Failed item phải có Notes và screenshot; Passed item không cần screenshot.
- Bug thật được tạo Markdown report và GitHub Issue ngay khi phát hiện, kèm ảnh
  và liên kết ngược về checklist item.
- Không đánh Passed dựa trên source code hoặc phỏng đoán.

**Output:** checklist đã execute, failed evidence, bug reports và GitHub Issues.

### M4 — Export và tổng hợp Task 1

- Export checklist sang Excel.
- Kiểm tra tổng designed/executed/passed/failed theo screen và IA.
- Cập nhật phần Task 1 trong `reports/main-report.md` cùng bug links.

## 6. Task 2 — Usability Evaluation

### M5 — Chuẩn bị usability study

Một prompt lớn tạo bộ tài liệu chuẩn bị cho flow đã chọn:

- Objectives và task scenario theo mục tiêu, không hướng dẫn từng click.
- Chọn SUS, UEQ-S hoặc custom scale có justification.
- Survey và probe questions tối thiểu về clarity, error recovery, speed, trust.
- Moderator script, consent và session-note structure.
- Participant table cho 7 người thật ngoài lớp; chỉ sinh viên nhập contact/profile
  thật và mask bốn chữ số giữa.

**Output:** `usability/plan.md`, survey, moderator script và participant table.

### M6 — Pilot và 7 moderated sessions

- Pilot với một người không nằm trong 7 participant chính.
- Ghi vấn đề về wording, timing hoặc procedure và cập nhật tài liệu nếu cần.
- Chạy 7 session thật; thu think-aloud observation, timestamps, task success,
  friction/errors/hesitation, quote thật, scale responses và probe answers.
- Evidence và dữ liệu session phải đến từ việc thực hiện thật, không do AI tạo.

**Output:** pilot notes và 7 session records cùng evidence.

### M7 — Phân tích và tổng hợp Task 2

Một prompt lớn dùng đúng dữ liệu 7 session để:

- Tính điểm theo instrument đã chọn và kiểm tra công thức.
- Nhóm pain points, số người bị ảnh hưởng và khả năng recovery.
- Phân biệt bug thật với systemic UX issue và xếp severity có lý do.
- Cập nhật `usability/analysis.md` và phần Task 2 trong main report.

Không suy diễn participant data, observation hoặc quote không có trong evidence.

## 7. Task 3 — Cross-Browser / Cross-Platform

### M8 — Chạy full checklist trên 3 platform

Matrix dự kiến:

1. Chrome / Windows.
2. Firefox / Windows.
3. Android Chrome trên emulator hoặc thiết bị thật.

Trên mỗi platform phải chạy **toàn bộ checklist Task 1**, không dùng subset.
Android có thể được sinh viên tự chạy theo hướng dẫn nếu việc khởi động emulator
quá nặng cho agent.

Evidence phải thể hiện browser/OS/device và localhost URL; screenshot cần overlay
student email theo yêu cầu đề. Failed item phải có ảnh và bug thật phải được liên
kết với report/GitHub Issue.

**Output:** kết quả theo platform và `cross-platform/report.md` gồm matrix,
pass/fail, khác biệt giữa platform và bug links.

## 8. Finalization

### M9 — Hoàn thiện và preflight

- Hoàn thiện main report và export PDF.
- Hoàn thiện AI Audit cho các interaction chính thức đã dùng và AI Critique
  200–300 từ dựa trên lỗi/thiếu sót thực tế của AI.
- Cập nhật README: test summary, self-assessment và demo video link.
- Quay demo Agent Skill end-to-end trên một screen hoặc flow.
- Xuất Git log từ lịch sử thật.
- Kiểm tra không còn TODO bắt buộc, link hỏng, file thiếu, dữ liệu giả hoặc
  credential; mở thử Markdown/PDF/XLSX/screenshot/video.
- Đóng gói theo tên:
  `<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip`.

## 9. Thứ tự thực hiện rút gọn

1. M1 — 3 prompt tạo initial checklist theo màn hình.
2. M2 — 1 prompt hỗ trợ human gap review và quality gate.
3. M3 — 1 lượt baseline execution, ghi bug ngay khi phát hiện.
4. M4 — Export và tổng hợp Task 1.
5. M5 — 1 prompt tạo usability preparation pack.
6. M6 — Pilot và 7 session thật.
7. M7 — 1 prompt phân tích usability data và tổng hợp Task 2.
8. M8 — Full checklist trên 3 platform và tổng hợp Task 3.
9. M9 — Audit, critique, report, demo, Git log và preflight.

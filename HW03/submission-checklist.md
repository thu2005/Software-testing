# HW03 Submission / Preflight Checklist

> Đây là checklist kiểm tra tiến độ và đóng gói, không thay thế deliverable.
> Chỉ đánh dấu `[x]` sau khi đã mở file/evidence và xác minh nội dung thật.

## 1. Phạm vi và nguồn dữ liệu

- [ ] Mọi output của HW03 nằm trong `Software-testing/HW03/`.
- [ ] Requirements được đọc từ `CSC13003-eshop/README.md` (FR-01–FR-24).
- [ ] Đã ghi primary GUI screen và usability flow; không trùng thành viên cùng nhóm.
- [ ] `README.md` có họ tên, MSSV, lớp/khoá và scope; không chứa thông tin bịa đặt.

## 2. Task 1 — GUI Checklist

- [ ] `checklist/gui-checklist.md` có ít nhất 41 item không trùng lặp.
- [ ] Bao phủ đủ `IA-01`, `IA-02`, `IA-03`, `IA-04` và phân bố hợp lý.
- [ ] Mỗi item có `Source = AI|Human`; item Human có lý do AI bỏ sót trong
      `ai-gap-analysis/gui-checklist-gaps.md`.
- [ ] Mọi item đã được thực thi thật và có `Passed` hoặc `Failed`.
- [ ] Chỉ item Failed có screenshot và Notes mô tả expected/actual rõ ràng.
- [ ] Mỗi bug thật có Markdown report, GitHub Issue và screenshot đính kèm/link hợp lệ.
- [ ] Đã export checklist sang `.xlsx` và có test summary.

## 3. Task 2 — Usability Evaluation

- [ ] Có objectives, scenario theo mục tiêu (không hướng dẫn từng click), thang
      usability chuẩn hoặc custom scale có justification, và probe questions
      về clarity, error recovery, speed, trust.
- [ ] Đã chạy pilot và ghi lại điều chỉnh.
- [ ] Có đúng 7 người tham gia thật, ngoài lớp; contact kiểm chứng được và đã mask
      bốn chữ số giữa; đã có consent phù hợp.
- [ ] Có 7 session files với thời gian, task success, observation notes, câu trả
      lời từng scale item và probe answers.
- [ ] Screen/audio recording là dữ liệu thật; audio chỉ có khi người tham gia đồng ý.
- [ ] `usability/analysis.md` tính điểm đúng, tổng hợp pain points, tách bug khỏi
      systemic design issue và xếp severity.
- [ ] TA có thể kiểm chứng người tham gia; không có tên/contact/quote/score do AI tạo.

## 4. Task 3 — Cross-browser / Cross-platform

- [ ] Toàn bộ checklist Task 1 được chạy lại trên ít nhất 3 platform hợp lệ.
- [ ] Matrix Windows ưu tiên: Chrome/Windows + Firefox/Windows + Android Chrome;
      hoặc Expo Go thay một platform.
- [ ] Nếu dùng Safari, Safari chạy trên BrowserStack/LambdaTest/Sauce Labs hoặc
      thiết bị Apple thật — không khai Safari local trên Windows.
- [ ] Nếu cloud browser truy cập localhost, local tunnel đã được bật và ghi nhận.
- [ ] Có result table theo từng checklist item cho mỗi platform.
- [ ] Evidence hiển thị browser/OS/device và localhost URL.
- [ ] Mọi screenshot có overlay họ tên và `<StudentID>@student.hcmus.edu.vn`.
- [ ] Không tái sử dụng hoặc giả lập cùng một screenshot cho nhiều platform.

## 5. AI evidence

- [ ] `reports/prompt-log.md` ghi verbatim mọi prompt/response, kể cả chat thường,
      clarification, edit nhỏ và output bị bỏ.
- [ ] `reports/ai-audit-report.md` chỉ audit prompt/task tạo hoặc review artifact
      đáng kể; mỗi entry có Tool, Model, Timestamp, Prompt, Output, Verdict,
      Reasoning và Student Fix.
- [ ] Verdict là review thật của sinh viên, không tự động gắn `VALID`.
- [ ] Summary counts/percentages trong AI Audit khớp toàn bộ entries.
- [ ] `reports/ai-critique.md` dài 200–300 từ và dựa trên lỗi/thiếu sót cụ thể.
- [ ] AI Audit Report và AI Critique đã export sang PDF.

## 6. Báo cáo, Git và demo

- [ ] `reports/main-report.md` tổng hợp Task 1–3 và đã export PDF.
- [ ] Có commit riêng cho checklist design, execution, bug logging, từng usability
      session, analysis và từng platform run; không sửa lịch sử để giả lập tiến độ.
- [ ] `git-log.txt` được tạo từ lịch sử thật và nằm trong HW03.
- [ ] Có video demo Agent Skills end-to-end trên một screen/flow và link YouTube
      trong `README.md`.
- [ ] `README.md` có self-assessment table và test summary: số screen/flow, số item
      designed/executed/passed/failed, số bug, số participant và demo links.

## 7. Đóng gói cuối

- [ ] Mở thử mọi Markdown/PDF/XLSX/link/screenshot/video cần nộp.
- [ ] Không có placeholder như `[TODO]`, `<...>`, dữ liệu giả hoặc credential/token.
- [ ] ZIP chứa main report MD+PDF, bug evidence, AI Audit/Critique MD+PDF, git log,
      Excel checklist + summary, usability evidence, participant table,
      cross-platform screenshots, README và supporting materials.
- [ ] Tên file đúng: `<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip`,
      trong đó grade là ba chữ số `000`–`100`.

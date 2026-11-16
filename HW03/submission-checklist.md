# HW03 Submission / Preflight Checklist

> Đây là checklist kiểm tra tiến độ và đóng gói, không thay thế deliverable.
> Chỉ đánh dấu `[x]` sau khi đã mở file/evidence và xác minh nội dung thật.

## 1. Phạm vi và nguồn dữ liệu

- [x] Mọi output của HW03 nằm trong `Software-testing/HW03/`.
- [x] Requirements được đọc từ `CSC13003-eshop/README.md` (FR-01–FR-24).
- [x] Đã ghi primary GUI screen và usability flow; không trùng thành viên cùng nhóm.
- [x] `README.md` có họ tên, MSSV, trạng thái lớp/khoá và scope; không chứa thông tin bịa đặt.

## 2. Task 1 — GUI Checklist

- [x] `checklist/gui-checklist.md` có ít nhất 41 item không trùng lặp.
- [x] Bao phủ đủ `IA-01`, `IA-02`, `IA-03`, `IA-04` và phân bố hợp lý.
- [x] Mỗi item có `Source = AI|Human`; item Human có lý do AI bỏ sót trong
      `ai-gap-analysis/gui-checklist-gaps.md`.
- [x] Mọi item đã được thực thi thật và có `Passed` hoặc `Failed`.
- [x] Chỉ item Failed có screenshot và Notes mô tả expected/actual rõ ràng.
- [x] Mỗi bug thật có Markdown report, GitHub Issue và screenshot đính kèm/link hợp lệ.
- [x] Đã export checklist sang `.xlsx` và có test summary.

## 3. Task 2 — Usability Evaluation

- [x] Có objectives, scenario theo mục tiêu (không hướng dẫn từng click), thang
      usability chuẩn hoặc custom scale có justification, và probe questions
      về clarity, error recovery, speed, trust.
- [x] Đã chạy pilot và ghi lại điều chỉnh.
- [x] Có đúng 7 người tham gia thật, ngoài lớp; contact kiểm chứng được và đã mask
      bốn chữ số giữa; đã có consent phù hợp.
- [x] Có 7 session files với thời gian, task success, observation notes, câu trả
      lời từng scale item và probe answers.
- [x] Screen/audio recording là dữ liệu thật; audio chỉ có khi người tham gia đồng ý.
- [x] `usability/analysis.md` tính điểm đúng, tổng hợp pain points, tách bug khỏi
      systemic design issue và xếp severity.
- [x] TA có thể kiểm chứng người tham gia; không có tên/contact/quote/score do AI tạo.

## 4. Task 3 — Cross-browser / Cross-platform

- [x] Toàn bộ checklist Task 1 được chạy lại trên ít nhất 3 platform hợp lệ.
- [x] Matrix Windows ưu tiên: Chrome/Windows + Firefox/Windows + Android Chrome;
      hoặc Expo Go thay một platform.
- [x] Nếu dùng Safari, Safari chạy trên BrowserStack/LambdaTest/Sauce Labs hoặc
      thiết bị Apple thật — không khai Safari local trên Windows.
- [x] Không dùng cloud browser; yêu cầu local tunnel không áp dụng.
- [x] Có result table theo từng checklist item cho mỗi platform.
- [x] Evidence hiển thị browser/OS/device và localhost URL.
- [x] Mọi screenshot có overlay họ tên và `23120170@student.hcmus.edu.vn`.
- [x] Không tái sử dụng hoặc giả lập cùng một screenshot cho nhiều platform.

## 5. AI evidence

- [x] `reports/prompt-log.md` ghi verbatim mọi prompt/response, kể cả chat thường,
      clarification, edit nhỏ và output bị bỏ.
- [x] `reports/ai-audit-report.md` chỉ audit prompt/task tạo hoặc review artifact
      đáng kể; mỗi entry có Tool, Model, Timestamp, Prompt, Output, Verdict,
      Reasoning và Student Fix.
- [x] Verdict là review thật của sinh viên, không tự động gắn `VALID`.
- [x] Summary counts/percentages trong AI Audit khớp toàn bộ entries.
- [x] `reports/ai-critique.md` dài 200–300 từ và dựa trên lỗi/thiếu sót cụ thể.
- [x] AI Audit Report và AI Critique đã export sang PDF.

## 6. Báo cáo, Git và demo

- [x] `reports/main-report.md` tổng hợp Task 1–3 và đã export PDF.
- [x] Có commit riêng cho checklist design, execution, bug logging, từng usability
      session, analysis và từng platform run; không sửa lịch sử để giả lập tiến độ.
- [x] `git-log.txt` được tạo từ lịch sử thật và nằm trong HW03.
- [x] Có video demo Agent Skills end-to-end trên một screen/flow và link YouTube
      trong `README.md`.
- [x] `README.md` có self-assessment table và test summary: số screen/flow, số item
      designed/executed/passed/failed, số bug, số participant và demo links.

## 7. Đóng gói cuối

- [ ] Mở thử mọi Markdown/PDF/XLSX/link/screenshot/video cần nộp.
- [ ] Không có placeholder như `[TODO]`, `<...>`, dữ liệu giả hoặc credential/token.
- [ ] ZIP chứa main report MD+PDF, bug evidence, AI Audit/Critique MD+PDF, git log,
      Excel checklist + summary, usability evidence, participant table,
      cross-platform screenshots, README và supporting materials.
- [ ] Tên file đúng: `<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip`,
      trong đó grade là ba chữ số `000`–`100`.

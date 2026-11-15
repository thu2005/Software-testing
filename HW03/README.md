# HW03 — GUI & Usability

## Thông tin sinh viên

| Trường | Giá trị |
|---|---|
| Họ và tên | Nguyễn Đoàn Xuân Thu |
| MSSV | 23120170 |
| Lớp / Khoá | TODO |
| Email sinh viên | `23120170@student.hcmus.edu.vn` |
| Ngày thực hiện | 14–15/11/2026 (usability sessions và survey bổ sung) |

Không tự động điền hoặc suy đoán thông tin cá nhân còn thiếu.

## Repository và môi trường

| Thành phần | Vị trí / Giá trị |
|---|---|
| Course repository | `Software-testing/` |
| Homework root | `Software-testing/HW03/` |
| SUT repository | `CSC13003-eshop/` |
| Requirement source | `CSC13003-eshop/README.md` (`FR-01`–`FR-24`) |
| SUT branch / commit chuẩn bị kiểm thử | `main` / `85af3ba` |
| SUT working tree tại P0.3 | Dirty từ trước: `backend/database.sqlite` modified; `backend/node_modules/` untracked. Lần khởi động xác minh đã reseed database theo logic hiện có của backend; không xoá/khôi phục các thay đổi runtime |
| Frontend Web URL | `http://localhost:5173` — HTTP `200` đã xác minh tại P0.3 |
| Backend API URL | `http://localhost:3000` — `/api/products` trả HTTP `200` tại P0.3 |

### Trạng thái môi trường P0.3

| Thành phần | Trạng thái | Việc cần làm |
|---|---|---|
| Node.js / npm | Sẵn sàng: Node `v22.16.0`, npm `10.9.2`; `C:\Program Files\nodejs` đã được thêm vào USER `PATH` | Mở terminal mới để nhận `PATH` vừa cập nhật |
| Chrome | Sẵn sàng: `157.0.8103.50` | Không |
| Firefox | Sẵn sàng: `160.0` (`C:\Program Files\Mozilla Firefox\firefox.exe`) | Không |
| Android SDK | Có ADB `36.0.0`; có AVD `Medium_Phone`, `Pixel_4a`, `Pixel_6` | Khởi động emulator hoặc kết nối điện thoại; hiện chưa có device attached |
| Python | Sẵn sàng: `3.13.5` | Không |
| PDF / watermark tooling | Sẵn sàng: `pypdf 7.0.1`, `Pillow 13.0.0`; đọc được đủ 9 trang đề bài | Không |
| GitHub | GitHub plugin đã kết nối; CLI `gh 2.103.3` đã cài nhưng chưa đăng nhập | Dùng plugin để tạo Issue; `gh auth login` chỉ cần nếu chọn dùng CLI |
| Frontend Web | Online; HTTP `200` tại `5173` | Không |
| Backend API | Online; `/api/products` trả HTTP `200` tại `3000` | Không |

## Scope

### Task 1 — GUI Checklist

Kiểm thử GUI trên ba màn hình:

| Màn hình | Functional requirement | Vai trò trong scope |
|---|---|---|
| Product Detail | `FR-06` | Xem thông tin sản phẩm, chọn số lượng và thêm vào giỏ |
| Shopping Cart | `FR-07` | Xem/cập nhật/xoá sản phẩm và chuyển sang checkout |
| Checkout | `FR-08` | Xem tóm tắt đơn hàng và hoàn tất thanh toán |

- Primary GUI screen dùng để tránh trùng scope trong nhóm: **Product Detail (`FR-06`)**.
- Checklist phải có ít nhất 41 item có ý nghĩa và bao phủ `IA-01`–`IA-04`.
- Chưa tạo hoặc thực thi checklist item tại bước khóa scope này.

### Task 2 — Usability Evaluation

Luồng end-to-end đã chọn:

`Search (FR-05) → Product Detail (FR-06) → Shopping Cart (FR-07) → Coupon (FR-09) → Checkout (FR-08)`

- Task scenario: mua `AirPods Pro 2` với ngân sách 7.000.000 ₫, áp dụng coupon
  `SAVE10`; scenario nêu mục tiêu, không chỉ dẫn từng click.
- Instrument: custom 4-item scale 1–5 đo clarity, error recovery, speed và trust;
  ba câu phỏng vấn mở được hỏi trong session.
- Đã có pilot P00 riêng và 7 người tham gia thật ngoài lớp HW03, recording,
  Google Form, raw scale response cùng task success `7/7`. Pilot diễn ra lúc
  12:30 ngày 14/11/2026; moderator không đưa leading hint hoặc chỉ dẫn UI.
- Custom scale được thu follow-up ngày 15/11/2026, không phải ngay sau từng
  session; chronology và protocol deviation được công bố trong analysis/report.
- Artifact: [study plan](usability/plan.md), [participants](usability/participants.md),
  [sessions](usability/sessions/), [analysis](usability/analysis.md).

### Task 3 — Cross-browser / Cross-platform

Chạy lại toàn bộ checklist Task 1 trên ít nhất ba platform. Matrix chính thức sẽ
được khóa tại Phase T3.1; phương án phù hợp Windows đang dự kiến là Chrome /
Windows, Firefox / Windows và Android Chrome.

## Kế hoạch

Thực hiện tuần tự theo [PLAN.md](PLAN.md) và kiểm tra trước khi nộp bằng
[submission-checklist.md](submission-checklist.md).

## Test summary

| Chỉ số | Kết quả |
|---|---:|
| Số màn hình GUI trong scope | 3 |
| Checklist items designed | 65 (`55 AI + 10 Human`) |
| Checklist items executed | 65 / 65 |
| Passed | 31 |
| Failed | 34 |
| Bugs | 21 bug reports; 21 GitHub Issues (#44–#64), gồm 20 bug Task 1 và 1 bug được xác nhận thêm từ Task 2 |
| Usability flows | 1 |
| Real participants | 7 / 7, tất cả ngoài lớp HW03 |
| Cross-platform targets completed | TODO / ≥3 |

## Demo videos

| Nội dung | Link |
|---|---|
| Agent Skill demo — complete screen/flow | TODO |

## Self-assessment

| No. | Tiêu chí | Điểm tối đa | Tự đánh giá |
|---:|---|---:|---:|
| 1 | Task 1 — GUI Checklist | 30 | TODO |
| 2 | Task 2 — Usability Evaluation | 40 | TODO |
| 3 | Task 3 — Cross-Browser / Cross-Platform | 20 | TODO |
| 4 | Agent Skills | 10 | TODO |
| | **Tổng** | **100** | **TODO** |

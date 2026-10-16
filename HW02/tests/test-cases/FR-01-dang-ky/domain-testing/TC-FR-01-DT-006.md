# TC-FR-01-DT-006: Từ chối khi Xác nhận mật khẩu không khớp

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](../../../../analysis/FR-01-dang-ky/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-CONFIRM-I02 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-006 | EC-CONFIRM-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt006@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xz | EC-RESULT-O04 | Đăng ký bị từ chối vì hai mật khẩu không khớp; không tạo tài khoản. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email của ca chưa tồn tại nếu có.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.dt006@example.com |
| Mật khẩu | Abcdef1!xy |
| Xác nhận mật khẩu | Abcdef1!xz |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập dữ liệu trong bảng; với ca UI, đồng thời quan sát nhãn và loại input.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, vị trí lỗi, điều hướng và trạng thái tài khoản.

## Kết quả mong đợi

Đăng ký bị từ chối vì hai mật khẩu không khớp; không tạo tài khoản.

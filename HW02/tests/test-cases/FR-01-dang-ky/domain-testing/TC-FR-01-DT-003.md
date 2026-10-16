# TC-FR-01-DT-003: Từ chối khi Email để trống

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](../../../../analysis/FR-01-dang-ky/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Pass / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-EMAIL-I01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-003 | EC-EMAIL-I01 | Họ Tên=Nguyễn Văn An; Email=[để trống]; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | EC-RESULT-O02 | Đăng ký bị từ chối; không chuyển tới trang Đăng nhập. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email của ca chưa tồn tại nếu có.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | [để trống] |
| Mật khẩu | Abcdef1!xy |
| Xác nhận mật khẩu | Abcdef1!xy |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng.
3. Nhấn nút đăng ký.
4. Xác nhận yêu cầu bị từ chối và trang không chuyển tới Đăng nhập.

## Kết quả mong đợi

Đăng ký bị từ chối; không chuyển tới trang Đăng nhập.

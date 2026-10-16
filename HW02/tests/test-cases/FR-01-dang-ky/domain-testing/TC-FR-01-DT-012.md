# TC-FR-01-DT-012: Từ chối khi Xác nhận mật khẩu để trống

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký tài khoản / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](../../../../analysis/FR-01-dang-ky/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-CONFIRM-I01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-012 | EC-CONFIRM-I01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt012@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=[để trống] | EC-RESULT-O02 | Đăng ký bị từ chối vì thiếu Xác nhận mật khẩu; không tạo tài khoản. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email dùng trong ca chưa tồn tại, trừ khi ca quy định khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.dt012@example.com |
| Mật khẩu | Abcdef1!xy |
| Xác nhận mật khẩu | [để trống] |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập Họ Tên `Nguyễn Văn An`, Email `fr01.dt012@example.com`, Mật khẩu `Abcdef1!xy` và Xác nhận mật khẩu `[để trống]`.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, trang hiện tại và trạng thái tài khoản.

## Kết quả mong đợi

Đăng ký bị từ chối vì thiếu Xác nhận mật khẩu; không tạo tài khoản.

# TC-FR-01-DT-004: Từ chối Email sai định dạng

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
| Lớp mục tiêu | Equivalence class | EC-EMAIL-I02 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-004 | EC-EMAIL-I02 | Họ Tên=Nguyễn Văn An; Email=user-domain.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | EC-RESULT-O02 | Đăng ký bị từ chối vì Email không có định dạng hợp lệ; không tạo tài khoản. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email dùng trong ca chưa tồn tại, trừ khi ca quy định khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | user-domain.com |
| Mật khẩu | Abcdef1!xy |
| Xác nhận mật khẩu | Abcdef1!xy |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập Họ Tên `Nguyễn Văn An`, Email `user-domain.com`, Mật khẩu `Abcdef1!xy` và Xác nhận mật khẩu `Abcdef1!xy`.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, trang hiện tại và trạng thái tài khoản.

## Kết quả mong đợi

Đăng ký bị từ chối vì Email không có định dạng hợp lệ; không tạo tài khoản.

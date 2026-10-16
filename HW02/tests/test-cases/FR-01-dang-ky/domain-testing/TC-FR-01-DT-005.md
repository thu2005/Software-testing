# TC-FR-01-DT-005: Từ chối Mật khẩu không đủ mạnh

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
| Lớp mục tiêu | Equivalence class | EC-PASSWORD-I02 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-005 | EC-PASSWORD-I02 | Họ Tên=Nguyễn Văn An; Email=fr01.dt005@example.com; Mật khẩu=abcdefgh; Xác nhận=abcdefgh | EC-RESULT-O02 | Đăng ký bị từ chối vì Mật khẩu không thỏa đầy đủ các nhóm ký tự bắt buộc; không tạo tài khoản. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email của ca chưa tồn tại nếu có.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.dt005@example.com |
| Mật khẩu | abcdefgh |
| Xác nhận mật khẩu | abcdefgh |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập dữ liệu trong bảng; với ca UI, đồng thời quan sát nhãn và loại input.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, vị trí lỗi, điều hướng và trạng thái tài khoản.

## Kết quả mong đợi

Đăng ký bị từ chối vì Mật khẩu không thỏa đầy đủ các nhóm ký tự bắt buộc; không tạo tài khoản.

# TC-FR-01-BVA-003: Kiểm tra Độ dài Mật khẩu và số chữ thường tại OFF⁺ / ON

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [bva-analysis.md](../../../../analysis/FR-01-dang-ky/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / Pending |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Độ dài Mật khẩu và số chữ thường | Độ dài ≥8 | Cận dưới | 8 ký tự | δ=1 | 7 | 8 | 9 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-01-BVA-003 | BV-PWLEN-003, BV-LOWER-ON | ABCDEF1!a (9 ký tự; đúng 1 chữ thường) | OFF⁺ / ON | Email mới; Xác nhận khớp; các nhóm không phải mục tiêu hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email `fr01.bva003@example.com` chưa tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.bva003@example.com |
| Mật khẩu | ABCDEF1!a (9 ký tự; đúng 1 chữ thường) |
| Xác nhận mật khẩu | ABCDEF1!a |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, điều hướng và trạng thái tài khoản.

## Kết quả mong đợi

Chấp nhận và chuyển tới trang Đăng nhập.

# TC-FR-01-BVA-002: Kiểm tra Độ dài và số lượng từng nhóm ký tự tại ON

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [bva-analysis.md](../../../../analysis/FR-01-dang-ky/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Độ dài và số lượng từng nhóm ký tự | Độ dài ≥8 | Cận dưới | 8 ký tự | δ=1 | 7 | 8 | 9 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-01-BVA-002 | BV-PWLEN-002, BV-GROUP-ON | Aa1!#### (8 ký tự; đúng 1 chữ hoa, 1 chữ thường, 1 số, 1 ký tự đặc biệt cho phép) | ON | Email mới; Xác nhận khớp; các nhóm không phải mục tiêu hợp lệ | Chấp nhận và chuyển tới trang Đăng nhập. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email `fr01.bva002@example.com` chưa tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.bva002@example.com |
| Mật khẩu | Aa1!#### (8 ký tự; đúng 1 chữ hoa, 1 chữ thường, 1 số, 1 ký tự đặc biệt cho phép) |
| Xác nhận mật khẩu | Aa1!#### |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, điều hướng và trạng thái tài khoản.

## Kết quả mong đợi

Chấp nhận và chuyển tới trang Đăng nhập.

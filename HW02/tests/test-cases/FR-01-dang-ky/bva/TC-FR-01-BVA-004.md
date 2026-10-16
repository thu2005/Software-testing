# TC-FR-01-BVA-004: Kiểm tra Độ dài Mật khẩu tại OFF⁻

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký tài khoản / Chức năng / Boundary Value Analysis |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [bva-analysis.md](../../../../analysis/FR-01-dang-ky/bva-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích biên

| Variable / Expression | Constraint | Boundary Type | Boundary | Step | OFF- | ON | OFF+ |
|---|---|---|---|---|---|---|---|
| Độ dài Mật khẩu | min length=8 | Cận dưới | min length=8 | δ=1 | 7 | 8 | 9 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-01-BVA-004 | BV-PWLEN-001 | Aa1!xyz (7 ký tự) | OFF⁻ | Email mới; các field khác hợp lệ; Xác nhận khớp Mật khẩu | Từ chối đăng ký vì Mật khẩu ngắn hơn 8 ký tự. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email `fr01.bva004@example.com` chưa tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.bva004@example.com |
| Mật khẩu | Aa1!xyz |
| Xác nhận mật khẩu | Aa1!xyz |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng trên.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, trang hiện tại và trạng thái tài khoản.

## Kết quả mong đợi

Từ chối đăng ký vì Mật khẩu ngắn hơn 8 ký tự.

# TC-FR-01-BVA-013: Kiểm tra Số chữ số tại OFF⁻

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
| Số chữ số | min count=1 | Cận dưới | min count=1 | δ=1 | 0 | 1 | 2 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-01-BVA-013 | BV-DIGIT-001 | Abcdef!xyz (0 chữ số) | OFF⁻ | Email mới; các field khác hợp lệ; Xác nhận khớp Mật khẩu | Từ chối đăng ký vì Mật khẩu thiếu chữ số. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email `fr01.bva013@example.com` chưa tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.bva013@example.com |
| Mật khẩu | Abcdef!xyz |
| Xác nhận mật khẩu | Abcdef!xyz |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng trên.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, trang hiện tại và trạng thái tài khoản.

## Kết quả mong đợi

Từ chối đăng ký vì Mật khẩu thiếu chữ số.

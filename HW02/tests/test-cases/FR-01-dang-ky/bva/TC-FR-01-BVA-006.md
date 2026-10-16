# TC-FR-01-BVA-006: Kiểm tra Số chữ số tại OFF⁻

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
| Số chữ số | Số lượng nhóm mục tiêu ≥1 | Cận dưới | 1 lần xuất hiện | δ=1 | 0 | 1 | 2 |

| Test Condition ID | Boundary Value ID | Test Value | Point | Other Constraints | Expected Result |
|---|---|---|---|---|---|
| COND-FR-01-BVA-006 | BV-DIGIT-001 | Abcdefg! (0 chữ số; 8 ký tự) | OFF⁻ | Email mới; Xác nhận khớp; các nhóm không phải mục tiêu hợp lệ | Từ chối vì Mật khẩu thiếu chữ số; không chuyển tới trang Đăng nhập. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email `fr01.bva006@example.com` chưa tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.bva006@example.com |
| Mật khẩu | Abcdefg! (0 chữ số; 8 ký tự) |
| Xác nhận mật khẩu | Abcdefg! |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập đúng dữ liệu trong bảng.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, điều hướng và trạng thái tài khoản.

## Kết quả mong đợi

Từ chối vì Mật khẩu thiếu chữ số; không chuyển tới trang Đăng nhập.

# TC-FR-01-DT-006: Từ chối khi Mật khẩu để trống

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
| Lớp mục tiêu | Equivalence class | EC-PASSWORD-I01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-006 | EC-PASSWORD-I01 | Họ Tên=Nguyễn Văn An; Email=fr01.dt006@example.com; Mật khẩu=[để trống]; Xác nhận=[để trống] | EC-RESULT-O02 | Đăng ký bị từ chối; không tạo tài khoản. Ca này đồng thời không thể thỏa quan hệ xác nhận do Mật khẩu bắt buộc bị thiếu. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email dùng trong ca chưa tồn tại, trừ khi ca quy định khác.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.dt006@example.com |
| Mật khẩu | [để trống] |
| Xác nhận mật khẩu | [để trống] |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Nhập Họ Tên `Nguyễn Văn An`, Email `fr01.dt006@example.com`, Mật khẩu `[để trống]` và Xác nhận mật khẩu `[để trống]`.
3. Nhấn nút đăng ký.
4. Quan sát phản hồi, trang hiện tại và trạng thái tài khoản.

## Kết quả mong đợi

Đăng ký bị từ chối; không tạo tài khoản. Ca này đồng thời không thể thỏa quan hệ xác nhận do Mật khẩu bắt buộc bị thiếu.

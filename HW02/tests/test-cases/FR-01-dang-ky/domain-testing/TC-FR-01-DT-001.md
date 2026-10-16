# TC-FR-01-DT-001: Đăng ký với dữ liệu hợp lệ

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-01 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Đăng ký / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-01-đăng-ký-tài-khoản); [domain-testing-analysis.md](../../../../analysis/FR-01-dang-ky/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / BUG-FR01-001, BUG-FR01-002, BUG-FR01-003, BUG-FR01-004 |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01, EC-FORM-V01, EC-FORM-V02, EC-FORM-V03 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-001 | EC-NAME-V01, EC-EMAIL-V01, EC-EMAILSTATE-V01, EC-PASSWORD-V01, EC-CONFIRM-V01, EC-FORM-V01, EC-FORM-V02, EC-FORM-V03 | Họ Tên=Nguyễn Văn An; Email=fr01.dt001@example.com; Mật khẩu=Abcdef1!xy; Xác nhận=Abcdef1!xy | EC-RESULT-O01, EC-RESULT-O05 | Form có dấu * và đúng input type; đăng ký được chấp nhận và chuyển tới trang Đăng nhập. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công; Email của ca chưa tồn tại nếu có.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Nguyễn Văn An |
| Email | fr01.dt001@example.com |
| Mật khẩu | Abcdef1!xy |
| Xác nhận mật khẩu | Abcdef1!xy |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Xác nhận bốn nhãn bắt buộc có dấu `*`, Email dùng `type=email`, Mật khẩu và Xác nhận mật khẩu dùng `type=password`.
3. Nhập đúng dữ liệu trong bảng.
4. Nhấn nút đăng ký và quan sát điều hướng.

## Kết quả mong đợi

Form có dấu * và đúng input type; đăng ký được chấp nhận và chuyển tới trang Đăng nhập.

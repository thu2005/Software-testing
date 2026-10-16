# TC-FR-01-DT-014: Kiểm tra cấu trúc form đăng ký

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
| Lớp mục tiêu | Equivalence class | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-01-DT-014 | EC-FORM-V01, EC-FORM-V02, EC-FORM-V03 | Họ Tên=Không nhập dữ liệu; Email=Không nhập dữ liệu; Mật khẩu=Không nhập dữ liệu; Xác nhận=Không nhập dữ liệu | EC-RESULT-O05 | Nhãn của bốn trường bắt buộc có ký hiệu *; Email dùng type=email; Mật khẩu và Xác nhận mật khẩu dùng type=password. |

## Điều kiện tiên quyết

- Trang đăng ký tải thành công.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Họ Tên | Không nhập dữ liệu |
| Email | Không nhập dữ liệu |
| Mật khẩu | Không nhập dữ liệu |
| Xác nhận mật khẩu | Không nhập dữ liệu |

## Các bước kiểm thử

1. Mở trang đăng ký.
2. Quan sát nhãn và kiểm tra thuộc tính `type` của Email, Mật khẩu và Xác nhận mật khẩu.

## Kết quả mong đợi

Nhãn của bốn trường bắt buộc có ký hiệu *; Email dùng type=email; Mật khẩu và Xác nhận mật khẩu dùng type=password.

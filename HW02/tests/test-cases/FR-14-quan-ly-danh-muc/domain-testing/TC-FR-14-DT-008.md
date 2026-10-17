# TC-FR-14-DT-008: Kiểm tra Tab Order trên trang quản lý danh mục

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-21](../../../../requirements/system-requirements.md#fr-21-tiêu-chuẩn-giao-diện-chung); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Điều hướng bàn phím | Chuỗi thao tác | Nhấn Tab tuần tự |
| Thứ tự focus | Output UI | Trên xuống dưới, trái sang phải |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-008 | EC-AUTH-V01, EC-PAGE-V01, EC-KEYBOARD-V01 | Admin dùng Tab trên trang Danh mục | EC-RESULT-O07 | Focus theo thứ tự quy định. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin và mở mục Danh mục.
- Focus chưa nằm trong một control của form.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Phím thao tác | `Tab` |
| Phạm vi | Các control tương tác trên trang Danh mục |

## Các bước kiểm thử

1. Đưa focus tới đầu trang bằng cách phù hợp với trình duyệt.
2. Nhấn `Tab` từng lần và ghi lại control nhận focus.
3. Tiếp tục tới khi đi qua toàn bộ control của trang.

## Kết quả mong đợi

Focus di chuyển qua các control theo thứ tự từ trên xuống dưới, trái sang phải.

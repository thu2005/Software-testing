# TC-FR-07-DT-003: Tăng số lượng bằng nút +

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](../../../../analysis/FR-07-gio-hang/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR07-002](../../../../bug-reports/BUG-FR07-002.md) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-ADJUST-V01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-003 | EC-ADJUST-V01 | Giỏ có SP-A số lượng 1; bấm + | EC-RESULT-O03 | Số lượng SP-A tăng so với giá trị 1 ban đầu. |

## Điều kiện tiên quyết

- Giỏ có SP-A với số lượng 1.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | SP-A — ID FR07-A, tên Áo kiểm thử FR07 |
| Số lượng ban đầu | 1 |
| Thao tác | + |

## Các bước kiểm thử

1. Mở giỏ theo điều kiện tiên quyết.
2. Ghi nhận số lượng SP-A ban đầu.
3. Bấm nút `+` của SP-A một lần.
4. Quan sát số lượng SP-A.

## Kết quả mong đợi

Số lượng SP-A tăng so với giá trị 1 ban đầu.

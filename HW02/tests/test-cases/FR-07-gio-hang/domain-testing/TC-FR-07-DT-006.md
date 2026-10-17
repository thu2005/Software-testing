# TC-FR-07-DT-006: Xác nhận xóa sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](../../../../analysis/FR-07-gio-hang/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR07-006](../../../../bug-reports/BUG-FR07-006.md) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-DELETE-V02 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-006 | EC-DELETE-V02 | Giỏ có SP-A; bấm Xóa rồi chọn Xác nhận | EC-RESULT-O04, EC-RESULT-O05 | Dialog xác nhận xuất hiện trước khi xóa; SP-A chỉ bị xóa sau khi chọn Xác nhận. |

## Điều kiện tiên quyết

- Giỏ có SP-A.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | SP-A — ID FR07-A, tên Áo kiểm thử FR07 |
| Quyết định dialog | Xác nhận |

## Các bước kiểm thử

1. Mở giỏ có SP-A.
2. Bấm nút Xóa của SP-A.
3. Xác nhận dialog xuất hiện khi SP-A vẫn còn trong giỏ.
4. Chọn hành động xác nhận trong dialog.
5. Quan sát danh sách sản phẩm.

## Kết quả mong đợi

Dialog xác nhận xuất hiện trước khi xóa; SP-A chỉ bị xóa sau khi chọn Xác nhận.

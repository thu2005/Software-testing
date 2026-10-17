# TC-FR-07-DT-005: Hiển thị dialog trước khi xóa sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Giỏ hàng / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart); [domain-testing-analysis.md](../../../../analysis/FR-07-gio-hang/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Fail / [BUG-FR07-006](../../../../bug-reports/BUG-FR07-006.md) ([Issue #10](https://github.com/thu2005/CSC13003_eshop/issues/10)) |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Lớp mục tiêu | Equivalence class | EC-DELETE-V01 |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-07-DT-005 | EC-DELETE-V01 | Giỏ có SP-A; bấm Xóa và chưa xác nhận | EC-RESULT-O04 | Dialog xác nhận xuất hiện và SP-A chưa bị xóa trước khi có quyết định xác nhận. |

## Điều kiện tiên quyết

- Giỏ có SP-A.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Sản phẩm | SP-A — ID FR07-A, tên Áo kiểm thử FR07 |
| Trạng thái dialog | Chưa xác nhận |

## Các bước kiểm thử

1. Mở giỏ có SP-A.
2. Bấm nút Xóa của SP-A.
3. Quan sát dialog và danh sách sản phẩm trước khi đưa ra quyết định xác nhận.

## Kết quả mong đợi

Dialog xác nhận xuất hiện và SP-A chưa bị xóa trước khi có quyết định xác nhận.

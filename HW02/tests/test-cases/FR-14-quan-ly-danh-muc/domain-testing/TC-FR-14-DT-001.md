# TC-FR-14-DT-001: Xem danh sách và cấu trúc trang quản lý danh mục

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [system-requirements.md](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Trạng thái quyền / Trang | Điều kiện | Admin hợp lệ; mục Danh mục đang chọn |
| Danh sách / UI | Output | Danh mục hiện có và các yêu cầu FR-21 đến FR-23 áp dụng |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-001 | EC-AUTH-V01, EC-ACTION-V01, EC-PAGE-V01 | Admin mở mục Danh mục; `DM-FR14-XEM` tồn tại | EC-RESULT-O01, EC-RESULT-O06 | Danh sách có fixture; giao diện tuân thủ các quy tắc áp dụng. |

## Điều kiện tiên quyết

- Đăng nhập bằng tài khoản Admin mặc định.
- Danh mục `DM-FR14-XEM` đã tồn tại.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Tài khoản | `admin@eshop.com` / `Admin123!` |
| Danh mục fixture | `DM-FR14-XEM` |

## Các bước kiểm thử

1. Mở phân hệ Web Admin và chọn mục `Danh mục`.
2. Quan sát danh sách và xác nhận `DM-FR14-XEM` xuất hiện.
3. Kiểm tra ngôn ngữ, số thẻ `<h1>`, trạng thái highlight của mục đang chọn, ký hiệu `*` cạnh nhãn tên và màu của nút Thêm/Xóa.

## Kết quả mong đợi

Danh sách hiển thị `DM-FR14-XEM`. Trang dùng tiếng Việt, có đúng một `<h1>` mô tả nội dung; mục `Danh mục` được highlight; trường tên bắt buộc có `*`; nút thêm là màu xanh dương và nút xóa là màu đỏ.

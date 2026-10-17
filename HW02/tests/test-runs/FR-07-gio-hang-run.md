# Lần thực thi — FR-07: Giỏ hàng

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Người thực hiện / Thời điểm | Thu / 2026-10-16 22:24:00 +07:00 |
| Môi trường | Google Chrome `155.0.8059.40`; Windows |
| URL / Phiên bản ứng dụng / Bản dựng | Frontend `http://127.0.0.1:5174`; commit `85af3ba875c88283615e22cb108f13e2fccaf0e9` (`main`) |
| Chuẩn bị và khôi phục dữ liệu | Do tester thực hiện và review. |
| Nguồn kết quả | Actual Result do Thu cung cấp và 11 screenshot cục bộ; thời điểm lấy từ metadata evidence |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-07-DT-001 | Hiển thị giỏ hàng có sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Danh sách có hai dòng; mỗi dòng hiển thị Sản phẩm, Đơn giá, Số lượng với nút +/-, Thành tiền và Thao tác; nhãn tổng tiền là `Tổng cộng`, không phải `Tổng tạm tính`. | Đúng 2 dòng với số lượng `2, 1`, nhưng thiếu nút `+/-`, dùng cột `Giá` thay cho `Đơn giá` và nhãn `Tổng tạm tính` thay cho `Tổng cộng`. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-001-actual-result.png) | [BUG-FR07-002](../../bug-reports/BUG-FR07-002.md), [BUG-FR07-003](../../bug-reports/BUG-FR07-003.md), [BUG-FR07-004](../../bug-reports/BUG-FR07-004.md) | Không có. |
| TC-FR-07-DT-002 | Thêm lại cùng một sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Số lượng của SP-A tăng và giỏ vẫn chỉ có một dòng SP-A. | Thêm lại SP-A tạo 2 dòng riêng, mỗi dòng số lượng 1; không cộng dồn. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-002-actual-result.png) | [BUG-FR07-005](../../bug-reports/BUG-FR07-005.md) | Không có. |
| TC-FR-07-DT-003 | Tăng số lượng bằng nút + | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Số lượng SP-A tăng so với giá trị 1 ban đầu. | Không có nút `+` để tăng số lượng. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-003-actual-result.png) | [BUG-FR07-002](../../bug-reports/BUG-FR07-002.md) | Không có. |
| TC-FR-07-DT-004 | Giảm số lượng bằng nút - | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Số lượng SP-A giảm so với giá trị 2 ban đầu. | Không có nút `-` để giảm số lượng. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-004-actual-result.png) | [BUG-FR07-002](../../bug-reports/BUG-FR07-002.md) | Không có. |
| TC-FR-07-DT-005 | Hiển thị dialog trước khi xóa sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Dialog xác nhận xuất hiện và SP-A chưa bị xóa trước khi có quyết định xác nhận. | Không xuất hiện dialog; SP-A bị xóa ngay khi bấm `Xóa`. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-005-actual-result.png) | [BUG-FR07-006](../../bug-reports/BUG-FR07-006.md) | Không có. |
| TC-FR-07-DT-006 | Xác nhận xóa sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Dialog xác nhận xuất hiện trước khi xóa; SP-A chỉ bị xóa sau khi chọn Xác nhận. | Sản phẩm bị xóa nhưng không có bước xác nhận trước khi xóa. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-006-actual-result.png) | [BUG-FR07-006](../../bug-reports/BUG-FR07-006.md) | Không có. |
| TC-FR-07-DT-007 | Tiếp tục mua sắm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Nút `Tiếp tục mua sắm` đưa người dùng về trang chủ. | `Tiếp tục mua sắm` đưa về đúng trang chủ. | Pass | [Ảnh Pass](screenshots/TC-FR-07-DT-007-pass.png) | None | Không có. |
| TC-FR-07-DT-008 | Hiển thị giỏ hàng trống | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Trang giỏ hàng hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống. | Có thông báo giỏ trống nhưng không có hình minh họa. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-DT-008-actual-result.png) | [BUG-FR07-001](../../bug-reports/BUG-FR07-001.md) | Không có. |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-07-BVA-001 | Giỏ hàng tại cận rỗng 0 dòng | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống. | Có thông báo giỏ trống nhưng không có hình minh họa. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-BVA-001-actual-result.png) | [BUG-FR07-001](../../bug-reports/BUG-FR07-001.md) | Không có. |
| TC-FR-07-BVA-002 | Giỏ hàng có 1 dòng sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Hiển thị đúng một dòng SP-A với các cột bắt buộc và nhãn `Tổng cộng`. | Có đúng 1 dòng, nhưng thiếu nút `+/-`, dùng cột `Giá` và nhãn `Tổng tạm tính` thay vì `Tổng cộng`. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-BVA-002-actual-result.png) | [BUG-FR07-002](../../bug-reports/BUG-FR07-002.md), [BUG-FR07-003](../../bug-reports/BUG-FR07-003.md), [BUG-FR07-004](../../bug-reports/BUG-FR07-004.md) | Không có. |
| TC-FR-07-BVA-003 | Giỏ hàng có 2 dòng sản phẩm | Thu | 2026-10-16 22:24:00 +07:00 / Lần 1 | Hiển thị đúng hai dòng sản phẩm; mỗi dòng có các cột bắt buộc và khu vực tổng tiền mang nhãn `Tổng cộng`. | Có đúng 2 dòng, nhưng thiếu nút `+/-`, dùng cột `Giá` và nhãn `Tổng tạm tính` thay vì `Tổng cộng`. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-07-BVA-003-actual-result.png) | [BUG-FR07-002](../../bug-reports/BUG-FR07-002.md), [BUG-FR07-003](../../bug-reports/BUG-FR07-003.md), [BUG-FR07-004](../../bug-reports/BUG-FR07-004.md) | Không có. |

## Tổng kết

| Metric | Count |
|---|---:|
| Ca thiết kế | 11 |
| Đã chạy hoàn tất | 11 |
| Đạt | 1 |
| Không đạt | 10 |
| Bị chặn | 0 |
| Chưa chạy | 0 |
| Chưa thực thi hoàn tất | 0 |
| Bug riêng biệt | 6 |

Đếm theo kết quả gần nhất của từng test case. Sáu bug được tách theo sáu hành vi độc lập, không đếm trực tiếp từ số ca Fail.

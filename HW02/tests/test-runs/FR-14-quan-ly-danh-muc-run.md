# Lần thực thi — FR-14: Quản lý Danh mục

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin và API categories |
| Người thực hiện / Thời điểm | Thu / 2026-10-17 18:26:08–18:26:42 +07:00 |
| Môi trường | Google Chrome `155.0.8059.80`; Windows `10.0.26100.0`; Desktop viewport `1440×1000`; Playwright `1.64.0` |
| URL / Phiên bản ứng dụng / Bản dựng | Frontend `http://127.0.0.1:5174`; API `http://127.0.0.1:3000`; SUT `main` tại commit `85af3ba875c88283615e22cb108f13e2fccaf0e9` |
| Repository bài làm / SUT và Issues | [`thu2005/Software-testing`](https://github.com/thu2005/Software-testing) / [`thu2005/CSC13003_eshop`](https://github.com/thu2005/CSC13003_eshop) |
| Chuẩn bị và khôi phục dữ liệu | Backend và database được chạy từ bản sao tạm; seed `DM-FR14-XEM`, `DM-FR14-XOA`, `DM-FR14-BAOVE`; mỗi UI case dùng browser context mới. Server và dữ liệu tạm đã được xóa sau execution; source/database working tree không bị thay đổi. |
| Nguồn kết quả | Actual Result do Thu cung cấp và 11 screenshot cục bộ; thời điểm lấy từ metadata evidence |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-14-DT-001 | Xem danh sách và cấu trúc trang quản lý danh mục | Thu | 2026-10-17 18:26:08 +07:00 / Lần 1 | Danh sách có fixture; trang dùng tiếng Việt, có đúng một `<h1>`, mục hiện tại được highlight, trường bắt buộc có `*`, nút thêm xanh dương và nút xóa đỏ. | Fixture hiển thị, đúng 1 `<h1>`, menu active và màu nút đúng; nhưng thiếu dấu `*` cạnh trường bắt buộc và còn nội dung tiếng Anh như `Dashboard`. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-14-DT-001-actual-result.png) | [BUG-FR14-001](../../bug-reports/BUG-FR14-001.md) ([Issue #11](https://github.com/thu2005/CSC13003_eshop/issues/11)), [BUG-FR14-002](../../bug-reports/BUG-FR14-002.md) ([Issue #12](https://github.com/thu2005/CSC13003_eshop/issues/12)) | Không có. |
| TC-FR-14-DT-002 | Thêm danh mục với tên không rỗng | Thu | 2026-10-17 18:26:10 +07:00 / Lần 1 | Tạo danh mục `DM-FR14-THEM` và hiển thị trong danh sách. | Tạo thành công `DM-FR14-THEM`, danh mục xuất hiện trong danh sách. | Pass | [Ảnh Pass](screenshots/TC-FR-14-DT-002-pass.png) | None | Không có. |
| TC-FR-14-DT-003 | Từ chối thêm danh mục có tên rỗng | Thu | 2026-10-17 18:26:12 +07:00 / Lần 1 | Hiển thị lỗi phía trên nút submit và không tạo danh mục. | Tên rỗng vẫn được gửi và tạo thành một dòng danh mục trống; không có validation phù hợp. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-14-DT-003-actual-result.png) | [BUG-FR14-003](../../bug-reports/BUG-FR14-003.md) ([Issue #13](https://github.com/thu2005/CSC13003_eshop/issues/13)) | Không có. |
| TC-FR-14-DT-004 | Xóa danh mục hiện có | Thu | 2026-10-17 18:26:13 +07:00 / Lần 1 | Chỉ `DM-FR14-XOA` bị xóa và không còn trong danh sách. | Xóa đúng `DM-FR14-XOA`; các danh mục khác không bị ảnh hưởng. | Pass | [Ảnh Pass](screenshots/TC-FR-14-DT-004-pass.png) | None | Không có. |
| TC-FR-14-DT-005 | Từ chối thêm danh mục khi không có token | Thu | 2026-10-17 18:26:14 +07:00 / Lần 1 | Request bị từ chối; `DM-FR14-NOTOKEN` không được tạo. | POST không token bị từ chối với HTTP `401 Unauthorized`; danh mục không được tạo. | Pass | [Ảnh Pass](screenshots/TC-FR-14-DT-005-pass.png) | None | HTTP status lấy từ kết quả tester cung cấp. |
| TC-FR-14-DT-006 | Từ chối user thường xóa danh mục qua API | Thu | 2026-10-17 18:26:15 +07:00 / Lần 1 | Request bị từ chối vì role không phải Admin; `DM-FR14-BAOVE` vẫn tồn tại. | Token user thường xóa danh mục thành công với HTTP `200`; `DM-FR14-BAOVE` bị xóa. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-14-DT-006-actual-result.png) | [BUG-FR14-004](../../bug-reports/BUG-FR14-004.md) ([Issue #14](https://github.com/thu2005/CSC13003_eshop/issues/14)) | HTTP status lấy từ kết quả tester cung cấp. |
| TC-FR-14-DT-007 | Chặn user thường truy cập quản lý danh mục | Thu | 2026-10-17 18:26:16 +07:00 / Lần 1 | User thường không được truy cập chức năng quản lý danh mục. | User thường bị giữ tại trang login, nhận thông báo không phải admin và không có `adminToken`. | Pass | [Ảnh Pass](screenshots/TC-FR-14-DT-007-pass.png) | None | Không có. |
| TC-FR-14-DT-008 | Kiểm tra Tab Order trên trang quản lý danh mục | Thu | 2026-10-17 18:26:36 +07:00 / Lần 1 | Focus di chuyển qua các control từ trên xuống dưới, trái sang phải. | Các mục navigation không thể nhận focus bằng Tab; focus bắt đầu từ ô tên rồi chuyển sang nút Thêm/Xóa. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-14-DT-008-actual-result.png) | [BUG-FR14-005](../../bug-reports/BUG-FR14-005.md) ([Issue #15](https://github.com/thu2005/CSC13003_eshop/issues/15)) | Chuỗi focus lấy từ kết quả tester cung cấp. |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-14-BVA-001 | Tên danh mục tại cận rỗng 0 ký tự | Thu | 2026-10-17 18:26:39 +07:00 / Lần 1 | Từ chối tên rỗng, hiển thị lỗi phía trên nút submit và không tạo danh mục. | Tên 0 ký tự vẫn tạo thêm danh mục trống, không hiển thị lỗi validation. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-14-BVA-001-actual-result.png) | [BUG-FR14-003](../../bug-reports/BUG-FR14-003.md) ([Issue #13](https://github.com/thu2005/CSC13003_eshop/issues/13)) | Cùng defect với DT-003. |
| TC-FR-14-BVA-002 | Tên danh mục tại giá trị nhỏ nhất hợp lệ 1 ký tự | Thu | 2026-10-17 18:26:40 +07:00 / Lần 1 | Tạo danh mục tên `A`. | Tạo thành công danh mục `A` dài 1 ký tự. | Pass | [Ảnh Pass](screenshots/TC-FR-14-BVA-002-pass.png) | None | Không có. |
| TC-FR-14-BVA-003 | Tên danh mục tại đại diện bên trong 2 ký tự | Thu | 2026-10-17 18:26:42 +07:00 / Lần 1 | Tạo danh mục tên `AB`. | Tạo thành công danh mục `AB` dài 2 ký tự. | Pass | [Ảnh Pass](screenshots/TC-FR-14-BVA-003-pass.png) | None | Không có. |

## Tổng kết

| Metric | Count |
|---|---:|
| Ca thiết kế | 11 |
| Đã chạy hoàn tất | 11 |
| Đạt | 6 |
| Không đạt | 5 |
| Bị chặn | 0 |
| Chưa chạy | 0 |
| Chưa thực thi hoàn tất | 0 |
| Bug riêng biệt | 5 |

Đếm theo kết quả gần nhất của từng test case. DT-003 và BVA-001 cùng phát hiện lỗi tên rỗng nên liên kết tới một bug; các lỗi còn lại được tách theo hành vi và yêu cầu độc lập.

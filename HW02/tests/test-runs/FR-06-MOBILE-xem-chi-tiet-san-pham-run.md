# Lần thực thi — FR-06-MOBILE: Xem chi tiết sản phẩm

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / React Native Mobile |
| Người thực hiện / Thời điểm | Thu / 2026-10-17 20:37:07–20:48:07 +07:00 |
| Thiết bị / Hệ điều hành | Android Emulator Pixel 4a (`sdk_gphone64_x86_64`); Android 13, API 33; độ phân giải `1080×2340` |
| Ứng dụng / Bản dựng | Expo Go / Expo SDK 54; SUT commit `85af3ba875c88283615e22cb108f13e2fccaf0e9` |
| Repository bài làm / SUT | [`thu2005/Software-testing`](https://github.com/thu2005/Software-testing) / [`thu2005/CSC13003_eshop`](https://github.com/thu2005/CSC13003_eshop) |
| Chuẩn bị và khôi phục dữ liệu | Do tester thực hiện và review. |
| Nguồn kết quả | Actual Result do Thu cung cấp và 14 screenshot cục bộ; thời điểm lấy từ metadata evidence |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-06-MOBILE-DT-001 | Hiển thị đầy đủ chi tiết sản phẩm | Thu | 2026-10-17 20:37:07 +07:00 / Lần 1 | Trang hiển thị đủ ảnh lớn, tên, giá, mô tả và danh mục của fixture. | Thiếu thông tin danh mục sản phẩm. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-001-actual-result.png) | [BUG-FR06-001](../../bug-reports/BUG-FR06-001.md) | Không có. |
| TC-FR-06-MOBILE-DT-002 | Kiểm tra yêu cầu giao diện áp dụng trên trang chi tiết Mobile | Thu | 2026-10-17 20:37:07 +07:00 / Lần 1 | Trang đáp ứng các yêu cầu giao diện, navigation và accessibility áp dụng trên Mobile. | Không có breadcrumb; nút thêm giỏ màu xanh lá thay vì xanh dương; ảnh không có mô tả accessibility. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-002-actual-result.png) | [BUG-FR06-002](../../bug-reports/BUG-FR06-002.md), [BUG-FR06-003](../../bug-reports/BUG-FR06-003.md), [BUG-FR06-004](../../bug-reports/BUG-FR06-004.md) | Không có. |
| TC-FR-06-MOBILE-DT-003 | Chấp nhận số nguyên dương danh nghĩa | Thu | 2026-10-17 20:38:49 +07:00 / Lần 1 | Control chấp nhận và giữ số lượng `3`. | Control chấp nhận và giữ đúng số lượng `3`. | Pass | [Ảnh Pass](screenshots/TC-FR-06-MOBILE-DT-003-pass.png) | None | Không có. |
| TC-FR-06-MOBILE-DT-004 | Từ chối số lượng rỗng | Thu | 2026-10-17 20:39:51 +07:00 / Lần 1 | Không dùng giá trị rỗng để thêm sản phẩm. | Để trống số lượng vẫn báo thêm giỏ thành công. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-004-actual-result.png) | [BUG-FR06-005](../../bug-reports/BUG-FR06-005.md) | Không có. |
| TC-FR-06-MOBILE-DT-005 | Từ chối số lượng nguyên âm | Thu | 2026-10-17 20:40:44 +07:00 / Lần 1 | Không chấp nhận số lượng `-1` để thêm sản phẩm. | Số lượng `-1` vẫn được thêm. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-005-actual-result.png) | [BUG-FR06-005](../../bug-reports/BUG-FR06-005.md) | Không có. |
| TC-FR-06-MOBILE-DT-006 | Từ chối số lượng thập phân | Thu | 2026-10-17 20:41:16 +07:00 / Lần 1 | Không chấp nhận số lượng `1.5` để thêm sản phẩm. | Số lượng `1.5` vẫn được thêm. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-006-actual-result.png) | [BUG-FR06-005](../../bug-reports/BUG-FR06-005.md) | Không có. |
| TC-FR-06-MOBILE-DT-007 | Từ chối số lượng không phải số | Thu | 2026-10-17 20:41:30 +07:00 / Lần 1 | Không chấp nhận giá trị `abc` để thêm sản phẩm. | Giá trị `abc` vẫn được thêm. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-007-actual-result.png) | [BUG-FR06-005](../../bug-reports/BUG-FR06-005.md) | Không có. |
| TC-FR-06-MOBILE-DT-008 | Thêm sản phẩm vào giỏ và nhận phản hồi trực quan | Thu | 2026-10-17 20:45:53–20:47:02 +07:00 / Lần 1 | Thêm sản phẩm với số lượng `5`, có phản hồi trực quan và kiểm tra được sản phẩm trong giỏ. | Nhập `5` có thông báo thành công và badge cập nhật, nhưng mở giỏ chỉ hiện màn hình trắng nên không xác nhận được số lượng. | Fail | [Ảnh phản hồi](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-008-feedback.png), [Ảnh giỏ trắng](../../bug-reports/screenshots/TC-FR-06-MOBILE-DT-008-actual-result.png) | [BUG-FR06-006](../../bug-reports/BUG-FR06-006.md) | Fail do giỏ hiển thị trắng; phản hồi thêm giỏ vẫn xuất hiện. |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-FR-06-MOBILE-BVA-001 | Số lượng ngay dưới cận tối thiểu | Thu | 2026-10-17 20:41:44 +07:00 / Lần 1 | Không dùng `0` làm số lượng hiệu lực; từ chối hoặc chuẩn hóa về số nguyên dương trước khi thêm. | Số lượng `0` vẫn được thêm thay vì bị từ chối hoặc chuẩn hóa rõ ràng trước khi thêm. | Fail | [Ảnh Actual Result](../../bug-reports/screenshots/TC-FR-06-MOBILE-BVA-001-actual-result.png) | [BUG-FR06-005](../../bug-reports/BUG-FR06-005.md) | Không có. |
| TC-FR-06-MOBILE-BVA-002 | Số lượng tại cận tối thiểu hợp lệ | Thu | 2026-10-17 20:45:20–20:47:50 +07:00 / Lần 1 | Thêm sản phẩm với số lượng `1`, có phản hồi và kiểm tra được sản phẩm trong giỏ. | Nhập `1` có phản hồi thành công, nhưng màn hình giỏ hàng trắng, không xác nhận được sản phẩm và số lượng. | Fail | [Ảnh phản hồi](../../bug-reports/screenshots/TC-FR-06-MOBILE-BVA-002-feedback.png), [Ảnh giỏ trắng](../../bug-reports/screenshots/TC-FR-06-MOBILE-BVA-002-actual-result.png) | [BUG-FR06-006](../../bug-reports/BUG-FR06-006.md) | Fail do giỏ hiển thị trắng; phản hồi thêm giỏ vẫn xuất hiện. |
| TC-FR-06-MOBILE-BVA-003 | Số lượng ngay trên cận tối thiểu | Thu | 2026-10-17 20:45:37–20:48:07 +07:00 / Lần 1 | Thêm sản phẩm với số lượng `2`, có phản hồi và kiểm tra được sản phẩm trong giỏ. | Nhập `2` có phản hồi thành công, nhưng màn hình giỏ hàng trắng, không xác nhận được sản phẩm và số lượng. | Fail | [Ảnh phản hồi](../../bug-reports/screenshots/TC-FR-06-MOBILE-BVA-003-feedback.png), [Ảnh giỏ trắng](../../bug-reports/screenshots/TC-FR-06-MOBILE-BVA-003-actual-result.png) | [BUG-FR06-006](../../bug-reports/BUG-FR06-006.md) | Fail do giỏ hiển thị trắng; phản hồi thêm giỏ vẫn xuất hiện. |

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

Đếm theo kết quả gần nhất của từng test case. DT-004 đến DT-007 và BVA-001 cùng phát hiện lỗi validation số lượng nên liên kết tới một bug. DT-008, BVA-002 và BVA-003 cùng phát hiện màn hình giỏ Mobile trắng nên liên kết tới một bug. DT-002 phát hiện ba sai lệch độc lập về breadcrumb, màu nút và accessibility nên liên kết tới ba bug riêng.

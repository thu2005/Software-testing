# Lần thực thi — <FEATURE-ID>: <Tên chức năng>

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | <FR-ID> / <Nền tảng thực tế> |
| Người thực hiện / Thời điểm | <Tên> / <Ngày giờ và múi giờ> |
| Môi trường | <Trình duyệt, hệ điều hành, thiết bị/emulator> |
| URL / Phiên bản ứng dụng / Bản dựng | <Thông tin thực tế hoặc chưa biết> |
| Chuẩn bị và khôi phục dữ liệu | <Tài khoản thử nghiệm, dữ liệu, cách đặt lại trạng thái> |

## Kết quả kiểm thử miền

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| <TC-ID> | <Mô tả> | <Người chạy> | <Thời điểm/lần chạy hoặc chưa chạy> | <Theo ca kiểm thử> | <Quan sát thực tế hoặc chưa thực thi> | Not Run | <Bằng chứng thật hoặc chưa có> | <BUG-ID/URL hoặc không có> | <Ghi chú> |

## Kết quả phân tích giá trị biên

| Test Case ID | Description | Tester | Timestamp / Attempt | Expected Result | Actual Result | Result | Evidence | Related Bug | Notes |
|---|---|---|---|---|---|---|---|---|---|
| <TC-ID> | <Mô tả> | <Người chạy> | <Thời điểm/lần chạy hoặc chưa chạy> | <Theo ca kiểm thử> | <Quan sát thực tế hoặc chưa thực thi> | Not Run | <Bằng chứng thật hoặc chưa có> | <BUG-ID/URL hoặc không có> | <Ghi chú> |

## Tổng kết

| Metric | Count |
|---|---|
| Ca thiết kế | <Số TC duy nhất> |
| Đã chạy hoàn tất | <Pass + Fail> |
| Đạt | <Số Pass> |
| Không đạt | <Số Fail> |
| Bị chặn | <Số Blocked> |
| Chưa chạy | <Số Not Run> |
| Chưa thực thi hoàn tất | <Blocked + Not Run> |
| Bug riêng biệt | <Số defect không trùng> |

Đếm kết quả gần nhất theo TC; giữ lịch sử lần chạy cũ nếu có. Fail cần kết quả thực tế và liên kết bug hoặc lý do chờ xác minh; Blocked cần lý do cụ thể, không tự coi là bug.

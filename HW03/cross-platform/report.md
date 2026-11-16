# Báo cáo M8 — Cross-browser / Cross-platform

## 1. Platform matrix

Toàn bộ 65 item của Task 1 được chạy lại trên từng target ngày 16/11/2026.
Không dùng Safari vì máy kiểm thử là Windows và không có thiết bị Apple hoặc
dịch vụ cloud-browser trong scope M8.

| Target | Browser / OS / Device | Hình thức | Executed | Passed | Failed | Kết quả chi tiết | Evidence tổng quan |
|---|---|---|---:|---:|---:|---|---|
| Desktop 1 | Chrome `157.0.8103.50` / Windows | Selenium, local headless browser | 65 | 31 | 34 | [chrome-windows.md](results/chrome-windows.md) | [overview](screenshots/chrome-windows-overview.png) |
| Desktop 2 | Firefox `160.0` / Windows | Selenium, local headless browser | 65 | 32 | 33 | [firefox-windows.md](results/firefox-windows.md) | [overview](screenshots/firefox-windows-overview.png) |
| Mobile | Chrome `109.0.5414.123` / Android 13 / Pixel_4a emulator | Selenium qua Appium-compatible ChromeDriver, Android emulator | 65 | 31 | 34 | [chrome-android.md](results/chrome-android.md) | [overview](screenshots/chrome-android-overview.png) |
| **Tổng lượt kiểm tra** | **3 target** |  | **195** | **94** | **101** |  |  |

Mỗi file kết quả giữ nguyên 65 ID `GUI-001`–`GUI-065`. Mỗi item Failed có
Notes, screenshot đã stamp họ tên, email sinh viên, browser/OS/device và URL;
mỗi target có thêm một overview screenshot.

## 2. Kết quả đối chiếu

- Có 33 item Failed giống nhau trên cả ba target. Đây là các defect đã được
  ghi nhận từ Task 1; M8 tái sử dụng bug report và GitHub Issue hiện có thay vì
  tạo issue trùng.
- `GUI-029` Failed trên Chrome Windows và Chrome Android vì nút “Xóa” không có
  focus indicator nhìn thấy. Firefox tự hiển thị outline `3px`, nên item này
  Passed trên Firefox. Khác biệt này củng cố [BUG-IA-03-CROSS-001](../bug-reports/BUG-IA-03-CROSS-001.md)
  và [Issue #52](https://github.com/thu2005/CSC13003_eshop/issues/52).
- `GUI-002` Failed trên cả ba target ở lần chạy chốt vì ảnh ngoài có
  `naturalWidth=0`, hiển thị biểu tượng ảnh vỡ. Kết quả này tái hiện bug ảnh sản
  phẩm đã có, đồng thời cho thấy SUT phụ thuộc URL ảnh ngoài; không tạo defect
  tương thích Android mới. Evidence liên kết với
  [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64).
- 31 item Passed nhất quán trên cả ba target, bao gồm responsive layout ở
  viewport hẹp, currency format, loading state, keyboard order trên Product
  Detail, coupon loading/double-submit và network retry.

## 3. Traceability và giới hạn

M8 kiểm thử local SUT tại `http://localhost:5173`, dùng cùng working tree đã
được mô tả trong README; M8 không sửa source hoặc database của repo SUT. Android
dùng `adb reverse` cho port `5173` và `3000`. Chrome Android 109 là phiên bản có
sẵn trong AVD, cũ hơn hai browser desktop; kết quả không đại diện cho mọi thiết
bị hoặc phiên bản Android.

Không có defect cross-platform mới đủ bằng chứng để tạo thêm GitHub Issue. Các
failure đều liên kết tới 21 issue hiện có của Task 1–2. Raw state screenshot và
script chạy lại nằm trong `cross-platform/raw/` và `cross-platform/scripts/`;
evidence dùng để chấm nằm trong `cross-platform/screenshots/`.

## 4. Kết luận M8

Đã thực hiện đủ `65 × 3 = 195` lượt kiểm tra trên ba target hợp lệ. Firefox có
kết quả tốt hơn hai target Chrome một item nhờ focus outline mặc định ở
`GUI-029`; 64 item còn lại có cùng verdict trên cả ba target. Kết quả xác nhận
các defect chính không chỉ xuất hiện trên một browser desktop.

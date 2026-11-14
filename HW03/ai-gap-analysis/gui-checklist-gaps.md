# GUI Checklist — Human Gap Analysis

## Bối cảnh review

- Initial AI draft: 48 item.
- Kết quả human review: coverage đạt yêu cầu tối thiểu nhưng có item chưa nguyên
  tử, một số IA chưa đúng và còn thiếu các tiêu chí global/accessibility/recovery.
- Checklist sau M2: 65 item, gồm 55 `Source=AI` đã sửa/tách và 10
  `Source=Human`.

## Các item AI đã được sửa

| Initial ID | Thay đổi của sinh viên | Kết quả trong checklist sau M2 |
|---|---|---|
| GUI-002 | Tách kiểm tra hiển thị ảnh và alternative text. | GUI-002, GUI-003 |
| GUI-004 | Viết lại để chỉ kiểm tra responsive layout. | GUI-004 |
| GUI-008 | Tách Tab order và focus indicator; chuyển sang IA-03. | GUI-009, GUI-010 |
| GUI-011 | Tách khả năng truy cập link Giỏ hàng và độ chính xác của badge. | GUI-013, GUI-014 |
| GUI-016 | Tách product ID không tồn tại và lỗi API/network. | GUI-019, GUI-020 |
| GUI-024 | Tách accessible name/focus khỏi visual nguy hiểm; reclassify khỏi IA-02. | GUI-025, GUI-029 |
| GUI-040 | Giới hạn về coupon loading/double-submit; checkout loading giữ ở item riêng. | GUI-045, GUI-052 |
| GUI-042 | Bỏ expected dạng “hoặc”; yêu cầu navbar highlight Checkout rõ ràng. | GUI-047 |
| GUI-046 | Gom thành hành vi chung cho coupon không hợp lệ. | GUI-051 |
| GUI-048 | Tách thông báo thành công, xóa giỏ và điều hướng về trang chủ. | GUI-053–GUI-055 |

## Các gap do sinh viên bổ sung

| Checklist ID | Gap | Item bổ sung | Lý do AI bỏ sót |
|---|---|---|---|
| GUI-056 | Màu hành động | Nút tích cực dùng màu xanh dương; nút nguy hiểm/hủy bỏ dùng màu đỏ nhất quán. | **Prompt scope:** prompt theo chức năng từng màn hình nên bỏ sót visual consistency toàn hệ thống trong FR-21. |
| GUI-057 | Ngôn ngữ | Label, message, button và error trên ba màn hình dùng tiếng Việt nhất quán. | **Model limitation:** AI không chuyển global language requirement thành một item riêng. |
| GUI-058 | Contrast | Text, button, focus indicator và error message có contrast đủ đọc. | **Model limitation:** AI nhắc accessibility nhưng chưa chuyển thành expected check đo được. |
| GUI-059 | Keyboard Cart | Tab qua `−`, `+`, Xóa và Checkout theo thứ tự hợp lý, có focus indicator. | **Prompt scope:** AI chỉ tạo keyboard-flow item cho Product Detail. |
| GUI-060 | Keyboard Checkout | Tab qua coupon, Apply và Checkout đúng thứ tự, không có keyboard trap. | **Prompt scope:** batch Checkout bỏ sót keyboard-only flow. |
| GUI-061 | Touch target | Các nút thao tác chính có vùng chạm đủ lớn trên mobile. | **Interface-specific trait:** responsive/mobile behavior của EShop chưa được xét ở mức control. |
| GUI-062 | Long content | Tên sản phẩm và text tiếng Việt dài không làm vỡ layout hoặc che nút. | **Model limitation:** AI kiểm tra viewport nhưng chưa biến dữ liệu dài thành test condition riêng. |
| GUI-063 | All-image alt | Ảnh sản phẩm trong Cart/Checkout cũng có alternative text phù hợp. | **Prompt scope:** AI chỉ kiểm tra alt trên Product Detail dù FR-24 áp dụng cho mọi ảnh sản phẩm. |
| GUI-064 | Session expiry | Session hết hạn giữa Checkout có thông báo và không làm mất giỏ âm thầm. | **Prompt scope:** AI chỉ kiểm tra người chưa đăng nhập, không kiểm tra token hết hạn giữa flow. |
| GUI-065 | Network recovery | Sau lỗi mạng ở coupon/checkout, nút bật lại và có thể retry không tạo đơn trùng. | **Model limitation:** AI tạo loading state nhưng bỏ sót recovery state sau lỗi. |

## Kết luận quality gate M2

- Tổng số: 65 item (>40).
- ID liên tục: `GUI-001`–`GUI-065`.
- Bao phủ đủ ba screen và `IA-01`–`IA-04`.
- Có traceability `Source=AI`/`Source=Human` và lý do cho từng human gap.
- Mỗi item có một expected behavior chính; toàn bộ kết quả vẫn `Not Run`.

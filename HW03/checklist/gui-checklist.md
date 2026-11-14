# GUI Checklist — Initial AI Draft

## Phạm vi

- Product Detail — `FR-06`
- Shopping Cart — `FR-07`
- Checkout — `FR-08`
- GUI requirements dùng chung — `FR-21`–`FR-24`
- SUT baseline lúc thiết kế — frontend và API products trả HTTP `200`

Đây là initial checklist do AI tạo ở M1. Chưa có item nào được execute; toàn bộ
`Result` phải giữ `Not Run` cho đến M3. M2 sẽ loại item không phù hợp/trùng lặp
và bổ sung các gap do sinh viên tự xác nhận với `Source=Human`.

## Tổng hợp initial coverage

| Screen | IA-01 | IA-02 | IA-03 | IA-04 | Tổng |
|---|---:|---:|---:|---:|---:|
| Product Detail | 4 | 4 | 4 | 4 | 16 |
| Shopping Cart | 4 | 4 | 4 | 4 | 16 |
| Checkout | 4 | 4 | 4 | 4 | 16 |
| **Tổng** | **12** | **12** | **12** | **12** | **48** |

## Checklist items

| ID | IA | Screen | Item | Source | Result | Notes | Screenshot | Bug ID |
|---|---|---|---|---|---|---|---|---|
| GUI-001 | IA-01 | Product Detail | Trang chỉ có đúng một tiêu đề cấp `h1`, hiển thị chính xác tên sản phẩm đang xem. | AI | Not Run | | | |
| GUI-002 | IA-01 | Product Detail | Ảnh sản phẩm lớn hiển thị đúng tỷ lệ, không méo/vỡ và có alternative text mô tả đúng sản phẩm. | AI | Not Run | | | |
| GUI-003 | IA-01 | Product Detail | Giá sản phẩm dùng dấu phân cách hàng nghìn và ký hiệu `₫` nhất quán, không xuất hiện `NaN` hoặc giá trị khó đọc. | AI | Not Run | | | |
| GUI-004 | IA-01 | Product Detail | Tên, ảnh, giá, mô tả và danh mục vẫn đọc được, không chồng lấn hoặc tràn khỏi viewport ở desktop và mobile. | AI | Not Run | | | |
| GUI-005 | IA-02 | Product Detail | Ô “Số lượng” có nhãn hiển thị thường trực và dùng kiểu nhập số phù hợp. | AI | Not Run | | | |
| GUI-006 | IA-02 | Product Detail | Ô “Số lượng” chỉ chấp nhận số nguyên từ 1 trở lên và từ chối `0` hoặc số âm bằng phản hồi rõ ràng. | AI | Not Run | | | |
| GUI-007 | IA-02 | Product Detail | Ô “Số lượng” từ chối số thập phân, ký tự không phải số và giá trị rỗng thay vì thêm số lượng không hợp lệ vào giỏ. | AI | Not Run | | | |
| GUI-008 | IA-02 | Product Detail | Khi dùng bàn phím, focus đi từ ô số lượng đến nút “Thêm vào giỏ hàng” theo thứ tự hợp lý và luôn có focus indicator nhìn thấy được. | AI | Not Run | | | |
| GUI-009 | IA-03 | Product Detail | Trang có breadcrumb cho biết vị trí hiện tại và cung cấp đường quay lại danh sách sản phẩm. | AI | Not Run | | | |
| GUI-010 | IA-03 | Product Detail | Mở trực tiếp URL `/product/<id>` hợp lệ tải đúng sản phẩm, không buộc người dùng phải đi từ trang chủ. | AI | Not Run | | | |
| GUI-011 | IA-03 | Product Detail | Link “Giỏ hàng” trên navbar luôn truy cập được và badge hiển thị đúng tổng số lượng sản phẩm hiện có trong giỏ. | AI | Not Run | | | |
| GUI-012 | IA-03 | Product Detail | Nút Back/Forward của trình duyệt chuyển giữa danh sách và chi tiết đúng trang, không tạo dead end hoặc mất giỏ hàng. | AI | Not Run | | | |
| GUI-013 | IA-04 | Product Detail | Trong lúc tải dữ liệu, trang hiển thị loading state dễ nhận biết thay vì vùng nội dung trắng. | AI | Not Run | | | |
| GUI-014 | IA-04 | Product Detail | Sau một lần bấm “Thêm vào giỏ hàng”, sản phẩm được thêm ngay và có toast, badge hoặc phản hồi trực quan xác nhận thành công. | AI | Not Run | | | |
| GUI-015 | IA-04 | Product Detail | Thêm lại cùng một sản phẩm làm tăng số lượng trên dòng hiện có trong giỏ, không tạo dòng trùng lặp. | AI | Not Run | | | |
| GUI-016 | IA-04 | Product Detail | Với product ID không tồn tại hoặc API lỗi, trang hiển thị error/empty state thân thiện và đường quay lại mua sắm, không treo loading vô hạn hoặc trắng trang. | AI | Not Run | | | |
| GUI-017 | IA-01 | Shopping Cart | Trang chỉ có đúng một tiêu đề cấp `h1` mô tả nội dung “Giỏ hàng”. | AI | Not Run | | | |
| GUI-018 | IA-01 | Shopping Cart | Khi có sản phẩm, bảng hiển thị rõ năm cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền và Thao tác. | AI | Not Run | | | |
| GUI-019 | IA-01 | Shopping Cart | Đơn giá, thành tiền từng dòng và tổng cộng đều dùng dấu phân cách hàng nghìn cùng ký hiệu `₫` nhất quán. | AI | Not Run | | | |
| GUI-020 | IA-01 | Shopping Cart | Ở viewport hẹp, nội dung giỏ vẫn đọc và thao tác được, không bị cắt cột, chồng nút hoặc gây tràn ngang toàn trang. | AI | Not Run | | | |
| GUI-021 | IA-02 | Shopping Cart | Mỗi dòng sản phẩm có điều khiển `−` và `+` dễ nhận biết để giảm hoặc tăng số lượng. | AI | Not Run | | | |
| GUI-022 | IA-02 | Shopping Cart | Điều khiển giảm số lượng không cho giá trị xuống dưới 1 và thể hiện rõ trạng thái không thể giảm thêm. | AI | Not Run | | | |
| GUI-023 | IA-02 | Shopping Cart | Mỗi lần thay đổi số lượng cập nhật đúng thành tiền của chính dòng đó mà không sửa dòng sản phẩm khác. | AI | Not Run | | | |
| GUI-024 | IA-02 | Shopping Cart | Điều khiển “Xóa” có nhãn truy cập rõ, focus indicator nhìn thấy được và kiểu trình bày thể hiện đây là hành động nguy hiểm. | AI | Not Run | | | |
| GUI-025 | IA-03 | Shopping Cart | Trang có breadcrumb cho biết vị trí “Giỏ hàng” và cung cấp đường quay lại trang chủ. | AI | Not Run | | | |
| GUI-026 | IA-03 | Shopping Cart | Navbar highlight đúng vị trí hiện tại khi người dùng đang ở trang Giỏ hàng. | AI | Not Run | | | |
| GUI-027 | IA-03 | Shopping Cart | Link “Tiếp tục mua sắm” đưa về danh sách sản phẩm và giữ nguyên các sản phẩm đang có trong giỏ. | AI | Not Run | | | |
| GUI-028 | IA-03 | Shopping Cart | “Tiến hành thanh toán” đưa người đã đăng nhập đến Checkout; người chưa đăng nhập nhận thông báo rõ và được chuyển đến Login. | AI | Not Run | | | |
| GUI-029 | IA-04 | Shopping Cart | Khi giỏ trống, trang hiển thị icon/hình minh họa, thông báo thân thiện và hành động “Tiếp tục mua sắm”. | AI | Not Run | | | |
| GUI-030 | IA-04 | Shopping Cart | Bấm “Xóa” luôn mở dialog xác nhận trước khi sản phẩm bị loại khỏi giỏ. | AI | Not Run | | | |
| GUI-031 | IA-04 | Shopping Cart | Khu vực tổng tiền dùng đúng nhãn “Tổng cộng” và cập nhật ngay sau khi số lượng hoặc danh sách sản phẩm thay đổi. | AI | Not Run | | | |
| GUI-032 | IA-04 | Shopping Cart | Sau khi cập nhật hoặc xóa sản phẩm, bảng, tổng cộng và badge trên navbar đồng bộ với cùng một trạng thái giỏ hàng. | AI | Not Run | | | |
| GUI-033 | IA-01 | Checkout | Trang chỉ có đúng một tiêu đề cấp `h1` mô tả bước Checkout/Xác nhận đơn hàng. | AI | Not Run | | | |
| GUI-034 | IA-01 | Checkout | Phần tóm tắt hiển thị đầy đủ từng sản phẩm, số lượng và thành tiền tương ứng trước khi xác nhận. | AI | Not Run | | | |
| GUI-035 | IA-01 | Checkout | Tổng tiền, số tiền giảm và thành tiền cuối cùng đều dùng dấu phân cách hàng nghìn cùng ký hiệu `₫` nhất quán. | AI | Not Run | | | |
| GUI-036 | IA-01 | Checkout | Tóm tắt đơn hàng, vùng coupon và nút xác nhận vẫn đọc/thao tác được ở desktop và mobile, không chồng lấn hoặc tràn viewport. | AI | Not Run | | | |
| GUI-037 | IA-02 | Checkout | Tổng tiền thanh toán được tính tự động và hiển thị ở dạng chỉ đọc, người dùng không thể nhập hoặc sửa trực tiếp. | AI | Not Run | | | |
| GUI-038 | IA-02 | Checkout | Ô mã giảm giá có nhãn hiển thị thường trực và nút “Áp dụng” gắn rõ với đúng ô nhập. | AI | Not Run | | | |
| GUI-039 | IA-02 | Checkout | Khi mã coupon rỗng hoặc chỉ có khoảng trắng, nút “Áp dụng” bị vô hiệu hóa và không gửi request. | AI | Not Run | | | |
| GUI-040 | IA-02 | Checkout | Trong lúc áp dụng coupon hoặc gửi checkout, nút tương ứng thể hiện trạng thái xử lý và ngăn double-submit. | AI | Not Run | | | |
| GUI-041 | IA-03 | Checkout | Trang có breadcrumb cho biết vị trí “Thanh toán” và cung cấp đường quay lại Giỏ hàng. | AI | Not Run | | | |
| GUI-042 | IA-03 | Checkout | Navbar highlight đúng vị trí hiện tại hoặc flow có chỉ báo bước rõ ràng để người dùng biết mình đang ở giai đoạn thanh toán. | AI | Not Run | | | |
| GUI-043 | IA-03 | Checkout | Quay lại Giỏ hàng rồi trở về Checkout giữ nguyên sản phẩm và số lượng, không làm mất trạng thái đơn hàng. | AI | Not Run | | | |
| GUI-044 | IA-03 | Checkout | Truy cập trực tiếp `/checkout` khi chưa đăng nhập không hiển thị form thanh toán; người dùng được giải thích và chuyển đến Login. | AI | Not Run | | | |
| GUI-045 | IA-04 | Checkout | Coupon hợp lệ hiển thị thông báo thành công cùng số tiền tiết kiệm và thành tiền mới được tính đúng. | AI | Not Run | | | |
| GUI-046 | IA-04 | Checkout | Coupon không tồn tại, hết hạn, chưa đủ ngưỡng hoặc hết lượt hiển thị lỗi cụ thể gần vùng coupon và không thay đổi tổng tiền. | AI | Not Run | | | |
| GUI-047 | IA-04 | Checkout | Trong lúc gửi đơn hàng, trang hiển thị trạng thái “Đang xử lý” và không cho tạo nhiều đơn do bấm lặp. | AI | Not Run | | | |
| GUI-048 | IA-04 | Checkout | Sau checkout thành công, trang hiển thị xác nhận rõ ràng, giỏ hàng được xóa và có hành động quay lại trang chủ. | AI | Not Run | | | |

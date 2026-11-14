# GUI Checklist — Human-Reviewed Draft

## Phạm vi

- Product Detail — `FR-06`
- Shopping Cart — `FR-07`
- Checkout — `FR-08`
- GUI requirements dùng chung — `FR-21`–`FR-24`
- SUT baseline khi thiết kế — frontend/API trả HTTP `200`; Product Detail DOM
  động tải hoàn chỉnh (22.444 byte) và Chrome headless xuất được screenshot
  1440×1000 sau khi dùng profile tạm và chờ API 5 giây

Checklist đã qua human review ở M2. Các item ghép đã được tách, item mơ hồ đã
được viết lại/reclassify, và 10 gap do sinh viên xác định đã được thêm với
`Source=Human`. Chưa có item nào được execute; toàn bộ `Result` giữ `Not Run`
cho đến M3.

## Tổng hợp coverage sau M2

| Scope | IA-01 | IA-02 | IA-03 | IA-04 | Tổng |
|---|---:|---:|---:|---:|---:|
| Product Detail | 5 | 3 | 7 | 5 | 20 |
| Shopping Cart | 5 | 3 | 5 | 4 | 17 |
| Checkout | 4 | 4 | 4 | 6 | 18 |
| Cross-screen human gaps | 6 | 0 | 2 | 2 | 10 |
| **Tổng** | **20** | **10** | **18** | **17** | **65** |

| Source | Số item |
|---|---:|
| AI | 55 |
| Human | 10 |
| **Tổng** | **65** |

## Checklist items

| ID | IA | Screen | Item | Source | Result | Notes | Screenshot | Bug ID |
|---|---|---|---|---|---|---|---|---|
| GUI-001 | IA-01 | Product Detail | Trang chỉ có đúng một tiêu đề cấp `h1`, hiển thị chính xác tên sản phẩm đang xem. | AI | Not Run | | | |
| GUI-002 | IA-01 | Product Detail | Ảnh sản phẩm lớn hiển thị đúng tỷ lệ, không méo, vỡ hoặc bị cắt mất nội dung chính. | AI | Not Run | | | |
| GUI-003 | IA-01 | Product Detail | Ảnh sản phẩm lớn có alternative text mô tả đúng sản phẩm và không để rỗng. | AI | Not Run | | | |
| GUI-004 | IA-01 | Product Detail | Bố cục Product Detail thích ứng ở desktop và mobile, không chồng lấn hoặc tràn khỏi viewport. | AI | Not Run | | | |
| GUI-005 | IA-01 | Product Detail | Giá sản phẩm dùng dấu phân cách hàng nghìn và ký hiệu `₫` nhất quán, không xuất hiện `NaN` hoặc giá trị khó đọc. | AI | Not Run | | | |
| GUI-006 | IA-02 | Product Detail | Ô “Số lượng” có nhãn hiển thị thường trực và dùng kiểu nhập số phù hợp. | AI | Not Run | | | |
| GUI-007 | IA-02 | Product Detail | Ô “Số lượng” chỉ chấp nhận số nguyên từ 1 trở lên và từ chối `0` hoặc số âm bằng phản hồi rõ ràng. | AI | Not Run | | | |
| GUI-008 | IA-02 | Product Detail | Ô “Số lượng” từ chối số thập phân, ký tự không phải số và giá trị rỗng thay vì thêm số lượng không hợp lệ vào giỏ. | AI | Not Run | | | |
| GUI-009 | IA-03 | Product Detail | Khi dùng bàn phím, Tab di chuyển qua ô số lượng và nút “Thêm vào giỏ hàng” theo đúng thứ tự đọc. | AI | Not Run | | | |
| GUI-010 | IA-03 | Product Detail | Ô số lượng và nút “Thêm vào giỏ hàng” có focus indicator nhìn thấy rõ khi nhận focus. | AI | Not Run | | | |
| GUI-011 | IA-03 | Product Detail | Trang có breadcrumb cho biết vị trí hiện tại và cung cấp đường quay lại danh sách sản phẩm. | AI | Not Run | | | |
| GUI-012 | IA-03 | Product Detail | Mở trực tiếp URL `/product/<id>` hợp lệ tải đúng sản phẩm, không buộc người dùng phải đi từ trang chủ. | AI | Not Run | | | |
| GUI-013 | IA-03 | Product Detail | Link “Giỏ hàng” trên navbar luôn truy cập được bằng chuột và bàn phím. | AI | Not Run | | | |
| GUI-014 | IA-03 | Product Detail | Badge trên link “Giỏ hàng” hiển thị đúng tổng số lượng sản phẩm hiện có trong giỏ. | AI | Not Run | | | |
| GUI-015 | IA-03 | Product Detail | Nút Back/Forward của trình duyệt chuyển giữa danh sách và chi tiết đúng trang, không tạo dead end hoặc mất giỏ hàng. | AI | Not Run | | | |
| GUI-016 | IA-04 | Product Detail | Trong lúc tải dữ liệu, trang hiển thị loading state dễ nhận biết thay vì vùng nội dung trắng. | AI | Not Run | | | |
| GUI-017 | IA-04 | Product Detail | Sau một lần bấm “Thêm vào giỏ hàng”, sản phẩm được thêm ngay và có toast, badge hoặc phản hồi trực quan xác nhận thành công. | AI | Not Run | | | |
| GUI-018 | IA-04 | Product Detail | Thêm lại cùng một sản phẩm làm tăng số lượng trên dòng hiện có trong giỏ, không tạo dòng trùng lặp. | AI | Not Run | | | |
| GUI-019 | IA-04 | Product Detail | Với product ID không tồn tại, trang hiển thị not-found state thân thiện và có đường quay lại mua sắm. | AI | Not Run | | | |
| GUI-020 | IA-04 | Product Detail | Khi API sản phẩm hoặc mạng lỗi, trang hiển thị thông báo lỗi và cách thử lại, không treo loading vô hạn hoặc trắng trang. | AI | Not Run | | | |
| GUI-021 | IA-01 | Shopping Cart | Trang chỉ có đúng một tiêu đề cấp `h1` mô tả nội dung “Giỏ hàng”. | AI | Not Run | | | |
| GUI-022 | IA-01 | Shopping Cart | Khi có sản phẩm, bảng hiển thị rõ năm cột: Sản phẩm, Đơn giá, Số lượng, Thành tiền và Thao tác. | AI | Not Run | | | |
| GUI-023 | IA-01 | Shopping Cart | Đơn giá, thành tiền từng dòng và tổng cộng đều dùng dấu phân cách hàng nghìn cùng ký hiệu `₫` nhất quán. | AI | Not Run | | | |
| GUI-024 | IA-01 | Shopping Cart | Ở viewport hẹp, nội dung giỏ vẫn đọc và thao tác được, không bị cắt cột, chồng nút hoặc gây tràn ngang toàn trang. | AI | Not Run | | | |
| GUI-025 | IA-01 | Shopping Cart | Điều khiển “Xóa” dùng cách trình bày/màu sắc nhất quán để thể hiện đây là hành động nguy hiểm. | AI | Not Run | | | |
| GUI-026 | IA-02 | Shopping Cart | Mỗi dòng sản phẩm có điều khiển `−` và `+` dễ nhận biết để giảm hoặc tăng số lượng. | AI | Not Run | | | |
| GUI-027 | IA-02 | Shopping Cart | Điều khiển giảm số lượng không cho giá trị xuống dưới 1 và thể hiện rõ trạng thái không thể giảm thêm. | AI | Not Run | | | |
| GUI-028 | IA-02 | Shopping Cart | Mỗi lần thay đổi số lượng cập nhật đúng thành tiền của chính dòng đó mà không sửa dòng sản phẩm khác. | AI | Not Run | | | |
| GUI-029 | IA-03 | Shopping Cart | Điều khiển “Xóa” có accessible name rõ ràng và focus indicator nhìn thấy được khi điều hướng bằng bàn phím. | AI | Not Run | | | |
| GUI-030 | IA-03 | Shopping Cart | Trang có breadcrumb cho biết vị trí “Giỏ hàng” và cung cấp đường quay lại trang chủ. | AI | Not Run | | | |
| GUI-031 | IA-03 | Shopping Cart | Navbar highlight đúng vị trí hiện tại khi người dùng đang ở trang Giỏ hàng. | AI | Not Run | | | |
| GUI-032 | IA-03 | Shopping Cart | Link “Tiếp tục mua sắm” đưa về danh sách sản phẩm và giữ nguyên các sản phẩm đang có trong giỏ. | AI | Not Run | | | |
| GUI-033 | IA-03 | Shopping Cart | “Tiến hành thanh toán” đưa người đã đăng nhập đến Checkout; người chưa đăng nhập nhận thông báo rõ và được chuyển đến Login. | AI | Not Run | | | |
| GUI-034 | IA-04 | Shopping Cart | Khi giỏ trống, trang hiển thị icon/hình minh họa, thông báo thân thiện và hành động “Tiếp tục mua sắm”. | AI | Not Run | | | |
| GUI-035 | IA-04 | Shopping Cart | Bấm “Xóa” luôn mở dialog xác nhận trước khi sản phẩm bị loại khỏi giỏ. | AI | Not Run | | | |
| GUI-036 | IA-04 | Shopping Cart | Khu vực tổng tiền dùng đúng nhãn “Tổng cộng” và cập nhật ngay sau khi số lượng hoặc danh sách sản phẩm thay đổi. | AI | Not Run | | | |
| GUI-037 | IA-04 | Shopping Cart | Sau khi cập nhật hoặc xóa sản phẩm, bảng, tổng cộng và badge trên navbar đồng bộ với cùng một trạng thái giỏ hàng. | AI | Not Run | | | |
| GUI-038 | IA-01 | Checkout | Trang chỉ có đúng một tiêu đề cấp `h1` mô tả bước Checkout/Xác nhận đơn hàng. | AI | Not Run | | | |
| GUI-039 | IA-01 | Checkout | Phần tóm tắt hiển thị đầy đủ từng sản phẩm, số lượng và thành tiền tương ứng trước khi xác nhận. | AI | Not Run | | | |
| GUI-040 | IA-01 | Checkout | Tổng tiền, số tiền giảm và thành tiền cuối cùng đều dùng dấu phân cách hàng nghìn cùng ký hiệu `₫` nhất quán. | AI | Not Run | | | |
| GUI-041 | IA-01 | Checkout | Tóm tắt đơn hàng, vùng coupon và nút xác nhận vẫn đọc/thao tác được ở desktop và mobile, không chồng lấn hoặc tràn viewport. | AI | Not Run | | | |
| GUI-042 | IA-02 | Checkout | Tổng tiền thanh toán được tính tự động và hiển thị ở dạng chỉ đọc, người dùng không thể nhập hoặc sửa trực tiếp. | AI | Not Run | | | |
| GUI-043 | IA-02 | Checkout | Ô mã giảm giá có nhãn hiển thị thường trực và nút “Áp dụng” gắn rõ với đúng ô nhập. | AI | Not Run | | | |
| GUI-044 | IA-02 | Checkout | Khi mã coupon rỗng hoặc chỉ có khoảng trắng, nút “Áp dụng” bị vô hiệu hóa và không gửi request. | AI | Not Run | | | |
| GUI-045 | IA-02 | Checkout | Trong lúc áp dụng coupon, nút “Áp dụng” hiển thị trạng thái xử lý, bị vô hiệu hóa và không gửi request trùng khi bấm liên tiếp. | AI | Not Run | | | |
| GUI-046 | IA-03 | Checkout | Trang có breadcrumb cho biết vị trí “Thanh toán” và cung cấp đường quay lại Giỏ hàng. | AI | Not Run | | | |
| GUI-047 | IA-03 | Checkout | Navbar highlight đúng vị trí Checkout khi người dùng đang ở trang thanh toán. | AI | Not Run | | | |
| GUI-048 | IA-03 | Checkout | Quay lại Giỏ hàng rồi trở về Checkout giữ nguyên sản phẩm và số lượng, không làm mất trạng thái đơn hàng. | AI | Not Run | | | |
| GUI-049 | IA-03 | Checkout | Truy cập trực tiếp `/checkout` khi chưa đăng nhập không hiển thị form thanh toán; người dùng được giải thích và chuyển đến Login. | AI | Not Run | | | |
| GUI-050 | IA-04 | Checkout | Coupon hợp lệ hiển thị thông báo thành công cùng số tiền tiết kiệm và thành tiền mới được tính đúng. | AI | Not Run | | | |
| GUI-051 | IA-04 | Checkout | Mọi coupon không hợp lệ đều hiển thị lỗi cụ thể gần vùng coupon và không thay đổi tổng tiền thanh toán. | AI | Not Run | | | |
| GUI-052 | IA-04 | Checkout | Trong lúc gửi đơn hàng, nút xác nhận hiển thị “Đang xử lý”, bị vô hiệu hóa và không tạo nhiều đơn khi bấm lặp. | AI | Not Run | | | |
| GUI-053 | IA-04 | Checkout | Sau checkout thành công, trang hiển thị thông báo xác nhận rõ ràng. | AI | Not Run | | | |
| GUI-054 | IA-04 | Checkout | Sau checkout thành công, toàn bộ sản phẩm được xóa khỏi giỏ hàng. | AI | Not Run | | | |
| GUI-055 | IA-04 | Checkout | Sau checkout thành công, trang cung cấp hành động hoạt động đúng để quay lại trang chủ. | AI | Not Run | | | |
| GUI-056 | IA-01 | Product Detail / Shopping Cart / Checkout | Nút hành động tích cực dùng màu xanh dương và nút nguy hiểm/hủy bỏ dùng màu đỏ nhất quán trên ba màn hình. | Human | Not Run | | | |
| GUI-057 | IA-01 | Product Detail / Shopping Cart / Checkout | Toàn bộ label, message, button và error trên ba màn hình dùng tiếng Việt nhất quán, trừ thuật ngữ kỹ thuật chuẩn. | Human | Not Run | | | |
| GUI-058 | IA-01 | Product Detail / Shopping Cart / Checkout | Text, button, focus indicator và error message có độ tương phản đủ để đọc và phân biệt trạng thái. | Human | Not Run | | | |
| GUI-059 | IA-03 | Shopping Cart | Có thể Tab đến các điều khiển `−`, `+`, “Xóa” và “Tiến hành thanh toán” theo thứ tự hợp lý, với focus indicator nhìn thấy được. | Human | Not Run | | | |
| GUI-060 | IA-03 | Checkout | Có thể Tab qua ô coupon, nút “Áp dụng” và nút xác nhận thanh toán theo đúng thứ tự mà không gặp keyboard trap. | Human | Not Run | | | |
| GUI-061 | IA-01 | Shopping Cart / Checkout | Các nút `−`, `+`, “Xóa”, “Áp dụng” và xác nhận thanh toán có vùng chạm đủ lớn, không chồng lấn trên mobile. | Human | Not Run | | | |
| GUI-062 | IA-01 | Product Detail / Shopping Cart / Checkout | Tên sản phẩm và nội dung tiếng Việt dài không làm vỡ layout, che nút hoặc mất thông tin trên ba màn hình. | Human | Not Run | | | |
| GUI-063 | IA-01 | Shopping Cart / Checkout | Mọi ảnh sản phẩm được hiển thị trong Cart hoặc Checkout đều có alternative text phù hợp, không để rỗng. | Human | Not Run | | | |
| GUI-064 | IA-04 | Checkout | Nếu session hết hạn trong lúc Checkout, người dùng nhận thông báo rõ ràng và giỏ hàng không bị mất âm thầm. | Human | Not Run | | | |
| GUI-065 | IA-04 | Checkout | Khi áp dụng coupon hoặc checkout gặp lỗi mạng, nút tương ứng được bật lại và người dùng có thể thử lại mà không tạo đơn trùng. | Human | Not Run | | | |

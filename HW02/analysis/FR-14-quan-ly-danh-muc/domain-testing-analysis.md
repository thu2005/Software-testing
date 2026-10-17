# Phân tích kiểm thử miền — FR-14: Quản lý Danh mục

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Nguồn đặc tả | [system-requirements.md](../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud), FR-12, FR-14, FR-21 đến FR-23; [api-specification.md](../../requirements/api-specification.md#34-danh-mục-categories) |
| Tác nhân / Điều kiện tiên quyết | Admin đã xác thực quản lý danh mục; các API thay đổi dữ liệu yêu cầu JWT hợp lệ có `role = 'admin'` |
| Điều kiện thành công / lỗi | Admin xem, thêm, xóa danh mục; tên bắt buộc không rỗng; truy cập hoặc thay đổi trái quyền bị từ chối và dữ liệu không đổi |

Quy ước dữ liệu: `DM-FR14-XEM` là danh mục đã tồn tại để kiểm tra danh sách; `DM-FR14-THEM` chưa tồn tại; `DM-FR14-XOA` và `DM-FR14-BAOVE` đã tồn tại, không gắn dữ liệu phụ thuộc, dùng riêng cho thao tác xóa. Đặc tả không quy định tên phải duy nhất nên trạng thái tồn tại chỉ nhằm làm test data xác định, không tạo oracle về duplicate.

## 2. Biến đầu vào, đầu ra và ràng buộc

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| Trạng thái xác thực và vai trò | Input / trạng thái | Tập điều kiện | Có với phân hệ Admin và API thay đổi dữ liệu | JWT hợp lệ và `role = 'admin'`; thiếu token hoặc role khác không hợp lệ | FR-12 |
| Thao tác quản lý | Input | Tập {Xem, Thêm, Xóa} | Theo thao tác | FR-14 chỉ yêu cầu ba thao tác này | FR-14 |
| Tên danh mục | Input | Chuỗi | Có khi thêm | Không được rỗng; format, trim, tính duy nhất và độ dài tối đa chưa được đặc tả | FR-14 |
| Danh sách danh mục | Output | Danh sách | Khi xem | Hiển thị các danh mục hiện có | FR-14 |
| Kết quả thêm | Output | Thay đổi dữ liệu | Khi thêm | Tên hợp lệ tạo danh mục; tên rỗng bị từ chối và không tạo dữ liệu | FR-14 |
| Kết quả xóa | Output | Thay đổi dữ liệu | Khi xóa | Danh mục được chọn bị xóa | FR-14 |
| Kết quả kiểm soát truy cập | Output | Từ chối / cho phép | Có | Chỉ Admin được dùng phân hệ; POST/DELETE categories cần token Admin | FR-12 |
| Cấu trúc và trình bày trang | Output | UI | Có | Tiếng Việt; đúng một `<h1>`; nút tích cực xanh dương, nút nguy hiểm đỏ; trường bắt buộc có `*`; lỗi ở trên nút submit; mục đang chọn được highlight | FR-21, FR-22, FR-23 |
| Thứ tự focus | Output | Chuỗi focus | Có | Từ trên xuống dưới, trái sang phải | FR-21 |

## 3. Phân vùng tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| EC-AUTH-V01 | Xác thực và vai trò | JWT hợp lệ, role Admin | Hợp lệ | Tài khoản Admin mặc định | Được truy cập và thay đổi danh mục | FR-12 |
| EC-AUTH-I01 | Xác thực và vai trò | Không có JWT hợp lệ: thiếu, sai hoặc hết hạn | Không hợp lệ | POST không có `Authorization` | Request bị từ chối, dữ liệu không đổi | FR-12 |
| EC-AUTH-I02 | Xác thực và vai trò | JWT hợp lệ nhưng role không phải Admin | Không hợp lệ | Token của user test | Truy cập/thay đổi bị từ chối, dữ liệu không đổi | FR-12 |
| EC-ACTION-V01 | Thao tác quản lý | Xem danh sách | Hợp lệ | Mở mục Danh mục | Hiển thị danh mục hiện có | FR-14 |
| EC-ACTION-V02 | Thao tác quản lý | Thêm danh mục | Hợp lệ | Thêm `DM-FR14-THEM` | Danh mục mới được tạo | FR-14 |
| EC-ACTION-V03 | Thao tác quản lý | Xóa danh mục | Hợp lệ | Xóa `DM-FR14-XOA` | Danh mục được chọn bị xóa | FR-14 |
| EC-NAME-V01 | Tên danh mục | Chuỗi không rỗng | Hợp lệ | `DM-FR14-THEM` | Chấp nhận để tạo danh mục | FR-14 |
| EC-NAME-I01 | Tên danh mục | Chuỗi rỗng | Không hợp lệ | `""` | Từ chối, không tạo danh mục | FR-14 |
| EC-PAGE-V01 | Trạng thái trang | Admin mở trang quản lý danh mục | Hợp lệ | Mục Danh mục đang chọn | Áp dụng các yêu cầu giao diện chung | FR-21, FR-22, FR-23 |
| EC-KEYBOARD-V01 | Điều hướng bàn phím | Di chuyển focus bằng Tab | Hợp lệ | Tab qua các control của trang | Focus theo thứ tự quy định | FR-21 |
| EC-RESULT-O01 | Danh sách | Danh mục có sẵn xuất hiện | Output | `DM-FR14-XEM` | Quan sát được trong danh sách | FR-14 |
| EC-RESULT-O02 | Thêm hợp lệ | Danh mục mới được tạo | Output | `DM-FR14-THEM` | Xuất hiện trong danh sách sau thao tác | FR-14 |
| EC-RESULT-O03 | Tên rỗng | Validation từ chối | Output lỗi | Submit `""` | Có lỗi phía trên nút submit và không tạo dữ liệu | FR-14, FR-22 |
| EC-RESULT-O04 | Xóa hợp lệ | Danh mục mục tiêu bị xóa | Output | `DM-FR14-XOA` | Không còn trong danh sách | FR-14 |
| EC-RESULT-O05 | Sai quyền | Truy cập/request bị từ chối | Output lỗi | Thiếu token hoặc user token | Không thay đổi dữ liệu | FR-12 |
| EC-RESULT-O06 | Giao diện trang | Trang tuân thủ các quy tắc UI áp dụng | Output UI | Quan sát/kiểm tra DOM trang | Tiếng Việt, một `<h1>`, màu nút, `*`, active state đúng | FR-21, FR-22, FR-23 |
| EC-RESULT-O07 | Tab order | Focus theo thứ tự | Output UI | Nhấn Tab tuần tự | Từ trên xuống dưới, trái sang phải | FR-21 |

Tên danh mục được chia thành hai lớp theo điều kiện “bắt buộc”: không rỗng và rỗng. Các trạng thái quyền được tách để mỗi ca invalid chỉ vi phạm một điều kiện chính. Không tạo lớp cho sửa danh mục vì FR-14 không yêu cầu thao tác Sửa, dù tiêu đề dùng từ CRUD và API specification có endpoint PUT.

## 4. Quan hệ phụ thuộc giữa đầu vào và trạng thái

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| DC-01 | Thêm danh mục và tên | Tên không rỗng thì có thể tạo | Tên rỗng bị từ chối | Giữ quyền Admin hợp lệ, chỉ thay tên | FR-14 |
| DC-02 | Xóa và dữ liệu hiện có | Danh mục mục tiêu tồn tại | Không có mục tiêu để xóa | Chuẩn bị fixture riêng trước ca xóa | FR-14 |
| DC-03 | API thay đổi dữ liệu và quyền | Token hợp lệ có role Admin | Thiếu token hoặc role khác | Dùng cùng payload/fixture, chỉ thay token | FR-12 |
| DC-04 | Phân hệ Admin và role | Admin được truy cập | User thường bị chặn | Dùng hai tài khoản mặc định | FR-12 |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| COND-FR-14-DT-001 | EC-AUTH-V01, EC-ACTION-V01, EC-PAGE-V01 | Admin mở mục Danh mục; `DM-FR14-XEM` tồn tại | EC-RESULT-O01, EC-RESULT-O06 | Hợp lệ | Danh sách có `DM-FR14-XEM`; trang đáp ứng các yêu cầu UI áp dụng. | Bao phủ Xem và cấu trúc trang trên cùng trạng thái ổn định. |
| COND-FR-14-DT-002 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-V01 | Thêm `DM-FR14-THEM` | EC-RESULT-O02 | Hợp lệ | Tạo danh mục và hiển thị trong danh sách. | Đại diện nominal cho tên không rỗng. |
| COND-FR-14-DT-003 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-I01 | Submit tên `""` | EC-RESULT-O03 | Không hợp lệ | Hiển thị lỗi trên nút submit; không tạo danh mục. | Isolate lớp tên rỗng. |
| COND-FR-14-DT-004 | EC-AUTH-V01, EC-ACTION-V03 | Xóa `DM-FR14-XOA` đã tồn tại | EC-RESULT-O04 | Hợp lệ | Chỉ danh mục mục tiêu bị xóa và không còn trong danh sách. | Bao phủ thao tác Xóa. |
| COND-FR-14-DT-005 | EC-AUTH-I01, EC-ACTION-V02, EC-NAME-V01 | POST `/api/categories`, body `{"name":"DM-FR14-NOTOKEN"}`, không có token | EC-RESULT-O05 | Không hợp lệ | Request bị từ chối; danh mục không được tạo. | Isolate điều kiện thiếu token ở thao tác Thêm. |
| COND-FR-14-DT-006 | EC-AUTH-I02, EC-ACTION-V03 | DELETE danh mục `DM-FR14-BAOVE` bằng token user thường | EC-RESULT-O05 | Không hợp lệ | Request bị từ chối; danh mục vẫn tồn tại. | Isolate điều kiện sai role ở thao tác Xóa. |
| COND-FR-14-DT-007 | EC-AUTH-I02, EC-ACTION-V01 | User thường mở phân hệ Web Admin | EC-RESULT-O05 | Không hợp lệ | User thường không được truy cập chức năng quản lý danh mục. | Bao phủ giới hạn truy cập của phân hệ Admin. |
| COND-FR-14-DT-008 | EC-AUTH-V01, EC-PAGE-V01, EC-KEYBOARD-V01 | Admin dùng Tab trên trang Danh mục | EC-RESULT-O07 | Hợp lệ | Focus đi từ trên xuống dưới, trái sang phải qua các control. | Yêu cầu Tab Order cần thao tác riêng, không thể kết luận bằng quan sát tĩnh. |

## 6. Quá trình lựa chọn ca kiểm thử

Mỗi thao tác FR-14 có ít nhất một ca hợp lệ. Tên rỗng được tách thành ca invalid với quyền Admin hợp lệ; thiếu token và sai role dùng dữ liệu nghiệp vụ hợp lệ để isolate lỗi quyền. Các yêu cầu UI quan sát tĩnh được gộp với ca Xem, còn Tab Order tách riêng vì cần chuỗi thao tác bàn phím. Không tạo Cartesian product giữa mọi action và mọi trạng thái quyền; hai ca API đại diện kiểm tra riêng điều kiện token và role, còn ca giao diện kiểm tra giới hạn của toàn phân hệ.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| TC-FR-14-DT-001 | COND-FR-14-DT-001 | EC-AUTH-V01, EC-ACTION-V01, EC-PAGE-V01; EC-RESULT-O01, O06 | Không áp dụng | FR-14, FR-21, FR-22, FR-23 | Xem danh sách và kiểm tra cấu trúc trang |
| TC-FR-14-DT-002 | COND-FR-14-DT-002 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-V01; EC-RESULT-O02 | DC-01 | FR-14 | Thêm danh mục tên hợp lệ |
| TC-FR-14-DT-003 | COND-FR-14-DT-003 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-I01; EC-RESULT-O03 | DC-01 | FR-14, FR-22 | Từ chối tên rỗng |
| TC-FR-14-DT-004 | COND-FR-14-DT-004 | EC-AUTH-V01, EC-ACTION-V03; EC-RESULT-O04 | DC-02 | FR-14 | Xóa danh mục hiện có |
| TC-FR-14-DT-005 | COND-FR-14-DT-005 | EC-AUTH-I01, EC-ACTION-V02, EC-NAME-V01; EC-RESULT-O05 | DC-03 | FR-12, FR-14 | Thiếu token khi thêm qua API |
| TC-FR-14-DT-006 | COND-FR-14-DT-006 | EC-AUTH-I02, EC-ACTION-V03; EC-RESULT-O05 | DC-02, DC-03 | FR-12, FR-14 | User thường xóa qua API |
| TC-FR-14-DT-007 | COND-FR-14-DT-007 | EC-AUTH-I02, EC-ACTION-V01; EC-RESULT-O05 | DC-04 | FR-12, FR-14 | User thường truy cập Web Admin |
| TC-FR-14-DT-008 | COND-FR-14-DT-008 | EC-AUTH-V01, EC-PAGE-V01, EC-KEYBOARD-V01; EC-RESULT-O07 | Không áp dụng | FR-21 | Tab Order của trang Danh mục |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào hợp lệ / không hợp lệ | 7 / 3 |
| Số lớp đầu ra / quan hệ phụ thuộc | 7 / 4 |
| Số điều kiện / ca kiểm thử | 8 / 8 |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| EC-AUTH-V01, EC-ACTION-V01, EC-PAGE-V01, EC-RESULT-O01, O06 | DT-001 | Đã bao phủ | Chưa chạy | Gộp các quan sát trên cùng trang |
| EC-ACTION-V02, EC-NAME-V01, EC-RESULT-O02, DC-01 | DT-002 | Đã bao phủ | Chưa chạy | Không có |
| EC-NAME-I01, EC-RESULT-O03, DC-01 | DT-003 | Đã bao phủ | Chưa chạy | Không có |
| EC-ACTION-V03, EC-RESULT-O04, DC-02 | DT-004 | Đã bao phủ | Chưa chạy | Không có |
| EC-AUTH-I01, EC-RESULT-O05, DC-03 | DT-005 | Đã bao phủ | Chưa chạy | Chọn trường hợp thiếu token làm đại diện lớp không có JWT hợp lệ |
| EC-AUTH-I02, EC-RESULT-O05, DC-02, DC-03 | DT-006 | Đã bao phủ | Chưa chạy | Không có |
| EC-AUTH-I02, EC-RESULT-O05, DC-04 | DT-007 | Đã bao phủ | Chưa chạy | Không có |
| EC-KEYBOARD-V01, EC-RESULT-O07 | DT-008 | Đã bao phủ | Chưa chạy | Không có |
| Sửa danh mục | Chưa có | Chủ động loại trừ | Chưa chạy | FR-14 không yêu cầu Sửa; không suy ra từ tiêu đề CRUD hoặc API spec |
| Tên trùng, whitespace-only, ký tự/độ dài tối đa | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không tự đặt validation |

## 9. Giả định và thông tin chưa được đặc tả

- Không có quy tắc tên duy nhất, trim khoảng trắng, bộ ký tự, phân biệt hoa thường hoặc độ dài tối đa.
- Không có quy định về thông báo, HTTP status, redirect, dialog xác nhận xóa, thứ tự danh sách hoặc hành vi khi xóa danh mục đang được sản phẩm tham chiếu.
- FR-14 chỉ nêu Thêm/Xem/Xóa; không tạo oracle cho Sửa dù API specification liệt kê endpoint PUT.
- Test data phải được tester chuẩn bị độc lập; việc khôi phục dữ liệu do tester thực hiện và review.

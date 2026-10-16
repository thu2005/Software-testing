# Phân tích kiểm thử miền — FR-07: Giỏ hàng

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-07 / Web |
| Nguồn đặc tả | [system-requirements.md](../../requirements/system-requirements.md#fr-07-giỏ-hàng-shopping-cart) |
| Tác nhân / Điều kiện tiên quyết | Người dùng truy cập trang giỏ hàng; trạng thái đăng nhập không được đặc tả cho FR-07 |
| Điều kiện thành công / lỗi | Hiển thị đúng giỏ; thêm trùng làm tăng số lượng; +/- chỉnh số lượng; xóa phải qua dialog; tiếp tục mua sắm về trang chủ; empty state có hình và thông báo |

## 2. Biến đầu vào, đầu ra và ràng buộc

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| Trạng thái giỏ | Input / trạng thái | Tập hợp | Có | Rỗng hoặc có sản phẩm | FR-07 |
| Quan hệ sản phẩm thêm vào | Input / trạng thái | Quan hệ | Khi thêm | Cùng sản phẩm đã có trong giỏ | FR-07 |
| Thao tác chỉnh số lượng | Input | Tập {+, -} | Khi chỉnh | Có nút + và - | FR-07 |
| Quyết định xóa | Input | Tập {Hủy, Xác nhận} | Khi xóa | Phải có dialog trước khi thực hiện | FR-07 |
| Tiếp tục mua sắm | Input | Hành động | Không | Quay về trang chủ | FR-07 |
| Danh sách sản phẩm | Output | Bảng/danh sách | Không áp dụng | Sản phẩm, Đơn giá, Số lượng có +/-, Thành tiền, Thao tác | FR-07 |
| Nhãn tổng tiền | Output | Chuỗi | Không áp dụng | Chính xác `Tổng cộng`; không phải `Tổng tạm tính` | FR-07 |
| Empty state | Output | UI | Không áp dụng | Có hình minh họa và thông báo rõ ràng | FR-07 |

FR-07 không đặc tả dữ liệu nhập sai, min/max số lượng hoặc hành vi khi bấm `-` tại số lượng thấp nhất. Vì vậy không tạo lớp input invalid cho các quy tắc chưa tồn tại; các sai khác đầu ra được đánh giá là không tuân thủ khi thực thi.

## 3. Phân vùng tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| EC-CART-V01 | Trạng thái giỏ | Có ít nhất một dòng sản phẩm | Hợp lệ | 2 dòng sản phẩm | Hiển thị danh sách sản phẩm | FR-07 |
| EC-CART-V02 | Trạng thái giỏ | Không có dòng sản phẩm | Hợp lệ | 0 dòng | Hiển thị empty state | FR-07 |
| EC-SAME-V01 | Quan hệ sản phẩm thêm vào | Sản phẩm đã có trong giỏ | Hợp lệ | SP-A đã có số lượng 1 | Tăng số lượng, không tạo dòng mới | FR-07 |
| EC-ADJUST-V01 | Thao tác số lượng | Bấm nút + | Hợp lệ | SP-A có số lượng 1 | Số lượng tăng | FR-07 |
| EC-ADJUST-V02 | Thao tác số lượng | Bấm nút - | Hợp lệ | SP-A có số lượng 2 | Số lượng giảm | FR-07 |
| EC-DELETE-V01 | Quyết định tại dialog xóa | Hủy xóa | Hợp lệ | Chọn Hủy | Sản phẩm vẫn còn trong giỏ | FR-07 |
| EC-DELETE-V02 | Quyết định tại dialog xóa | Xác nhận xóa | Hợp lệ | Chọn Xác nhận | Sản phẩm bị xóa | FR-07 |
| EC-NAV-V01 | Thao tác điều hướng | Chọn Tiếp tục mua sắm | Hợp lệ | Bấm nút | Quay về trang chủ | FR-07 |
| EC-RESULT-O01 | Danh sách giỏ | Mỗi dòng có đủ năm cột và nút +/- | Output | Quan sát giỏ có dữ liệu | Hiển thị đúng cấu trúc | FR-07 |
| EC-RESULT-O02 | Kết quả thêm trùng | Số lượng tăng, số dòng không tăng | Output | Thêm lại SP-A | Cập nhật dòng hiện có | FR-07 |
| EC-RESULT-O03 | Kết quả chỉnh số lượng | Số lượng thay đổi theo nút +/- | Output | Bấm + hoặc - | Giá trị số lượng thay đổi | FR-07 |
| EC-RESULT-O04 | Dialog xóa | Dialog xuất hiện trước khi xóa | Output | Bấm Xóa sản phẩm | Chưa xóa trước quyết định | FR-07 |
| EC-RESULT-O05 | Kết quả xóa | Giữ lại hoặc xóa theo quyết định | Output | Hủy/Xác nhận | Trạng thái giỏ tương ứng | FR-07 |
| EC-RESULT-O06 | Điều hướng | Quay về trang chủ | Output | Tiếp tục mua sắm | Trang chủ được mở | FR-07 |
| EC-RESULT-O07 | Nhãn tổng tiền | Nhãn chính xác là Tổng cộng | Output | Quan sát khu vực tổng tiền | Không hiển thị Tổng tạm tính | FR-07 |
| EC-RESULT-O08 | Empty state | Có hình minh họa và thông báo rõ ràng | Output | Giỏ 0 dòng | Hiển thị đủ hai thành phần | FR-07 |

Các trạng thái rỗng/không rỗng, hai thao tác +/- và hai quyết định tại dialog được tách vì tạo hành vi quan sát khác nhau. Không chia lớp âm cho số lượng vì FR-07 không cho phép suy ra miền nhập số hoặc cận hợp lệ.

## 4. Quan hệ phụ thuộc giữa đầu vào và trạng thái

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| DC-01 | Sản phẩm thêm vào và dòng hiện có | Sản phẩm đã có thì tăng số lượng trên dòng đó | Tạo thêm dòng cho cùng sản phẩm | Chuẩn bị giỏ chỉ có một dòng SP-A rồi thêm lại SP-A | FR-07 |
| DC-02 | Xóa và quyết định trong dialog | Chỉ xóa sau khi xác nhận | Xóa trước dialog hoặc khi Hủy | Tách hai ca Hủy và Xác nhận với cùng trạng thái ban đầu | FR-07 |
| DC-03 | Số dòng và cách hiển thị | Có dòng thì hiển thị danh sách; 0 dòng thì hiển thị empty state | Hiển thị sai trạng thái | Chuẩn bị riêng giỏ có dữ liệu và giỏ rỗng | FR-07 |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| COND-FR-07-DT-001 | EC-CART-V01 | Giỏ có SP-A số lượng 2 và SP-B số lượng 1 | EC-RESULT-O01, EC-RESULT-O07 | Hợp lệ | Danh sách có hai dòng; mỗi dòng hiển thị Sản phẩm, Đơn giá, Số lượng với nút +/-, Thành tiền và Thao tác; nhãn tổng tiền là `Tổng cộng`, không phải `Tổng tạm tính`. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-002 | EC-SAME-V01 | Giỏ có đúng một dòng SP-A số lượng 1; thêm lại SP-A | EC-RESULT-O02 | Hợp lệ | Số lượng của SP-A tăng và giỏ vẫn chỉ có một dòng SP-A. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-003 | EC-ADJUST-V01 | Giỏ có SP-A số lượng 1; bấm + | EC-RESULT-O03 | Hợp lệ | Số lượng SP-A tăng so với giá trị 1 ban đầu. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-004 | EC-ADJUST-V02 | Giỏ có SP-A số lượng 2; bấm - | EC-RESULT-O03 | Hợp lệ | Số lượng SP-A giảm so với giá trị 2 ban đầu. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-005 | EC-DELETE-V01 | Giỏ có SP-A; bấm Xóa rồi chọn Hủy | EC-RESULT-O04, EC-RESULT-O05 | Hợp lệ | Dialog xác nhận xuất hiện trước khi xóa; sau khi chọn Hủy, SP-A vẫn còn trong giỏ. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-006 | EC-DELETE-V02 | Giỏ có SP-A; bấm Xóa rồi chọn Xác nhận | EC-RESULT-O04, EC-RESULT-O05 | Hợp lệ | Dialog xác nhận xuất hiện trước khi xóa; SP-A chỉ bị xóa sau khi chọn Xác nhận. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-007 | EC-NAV-V01 | Đang ở trang giỏ hàng | EC-RESULT-O06 | Hợp lệ | Nút `Tiếp tục mua sắm` đưa người dùng về trang chủ. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |
| COND-FR-07-DT-008 | EC-CART-V02 | Giỏ có 0 dòng sản phẩm | EC-RESULT-O08 | Hợp lệ | Trang giỏ hàng hiển thị hình minh họa và thông báo rõ ràng rằng giỏ hàng đang trống. | Đại diện một trạng thái hoặc thao tác có hành vi riêng trong FR-07. |

## 6. Quá trình lựa chọn ca kiểm thử

Mỗi trạng thái hoặc thao tác có hành vi riêng được chọn một đại diện. Hai quyết định Hủy/Xác nhận được tách để xác minh dialog thực sự kiểm soát việc xóa. Nút `-` dùng số lượng ban đầu 2 để không dựa vào hành vi tại cận dưới chưa được đặc tả. Kiểm tra giỏ có dữ liệu gộp các cột bắt buộc và nhãn `Tổng cộng` vì chúng cùng quan sát trên một màn hình. Không tạo Cartesian product giữa số dòng, số lượng và mọi hành động.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| TC-FR-07-DT-001 | COND-FR-07-DT-001 | EC-CART-V01; EC-RESULT-O01, EC-RESULT-O07 | DC-03 | FR-07 | Hiển thị giỏ hàng có sản phẩm |
| TC-FR-07-DT-002 | COND-FR-07-DT-002 | EC-SAME-V01; EC-RESULT-O02 | DC-01 | FR-07 | Thêm lại cùng một sản phẩm |
| TC-FR-07-DT-003 | COND-FR-07-DT-003 | EC-ADJUST-V01; EC-RESULT-O03 | Không áp dụng | FR-07 | Tăng số lượng bằng nút + |
| TC-FR-07-DT-004 | COND-FR-07-DT-004 | EC-ADJUST-V02; EC-RESULT-O03 | Không áp dụng | FR-07 | Giảm số lượng bằng nút - |
| TC-FR-07-DT-005 | COND-FR-07-DT-005 | EC-DELETE-V01; EC-RESULT-O04, EC-RESULT-O05 | DC-02 | FR-07 | Hủy xóa sản phẩm tại dialog xác nhận |
| TC-FR-07-DT-006 | COND-FR-07-DT-006 | EC-DELETE-V02; EC-RESULT-O04, EC-RESULT-O05 | DC-02 | FR-07 | Xác nhận xóa sản phẩm |
| TC-FR-07-DT-007 | COND-FR-07-DT-007 | EC-NAV-V01; EC-RESULT-O06 | Không áp dụng | FR-07 | Tiếp tục mua sắm |
| TC-FR-07-DT-008 | COND-FR-07-DT-008 | EC-CART-V02; EC-RESULT-O08 | DC-03 | FR-07 | Hiển thị giỏ hàng trống |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào hợp lệ / không hợp lệ | 8 / 0 |
| Số lớp đầu ra / quan hệ phụ thuộc | 8 / 3 |
| Số điều kiện / ca kiểm thử | 8 / 8 |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| EC-CART-V01, EC-RESULT-O01, EC-RESULT-O07, DC-03 | TC-FR-07-DT-001 | Đã bao phủ | Chưa chạy | Gộp các quan sát trên cùng trang giỏ có dữ liệu |
| EC-SAME-V01, EC-RESULT-O02, DC-01 | TC-FR-07-DT-002 | Đã bao phủ | Chưa chạy | Không có |
| EC-ADJUST-V01, EC-ADJUST-V02, EC-RESULT-O03 | TC-FR-07-DT-003, TC-FR-07-DT-004 | Đã bao phủ | Chưa chạy | Mỗi nút một ca |
| EC-DELETE-V01, EC-DELETE-V02, EC-RESULT-O04, EC-RESULT-O05, DC-02 | TC-FR-07-DT-005, TC-FR-07-DT-006 | Đã bao phủ | Chưa chạy | Tách hai nhánh dialog |
| EC-NAV-V01, EC-RESULT-O06 | TC-FR-07-DT-007 | Đã bao phủ | Chưa chạy | Không có |
| EC-CART-V02, EC-RESULT-O08, DC-03 | TC-FR-07-DT-008 | Đã bao phủ | Chưa chạy | Không có |
| Số lượng bằng 0/âm; cận trên; thêm sản phẩm khác | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | FR-07 không đặc tả miền hoặc hành vi này |

## 9. Giả định và thông tin chưa được đặc tả

- Không có min/max số lượng, giới hạn số dòng, cách làm tròn/định dạng tiền hoặc công thức tính Thành tiền/Tổng cộng.
- Không có hành vi khi bấm `-` tại số lượng thấp nhất, chỉnh trực tiếp số lượng, thêm sản phẩm chưa có, hay trạng thái đăng nhập.
- Tên nút xác nhận/hủy trong dialog chưa được đặc tả; bước kiểm thử dùng hành động theo ý nghĩa, không áp đặt nhãn UI.
- Các ca chưa được thực thi; trạng thái ban đầu là `Not Run / None`.

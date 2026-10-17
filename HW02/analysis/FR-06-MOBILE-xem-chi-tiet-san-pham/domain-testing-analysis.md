# Phân tích kiểm thử miền — FR-06-MOBILE: Xem chi tiết sản phẩm

## 1. Tóm tắt yêu cầu

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-06 / Mobile (mã tệp `FR-06-MOBILE`) |
| Nguồn đặc tả | [system-requirements.md](../../requirements/system-requirements.md#fr-06-xem-chi-tiết-sản-phẩm), FR-06 và các yêu cầu FR-21, FR-23, FR-24 áp dụng; [api-specification.md](../../requirements/api-specification.md#32-xem-chi-tiết-một-sản-phẩm) |
| Tác nhân / Điều kiện tiên quyết | Người dùng mở ứng dụng Mobile, ứng dụng kết nối được Backend và có sản phẩm fixture trong danh sách |
| Điều kiện thành công / lỗi | Trang hiển thị đủ chi tiết sản phẩm; số lượng chỉ nhận số nguyên dương, tối thiểu 1; thêm vào giỏ với số lượng hợp lệ và có phản hồi trực quan; dữ liệu số lượng không hợp lệ không được chấp nhận |

Quy ước dữ liệu: sản phẩm fixture `SP-FR06-MOBILE` có ảnh hợp lệ, giá `1234000`, mô tả `Sản phẩm dùng kiểm thử FR-06 Mobile` và danh mục `Điện thoại`. Fixture dùng để có oracle cụ thể, không tạo thêm quy tắc nghiệp vụ.

## 2. Biến đầu vào, đầu ra và ràng buộc

| Variable / Condition | Input / Output | Type | Required | Domain / Constraints | Requirement Reference |
|---|---|---|---|---|---|
| Sản phẩm được chọn | Input / trạng thái | Thực thể | Có | Sản phẩm fixture tồn tại và có đủ dữ liệu cần hiển thị | FR-06 |
| Thao tác | Input | Tập {Xem, Nhập số lượng, Thêm vào giỏ} | Theo mục tiêu | Xem chi tiết hoặc thao tác với số lượng trên trang | FR-06 |
| Số lượng | Input | Số nguyên | Có khi thêm giỏ | Số nguyên dương, tối thiểu 1; cận trên chưa được đặc tả | FR-06 |
| Chi tiết sản phẩm | Output | Nhóm dữ liệu | Khi xem | Ảnh lớn, Tên, Giá, Mô tả, Danh mục phải hiển thị đầy đủ | FR-06 |
| Kết quả nhập số lượng | Output | Chấp nhận / từ chối | Có | Chỉ giá trị thuộc tập số nguyên dương được chấp nhận | FR-06 |
| Kết quả thêm giỏ | Output | Thay đổi trạng thái | Khi bấm nút | Sản phẩm với số lượng hợp lệ được thêm vào giỏ | FR-06 |
| Phản hồi sau khi thêm | Output | UI feedback | Có | Toast notification hoặc badge cập nhật | FR-06, FR-24 |
| Trình bày trên Mobile | Output | UI / navigation / accessibility | Có với các quy tắc áp dụng | Tiếng Việt; giá có phân cách hàng nghìn và `₫`; nút tích cực xanh dương; breadcrumb ở Chi tiết sản phẩm; link Giỏ hàng có badge; ảnh sản phẩm có mô tả hỗ trợ truy cập không rỗng | FR-21, FR-23, FR-24 |

## 3. Phân vùng tương đương

| Class ID | Variable / Condition | Description | Validity / Output Category | Representative | Expected Behavior | Requirement Reference |
|---|---|---|---|---|---|---|
| EC-PRODUCT-V01 | Sản phẩm được chọn | Sản phẩm tồn tại, có đủ dữ liệu fixture | Hợp lệ | `SP-FR06-MOBILE` | Mở được trang và hiển thị dữ liệu tương ứng | FR-06 |
| EC-ACTION-V01 | Thao tác | Xem chi tiết sản phẩm | Hợp lệ | Chọn fixture từ danh sách | Hiển thị trang chi tiết | FR-06 |
| EC-ACTION-V02 | Thao tác | Thêm vào giỏ hàng | Hợp lệ | Bấm `Thêm vào giỏ hàng` | Thêm sản phẩm khi số lượng hợp lệ | FR-06 |
| EC-QTY-V01 | Số lượng | Số nguyên dương `q ≥ 1` | Hợp lệ | `3` | Giá trị được chấp nhận | FR-06 |
| EC-QTY-I01 | Số lượng | Không có giá trị | Không hợp lệ | Chuỗi rỗng `""` | Không được chấp nhận làm số lượng thêm giỏ | FR-06 |
| EC-QTY-I02 | Số lượng | Số nguyên không dương `q ≤ 0` | Không hợp lệ | `-1` | Không được chấp nhận | FR-06 |
| EC-QTY-I03 | Số lượng | Số có phần thập phân | Không hợp lệ | `1.5` | Không được chấp nhận vì không phải số nguyên | FR-06 |
| EC-QTY-I04 | Số lượng | Giá trị không phải số | Không hợp lệ | `abc` | Không được chấp nhận | FR-06 |
| EC-PAGE-V01 | Trạng thái trang | Trang chi tiết sản phẩm trên Mobile | Hợp lệ | Fixture đang mở | Áp dụng các yêu cầu giao diện chung có ý nghĩa trên Mobile | FR-21, FR-23, FR-24 |
| EC-RESULT-O01 | Chi tiết sản phẩm | Hiển thị đủ năm thành phần | Output | Dữ liệu fixture | Ảnh lớn, Tên, Giá, Mô tả, Danh mục đều quan sát được | FR-06 |
| EC-RESULT-O02 | Giao diện Mobile | Các quy tắc UI/navigation/accessibility áp dụng được đáp ứng | Output UI | Quan sát trang và dùng trình đọc màn hình | Tiếng Việt, định dạng giá, màu nút, breadcrumb, badge và mô tả ảnh đúng yêu cầu | FR-21, FR-23, FR-24 |
| EC-RESULT-O03 | Số lượng hợp lệ | Control nhận số nguyên dương | Output hợp lệ | `3` | Giá trị được giữ và có thể dùng cho thao tác thêm | FR-06 |
| EC-RESULT-O04 | Số lượng không hợp lệ | Control hoặc validation từ chối | Output lỗi | `""`, `-1`, `1.5`, `abc` | Không dùng giá trị không hợp lệ để thêm sản phẩm; cách chặn và nội dung lỗi chưa được đặc tả | FR-06 |
| EC-RESULT-O05 | Thêm giỏ thành công | Sản phẩm được thêm và có phản hồi trực quan | Output thành công | Số lượng `5` | Giỏ nhận sản phẩm với số lượng đã chọn; toast hoặc badge cập nhật | FR-06, FR-24 |

Số lượng được chia theo kiểu và dấu: số nguyên dương; số nguyên không dương; số có phần thập phân; không phải số; và thiếu giá trị. Các lớp invalid được tách để mỗi ca chỉ vi phạm một điều kiện chính. Trạng thái sản phẩm không tồn tại không được tạo lớp kiểm thử vì đặc tả không quy định hành vi lỗi cho ID không tồn tại.

## 4. Quan hệ phụ thuộc giữa đầu vào và trạng thái

| Dependency ID | Dependency | Valid Condition | Invalid Condition | Feasibility / Isolation | Requirement Reference |
|---|---|---|---|---|---|
| DC-01 | Sản phẩm được chọn và dữ liệu chi tiết | Fixture tồn tại, dữ liệu đầy đủ | Sản phẩm không tồn tại hoặc dữ liệu nguồn thiếu | Giữ cùng một fixture cho toàn bộ bộ test; hành vi lỗi nguồn dữ liệu chưa được đặc tả | FR-06 |
| DC-02 | Số lượng và thao tác thêm giỏ | `q` là số nguyên và `q ≥ 1` | Rỗng, `q ≤ 0`, thập phân hoặc không phải số | Giữ sản phẩm và trạng thái giỏ ổn định, chỉ thay số lượng | FR-06 |
| DC-03 | Thêm giỏ và phản hồi | Thao tác thêm với số lượng hợp lệ hoàn tất | Không có thao tác thành công | Quan sát toast hoặc badge ngay sau cùng thao tác | FR-06, FR-24 |

## 5. Ma trận miền

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Validity | Expected Result | Selection Reason |
|---|---|---|---|---|---|---|
| COND-FR-06-MOBILE-DT-001 | EC-PRODUCT-V01, EC-ACTION-V01 | Mở `SP-FR06-MOBILE` | EC-RESULT-O01 | Hợp lệ | Hiển thị đúng ảnh lớn, tên, giá, mô tả và danh mục của fixture. | Bao phủ output cốt lõi của FR-06. |
| COND-FR-06-MOBILE-DT-002 | EC-PRODUCT-V01, EC-PAGE-V01 | Quan sát trang fixture; dùng trình đọc màn hình cho ảnh | EC-RESULT-O02 | Hợp lệ | Các quy tắc UI/navigation/accessibility có ý nghĩa trên Mobile được đáp ứng. | Gộp các quan sát tĩnh trên cùng trạng thái trang. |
| COND-FR-06-MOBILE-DT-003 | EC-PRODUCT-V01, EC-QTY-V01 | Nhập `3` | EC-RESULT-O03 | Hợp lệ | Control chấp nhận và giữ số lượng `3`. | Đại diện nominal cho miền số nguyên dương. |
| COND-FR-06-MOBILE-DT-004 | EC-PRODUCT-V01, EC-QTY-I01 | Xóa toàn bộ giá trị thành `""` | EC-RESULT-O04 | Không hợp lệ | Không dùng giá trị rỗng để thêm sản phẩm. | Isolate lớp thiếu giá trị. |
| COND-FR-06-MOBILE-DT-005 | EC-PRODUCT-V01, EC-QTY-I02 | Nhập `-1` | EC-RESULT-O04 | Không hợp lệ | Không chấp nhận số nguyên âm. | Đại diện ngoài miền không dương, tách khỏi cận 0 của BVA. |
| COND-FR-06-MOBILE-DT-006 | EC-PRODUCT-V01, EC-QTY-I03 | Nhập `1.5` | EC-RESULT-O04 | Không hợp lệ | Không chấp nhận số có phần thập phân. | Isolate ràng buộc số nguyên. |
| COND-FR-06-MOBILE-DT-007 | EC-PRODUCT-V01, EC-QTY-I04 | Nhập `abc` | EC-RESULT-O04 | Không hợp lệ | Không chấp nhận giá trị không phải số. | Isolate lớp sai kiểu. |
| COND-FR-06-MOBILE-DT-008 | EC-PRODUCT-V01, EC-ACTION-V02, EC-QTY-V01 | Nhập `5`, bấm `Thêm vào giỏ hàng` | EC-RESULT-O05 | Hợp lệ | Thêm fixture với số lượng `5` và hiển thị toast hoặc badge cập nhật. | Bao phủ hành động chính và feedback bằng dữ liệu nominal riêng. |

## 6. Quá trình lựa chọn ca kiểm thử

Ca xem chi tiết và ca kiểm tra giao diện được tách vì một ca đối chiếu dữ liệu nghiệp vụ, ca còn lại cần kiểm tra navigation và hỗ trợ truy cập. Giá trị `3` đại diện miền số nguyên dương; `5` dùng riêng cho hành động thêm giỏ để kết quả dễ nhận biết. Bốn lớp invalid dùng cùng fixture hợp lệ và chỉ thay số lượng. `0`, `1`, `2` được chuyển sang BVA để chứng minh cận dưới thay vì lặp trong Domain Testing.

## 7. Ma trận truy vết

| Test Case ID | Test Condition ID | Input / Output Classes | Dependency ID | Requirement Reference | Selection Reason |
|---|---|---|---|---|---|
| TC-FR-06-MOBILE-DT-001 | COND-FR-06-MOBILE-DT-001 | EC-PRODUCT-V01, EC-ACTION-V01; EC-RESULT-O01 | DC-01 | FR-06 | Hiển thị đủ dữ liệu sản phẩm |
| TC-FR-06-MOBILE-DT-002 | COND-FR-06-MOBILE-DT-002 | EC-PRODUCT-V01, EC-PAGE-V01; EC-RESULT-O02 | DC-01 | FR-21, FR-23, FR-24 | UI/navigation/accessibility áp dụng trên Mobile |
| TC-FR-06-MOBILE-DT-003 | COND-FR-06-MOBILE-DT-003 | EC-QTY-V01; EC-RESULT-O03 | DC-02 | FR-06 | Đại diện số nguyên dương |
| TC-FR-06-MOBILE-DT-004 | COND-FR-06-MOBILE-DT-004 | EC-QTY-I01; EC-RESULT-O04 | DC-02 | FR-06 | Giá trị rỗng |
| TC-FR-06-MOBILE-DT-005 | COND-FR-06-MOBILE-DT-005 | EC-QTY-I02; EC-RESULT-O04 | DC-02 | FR-06 | Số nguyên âm |
| TC-FR-06-MOBILE-DT-006 | COND-FR-06-MOBILE-DT-006 | EC-QTY-I03; EC-RESULT-O04 | DC-02 | FR-06 | Số thập phân |
| TC-FR-06-MOBILE-DT-007 | COND-FR-06-MOBILE-DT-007 | EC-QTY-I04; EC-RESULT-O04 | DC-02 | FR-06 | Giá trị không phải số |
| TC-FR-06-MOBILE-DT-008 | COND-FR-06-MOBILE-DT-008 | EC-ACTION-V02, EC-QTY-V01; EC-RESULT-O05 | DC-02, DC-03 | FR-06, FR-24 | Thêm giỏ và feedback |

## 8. Tổng kết độ bao phủ

| Metric | Value |
|---|---|
| Số lớp đầu vào hợp lệ / không hợp lệ | 5 / 4 |
| Số lớp đầu ra / quan hệ phụ thuộc | 5 / 3 |
| Số điều kiện / ca kiểm thử | 8 / 8 |

| Class / Dependency ID | Test Case IDs | Design Coverage | Execution Coverage | Gap / Exclusion Reason |
|---|---|---|---|---|
| EC-PRODUCT-V01, EC-ACTION-V01, EC-RESULT-O01, DC-01 | DT-001 | Đã bao phủ | Chưa chạy | Không có |
| EC-PAGE-V01, EC-RESULT-O02 | DT-002 | Đã bao phủ | Chưa chạy | Gộp quan sát tĩnh và kiểm tra accessibility trên cùng trang |
| EC-QTY-V01, EC-RESULT-O03, DC-02 | DT-003, DT-008 | Đã bao phủ | Chưa chạy | Tách nhập nominal và hành động thêm giỏ |
| EC-QTY-I01, EC-RESULT-O04 | DT-004 | Đã bao phủ | Chưa chạy | Không có |
| EC-QTY-I02, EC-RESULT-O04 | DT-005 | Đã bao phủ | Chưa chạy | Không có |
| EC-QTY-I03, EC-RESULT-O04 | DT-006 | Đã bao phủ | Chưa chạy | Không có |
| EC-QTY-I04, EC-RESULT-O04 | DT-007 | Đã bao phủ | Chưa chạy | Không có |
| EC-ACTION-V02, EC-RESULT-O05, DC-03 | DT-008 | Đã bao phủ | Chưa chạy | Không có |
| Sản phẩm không tồn tại / lỗi tải chi tiết | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không có expected behavior, loading/error state cho trang chi tiết |
| Số lượng tối đa / tồn kho | Chưa có | Bị chặn do thiếu requirement | Chưa chạy | Không tự đặt cận trên hoặc quan hệ tồn kho |

## 9. Giả định và thông tin chưa được đặc tả

- Không có quy định về số lượng tối đa, tồn kho, giá trị mặc định, cách hiển thị lỗi hoặc cách control ngăn dữ liệu không hợp lệ.
- Không có expected behavior cho sản phẩm không tồn tại, API lỗi, ảnh lỗi hoặc trạng thái loading của trang chi tiết.
- FR-21 dùng thuật ngữ HTML `<h1>` và Tab Order; cách ánh xạ sang React Native chưa được đặc tả nên không tạo oracle cho hai mục này. FR-23 và FR-24 được kiểm tra theo kết quả quan sát được trên Mobile.
- FR-22 không nói rõ ô Số lượng của FR-06 là trường bắt buộc có nhãn `*` hay có giá trị mặc định trên Mobile; bộ test không tự áp đặt ký hiệu này.
- Đặc tả không yêu cầu đăng nhập để xem hoặc thêm giỏ trong FR-06; bộ test không tự thêm điều kiện xác thực.
- Fixture và trạng thái giỏ phải được tester chuẩn bị độc lập; việc khôi phục dữ liệu do tester thực hiện và review.

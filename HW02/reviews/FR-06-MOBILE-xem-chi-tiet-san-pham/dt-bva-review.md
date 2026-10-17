# Rà soát ca kiểm thử — FR-06-MOBILE: Xem chi tiết sản phẩm

## 1. Phạm vi rà soát

- Đặc tả: `requirements/system-requirements.md`, FR-06 và các yêu cầu FR-21, FR-23, FR-24 áp dụng; `requirements/api-specification.md`, endpoint chi tiết sản phẩm.
- Phân tích: `analysis/FR-06-MOBILE-xem-chi-tiet-san-pham/domain-testing-analysis.md` và `bva-analysis.md`.
- Ca kiểm thử: 8 ca Domain Testing và 3 ca Boundary Value Analysis trong `tests/test-cases/FR-06-MOBILE-xem-chi-tiet-san-pham/`.
- Kỹ thuật và nền tảng: Domain Testing + Boundary Value Analysis / React Native Mobile.

## 2. Tóm tắt kết quả

Đã thực thi đủ 11 test case trên Android Emulator: 1 Pass, 10 Fail, không có Blocked hoặc Not Run. Mười ca Fail quy về 6 bug độc lập: thiếu danh mục; thiếu breadcrumb; sai màu nút tích cực; thiếu mô tả accessibility; chấp nhận năm lớp số lượng không hợp lệ; và màn hình giỏ Mobile trắng. DT-008, BVA-002, BVA-003 giữ trạng thái Fail vì màn hình trắng là sai lệch quan sát được của SUT, không phải trở ngại môi trường.

## 3. Phát hiện cần sửa

| Finding ID | Severity | File / Location | Issue | Impact | Proposed Correction | Status |
|---|---|---|---|---|---|---|
| REV-FR-06-MOBILE-001 | Major | TC-FR-06-MOBILE-DT-004 đến DT-007 | Oracle nói sản phẩm không được thêm nhưng dữ liệu và bước chạy chưa cố định giỏ ban đầu. | Tester không thể phân biệt item có sẵn với item mới bị thêm bởi giá trị invalid. | Ghi giỏ ban đầu không có fixture và thêm bước bảo đảm trạng thái này trước thao tác. | Đã sửa |
| REV-FR-06-MOBILE-002 | Major | BVA analysis và TC-FR-06-MOBILE-BVA-001 | Oracle ban đầu yêu cầu không thêm và không có feedback khi nhập `0`, trong khi control tự chuẩn hóa thành `1` trước submit vẫn tuân thủ `q ≥ 1`. | Có thể kết luận Fail cho một cách xử lý hợp lệ nhưng chưa được đặc tả. | Đánh giá số lượng hiệu lực: `0` không được dùng; chấp nhận từ chối hoặc chuẩn hóa về số nguyên dương trước thao tác. | Đã sửa |
| REV-FR-06-MOBILE-003 | Minor | Domain analysis, mục giả định | Chưa nói rõ vì sao không kiểm tra dấu `*` của FR-22 cho ô Số lượng trên Mobile. | Reviewer có thể hiểu nhầm đây là coverage gap bị bỏ quên. | Ghi FR-06 không đặc tả ô Số lượng là trường bắt buộc có nhãn `*` hay có giá trị mặc định; không tự áp đặt oracle. | Đã sửa |

## 4. Kiểm tra truy vết

| Test Case ID | Requirement Reference | Analysis Condition | Class / Boundary / Output ID | Status | Notes |
|---|---|---|---|---|---|
| TC-FR-06-MOBILE-DT-001 | FR-06 | COND-FR-06-MOBILE-DT-001 | EC-PRODUCT-V01, EC-ACTION-V01; EC-RESULT-O01; DC-01 | Hợp lệ | Đối chiếu đủ năm thành phần với fixture cụ thể. |
| TC-FR-06-MOBILE-DT-002 | FR-21, FR-23, FR-24 | COND-FR-06-MOBILE-DT-002 | EC-PAGE-V01; EC-RESULT-O02 | Hợp lệ | Gộp quan sát tĩnh và kiểm tra ảnh bằng công cụ accessibility. |
| TC-FR-06-MOBILE-DT-003 | FR-06 | COND-FR-06-MOBILE-DT-003 | EC-QTY-V01; EC-RESULT-O03; DC-02 | Hợp lệ | Đại diện nominal `3`, không trùng điểm biên. |
| TC-FR-06-MOBILE-DT-004 | FR-06 | COND-FR-06-MOBILE-DT-004 | EC-QTY-I01; EC-RESULT-O04; DC-02 | Hợp lệ | Isolate thiếu giá trị. |
| TC-FR-06-MOBILE-DT-005 | FR-06 | COND-FR-06-MOBILE-DT-005 | EC-QTY-I02; EC-RESULT-O04; DC-02 | Hợp lệ | Đại diện `-1`, tách khỏi điểm biên `0`. |
| TC-FR-06-MOBILE-DT-006 | FR-06 | COND-FR-06-MOBILE-DT-006 | EC-QTY-I03; EC-RESULT-O04; DC-02 | Hợp lệ | Isolate số thập phân `1.5`. |
| TC-FR-06-MOBILE-DT-007 | FR-06 | COND-FR-06-MOBILE-DT-007 | EC-QTY-I04; EC-RESULT-O04; DC-02 | Hợp lệ | Isolate giá trị không phải số `abc`. |
| TC-FR-06-MOBILE-DT-008 | FR-06, FR-24 | COND-FR-06-MOBILE-DT-008 | EC-ACTION-V02, EC-QTY-V01; EC-RESULT-O05; DC-02, DC-03 | Hợp lệ | Thêm giỏ với nominal `5` và kiểm tra feedback. |
| TC-FR-06-MOBILE-BVA-001 | FR-06 | COND-FR-06-MOBILE-BVA-001 | BV-QTY-001; DB-01 | Hợp lệ | OFF⁻ bằng `0`, không áp đặt cơ chế validation. |
| TC-FR-06-MOBILE-BVA-002 | FR-06, FR-24 | COND-FR-06-MOBILE-BVA-002 | BV-QTY-002; DB-01 | Hợp lệ | ON bằng `1`, nhỏ nhất hợp lệ. |
| TC-FR-06-MOBILE-BVA-003 | FR-06, FR-24 | COND-FR-06-MOBILE-BVA-003 | BV-QTY-003; DB-01 | Hợp lệ | OFF⁺ bằng `2`, ngay trong miền. |

## 5. Độ bao phủ và ca trùng lặp

| Coverage Item | Test Case IDs | Coverage Status | Duplicate / Gap | Notes |
|---|---|---|---|---|
| Ảnh lớn, Tên, Giá, Mô tả, Danh mục | DT-001 | Đã cover | Không | Fixture có giá trị cụ thể cho từng trường. |
| Tiếng Việt, màu nút, tiền tệ, breadcrumb, badge, mô tả ảnh | DT-002 | Đã cover | Gộp có chủ đích | Cùng trạng thái trang; accessibility cần công cụ hỗ trợ. |
| Số nguyên dương | DT-003, DT-008; BVA-002, BVA-003 | Đã cover | Trùng có chủ đích giữa DT/BVA | DT dùng nominal `3/5`; BVA chứng minh `1/2`. |
| Số lượng rỗng | DT-004 | Đã cover | Không | Lớp thiếu giá trị. |
| Số nguyên không dương | DT-005; BVA-001 | Đã cover | Trùng có chủ đích | DT dùng `-1`; BVA dùng điểm ngay dưới cận `0`. |
| Số thập phân | DT-006 | Đã cover | Không | Kiểm tra ràng buộc số nguyên. |
| Không phải số | DT-007 | Đã cover | Không | Kiểm tra sai kiểu. |
| Thêm giỏ và feedback | DT-008; BVA-002, BVA-003 | Đã cover | Trùng có chủ đích | BVA cần thao tác thêm để quan sát tính hợp lệ tại cận. |
| Cận dưới `0/1/2` | BVA-001 đến BVA-003 | Đã cover | Không | Robust BVA tại cận dưới đóng 1. |
| Cận trên / tồn kho | Chưa có | Bị chặn do thiếu đặc tả | Requirement gap | Không tự đặt giới hạn. |
| Sản phẩm không tồn tại, loading, lỗi API/ảnh | Chưa có | Bị chặn do thiếu đặc tả | Requirement gap | FR-06 không nêu expected behavior. |
| `<h1>`, Tab Order, dấu `*` của ô Số lượng | Chưa có | Bị chặn do thiếu ánh xạ/đặc tả Mobile | Không phải test omission đã xác nhận | Không chuyển thuật ngữ Web sang React Native hoặc suy ra field bắt buộc. |

## 6. Kết luận sau thực thi

Test run, 11 test case, hai tài liệu phân tích và 6 bug report đã được đồng bộ hai chiều. Kết quả `1 Pass / 10 Fail` khớp 14 evidence: một ảnh Pass, tám ảnh Fail đơn và ba cặp ảnh phản hồi–giỏ trắng. Năm ca invalid cùng liên kết `BUG-FR06-005`; ba ca số lượng hợp lệ không kiểm tra được trong giỏ cùng liên kết `BUG-FR06-006`. Ba sai lệch trong DT-002 được tách thành ba bug vì có tiêu chí sửa độc lập.

## 7. Rà soát của sinh viên và thông tin còn thiếu

- Rà soát/chỉnh sửa của sinh viên: Done.
- Môi trường: Android Emulator Pixel 4a (`sdk_gphone64_x86_64`), Android 13 API 33, `1080×2340`, Expo Go / Expo SDK 54, SUT commit `85af3ba875c88283615e22cb108f13e2fccaf0e9`.
- Chuẩn bị và khôi phục dữ liệu: do tester thực hiện và review.
- Chưa được đặc tả: số lượng tối đa, tồn kho, giá trị mặc định, nội dung validation, hành vi sản phẩm không tồn tại/loading/lỗi API, và cách ánh xạ `<h1>`/Tab Order/dấu `*` sang React Native.
- GitHub Issues: đã đăng Issues #16–#21 tại `thu2005/CSC13003_eshop`; sáu bug report đã có URL thật và ảnh chụp trang issue trong `bug-reports/screenshots/`.

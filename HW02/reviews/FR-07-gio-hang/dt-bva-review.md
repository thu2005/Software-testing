# Rà soát ca kiểm thử — FR-07: Giỏ hàng

## 1. Phạm vi rà soát

- Đặc tả: `requirements/system-requirements.md`, mục FR-07.
- Phân tích: `analysis/FR-07-gio-hang/domain-testing-analysis.md` và `bva-analysis.md`.
- Ca kiểm thử: 8 ca Domain Testing và 3 ca Boundary Value Analysis trong `tests/test-cases/FR-07-gio-hang/`.
- Kỹ thuật và nền tảng: Domain Testing + Boundary Value Analysis / Web.

## 2. Tóm tắt kết quả

Vòng đầu phát hiện một suy diễn ngoài đặc tả ở nhánh Hủy của dialog xóa và một điểm dữ liệu chưa đủ cụ thể ở ký hiệu `SP-A`/`SP-B`. Sau khi sửa, 11 test case có dữ liệu, bước chạy, oracle và liên kết truy vết nhất quán. Bộ test bao phủ toàn bộ hành vi được nêu trong FR-07; không đặt cận số lượng hoặc hành vi ở cận khi requirement không cung cấp. Các phát hiện thiết kế nằm ở mục 3–5; kết quả thực thi và hồ sơ defect được tổng hợp ở mục 6–7.

## 3. Phát hiện cần sửa

| Finding ID | Severity | File / Location | Issue | Impact | Proposed Correction | Status |
|---|---|---|---|---|---|---|
| REV-FR-07-001 | Major | Domain analysis và TC-FR-07-DT-005 ban đầu | Ca kiểm tra chọn Hủy giả định dialog có nhánh Hủy và quy định hành vi sau Hủy, trong khi FR-07 chỉ yêu cầu dialog xác nhận trước khi xóa. | Oracle vượt quá đặc tả và có thể kết luận sai. | Đổi ca 005 thành kiểm tra dialog xuất hiện và sản phẩm chưa bị xóa trước quyết định; giữ ca 006 cho hành động xác nhận xóa. | Đã sửa |
| REV-FR-07-002 | Minor | Analysis và test data ban đầu | `SP-A` và `SP-B` chưa có định nghĩa fixture cụ thể. | Tester khó xác định hai sản phẩm có thực sự phân biệt và tái sử dụng dữ liệu nhất quán. | Định nghĩa `SP-A` là ID `FR07-A`, tên `Áo kiểm thử FR07`; `SP-B` là ID `FR07-B`, tên `Túi kiểm thử FR07`. | Đã sửa |

## 4. Kiểm tra truy vết

| Test Case ID | Requirement Reference | Analysis Condition | Class / Boundary / Output ID | Status | Notes |
|---|---|---|---|---|---|
| TC-FR-07-DT-001 | FR-07 | COND-FR-07-DT-001 | EC-CART-V01; EC-RESULT-O01, O07; DC-03 | Hợp lệ | Kiểm tra năm cột, nút +/- và nhãn `Tổng cộng`. |
| TC-FR-07-DT-002 | FR-07 | COND-FR-07-DT-002 | EC-SAME-V01; EC-RESULT-O02; DC-01 | Hợp lệ | Thêm cùng sản phẩm làm tăng số lượng, không thêm dòng. |
| TC-FR-07-DT-003 | FR-07 | COND-FR-07-DT-003 | EC-ADJUST-V01; EC-RESULT-O03 | Hợp lệ | Kiểm tra nút + với số lượng ban đầu 1. |
| TC-FR-07-DT-004 | FR-07 | COND-FR-07-DT-004 | EC-ADJUST-V02; EC-RESULT-O03 | Hợp lệ | Kiểm tra nút - với số lượng ban đầu 2, tránh cận chưa đặc tả. |
| TC-FR-07-DT-005 | FR-07 | COND-FR-07-DT-005 | EC-DELETE-V01; EC-RESULT-O04; DC-02 | Hợp lệ | Chỉ kiểm tra dialog và thứ tự trước khi xóa. |
| TC-FR-07-DT-006 | FR-07 | COND-FR-07-DT-006 | EC-DELETE-V02; EC-RESULT-O04, O05; DC-02 | Hợp lệ | Xóa sau khi xác nhận. |
| TC-FR-07-DT-007 | FR-07 | COND-FR-07-DT-007 | EC-NAV-V01; EC-RESULT-O06 | Hợp lệ | Nút Tiếp tục mua sắm về trang chủ. |
| TC-FR-07-DT-008 | FR-07 | COND-FR-07-DT-008 | EC-CART-V02; EC-RESULT-O08; DC-03 | Hợp lệ | Empty state có hình và thông báo. |
| TC-FR-07-BVA-001 | FR-07 | COND-FR-07-BVA-001 | BV-ROWS-001; DB-01 | Hợp lệ | ON=0 dòng. |
| TC-FR-07-BVA-002 | FR-07 | COND-FR-07-BVA-002 | BV-ROWS-002; DB-01 | Hợp lệ | OFF⁺=1 dòng. |
| TC-FR-07-BVA-003 | FR-07 | COND-FR-07-BVA-003 | BV-ROWS-003; DB-01 | Hợp lệ | Đại diện bên trong=2 dòng. |

## 5. Độ bao phủ và ca trùng lặp

| Coverage Item | Test Case IDs | Coverage Status | Duplicate / Gap | Notes |
|---|---|---|---|---|
| Danh sách và năm cột bắt buộc | DT-001; BVA-002, BVA-003 | Đã cover | Trùng có chủ đích giữa hai kỹ thuật | DT kiểm tra cấu trúc; BVA chứng minh ở 1 và 2 dòng. |
| Thêm cùng sản phẩm | DT-002 | Đã cover | Không | Kiểm tra cả số lượng và số dòng. |
| Nút +/- | DT-003, DT-004 | Đã cover | Không | Mỗi hướng điều chỉnh một ca. |
| Dialog trước khi xóa | DT-005, DT-006 | Đã cover | Trùng quan sát có chủ đích | DT-005 cô lập việc mở dialog; DT-006 đi tiếp tới xác nhận. |
| Xóa sau xác nhận | DT-006 | Đã cover | Không | Không suy ra nhánh Hủy. |
| Tiếp tục mua sắm | DT-007 | Đã cover | Không | Đích đến là trang chủ theo FR-07. |
| Nhãn `Tổng cộng` | DT-001; BVA-002, BVA-003 | Đã cover | Trùng có chủ đích | Kiểm tra chính xác chuỗi và loại trừ `Tổng tạm tính`. |
| Empty state | DT-008; BVA-001 | Đã cover | Trùng có chủ đích giữa hai kỹ thuật | Yêu cầu cả hình minh họa và thông báo. |
| Biên số dòng 0/1 và đại diện 2 | BVA-001 đến BVA-003 | Đã cover | Không | -1 không khả thi; cận trên chưa được đặc tả. |
| Biên số lượng, hành vi tại số lượng thấp nhất | Chưa có | Bị chặn do thiếu đặc tả | Requirement gap | Không tự đặt min/max hoặc hành vi nút -. |
| Lớp input invalid | Chưa có | Không áp dụng | Không phải coverage gap | FR-07 không nêu dữ liệu nhập sai hoặc miền số lượng. |

## 6. Kết luận sau rà soát và thực thi

Bộ test đã được sinh viên review, duyệt và thực thi đủ 11/11 ca. Kết quả gồm 1 Pass, 10 Fail, 0 Blocked và 0 Not Run; 10 ca Fail được nhóm thành 6 defect riêng biệt. Expected Result không thay đổi trong quá trình ghi nhận execution. Sáu bug report đã liên kết với GitHub Issue #5–#10 trong repository SUT và có ảnh trang issue trong repository bài làm.

## 7. Rà soát của sinh viên và thông tin còn thiếu

- Rà soát/chỉnh sửa của sinh viên: sinh viên xác nhận đã review và duyệt bộ test case trước khi thực thi.
- Chưa được đặc tả: min/max số lượng, hành vi nút `-` tại số lượng thấp nhất, cận trên số dòng, thêm sản phẩm khác, định dạng/công thức tiền, nhãn cụ thể của nút xác nhận và trạng thái đăng nhập.
- Kết quả thực thi được lưu tại `tests/test-runs/FR-07-gio-hang-run.md`; 10 Fail đã được nhóm thành 6 defect riêng biệt.
- Human review: hoàn tất. Hồ sơ defect đã đăng tại GitHub Issue #5–#10 của `thu2005/CSC13003_eshop`; bug report và evidence được lưu tại `thu2005/Software-testing`.

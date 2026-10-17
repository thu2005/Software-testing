# Rà soát ca kiểm thử — FR-14: Quản lý Danh mục

## 1. Phạm vi rà soát

- Đặc tả: `requirements/system-requirements.md`, FR-12, FR-14 và các yêu cầu FR-21 đến FR-23 áp dụng; `requirements/api-specification.md`, mục Categories.
- Phân tích: `analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md` và `bva-analysis.md`.
- Ca kiểm thử: 8 ca Domain Testing và 3 ca Boundary Value Analysis trong `tests/test-cases/FR-14-quan-ly-danh-muc/`.
- Kỹ thuật và nền tảng: Domain Testing + Boundary Value Analysis / Web Admin và API categories liên quan.

## 2. Tóm tắt kết quả

Sau khi sửa năm finding thiết kế, 11/11 test case đã được thực thi và có evidence: 6 Pass, 5 Fail, 0 Blocked. Năm ca Fail quy về 5 bug độc lập; DT-003 và BVA-001 cùng phát hiện lỗi chấp nhận tên rỗng nên không đếm hai lần. Actual Result, trạng thái test case, test run, analysis và bug report đã được đối chiếu nhất quán.

## 3. Phát hiện cần sửa

| Finding ID | Severity | File / Location | Issue | Impact | Proposed Correction | Status |
|---|---|---|---|---|---|---|
| REV-FR-14-001 | Minor | TC-FR-14-DT-002, Test Data ban đầu | `DM-FR14-THEM` được ghi 14 ký tự nhưng độ dài thực là 12. | Dữ liệu mô tả không khớp chuỗi thực tế. | Đếm lại và sửa thành 12 ký tự. | Đã sửa |
| REV-FR-14-002 | Minor | TC-FR-14-DT-006, Request ban đầu | Endpoint DELETE còn placeholder ID, chưa nói cách lấy ID thật. | Tester không có request cụ thể để chạy. | Ghi `:id` lấy từ dòng `DM-FR14-BAOVE` trong danh sách hiện tại. | Đã sửa |
| REV-FR-14-003 | Minor | Domain analysis, EC-AUTH-I01 ban đầu | Lớp token không hợp lệ chỉ mô tả trường hợp thiếu token, hẹp hơn điều kiện “JWT hợp lệ” của FR-12. | Mô hình miền không thể hiện đầy đủ phần bù của lớp hợp lệ. | Mở rộng lớp thành thiếu, sai hoặc hết hạn; giữ thiếu token làm đại diện. | Đã sửa |
| REV-FR-14-004 | Minor | TC-FR-14-DT-008, Expected Result ban đầu | Oracle thêm điều kiện “không bỏ qua control”, trong khi FR-21 chỉ quy định thứ tự focus. | Có thể kết luận Fail dựa trên yêu cầu không được nêu rõ. | Giữ oracle đúng câu chữ: từ trên xuống dưới, trái sang phải. | Đã sửa |
| REV-FR-14-005 | Minor | Trường tham chiếu của các test case dùng yêu cầu chéo | Một số ca có truy vết FR-12 hoặc FR-21 đến FR-23 trong analysis nhưng liên kết ở file test case chỉ trỏ tới FR-14. | Người review khó mở đúng đoạn đặc tả tạo oracle. | Thêm liên kết trực tiếp tới các FR chéo tương ứng ở từng test case. | Đã sửa |

## 4. Kiểm tra truy vết

| Test Case ID | Requirement Reference | Analysis Condition | Class / Boundary / Output ID | Status | Notes |
|---|---|---|---|---|---|
| TC-FR-14-DT-001 | FR-14, FR-21, FR-22, FR-23 | COND-FR-14-DT-001 | EC-AUTH-V01, EC-ACTION-V01, EC-PAGE-V01; EC-RESULT-O01, O06 | Hợp lệ | Xem danh sách và quan sát các yêu cầu UI trên cùng trang. |
| TC-FR-14-DT-002 | FR-14 | COND-FR-14-DT-002 | EC-AUTH-V01, EC-ACTION-V02, EC-NAME-V01; EC-RESULT-O02; DC-01 | Hợp lệ | Tên nominal 12 ký tự. |
| TC-FR-14-DT-003 | FR-14, FR-22 | COND-FR-14-DT-003 | EC-NAME-I01; EC-RESULT-O03; DC-01 | Hợp lệ | Isolate tên rỗng với quyền Admin hợp lệ. |
| TC-FR-14-DT-004 | FR-14 | COND-FR-14-DT-004 | EC-ACTION-V03; EC-RESULT-O04; DC-02 | Hợp lệ | Fixture xóa tách biệt. |
| TC-FR-14-DT-005 | FR-12, FR-14 | COND-FR-14-DT-005 | EC-AUTH-I01; EC-RESULT-O05; DC-03 | Hợp lệ | Thiếu token đại diện lớp không có JWT hợp lệ. |
| TC-FR-14-DT-006 | FR-12, FR-14 | COND-FR-14-DT-006 | EC-AUTH-I02; EC-RESULT-O05; DC-02, DC-03 | Hợp lệ | User token hợp lệ nhưng sai role; dữ liệu phải giữ nguyên. |
| TC-FR-14-DT-007 | FR-12, FR-14 | COND-FR-14-DT-007 | EC-AUTH-I02; EC-RESULT-O05; DC-04 | Hợp lệ | Kiểm tra quyền truy cập toàn phân hệ Admin. |
| TC-FR-14-DT-008 | FR-21 | COND-FR-14-DT-008 | EC-KEYBOARD-V01; EC-RESULT-O07 | Hợp lệ | Tách riêng thao tác bàn phím. |
| TC-FR-14-BVA-001 | FR-14, FR-22 | COND-FR-14-BVA-001 | BV-NAME-001; DB-01 | Hợp lệ | ON tại cận mở 0, không hợp lệ. |
| TC-FR-14-BVA-002 | FR-14 | COND-FR-14-BVA-002 | BV-NAME-002; DB-01 | Hợp lệ | OFF⁺ bằng 1, giá trị nhỏ nhất hợp lệ. |
| TC-FR-14-BVA-003 | FR-14 | COND-FR-14-BVA-003 | BV-NAME-003; DB-01 | Hợp lệ | Đại diện bên trong bằng 2. |

## 5. Độ bao phủ và ca trùng lặp

| Coverage Item | Test Case IDs | Coverage Status | Duplicate / Gap | Notes |
|---|---|---|---|---|
| Xem danh sách danh mục | DT-001 | Đã cover | Không | Dùng fixture có tên cụ thể. |
| Thêm tên hợp lệ | DT-002; BVA-002, BVA-003 | Đã cover | Trùng có chủ đích giữa DT/BVA | DT dùng nominal; BVA dùng độ dài 1 và 2. |
| Tên bắt buộc, không rỗng | DT-003; BVA-001 | Đã cover | Trùng có chủ đích giữa DT/BVA | DT bao phủ lớp invalid; BVA chứng minh tại cận mở 0. |
| Xóa danh mục | DT-004 | Đã cover | Không | Không áp đặt dialog hoặc thông báo. |
| JWT hợp lệ và role Admin cho API thay đổi dữ liệu | DT-005, DT-006 | Đã cover đại diện | Không | Tách thiếu token và sai role; không tạo Cartesian product cho mọi action. |
| Phân hệ Admin chỉ dành cho Admin | DT-007 | Đã cover | Không | Cách chặn cụ thể chưa được đặc tả. |
| Tiếng Việt, màu nút, một h1, dấu *, lỗi trên submit, active state | DT-001, DT-003 | Đã cover | Gộp quan sát có chủ đích | Lỗi trên submit được kiểm tra khi kích hoạt validation ở DT-003. |
| Tab Order | DT-008 | Đã cover | Không | Cần thao tác bàn phím riêng. |
| Cận dưới độ dài tên 0/1 và đại diện 2 | BVA-001 đến BVA-003 | Đã cover | Không | `-1` không khả thi. |
| Sửa danh mục | Chưa có | Chủ động loại trừ | Không phải coverage gap | FR-14 chỉ yêu cầu Thêm/Xem/Xóa. |
| Độ dài tối đa, duplicate, whitespace-only, ký tự hợp lệ | Chưa có | Bị chặn do thiếu đặc tả | Requirement gap | Không tự đặt validation. |
| Xóa danh mục đang được tham chiếu | Chưa có | Bị chặn do thiếu đặc tả | Requirement gap | Không có quy tắc phụ thuộc hoặc cascade. |

## 6. Kết luận sau thực thi

Bộ FR-14 đã thực thi đủ 11 ca: 6 Pass và 5 Fail. Năm bug độc lập đã được lập báo cáo tại `bug-reports/BUG-FR14-001.md` đến `BUG-FR14-005.md`. Không có ca Blocked hoặc Not Run. Kết quả dùng đúng Actual Result do tester cung cấp; các chi tiết HTTP `401` và `200`, trạng thái token và chuỗi focus không được suy ra chỉ từ ảnh.

## 7. Rà soát của sinh viên và thông tin còn thiếu

- Human review: Done.
- Test run: [`FR-14-quan-ly-danh-muc-run.md`](../../tests/test-runs/FR-14-quan-ly-danh-muc-run.md).
- Trình duyệt, hệ điều hành, URL và build runtime của lần chạy FR-14 chưa được cung cấp nên không kế thừa dữ liệu môi trường từ feature khác.
- GitHub Issues cho 5 bug FR-14 chưa được đăng; các bug report hiện liên kết evidence cục bộ và ghi đúng trạng thái này.
- Các điểm chưa được đặc tả vẫn giữ nguyên: tên trùng, trim/whitespace-only, ký tự và độ dài tối đa, xác nhận xóa, cập nhật danh mục, thứ tự danh sách và xóa danh mục có dữ liệu phụ thuộc. Không biến các điểm này thành lỗi thực thi.

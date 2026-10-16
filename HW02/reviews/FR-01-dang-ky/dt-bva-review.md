# Rà soát ca kiểm thử — FR-01: Đăng ký tài khoản

## 1. Phạm vi rà soát

- Đặc tả: `requirements/system-requirements.md`, FR-01 và quy tắc form FR-22, phiên bản tài liệu 2.0 ngày 2026-05-14.
- Phân tích: `analysis/FR-01-dang-ky/domain-testing-analysis.md` và `bva-analysis.md`.
- Ca kiểm thử: 8 ca Domain Testing và 7 ca Boundary Value Analysis trong `tests/test-cases/FR-01-dang-ky/`.
- Kỹ thuật và nền tảng: Domain Testing + Boundary Value Analysis / Web.

## 2. Tóm tắt kết quả

Vòng đầu phát hiện ba vấn đề Major và một vấn đề Minor. Các ca đã được sửa để tách từng field bắt buộc, loại dữ liệu có oracle chưa rõ và thay bước chung bằng thao tác phù hợp từng mục tiêu. Vòng rà soát sau sửa xác nhận 15 test case có ID/truy vết nhất quán, dữ liệu cụ thể, độ dài đúng, expected result không vượt quá đặc tả và trạng thái `Not Run / None` tại thời điểm review. Đây là kết quả review tài liệu trước execution, không phải kết quả thực thi SUT.

## 3. Phát hiện cần sửa

| Finding ID | Severity | File / Location | Issue | Impact | Proposed Correction | Status |
|---|---|---|---|---|---|---|
| REV-FR-01-001 | Major | DT analysis và TC-FR-01-DT-002 cũ | Một ca bỏ trống đồng thời bốn field bắt buộc, không cô lập nguyên nhân từ chối. | Nếu ca fail hoặc pass sai, không xác định được validation của field nào có vấn đề. | Tách Họ Tên, Email và Xác nhận thành các ca riêng; ghi dependency không thể tránh khi Mật khẩu và Xác nhận cùng rỗng. | Đã sửa |
| REV-FR-01-002 | Major | BVA analysis và 7 ca BVA cũ | Dùng `#` làm ký tự đệm dù requirement chỉ nêu tập ký tự đặc biệt bắt buộc và không nói rõ việc chấp nhận ký tự khác. | Oracle của các ca hợp lệ phụ thuộc giả định ngoài đặc tả. | Thay bằng chuỗi chỉ gồm chữ, số và `!`; phân phối hai ca hợp lệ để cover các điểm ON. | Đã sửa |
| REV-FR-01-003 | Major | TC-FR-01-DT-005 cũ | `abcdefgh` vi phạm đồng thời nhiều rule mật khẩu và trùng mục tiêu đã được cô lập trong BVA. | Giảm khả năng chẩn đoán và tạo coverage trùng không cần thiết. | Bỏ ca DT mật khẩu yếu; giữ từng rule thành phần trong BVA. | Đã sửa |
| REV-FR-01-004 | Minor | Các test case DT cũ / Test steps | Mọi ca dùng cùng bước chung, kể cả quan sát loại input và vị trí lỗi không liên quan. | Bước kiểm thử kém chính xác, khó thực thi nhất quán. | Viết bước riêng cho baseline, vị trí lỗi và các ca từ chối còn lại. | Đã sửa |
| REV-FR-01-005 | Minor | TC-FR-01-DT-006 / Dependency | Không thể để Mật khẩu rỗng trong khi Xác nhận vừa bắt buộc, vừa hợp lệ và vừa khớp. | Ca không thể cô lập tuyệt đối chỉ một lớp invalid. | Giữ cả hai trường rỗng và ghi rõ dependency/giới hạn isolation trong analysis, coverage và review. | Đã ghi nhận; chấp nhận |

## 4. Kiểm tra truy vết

| Test Case ID | Requirement Reference | Analysis Condition | Class / Boundary / Output ID | Status | Notes |
|---|---|---|---|---|---|
| TC-FR-01-DT-001 | FR-01, FR-22 | COND-FR-01-DT-001 | Các lớp input hợp lệ; EC-FORM-V01..V03; EC-RESULT-O01/O05 | Hợp lệ | Baseline thành công và kiểm tra cấu trúc tĩnh khi mở form. |
| TC-FR-01-DT-002 | FR-01 | COND-FR-01-DT-002 | EC-NAME-I01; EC-RESULT-O02 | Hợp lệ | Chỉ Họ Tên rỗng. |
| TC-FR-01-DT-003 | FR-01 | COND-FR-01-DT-003 | EC-EMAIL-I01; EC-RESULT-O02 | Hợp lệ | Chỉ Email rỗng. |
| TC-FR-01-DT-004 | FR-01, FR-22 | COND-FR-01-DT-004 | EC-EMAIL-I02; EC-FORM-V04; EC-RESULT-O02/O05 | Hợp lệ | Email sai định dạng đồng thời tạo lỗi để kiểm tra vị trí. |
| TC-FR-01-DT-005 | FR-01 | COND-FR-01-DT-005 | EC-EMAILSTATE-I01; DC-01; EC-RESULT-O03 | Hợp lệ | Có tiền điều kiện Email tồn tại. |
| TC-FR-01-DT-006 | FR-01 | COND-FR-01-DT-006 | EC-PASSWORD-I01; EC-CONFIRM-I01; DC-02; EC-RESULT-O02 | Cần xác nhận | Dependency khiến hai field cùng rỗng; đã ghi rõ và không có cách cô lập theo requirement hiện tại. |
| TC-FR-01-DT-007 | FR-01 | COND-FR-01-DT-007 | EC-CONFIRM-I01; DC-02; EC-RESULT-O02 | Hợp lệ | Mật khẩu hợp lệ, chỉ Xác nhận rỗng. |
| TC-FR-01-DT-008 | FR-01 | COND-FR-01-DT-008 | EC-CONFIRM-I02; DC-02; EC-RESULT-O04 | Hợp lệ | Hai chuỗi cụ thể khác nhau. |
| TC-FR-01-BVA-001 | FR-01 | COND-FR-01-BVA-001 | BV-PWLEN-001 | Hợp lệ | OFF⁻=7, các nhóm ký tự khác hợp lệ. |
| TC-FR-01-BVA-002 | FR-01 | COND-FR-01-BVA-002 | BV-PWLEN-002; BV-UPPER-ON; BV-DIGIT-ON; BV-SPECIAL-ON | Hợp lệ | ON độ dài=8 và ba ngưỡng thành phần=1. |
| TC-FR-01-BVA-003 | FR-01 | COND-FR-01-BVA-003 | BV-PWLEN-003; BV-LOWER-ON | Hợp lệ | OFF⁺ độ dài=9 và ON chữ thường=1. |
| TC-FR-01-BVA-004 | FR-01 | COND-FR-01-BVA-004 | BV-UPPER-001 | Hợp lệ | Chỉ số chữ hoa bằng 0. |
| TC-FR-01-BVA-005 | FR-01 | COND-FR-01-BVA-005 | BV-LOWER-001 | Hợp lệ | Chỉ số chữ thường bằng 0. |
| TC-FR-01-BVA-006 | FR-01 | COND-FR-01-BVA-006 | BV-DIGIT-001 | Hợp lệ | Chỉ số chữ số bằng 0. |
| TC-FR-01-BVA-007 | FR-01 | COND-FR-01-BVA-007 | BV-SPECIAL-001 | Hợp lệ | Chỉ số ký tự đặc biệt cho phép bằng 0. |

## 5. Độ bao phủ và ca trùng lặp

| Coverage Item | Test Case IDs | Coverage Status | Duplicate / Gap | Notes |
|---|---|---|---|---|
| Luồng đăng ký thành công và redirect | TC-FR-01-DT-001; TC-FR-01-BVA-002, TC-FR-01-BVA-003 | Đã cover | Trùng có chủ đích giữa hai kỹ thuật | Mỗi kỹ thuật cần baseline/điểm hợp lệ. |
| Họ Tên bắt buộc | TC-FR-01-DT-002 | Đã cover | Không | Không tạo biên độ dài vì requirement không cho min/max ngoài bắt buộc. |
| Email bắt buộc, định dạng, duy nhất | TC-FR-01-DT-003 đến TC-FR-01-DT-005 | Đã cover | Không | Ba hành vi khác nhau được tách riêng. |
| Mật khẩu bắt buộc | TC-FR-01-DT-006 | Đã cover có dependency | Gap isolation | Xác nhận cũng rỗng; giới hạn được ghi rõ. |
| Độ dài Mật khẩu 7/8/9 | TC-FR-01-BVA-001 đến TC-FR-01-BVA-003 | Đã cover | Không | Robust BVA quanh cận dưới 8. |
| Tối thiểu một chữ hoa/thường/số/ký tự đặc biệt | TC-FR-01-BVA-002 đến TC-FR-01-BVA-007 | Đã cover | Không | Có điểm ON=1 và OFF⁻=0 cho từng nhóm. |
| OFF⁺=2 của số lượng nhóm | Chưa có | Chủ động loại trừ | Coverage chọn lọc | Cùng miền hợp lệ với ON; loại để giữ tổng 15 ca. |
| Xác nhận bắt buộc và khớp | TC-FR-01-DT-006 đến TC-FR-01-DT-008 | Đã cover | Không | Có rỗng và không khớp. |
| FR-22: dấu *, input type, vị trí lỗi | TC-FR-01-DT-001, TC-FR-01-DT-004 | Đã cover | Gộp assertion tương thích | Không cần ca độc lập. |
| Cận trên độ dài | Chưa có | Bị chặn | Requirement gap | Không được đặc tả; không tự đặt. |

## 6. Kết luận sẵn sàng thực thi

**Sẵn sàng thực thi**, với một dependency đã biết ở TC-FR-01-DT-006 và các giới hạn requirement được ghi trong analysis. Không còn finding Critical/Major/Minor chưa xử lý.

## 7. Rà soát của sinh viên và thông tin còn thiếu

- Rà soát/chỉnh sửa của sinh viên: sinh viên xác nhận đã review và duyệt bộ test case trong phiên làm việc ngày 2026-10-16.
- Chưa được đặc tả: cú pháp Email đầy đủ, nội dung thông báo lỗi, quy tắc trim/Unicode, độ dài tối đa và cận trên của các trường.
- Tại thời điểm review, tất cả test case ở trạng thái `Not Run / None`; kết quả chạy sau đó được lưu riêng trong `tests/test-runs/FR-01-dang-ky-run.md`.
- Chuẩn bị trước execution: bảo đảm các Email được ghi là “chưa tồn tại” thực sự chưa có trong dữ liệu đầu kỳ; khi chạy lại toàn bộ suite, khôi phục dữ liệu nền hoặc dùng một bộ Email mới có cùng miền dữ liệu.

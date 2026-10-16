# Rà soát kết quả thực thi và báo lỗi — FR-01: Đăng ký tài khoản

## 1. Phạm vi rà soát

- Test run: `tests/test-runs/FR-01-dang-ky-run.md`.
- Test case: 8 ca Domain Testing và 7 ca Boundary Value Analysis.
- Evidence: 8 ảnh Pass trong `tests/test-runs/screenshots/` và 7 ảnh Actual Result trong `bug-reports/screenshots/`.
- Bug report: `BUG-FR01-001` đến `BUG-FR01-004`.
- Người thực hiện và thời điểm: Thu, 2026-10-16 20:30:00 +07:00.

## 2. Tóm tắt kết quả

Đã đối chiếu đủ 15 test case, 15 screenshot và các liên kết bug. Số liệu nhất quán: 8 Pass, 4 Fail, 3 Blocked, 0 Not Run và 4 defect riêng biệt. Bốn bug được tách theo hành vi, không theo số ca: mật khẩu hợp lệ bị từ chối; thiếu Xác nhận mật khẩu; thiếu dấu `*`; Email dùng sai type/không validation định dạng. Không phát hiện bug duplicate. Test run và bug report đã sẵn sàng làm nguồn để tạo GitHub Issues; hồ sơ chưa sẵn sàng nộp hoàn chỉnh vì thiếu thông tin môi trường và issue thật.

## 3. Phát hiện cần sửa

| Finding ID | Severity | File / Location | Issue | Impact | Proposed Correction | Status |
|---|---|---|---|---|---|---|
| REV-FR-01-EX-001 | Major | Test run / metadata và Evidence | Tester, giờ chạy và evidence trước đó ghi chưa cung cấp dù đã có dữ liệu/ảnh. | Hồ sơ thực thi thiếu khả năng truy vết. | Ghi tester `Thu`, thời điểm `2026-10-16 20:30:00 +07:00` và liên kết đủ 15 ảnh. | Đã sửa |
| REV-FR-01-EX-002 | Major | Test run và test case / Related Bug | Các ca Fail/Blocked chưa liên kết defect; số bug bằng 0. | Không truy được từ kết quả chạy tới báo lỗi. | Tạo 4 bug report sau khi kiểm tra duplicate; cập nhật Related Bug và tổng số bug. | Đã sửa |
| REV-FR-01-EX-003 | Minor | TC-FR-01-DT-004 / Notes | Ghi chưa có bằng chứng vị trí lỗi dù screenshot cho thấy lỗi nằm trên nút submit. | Mô tả chưa phản ánh đầy đủ evidence. | Ghi phần vị trí lỗi đạt; chỉ báo defect cho loại input và validation Email. | Đã sửa |
| REV-FR-01-EX-004 | Minor | Test run và 4 bug report / Environment | Browser, OS, URL và build chưa được cung cấp. | Giảm khả năng tái hiện chính xác trên môi trường khác. | Bổ sung từ môi trường chạy thật trước khi đăng issue hoặc retest. | Chưa xử lý — thiếu dữ liệu |
| REV-FR-01-EX-005 | Major | 4 bug report / GitHub Issue | Chưa có URL issue và screenshot trang GitHub Issues. | Chưa đáp ứng yêu cầu nộp bug của HW02. | Đăng 4 issue lên repository nhóm, đính kèm ảnh và lưu screenshot trang issue. | Chưa xử lý — chưa được yêu cầu đăng |

## 4. Kiểm tra truy vết

| Test Case ID | Result | Evidence | Related Bug | Status | Notes |
|---|---|---|---|---|---|
| TC-FR-01-DT-001 | Fail | `bug-reports/screenshots/TC-FR-01-DT-001-actual-result.png` | BUG-FR01-001, BUG-FR01-002, BUG-FR01-003, BUG-FR01-004 | Hợp lệ | Một ảnh chứa bốn sai khác độc lập. |
| TC-FR-01-DT-002 | Pass | `tests/test-runs/screenshots/TC-FR-01-DT-002-pass.png` | None | Hợp lệ | Field Họ Tên rỗng bị chặn. |
| TC-FR-01-DT-003 | Pass | `tests/test-runs/screenshots/TC-FR-01-DT-003-pass.png` | None | Hợp lệ | Field Email rỗng bị HTML validation chặn. |
| TC-FR-01-DT-004 | Fail | `bug-reports/screenshots/TC-FR-01-DT-004-actual-result.png` | BUG-FR01-004 | Hợp lệ | Lỗi nằm đúng vị trí; validation Email sai. |
| TC-FR-01-DT-005 | Blocked | `bug-reports/screenshots/TC-FR-01-DT-005-actual-result.png` | BUG-FR01-001 | Hợp lệ | Lỗi mật khẩu chặn kiểm tra uniqueness. |
| TC-FR-01-DT-006 | Pass | `tests/test-runs/screenshots/TC-FR-01-DT-006-pass.png` | None | Hợp lệ | Password rỗng bị chặn. |
| TC-FR-01-DT-007 | Blocked | `bug-reports/screenshots/TC-FR-01-DT-007-actual-result.png` | BUG-FR01-002 | Hợp lệ | Không có trường Xác nhận. |
| TC-FR-01-DT-008 | Blocked | `bug-reports/screenshots/TC-FR-01-DT-008-actual-result.png` | BUG-FR01-002 | Hợp lệ | Không thể nhập hai giá trị khác nhau. |
| TC-FR-01-BVA-001 | Pass | `tests/test-runs/screenshots/TC-FR-01-BVA-001-pass.png` | None | Hợp lệ | OFF⁻ độ dài bị từ chối. |
| TC-FR-01-BVA-002 | Fail | `bug-reports/screenshots/TC-FR-01-BVA-002-actual-result.png` | BUG-FR01-001 | Hợp lệ | Mật khẩu hợp lệ dài 8 bị từ chối. |
| TC-FR-01-BVA-003 | Fail | `bug-reports/screenshots/TC-FR-01-BVA-003-actual-result.png` | BUG-FR01-001 | Hợp lệ | Mật khẩu hợp lệ dài 9 bị từ chối. |
| TC-FR-01-BVA-004 | Pass | `tests/test-runs/screenshots/TC-FR-01-BVA-004-pass.png` | None | Hợp lệ | Thiếu chữ hoa bị từ chối. |
| TC-FR-01-BVA-005 | Pass | `tests/test-runs/screenshots/TC-FR-01-BVA-005-pass.png` | None | Hợp lệ | Thiếu chữ thường bị từ chối. |
| TC-FR-01-BVA-006 | Pass | `tests/test-runs/screenshots/TC-FR-01-BVA-006-pass.png` | None | Hợp lệ | Thiếu chữ số bị từ chối. |
| TC-FR-01-BVA-007 | Pass | `tests/test-runs/screenshots/TC-FR-01-BVA-007-pass.png` | None | Hợp lệ | Thiếu ký tự đặc biệt bị từ chối. |

## 5. Độ bao phủ và duplicate

| Coverage Item | Test Case / Bug IDs | Coverage Status | Duplicate / Gap | Notes |
|---|---|---|---|---|
| Validation mật khẩu hợp lệ | DT-001, BVA-002, BVA-003 / BUG-FR01-001 | Đã report | Không duplicate | Ba ca cùng symptom được gộp một bug. |
| Trường Xác nhận mật khẩu | DT-001, DT-007, DT-008 / BUG-FR01-002 | Đã report | Không duplicate | Một Fail phát hiện UI; hai ca Blocked thể hiện tác động. |
| Dấu `*` cho trường bắt buộc | DT-001 / BUG-FR01-003 | Đã report | Không duplicate | Defect UI độc lập. |
| Email type và validation định dạng | DT-001, DT-004 / BUG-FR01-004 | Đã report | Không duplicate | Một bug bao phủ cùng hành vi Email. |
| Evidence của 15 ca | 15 screenshot | Đầy đủ | Không | Tên file khớp Test Case ID. |
| GitHub Issues và ảnh trang issue | Chưa có | Chưa cover | Submission gap | Không bịa URL hoặc trạng thái đăng. |

## 6. Kết luận

**Test run và bug report Markdown đã được rà soát và nhất quán.** Trước khi coi FR-01 hoàn tất để nộp, cần bổ sung browser/OS/URL/build nếu còn truy xuất được, đăng bốn GitHub Issues lên repository nhóm, đính kèm evidence và lưu screenshot từng trang issue. Ba ca Blocked cần retest sau khi BUG-FR01-001 và BUG-FR01-002 được sửa.

## 7. Rà soát của sinh viên và thông tin còn thiếu

- Người thực hiện: Nguyễn Đoàn Xuân Thu; tên hiển thị trong test run: `Thu` theo xác nhận của sinh viên.
- Thông tin còn thiếu: browser, OS, URL/build, GitHub Issue URLs, ảnh trang GitHub Issues và kết quả retest.
- Không thay đổi Expected Result trong quá trình review execution.

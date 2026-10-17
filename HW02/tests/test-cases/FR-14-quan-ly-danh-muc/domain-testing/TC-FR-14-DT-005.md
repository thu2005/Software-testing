# TC-FR-14-DT-005: Từ chối thêm danh mục khi không có token

## Thông tin chung

| Field | Value |
|---|---|
| Mã yêu cầu / Nền tảng | FR-14 / Web Admin |
| Phân hệ / Loại kiểm thử / Kỹ thuật | Quản lý Danh mục / Chức năng / Domain Testing |
| Tham chiếu yêu cầu và phân tích | [FR-12](../../../../requirements/system-requirements.md#fr-12-kiểm-soát-truy-cập-access-control), [FR-14](../../../../requirements/system-requirements.md#fr-14-quản-lý-danh-mục-category-crud); [domain-testing-analysis.md](../../../../analysis/FR-14-quan-ly-danh-muc/domain-testing-analysis.md) |
| Trạng thái / Lỗi liên quan | Not Run / None |

## Phân tích miền

| Variable / Condition | Type | Domain / Constraints |
|---|---|---|
| Token | Điều kiện xác thực | Không gửi token |
| Payload tên | Chuỗi | Không rỗng để isolate lỗi quyền |

| Test Condition ID | Input Classes | Test Data / State | Output Classes | Expected Result |
|---|---|---|---|---|
| COND-FR-14-DT-005 | EC-AUTH-I01, EC-ACTION-V02, EC-NAME-V01 | POST `/api/categories`; `DM-FR14-NOTOKEN`; không có token | EC-RESULT-O05 | Request bị từ chối; danh mục không được tạo. |

## Điều kiện tiên quyết

- Không có danh mục `DM-FR14-NOTOKEN`.
- Có công cụ gửi HTTP request tới backend.

## Dữ liệu kiểm thử

| Field | Value |
|---|---|
| Method / Endpoint | `POST /api/categories` |
| Body | `{"name":"DM-FR14-NOTOKEN"}` |
| Authorization | Không gửi |

## Các bước kiểm thử

1. Gửi POST `/api/categories` với body đã nêu và không có header `Authorization`.
2. Ghi nhận response.
3. Dùng phiên Admin xem lại danh sách danh mục.

## Kết quả mong đợi

Request bị từ chối vì thiếu token; `DM-FR14-NOTOKEN` không được tạo. Requirement không quy định HTTP status hoặc thông báo cụ thể.

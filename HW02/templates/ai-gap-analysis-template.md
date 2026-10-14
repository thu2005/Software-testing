# Phân tích thiếu sót AI — <FEATURE-ID>: <Tên chức năng>

## 1. Phạm vi và bằng chứng ban đầu

- Tương tác AI được đối chiếu: <Mã tương tác/vị trí trong prompt log>.
- Đặc tả, phân tích, rà soát và lần chạy: <Các tệp liên quan>.
- Giới hạn đối chiếu: <Thông tin thiếu hoặc không có>.

## 2. Thiếu sót đã ghi nhận

| Gap ID | Type | Original AI Evidence | Missing / Incorrect Item | Added Test Case / Bug | Discovery Evidence | Likely Cause | Correction | Verification Status |
|---|---|---|---|---|---|---|---|---|
| <Mã gap> | <Ca bỏ sót/Ca sai/Bug bỏ sót đã xác nhận> | <Đầu ra gốc hoặc tham chiếu> | <Quy tắc/lớp/biên bị ảnh hưởng> | <TC-ID/BUG-ID> | <Ai phát hiện và bằng chứng thật> | <Nguyên nhân có căn cứ; ghi rõ nếu là giả thuyết> | <Phần đã sửa> | <Kết quả xác minh hoặc chưa chạy> |

Nếu chưa tìm thấy thiếu sót, thay dòng mẫu bằng kết luận giới hạn trong phạm vi đã rà soát; không tạo gap giả. Rủi ro chưa kiểm chứng ghi riêng, không gọi là bug đã xác nhận.

## 3. Nguyên nhân và bài học

<Phân tích liên hệ giữa prompt, công cụ, đặc tả hoặc độ phức tạp với thiếu sót có bằng chứng. Nêu cách cộng tác/rà soát để cải thiện>.

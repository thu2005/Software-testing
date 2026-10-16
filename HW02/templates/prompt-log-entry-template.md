## Tương tác AI - <YYYY-MM-DD HH:mm:ss TZ>

- Model: <Tên công cụ; model nếu biết>
- Timestamp: <Ngày giờ tương tác và múi giờ, hoặc chưa ghi nhận>

### Hội thoại nguyên văn

```text
User:
<Copy nguyên văn prompt khả dụng>

Assistant:
<Copy nguyên văn đầu ra đã có>
```

### Ghi chú

<Chỉ ghi nếu nội dung log quá dài không thể append hết. Còn lại để trống mục này, không cần ghi>.

Chỉ thêm phần Tool khi người dùng yêu cầu log tool call. Khi gọi skill, ghi tên skill, không chép lại toàn bộ nội dung skill. Giữ ngôn ngữ gốc và tăng độ dài code fence nếu transcript có fence bên trong. Nối entry vào log hiện có; không thay nội dung cũ.

# BUG-IA-02-PRODUCT-001: Ô số lượng chấp nhận 0, số thập phân và giá trị rỗng

## Found by Test Case
GUI-007, GUI-008

## Requirement liên quan
FR-06, IA-02

## Severity / Priority
Major / P1

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/product/1

## Steps to reproduce
1. Mở chi tiết sản phẩm iPhone 15 Pro Max.
2. Lần lượt nhập 0, 1.5 và để rỗng trong ô Số lượng.
3. Bấm Thêm vào giỏ hàng và mở Giỏ hàng.

## Expected result
Hệ thống từ chối mọi giá trị không phải số nguyên dương từ 1 trở lên và hiển thị phản hồi rõ ràng.

## Actual result
Sản phẩm vẫn được thêm với số lượng 0, số thập phân bị ép thành số nguyên và giá trị rỗng tạo quantity không hợp lệ.

## Evidence
![BUG-IA-02-PRODUCT-001](screenshots/BUG-IA-02-PRODUCT-001.png)

## GitHub Issue
TODO — tạo sau khi sinh viên xác nhận title/labels và cho phép push evidence.

# BUG-IA-02-CART-001: Cart thiếu điều khiển tăng giảm số lượng

## Found by Test Case
GUI-026, GUI-027, GUI-028, GUI-059

## Requirement liên quan
FR-07, FR-21, IA-02, IA-03

## Severity / Priority
Major / P1

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/cart

## Steps to reproduce
1. Thêm sản phẩm vào giỏ và mở Cart.
2. Quan sát cột Số lượng.
3. Dùng Tab để tìm điều khiển giảm/tăng.

## Expected result
Mỗi dòng có nút −/+ dùng được bằng chuột và bàn phím, không giảm dưới 1 và cập nhật đúng thành tiền.

## Actual result
Cột chỉ hiển thị quantity dạng text; hoàn toàn không có nút −/+.

## Evidence
![BUG-IA-02-CART-001](screenshots/BUG-IA-02-CART-001.png)

## GitHub Issue
TODO — tạo sau khi sinh viên xác nhận title/labels và cho phép push evidence.

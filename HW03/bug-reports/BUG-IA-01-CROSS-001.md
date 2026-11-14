# BUG-IA-01-CROSS-001: Cart và Checkout không có tiêu đề h1

## Found by Test Case
GUI-021, GUI-038

## Requirement liên quan
FR-21, IA-01

## Severity / Priority
Minor / P2

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/cart, http://localhost:5173/checkout

## Steps to reproduce
1. Mở Cart có sản phẩm và Checkout.
2. Kiểm tra heading cấp cao nhất của mỗi trang.

## Expected result
Mỗi trang có đúng một h1 mô tả nội dung.

## Actual result
Cả Giỏ Hàng và Xác Nhận Đơn Hàng đều dùng h2; số h1 là 0.

## Evidence
![BUG-IA-01-CROSS-001](screenshots/BUG-IA-01-CROSS-001.png)

## GitHub Issue
TODO — tạo sau khi sinh viên xác nhận title/labels và cho phép push evidence.

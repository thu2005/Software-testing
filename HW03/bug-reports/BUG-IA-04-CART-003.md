# BUG-IA-04-CART-003: Cart dùng nhãn Tổng tạm tính thay vì Tổng cộng

## Found by Test Case
GUI-036

## Requirement liên quan
FR-07, IA-04

## Severity / Priority
Minor / P2

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/cart

## Steps to reproduce
1. Thêm sản phẩm vào giỏ và mở Cart.
2. Quan sát nhãn khu vực tổng tiền.

## Expected result
Nhãn hiển thị chính xác Tổng cộng.

## Actual result
Nhãn hiển thị Tổng tạm tính.

## Evidence
![BUG-IA-04-CART-003](screenshots/BUG-IA-04-CART-003.png)

## GitHub Issue
https://github.com/thu2005/CSC13003_eshop/issues/58

# BUG-IA-04-CHECKOUT-002: Coupon phần trăm tính sai số tiền giảm và thành tiền

## Found by Test Case
GUI-050

## Requirement liên quan
FR-09, IA-04

## Severity / Priority
Major / P1

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/checkout

## Steps to reproduce
1. Đăng nhập và tạo giỏ 30.000.000 ₫.
2. Mở Checkout, nhập SAVE10 và bấm Áp dụng.
3. Quan sát Tiết kiệm và Thành tiền.

## Expected result
SAVE10 giảm 3.000.000 ₫ và thành tiền còn 27.000.000 ₫.

## Actual result
UI hiển thị Tiết kiệm -270.000.000 ₫ và Thành tiền 300.000.000 ₫.

## Evidence
![BUG-IA-04-CHECKOUT-002](screenshots/BUG-IA-04-CHECKOUT-002.png)

## GitHub Issue
https://github.com/thu2005/CSC13003_eshop/issues/60

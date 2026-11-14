# BUG-IA-03-CART-001: Link Tiếp tục mua sắm dùng sai nhãn

## Found by Test Case
GUI-032

## Requirement liên quan
FR-07, IA-03

## Severity / Priority
Minor / P2

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/cart

## Steps to reproduce
1. Mở Cart có sản phẩm.
2. Quan sát link quay lại danh sách sản phẩm.

## Expected result
Link có nhãn Tiếp tục mua sắm và giữ nguyên giỏ khi điều hướng.

## Actual result
Link hoạt động và giữ giỏ nhưng hiển thị nhãn ← Mua tiếp.

## Evidence
![BUG-IA-03-CART-001](screenshots/BUG-IA-03-CART-001.png)

## GitHub Issue
https://github.com/thu2005/CSC13003_eshop/issues/51

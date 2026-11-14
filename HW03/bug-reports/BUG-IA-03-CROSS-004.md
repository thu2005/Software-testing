# BUG-IA-03-CROSS-004: Navbar không highlight Cart hoặc Checkout hiện tại

## Found by Test Case
GUI-031, GUI-047

## Requirement liên quan
FR-23, IA-03

## Severity / Priority
Minor / P2

## Environment
**Browser**: Google Chrome 157.0.8103.50
**OS**: Windows
**URL**: http://localhost:5173/cart, http://localhost:5173/checkout

## Steps to reproduce
1. Mở Cart rồi Checkout.
2. Quan sát navbar ở mỗi trang.

## Expected result
Navbar highlight đúng trang hiện tại.

## Actual result
Link Cart không có active style/aria-current; navbar không có mục Checkout để highlight.

## Evidence
![BUG-IA-03-CROSS-004](screenshots/BUG-IA-03-CROSS-004.png)

## GitHub Issue
https://github.com/thu2005/CSC13003_eshop/issues/55

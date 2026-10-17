# HW02 — Domain Testing trên EShop

> **Sinh viên:** Nguyễn Đoàn Xuân Thu
> **MSSV:** 23120170
> **Phạm vi:** FR-01, FR-07, FR-14 và FR-06 Mobile
> **Repository bài làm:** [thu2005/Software-testing](https://github.com/thu2005/Software-testing)
> **Repository SUT và Issues:** [thu2005/CSC13003_eshop](https://github.com/thu2005/CSC13003_eshop)

---

## 1. Bảng tự đánh giá

| No. | Criteria | Maximum Score | Selected Feature | Self-Assessed Score |
|---|---|---:|---|---:|
| 1 | Chức năng A — Domain Testing + Boundary Value Analysis | 25 | FR-01: Đăng ký tài khoản Web | 25 |
| 2 | Chức năng B — Domain Testing + Boundary Value Analysis | 25 | FR-07: Giỏ hàng Web | 25 |
| 3 | Chức năng C — Domain Testing + Boundary Value Analysis | 25 | FR-14: Quản lý danh mục Web Admin | 25 |
| 4 | Chức năng D — Mobile, Domain Testing + Boundary Value Analysis | 15 | FR-06: Xem chi tiết sản phẩm Mobile | 15 |
| 5 | Agent Skills | 10 | [`.agents/skills/`](.agents/skills/) | 10 |
| | **Total** | **100** | | **100** |

> Tên ZIP theo điểm tự đánh giá: `23120170_HW02_AI_DomainTesting_100.zip`.

---

## 2. Báo cáo tổng kết kiểm thử

### 2.1. Chức năng đã kiểm thử

| Pool | Feature ID | Feature Name | Platform | Status |
|---|---|---|---|---|
| A | FR-01 | Đăng ký tài khoản | Web | Completed |
| B | FR-07 | Giỏ hàng | Web | Completed |
| C | FR-14 | Quản lý danh mục | Web Admin | Completed |
| D | FR-06 | Xem chi tiết sản phẩm | Mobile | Completed |

### 2.2. Tổng hợp test case

| Feature | Technique | Designed | Executed | Passed | Failed | Not Run | Blocked |
|---|---|---:|---:|---:|---:|---:|---:|
| FR-01 | Domain Testing | 8 | 8 | 3 | 2 | 0 | 3 |
| FR-01 | Boundary Value Analysis | 7 | 7 | 5 | 2 | 0 | 0 |
| FR-07 | Domain Testing | 8 | 8 | 1 | 7 | 0 | 0 |
| FR-07 | Boundary Value Analysis | 3 | 3 | 0 | 3 | 0 | 0 |
| FR-14 | Domain Testing | 8 | 8 | 4 | 4 | 0 | 0 |
| FR-14 | Boundary Value Analysis | 3 | 3 | 2 | 1 | 0 | 0 |
| FR-06 Mobile | Domain Testing | 8 | 8 | 1 | 7 | 0 | 0 |
| FR-06 Mobile | Boundary Value Analysis | 3 | 3 | 0 | 3 | 0 | 0 |
| **Total** | | **48** | **48** | **16** | **29** | **0** | **3** |

Ba ca FR-01 bị `Blocked` do thiếu trường Xác nhận mật khẩu hoặc bị lỗi validation mật khẩu chặn trước khi có thể kiểm tra đúng oracle. Không đổi các ca này thành `Fail` khi hành vi mục tiêu chưa thể thực thi hoặc quan sát.

### 2.3. Tổng hợp bug

| Bug ID | Feature | Severity / Priority | Status | Local Report | GitHub Issue |
|---|---|---|---|---|---|
| BUG-FR01-001 | FR-01 | High / P1 | Đã báo cáo | [BUG-FR01-001](bug-reports/BUG-FR01-001.md) | [Issue #1](https://github.com/thu2005/CSC13003_eshop/issues/1) |
| BUG-FR01-002 | FR-01 | High / P1 | Đã báo cáo | [BUG-FR01-002](bug-reports/BUG-FR01-002.md) | [Issue #2](https://github.com/thu2005/CSC13003_eshop/issues/2) |
| BUG-FR01-003 | FR-01 | Low / P3 | Đã báo cáo | [BUG-FR01-003](bug-reports/BUG-FR01-003.md) | [Issue #3](https://github.com/thu2005/CSC13003_eshop/issues/3) |
| BUG-FR01-004 | FR-01 | Medium / P2 | Đã báo cáo | [BUG-FR01-004](bug-reports/BUG-FR01-004.md) | [Issue #4](https://github.com/thu2005/CSC13003_eshop/issues/4) |
| BUG-FR07-001 | FR-07 | Low / P3 | Đã báo cáo | [BUG-FR07-001](bug-reports/BUG-FR07-001.md) | [Issue #5](https://github.com/thu2005/CSC13003_eshop/issues/5) |
| BUG-FR07-002 | FR-07 | High / P1 | Đã báo cáo | [BUG-FR07-002](bug-reports/BUG-FR07-002.md) | [Issue #6](https://github.com/thu2005/CSC13003_eshop/issues/6) |
| BUG-FR07-003 | FR-07 | Low / P3 | Đã báo cáo | [BUG-FR07-003](bug-reports/BUG-FR07-003.md) | [Issue #7](https://github.com/thu2005/CSC13003_eshop/issues/7) |
| BUG-FR07-004 | FR-07 | Low / P2 | Đã báo cáo | [BUG-FR07-004](bug-reports/BUG-FR07-004.md) | [Issue #8](https://github.com/thu2005/CSC13003_eshop/issues/8) |
| BUG-FR07-005 | FR-07 | High / P1 | Đã báo cáo | [BUG-FR07-005](bug-reports/BUG-FR07-005.md) | [Issue #9](https://github.com/thu2005/CSC13003_eshop/issues/9) |
| BUG-FR07-006 | FR-07 | High / P1 | Đã báo cáo | [BUG-FR07-006](bug-reports/BUG-FR07-006.md) | [Issue #10](https://github.com/thu2005/CSC13003_eshop/issues/10) |
| BUG-FR14-001 | FR-14 | Low / P3 | Đã báo cáo | [BUG-FR14-001](bug-reports/BUG-FR14-001.md) | [Issue #11](https://github.com/thu2005/CSC13003_eshop/issues/11) |
| BUG-FR14-002 | FR-14 | Low / P3 | Đã báo cáo | [BUG-FR14-002](bug-reports/BUG-FR14-002.md) | [Issue #12](https://github.com/thu2005/CSC13003_eshop/issues/12) |
| BUG-FR14-003 | FR-14 | High / P1 | Đã báo cáo | [BUG-FR14-003](bug-reports/BUG-FR14-003.md) | [Issue #13](https://github.com/thu2005/CSC13003_eshop/issues/13) |
| BUG-FR14-004 | FR-14 | Critical / P1 | Đã báo cáo | [BUG-FR14-004](bug-reports/BUG-FR14-004.md) | [Issue #14](https://github.com/thu2005/CSC13003_eshop/issues/14) |
| BUG-FR14-005 | FR-14 | Medium / P2 | Đã báo cáo | [BUG-FR14-005](bug-reports/BUG-FR14-005.md) | [Issue #15](https://github.com/thu2005/CSC13003_eshop/issues/15) |
| BUG-FR06-001 | FR-06 Mobile | Medium / P2 | Đã báo cáo | [BUG-FR06-001](bug-reports/BUG-FR06-001.md) | [Issue #16](https://github.com/thu2005/CSC13003_eshop/issues/16) |
| BUG-FR06-002 | FR-06 Mobile | Low / P3 | Đã báo cáo | [BUG-FR06-002](bug-reports/BUG-FR06-002.md) | [Issue #17](https://github.com/thu2005/CSC13003_eshop/issues/17) |
| BUG-FR06-003 | FR-06 Mobile | Low / P3 | Đã báo cáo | [BUG-FR06-003](bug-reports/BUG-FR06-003.md) | [Issue #18](https://github.com/thu2005/CSC13003_eshop/issues/18) |
| BUG-FR06-004 | FR-06 Mobile | Medium / P2 | Đã báo cáo | [BUG-FR06-004](bug-reports/BUG-FR06-004.md) | [Issue #19](https://github.com/thu2005/CSC13003_eshop/issues/19) |
| BUG-FR06-005 | FR-06 Mobile | High / P1 | Đã báo cáo | [BUG-FR06-005](bug-reports/BUG-FR06-005.md) | [Issue #20](https://github.com/thu2005/CSC13003_eshop/issues/20) |
| BUG-FR06-006 | FR-06 Mobile | High / P1 | Đã báo cáo | [BUG-FR06-006](bug-reports/BUG-FR06-006.md) | [Issue #21](https://github.com/thu2005/CSC13003_eshop/issues/21) |

**Tổng số:** 21 bug riêng biệt. Mỗi report có actual result, evidence cục bộ, liên kết issue và ảnh chụp trang GitHub Issue.

### 2.4. Bằng chứng test run

| Feature | Test Run | Result |
|---|---|---|
| FR-01 | [FR-01-dang-ky-run.md](tests/test-runs/FR-01-dang-ky-run.md) | 8 Pass / 4 Fail / 3 Blocked |
| FR-07 | [FR-07-gio-hang-run.md](tests/test-runs/FR-07-gio-hang-run.md) | 1 Pass / 10 Fail |
| FR-14 | [FR-14-quan-ly-danh-muc-run.md](tests/test-runs/FR-14-quan-ly-danh-muc-run.md) | 6 Pass / 5 Fail |
| FR-06 Mobile | [FR-06-MOBILE-xem-chi-tiet-san-pham-run.md](tests/test-runs/FR-06-MOBILE-xem-chi-tiet-san-pham-run.md) | 1 Pass / 10 Fail |

- Evidence Pass: [`tests/test-runs/screenshots/`](tests/test-runs/screenshots/)
- Evidence Fail và ảnh GitHub Issues: [`bug-reports/screenshots/`](bug-reports/screenshots/)

### 2.5. Video minh họa

| Item | Video Link |
|---|---|
| Agent Skill Demo | https://youtu.be/1XcRN-zMr2U |

---

## 3. Deliverables chính

| Deliverable | Path | Status |
|---|---|---|
| Báo cáo chính | [reports/main-report.md](reports/main-report.md) | Đã có |
| Báo cáo chính PDF | `reports/main-report.pdf` | Chưa xuất PDF |
| AI Critique | [reports/ai-critique.md](reports/ai-critique.md) | Đã có |
| AI Critique PDF | `reports/ai-critique.pdf` | Chưa xuất PDF |
| AI Audit Report | [reports/ai-audit-report.md](reports/ai-audit-report.md) | Đã có |
| AI Audit Report PDF | `reports/ai-audit-report.pdf` | Chưa xuất PDF |
| AI Gap Analysis | [ai-gap-analysis/HW02-ai-gap-analysis.md](ai-gap-analysis/HW02-ai-gap-analysis.md) | Đã có |
| Prompt log | [reports/prompt_log.md](reports/prompt_log.md) | Đã có |
| Git commit log | `git_log.md` | Chưa xuất |
| Requirements | [requirements/](requirements/) | Đã có |
| Analysis artifacts | [analysis/](analysis/) | Đã có |
| Test cases | [tests/test-cases/](tests/test-cases/) | Đã có |
| Test runs | [tests/test-runs/](tests/test-runs/) | Đã có |
| Reviews | [reviews/](reviews/) | Đã có |
| Bug reports | [bug-reports/](bug-reports/) | Đã có |

---

## 4. Agent Skills

Project-level skills nằm trong [`.agents/skills/`](.agents/skills/):

- `$domain-testing`
- `$boundary-value-analysis`
- `$test-case-review`
- `$test-execution`
- `$bug-report`
- `$qa-workflow`
- `$prompt-log`

Các skill hỗ trợ tạo analysis, thiết kế và review test case, ghi nhận execution, tạo bug report, kiểm tra traceability và lưu prompt log theo quy trình black-box testing. Kết quả do AI tạo được human review trước khi dùng làm artifact cuối.

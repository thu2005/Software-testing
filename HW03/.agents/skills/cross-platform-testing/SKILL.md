---
name: cross-platform-testing
description: Run the complete HW03 Task 1 GUI checklist on at least three valid browser/platform targets, using Chrome, Firefox, and either cloud-hosted Safari or Android Chrome, with Expo Go allowed as one replacement platform. Capture real evidence, overlay the student's full name and <StudentID>@student.hcmus.edu.vn, and report per-item results. Use when starting or continuing HW03 Task 3.
---

# Cross-Browser / Cross-Platform (HW03 Task 3)

## Workspace boundary

The course-assignment Git repository is `Software-testing/`; the homework
root is `Software-testing/HW03/`; and the SUT is the separate sibling
repository `CSC13003-eshop/`. Treat every relative output path in this skill
as relative to `Software-testing/HW03/`. Never place homework evidence in the
SUT repository.

**Language: every file this skill writes (`cross-platform/report.md`, the
Task 3 section of `reports/main-report.md`) must be natural, fluent
Vietnamese — notes, descriptions of rendering issues, everything. Only keep
jargon in English: browser/OS/device names, column names that are fixed
schema (`Platform`, `Result`), and CSS/rendering terms with no natural
Vietnamese equivalent. The username watermark stamped on screenshots stays
as literally specified (`<StudentID>@student.hcmus.edu.vn`) — do not translate
it. Also include the student's full name in the overlay so the evidence meets
the anti-cheat identity requirement. Never guess either value.**

Output lives in `cross-platform/report.md`, one per-platform execution table
under `cross-platform/results/`, and stamped evidence under
`cross-platform/screenshots/`. Task 3 says to perform Task 1 across at least
three platforms, so execute the complete Task 1 checklist on every selected
platform; a single flow or a reduced subset is not sufficient.

## Phase A — Choose the platform matrix

1. Select at least three valid targets. On the student's Windows machine, the
   practical native matrix is **Chrome on Windows + Firefox on Windows +
   Android Chrome on a real/emulated Android device**. Expo Go on a real phone
   may replace one browser platform if the mobile app is tested.
2. Safari is valid only through BrowserStack/LambdaTest/Sauce Labs or a real
   Apple device. Safari is not available as a supported local Windows browser;
   never suggest installing or claiming a local Safari-on-Windows run.
3. If Safari is selected through a cloud service, configure its local tunnel
   so the remote browser can reach the SUT's localhost URL.
4. Use the complete final `checklist/gui-checklist.md` on every platform. Copy
   its item IDs and expected checks into a per-platform result file; do not
   replace it with only the usability flow or a summary smoke test.
5. Record the chosen matrix at the top of `cross-platform/report.md`.
6. Commit:
   ```bash
   git add cross-platform/report.md
   git commit -m "docs(xplat): select platform matrix"
   ```

## Phase B — Get access

- Optional/preferred for Safari and additional OS coverage: a BrowserStack or
  LambdaTest trial (student's own account —
  they're responsible for obtaining it). If the trial is expired, fall back
  to Sauce Labs / CrossBrowserTesting, or real physical devices — but then
  the screenshot **must** clearly show the browser/OS/device name next to the
  SUT's localhost URL (e.g. don't crop out the browser chrome / window
  title).
- For Expo Go: run the EShop mobile app via Expo Go on a real phone, per the
  `eshop-sut` mobile app's setup instructions.

## Phase C — Execute and capture

For each platform:
1. Create `cross-platform/results/<platform>.md` with one row for every item
   in `checklist/gui-checklist.md`, retaining the original ID and adding
   `Platform Result`, `Notes`, `Screenshot`, and `Bug ID` columns.
2. Execute every checklist item and record Passed/Failed. Use browser
   automation when it can genuinely reach the target; otherwise the student
   drives the real device/cloud session and records the observation. Never
   infer an unobserved result.
3. For each failure, capture evidence showing the SUT plus the browser/OS/
   device identity and localhost URL. Also capture at least one overview
   screenshot per platform even when all items pass.
4. **Stamp the identity overlay** — mandatory for every screenshot, §6 and
   §11. From PowerShell in `Software-testing/HW03/` run:
   ```powershell
   python .agents/skills/cross-platform-testing/scripts/stamp_screenshot.py `
     <raw-screenshot.png> `
     cross-platform/screenshots/<platform>-<checklist-id>.png `
     "<StudentID>@student.hcmus.edu.vn" `
     --label "<Full name>" `
     --label "<Browser / OS / Device>"
   ```
   Ask the student for their real StudentID if not already known — never
   guess or leave a placeholder ID in a submitted screenshot.
5. If a real bug/rendering defect is found, file it with `bug-report`
   (area tag `XPLAT-<platform>`).
6. Add a platform summary row to `cross-platform/report.md`:

   | Platform | Browser/OS/Device | Checklist items executed | Passed | Failed | Result file | Evidence |
   |---|---|---|---|---|---|---|
   | Local | Chrome / Windows 11 | 45 | 43 | 2 | `results/chrome-windows.md` | `screenshots/chrome-windows-overview.png` |

7. Commit after each platform (keep it granular per §12, don't batch all
   three into one commit):
   ```bash
   git add cross-platform/report.md cross-platform/screenshots/
   git commit -m "test(xplat): run <flow> on <platform>"
   ```

## Phase D — Roll up

Update `reports/main-report.md`'s Task 3 section with the matrix covered,
pass/fail summary, and any bugs found, linking back to
`cross-platform/report.md` for the full table. Then:
```bash
git log --pretty=format:'%h %ad %s' --date=short > git-log.txt
git add git-log.txt reports/main-report.md
git commit -m "docs: roll up cross-platform results into main report"
```

## Guardrails

- Never fabricate or reuse the same screenshot across platforms — the
  anti-cheat constraints (§11) apply to the spirit of Task 3 too, even though
  it's only explicitly named for participants: screenshots are graded
  evidence.
- Never claim Safari was tested locally on Windows. Record whether each run
  used a local browser, Android device/emulator, cloud service with local
  tunnel, or real Apple device.
- Don't stamp over content needed to judge the bug (e.g. an error message) —
  use `--corner` to place the watermark in an empty area of the screenshot.
- If Pillow/Python isn't available in the environment, the watermark can be
  added via the BrowserStack/LambdaTest live-session on-screen annotation
  tools instead, or any screenshot markup tool — the requirement is the
  overlay appearing in the final image, not this specific script.

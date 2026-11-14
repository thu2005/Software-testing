# AI Audit Report (AI-02)

## 1. Thông tin Sinh viên

| Field | Value |
|---|---|
| Họ tên | [TODO — sinh viên điền] |
| MSSV | [TODO — sinh viên điền] |
| Lớp / Khoá | [TODO — sinh viên điền] |
| Assignment ID | HW03-AI |
| Ngày làm bài | 12/11/2026 |
| Công cụ AI đã dùng | Codex |

## 2. Hướng dẫn

Mỗi entry bên dưới chỉ ghi một prompt hoặc task AI tạo, sửa đáng kể, hoặc đánh
giá một artifact dùng cho HW03. Chat thông thường và edit nhỏ chỉ nằm trong
`reports/prompt-log.md`. Prompt và output phải giữ nguyên văn; verdict phải do
sinh viên review và xác nhận.

## 3. Audit Entries

## Entry #1

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 6:16 PM 12/11/2026 |
| **Artifact type** | Chỉnh sửa bộ Agent Skills HW03 và tạo submission preflight checklist |

**Full prompt:**

```text
3, repo @CSC13003-eshop/ là repo eshop để test, chứa requirements, chứa toàn bộ feature của đề. 4, vậy sửa thành agents đi, không để claude, email đúng là <id>@student.hcmus.edu.vn. 5, format như vậy là được rồi, thêm model nữa là được, quan trọng của cái ai-audit này là verdict. prompt log là bắt buộc sau mỗi prompt nhé, còn ai-audit thì khi 1 prompt, 1 task được AI generate ra thì mới log vào, còn chat bình thường, edit các thứ nhỏ thì không cần. 7, tất cả các output của homework này đều làm vào @Software-testing/HW03/. @CSC13003-eshop/ là repo eshop. @Software-testing/ là repo bài tập của course, gồm nhiều week.
Máy mình là window, bạn kiểm tra lại những chỗ đang suggest test bằng safari. 
Những chỗ còn lại, chỗ nào sai thì sửa theo đúng yêu cầu của homework nhé. checklist không cần là 1 skill, có thể dùng 1 md để check là ổn
```

### (2) AI Output

```text
Đã sửa xong bộ skill theo đúng cấu trúc repo và yêu cầu HW03.

- Requirements giờ đọc trực tiếp từ `CSC13003-eshop/README.md`; giữ `FR-21`–`FR-24` vì repo SUT thực sự có các requirement này.
- Tất cả output được cố định dưới `Software-testing/HW03/`; repo SUT chỉ được đọc, không nhận deliverable.
- Task 1 dùng mã `IA-01`–`IA-04` và yêu cầu tối thiểu 41 checklist items.
- Task 3 giờ chạy toàn bộ checklist Task 1 trên từng platform, không còn cho phép chỉ chạy một flow/subset.
- Trên Windows, matrix native được đề xuất là Chrome/Windows + Firefox/Windows + Android Chrome; Safari chỉ chạy qua BrowserStack/LambdaTest/Sauce Labs hoặc thiết bị Apple thật, không chạy Safari local trên Windows.
- Watermark dùng `<StudentID>@student.hcmus.edu.vn` và full name; đường dẫn đã đổi sang `.agents`, command đổi sang PowerShell/`python`, và script có Windows fonts cùng tự tạo output directory.
- `prompt-log` ghi mọi prompt; `ai-audit-log` chỉ ghi task/prompt tạo hoặc review artifact đáng kể, có thêm field `Model` và giữ `Verdict` là trọng tâm.
- Bug-report đã dùng đúng template chung ở `Software-testing/.github`, PowerShell thay Bash heredoc, và raw GitHub URL có prefix `HW03/`.
- Đã thêm `submission-checklist.md` thay vì tạo thêm skill.

Đã kiểm tra frontmatter của cả 6 skill và compile cú pháp script thành công. Hai dependency runtime vẫn cần chuẩn bị trước khi dùng: `Pillow` cho watermark và GitHub CLI `gh` cho việc tạo issue. Mình chưa commit thay đổi.
```

### (3) Verdict

**`VALID`**

### (4) Reasoning

Sinh viên đã review bộ skill và xác nhận bằng thông báo “skill done”. Các thay
đổi phản ánh đúng cấu trúc hai repository, phạm vi output HW03, cách chạy Safari
trên Windows, email sinh viên và quy tắc tách prompt log khỏi AI audit.

### (5) Student Fix

Không cần chỉnh sửa thêm sau review; sinh viên không báo vấn đề với bộ skill.

---

## Entry #2

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 7:16 PM 12/11/2026 |
| **Artifact type** | Kế hoạch thực hiện HW03 theo từng bước và skill |

**Full prompt:**

```text
done skill. đây là các task mình sẽ làm nè: task 1: product detail (fr 06), shopping cart (fr 07, check out (fr 08)
task 2: luồng mua hàng (search -> product detail -> cart -> coupon -> checkout).
Lên 1 markdown plan, với mỗi bước cần dùng skill gì luôn nhé, mình sẽ flow theo plan của bạn để prompt.
```

### (2) AI Output

```text
Đã tạo [PLAN.md](/D:/testing/CSC13003/Software-testing/HW03/PLAN.md) với 23 bước prompt tuần tự.

Plan đã chốt:

- Task 1: Product Detail `FR-06`, Shopping Cart `FR-07`, Checkout `FR-08`.
- Task 2: Search `FR-05` → Product Detail → Cart → Coupon `FR-09` → Checkout.
- 12 batch tạo checklist theo từng `screen × IA`, sau đó human gap review, quality gate và execution thật.
- Mỗi bước ghi rõ skill chính cùng `$prompt-log`, `$ai-audit-log` hoặc `$bug-report` khi áp dụng.
- Task 2 có bước chọn SUS/UEQ-S, pilot, 7 session thật, analysis và severity.
- Task 3 chạy toàn bộ checklist Task 1 trên 3 platform; matrix Windows khuyến nghị là Chrome + Firefox + Android Chrome.
- Cuối plan có AI Audit/Critique, report, README, git log, demo video, preflight và đóng gói ZIP.

Bắt đầu từ `P0.1`: bạn review Audit Entry #1 và xác nhận verdict trước, sau đó prompt lần lượt theo mục “Thứ tự prompt ngắn gọn” ở cuối plan. Lượt tạo plan này đã được thêm vào prompt log và AI Audit với verdict `INCOMPLETE` chờ bạn review. Mình chưa commit thay đổi.
```

### (3) Verdict

**`INCOMPLETE`**

### (4) Reasoning

Plan đúng scope nhưng quá chi tiết và chia checklist thành 12 prompt nhỏ, trong
khi sinh viên muốn workflow gọn theo milestone và ba prompt lớn theo màn hình.
Vì cần sinh viên viết lại đáng kể trước khi dùng, output chỉ đạt `INCOMPLETE`.

### (5) Student Fix

Sinh viên đã tự rút plan còn M1–M9, đổi M1 thành ba prompt lớn theo Product
Detail, Shopping Cart và Checkout, bỏ các bước nhỏ không cần thiết, đồng thời
cập nhật lại trạng thái blocker và quy tắc chỉ audit interaction chính thức.

---

## Entry #3

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 8:14 PM 12/11/2026 |
| **Artifact type** | README HW03 — scope, repository context và submission summary scaffold |

**Full prompt:**

```text
nãy mình ghi skill done, nghĩa là mình đã review, bạn tự cập nhật vào, khi nào có vấn đề gì mình cũng nhắn luôn vấn đề vào chat, bạn tự cập nhật cho dễ follow.
Dùng $gui-checklist. Tạo/cập nhật README.md trong Software-testing/HW03 để ghi
scope Task 1 là Product Detail FR-06, Shopping Cart FR-07, Checkout FR-08;
scope Task 2 là Search → Product Detail → Cart → Coupon → Checkout. Để TODO
cho thông tin cá nhân chưa có, không tự đoán. Chưa sinh checklist items.
```

### (2) AI Output

```text
Đã tạo [README.md](/D:/testing/CSC13003/Software-testing/HW03/README.md) đúng scope và chưa sinh checklist item.

Đã tự cập nhật trạng thái follow:

- Audit Entry #1 chuyển từ `INCOMPLETE` sang `VALID` theo xác nhận “skill done”.
- `PLAN.md`: P0.1 và P0.2 được đánh dấu hoàn thành.
- Thông tin cá nhân, primary GUI screen, SUT commit/build và URL vẫn là `TODO`; không có dữ liệu nào được đoán.
- README đã có sẵn khung test summary, demo video và self-assessment để cập nhật dần.

Lượt tạo README được ghi thành Audit Entry #3 với verdict `INCOMPLETE` chờ bạn review. Theo convention mới, khi bạn nói `README done` mình sẽ tự chuyển entry này sang `VALID`; nếu bạn nêu lỗi, mình sẽ cập nhật Reasoning và Student Fix theo nội dung chat. Bước tiếp theo trong plan là P0.3 — kiểm tra môi trường SUT/tooling. Mình chưa commit thay đổi.
```

### (3) Verdict

**`VALID`**

### (4) Reasoning

README đã được kiểm tra tự động để xác nhận có đúng ba màn hình Task 1, đúng flow
Task 2, các TODO cần thiết và không có checklist item. Sinh viên đã review và
xác nhận bằng thông báo “đã review”.

### (5) Student Fix

Không cần sửa nội dung scope sau review. Thông tin môi trường P0.3 được bổ sung
sau đó như một cập nhật nhỏ và không tạo audit entry mới theo yêu cầu sinh viên.

---

## Entry #4

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 3:56 PM 14/11/2026 |
| **Artifact type** | M1 — Initial GUI checklist cho Product Detail, Shopping Cart và Checkout |

**Full prompt:**

```text
mình đã fix vài điểm bị block và lên lại plan. plan của bạn chi tiết quá (vài điểm không cần). Bây giờ, thực hiện M1 trong PLAN cho mình
```

### (2) AI Output

```text
M1 đã hoàn thành: tạo [gui-checklist.md](/D:/testing/CSC13003/Software-testing/HW03/checklist/gui-checklist.md) với 48 initial items.

- 16 item cho mỗi màn hình: Product Detail, Shopping Cart và Checkout.
- 12 item cho mỗi nhóm `IA-01`–`IA-04`.
- ID liên tục `GUI-001`–`GUI-048`, không có item trùng nguyên văn.
- Tất cả đều `Source=AI`, `Result=Not Run`; chưa có Pass/Fail, screenshot hay bug giả.
- `PLAN.md` đã ghi M1 “đã tạo initial draft, chờ sinh viên review trước M2”.

Checklist được ground từ `FR-06`–`FR-08`, `FR-21`–`FR-24`, API/frontend đang trả HTTP 200 và các route/component hiện tại. Chrome headless không xuất được ảnh/DOM trong môi trường này, nên mình không đưa ra claim về visual correctness; các kiểm tra đó vẫn để `Not Run` cho M3.

Lượt này đã được ghi vào prompt log, không tạo AI Audit entry và chưa commit. Sau khi bạn review M1, bước kế tiếp là M2 — human gap analysis và quality gate.
```

### (3) Verdict

**`INCOMPLETE`**

### (4) Reasoning

Initial checklist đạt coverage: 48 item, đủ ba màn hình và bốn IA. Tuy nhiên
human review phát hiện sáu item ghép nhiều expected behavior, một số item cần
viết lại hoặc reclassify, và mười gap về global visual rules, accessibility,
keyboard/mobile, session expiry và network recovery. Kết luận Chrome headless
không xuất được DOM/screenshot cũng không chính xác: nguyên nhân là profile mặc
định bị từ chối và dump quá sớm trước khi React/API hoàn tất.

### (5) Student Fix

Sinh viên xác minh lại Chrome bằng profile tạm và chờ API 5 giây: DOM động tải
đủ 22.444 byte, có `h1`, ảnh, “Số lượng”, “Thêm vào giỏ hàng”, và screenshot
1440×1000 được tạo bình thường. Checklist được sửa ở M2: tách item ghép,
reclassify/viết lại các item được review, thêm 10 human gaps và ghi rõ lý do AI
bỏ sót trong gap analysis.

---

## Entry #5

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 4:18 PM 14/11/2026 |
| **Artifact type** | M2 — Human review, gap analysis và quality gate cho GUI checklist |

**Full prompt:**

```text
Về Chrome: câu “Chrome headless không xuất được ảnh/DOM” không còn đúng. Nguyên nhân là Chrome ban đầu bị từ chối quyền truy cập profile mặc định và dump DOM quá sớm khi React còn hiển thị “Đang tải…”.

Sau khi dùng profile tạm và chờ API 5 giây, mình đã xác minh:

- DOM động tải hoàn chỉnh: 22.444 byte.
- Có `h1`, ảnh, “Số lượng” và “Thêm vào giỏ hàng”.
- Chrome headless xuất được screenshot 1440×1000 bình thường.

Về human review: **M1 đạt về coverage nhưng cần chỉnh trước khi execute M3**.

### 1. Các item cần tách để bảo đảm nguyên tử

- `GUI-002`: tách “ảnh không méo/vỡ” và “ảnh có alt đúng”.
- `GUI-008`: tách “Tab order hợp lý” và “focus indicator nhìn thấy”.
- `GUI-011`: tách “link Giỏ hàng truy cập được” và “badge đúng số lượng”.
- `GUI-016`: tách error state của product ID không tồn tại và lỗi API/network.
- `GUI-024`: tách accessible label/focus và màu sắc thể hiện hành động nguy hiểm.
- `GUI-048`: tách xác nhận thành công, xóa giỏ hàng và điều hướng về trang chủ.

### 2. Các item cần viết lại

- `GUI-040`: chỉ kiểm tra coupon loading/double-submit; phần checkout đã được `GUI-047` kiểm tra.
- `GUI-042`: bỏ từ “hoặc”. Expected nên rõ: navbar phải highlight đúng vị trí Checkout. Step indicator chỉ kiểm tra nếu checkout thực sự nhiều bước.
- `GUI-046`: viết thành một hành vi chung cho mọi coupon không hợp lệ, hoặc tách từng loại coupon nếu cần truy vết riêng.
- `GUI-004`: nên tập trung vào responsive layout; không gộp việc kiểm tra đầy đủ tất cả nội dung.
- `GUI-024` phù hợp với IA-01/IA-04 hơn IA-02.
- `GUI-008` phù hợp IA-03 hơn IA-02 vì thuộc keyboard navigation.

### 3. Các human gaps nên bổ sung

| Gap               | Item đề xuất                                                                                           | Lý do AI bỏ sót                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Màu hành động     | Nút hành động tích cực phải dùng màu xanh dương; nút nguy hiểm dùng màu đỏ nhất quán                   | Prompt tập trung vào chức năng từng màn hình, bỏ sót yêu cầu visual consistency toàn hệ thống trong FR-21 |
| Ngôn ngữ          | Toàn bộ label, message, button và error trên ba màn hình phải dùng tiếng Việt nhất quán                | AI không tạo item riêng cho global language requirement                                                   |
| Contrast          | Text, button, focus indicator và error message phải đạt contrast dễ đọc                                | Giới hạn model: chưa chuyển accessibility thành tiêu chí đo được                                          |
| Keyboard Cart     | Có thể Tab đến `−`, `+`, Xóa và Checkout theo thứ tự hợp lý, có focus indicator                        | AI chỉ kiểm tra keyboard trên Product Detail                                                              |
| Keyboard Checkout | Có thể Tab qua coupon, Apply và Checkout theo đúng thứ tự, không bị keyboard trap                      | Prompt Checkout bỏ sót keyboard-only flow                                                                 |
| Touch target      | Nút `−`, `+`, Xóa, Apply và Checkout có vùng chạm đủ lớn trên mobile                                   | Đặc điểm responsive/mobile của EShop chưa được xét                                                        |
| Long content      | Tên sản phẩm và text tiếng Việt dài không làm vỡ layout hoặc che nút                                   | AI chỉ kiểm tra viewport, chưa kiểm tra dữ liệu dài                                                       |
| All-image alt     | Ảnh sản phẩm trong Cart/Checkout cũng phải có alt phù hợp                                              | AI chỉ kiểm tra alt trên Product Detail, trong khi FR-24 yêu cầu tất cả ảnh                               |
| Session expiry    | Nếu session hết hạn khi đang Checkout, người dùng nhận thông báo rõ và không mất giỏ hàng âm thầm      | AI chỉ kiểm tra người chưa đăng nhập, không kiểm tra session hết hạn giữa flow                            |
| Network recovery  | Khi coupon/checkout gặp lỗi mạng, nút được bật lại và người dùng có thể thử lại mà không tạo đơn trùng | AI có loading state nhưng thiếu recovery sau lỗi                                                          |

###

prompt này và prompt trước nên có ai-audit, prompt trước verdict incomplete vì ở prompt này mình có sửa (human review), prompt này complete vì bạn sẽ sửa xong gui-checklist. Đây là bước M2.
```

### (2) AI Output

```text
M2 đã hoàn thành và đạt quality gate.

- [gui-checklist.md](/D:/testing/CSC13003/Software-testing/HW03/checklist/gui-checklist.md): 65 item, gồm 55 `Source=AI` và 10 `Source=Human`.
- [gui-checklist-gaps.md](/D:/testing/CSC13003/Software-testing/HW03/ai-gap-analysis/gui-checklist-gaps.md): ghi mapping các item đã tách/viết lại/reclassify và lý do cho từng human gap.
- ID liên tục `GUI-001`–`GUI-065`; không trùng item; đủ ba screen và `IA-01`–`IA-04`; tất cả vẫn `Not Run`.
- Đã sửa toàn bộ item bạn chỉ ra, đồng thời cập nhật baseline Chrome: DOM động 22.444 byte và screenshot headless 1440×1000 hoạt động với profile tạm/chờ API.
- `PLAN.md` đã đánh dấu M1 `INCOMPLETE` sau review và M2 `VALID`.

AI Audit đã được cập nhật: Entry #4 cho M1 là `INCOMPLETE`; Entry #5 cho M2 là `VALID`, kèm Reasoning và Student Fix dựa đúng trên human review của bạn. Prompt này cũng đã được ghi vào prompt log. Chưa execute item, chưa tạo Pass/Fail/bug và chưa commit.
```

### (3) Verdict

**`VALID`**

### (4) Reasoning

M2 áp dụng đầy đủ human review: sáu item ghép đã được tách thành các expected
behavior nguyên tử, các item được chỉ định đã được viết lại/reclassify, và 10
gap đã được thêm với `Source=Human`. Quality gate tự động xác nhận 65 ID liên
tục, không có item trùng nguyên văn, đủ ba screen/bốn IA, và toàn bộ vẫn
`Not Run`. Baseline Chrome cũng được sửa theo bằng chứng sinh viên cung cấp.

### (5) Student Fix

Checklist tăng từ 48 lên 65 item (`55 AI + 10 Human`); tạo
`ai-gap-analysis/gui-checklist-gaps.md`; tách/viết lại/reclassify toàn bộ item
được review; bổ sung traceability và lý do AI bỏ sót; cập nhật PLAN M1/M2 và
thông tin Chrome. Không cần chỉnh sửa thêm sau khi quality gate đạt.

---

## Entry #6

### (1) Prompt + Tool

| Field             | Content         |
| ----------------- | --------------- |
| **Tool**          | Codex |
| **Model**         | GPT-5 |
| **Timestamp**     | 4:58 PM 14/11/2026 |
| **Artifact type** | M3 — Baseline execution, failed evidence và Markdown bug reports |

**Full prompt:**

```text
bắt đầu thục hiện M3 nhé
```

### (2) AI Output

```text
M3 đã hoàn tất phần execution và chuẩn bị bug local:

- Đã chạy 65/65 item trên Chrome 157 / Windows: 31 Passed, 34 Failed.
- Có 34 screenshot, chỉ dành cho failed items.
- Đã gom 34 failure theo nguyên nhân và tạo 20 Markdown bug reports.
- Đã cập nhật gui-checklist.md, README.md và PLAN.md; không tạo AI audit cho lượt này.
- Chưa commit/push và chưa tạo 20 GitHub Issues.

Cần bạn xác nhận bước public: cho phép mình commit + push evidence/report lên thu2005/Software-testing nhánh main, sau đó tạo 20 Issues trong thu2005/CSC13003_eshop với title dạng [BUG][BUG-ID] <title> và label bug nhé?
```

### (3) Verdict

**`INCOMPLETE`**

### (4) Reasoning

AI đã execute đủ 65/65 checklist item trên SUT thật, retest các kết quả bị ảnh
hưởng bởi timing của automation, chỉ lưu screenshot cho 34 failed item và gom
các failure cùng nguyên nhân thành 20 Markdown bug report có traceability. Tuy
nhiên, M3 yêu cầu bug thật phải được tạo trên GitHub Issues và liên kết ngược
về checklist/report. Output dừng ở trạng thái local, chưa commit/push evidence,
chưa có issue URL nên chưa thể xem là hoàn tất milestone.

### (5) Student Fix

Sinh viên review và xác nhận verdict `INCOMPLETE`, sau đó cho phép commit/push
artifact với tiền tố commit `[HW03]` và tạo 20 GitHub Issues. Các issue URL sẽ
được cập nhật ngược vào Markdown bug report và checklist trong follow-up này.

---

## 4. Tổng hợp độ chính xác của AI

| Metric | Count | Percentage |
|---|---:|---:|
| Total audited | 6 | 100% |
| VALID | 3 | 50% |
| INVALID | 0 | 0% |
| INCOMPLETE | 3 | 50% |

## 5. Kết luận

[TODO — hoàn thiện sau khi có đủ audit entries]

## 6. Mandatory Disclosure

[TODO — hoàn thiện trước khi nộp]

## Signature

| Field | Value |
|---|---|
| Student name | [TODO] |
| Student ID | [TODO] |
| Class / Cohort | [TODO] |
| Date | [TODO] |
| Signature | [TODO] |

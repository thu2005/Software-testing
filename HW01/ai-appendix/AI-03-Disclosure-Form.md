# AI Use Disclosure Form (AI-03)

## 1. Course & Student Information

| Field | Value |
|---|---|
| Course | CSC130003 — Software Testing |
| Assignment ID | HW01 |
| Assignment title | QA/QC Jobs · 20 Software Defects · Test a Physical Product |
| AI Use Category (1–5) | Category 4 |
| Date | 28/09/2026 |
| Student name | Nguyễn Đoàn Xuân Thu |
| Student ID | 23120170 |

## 2. Disclosure Questions

### 2.1 AI tool(s) used

- OpenAI Codex (`gpt-5.6-sol`, `GPT-5.6 Sol Medium`, and `GPT-5.6 Sol` in the recorded turns).
- ChatGPT Web / GPT Web (`GPT Web` and `GPT-6 Luna` in the recorded turns).

### 2.2 Assignment stage(s) where AI was used

- [x] Brainstorming
- [x] Outlining
- [x] Drafting
- [x] Feedback
- [x] Revision
- [ ] Coding
- [ ] Data analysis
- [x] Visual design
- [x] Other: Test-case design, source-based defect-report structuring, screenshot integration, and AI-audit documentation

### 2.3 Main prompts or tasks given to AI

The three prompts below are reproduced verbatim. The complete chronological record is attached in `HW01/prompt_log.md`.

1. 

   > giải thích cho mình về các software defect này, ngắn gọn dễ hiểu:
   > [AI] ChatGPT — cross-user chat history and payment data exposure (2023)
   > [AI] Bing Chat — indirect prompt injection and data leakage (2023)
   > [AI] Air Canada chatbot — bereavement-fare misinformation (2024)
   > [AI] DPD customer-service chatbot — offensive and brand-damaging responses (2024)
   > [AI] Gemini image generation — inaccurate and biased depictions (2024)
   > [AI] Google Search AI Overviews — false or misleading answers (2024)
   > [AI] Replit AI agent — production database deletion (2025)
   > Atlassian Confluence — CVE-2022-26134
   > Spring Framework “Spring4Shell” — CVE-2022-22965
   > Google Chrome — CVE-2022-0609
   > OpenSSL — CVE-2022-3602
   > Microsoft Support Diagnostic Tool “Follina” — CVE-2022-30190
   > Progress MOVEit Transfer — CVE-2023-34362
   > Citrix NetScaler “CitrixBleed” — CVE-2023-4966
   > Barracuda Email Security Gateway — CVE-2023-2868
   > 3CX DesktopApp supply-chain compromise (2023)
   > XZ Utils supply-chain compromise — CVE-2024-3094
   > CrowdStrike Falcon Channel File 291 outage (2024)
   > Palo Alto Networks PAN-OS — CVE-2024-3400
   > Ivanti Connect Secure / Policy Secure — CVE-2023-46805 and CVE-2024-21887

2. 

   > Design 15 test cases (Objective / Input / Steps / Expected / Actual / Verdict). my device: fan. in vietnamese

3. 

   > draw an ISTQB QA/QC role mindmap for me. output in [mindmap.md](HW01/mindmap.md) , use mermaid

### 2.4 Specific parts to which AI contributed

- **Requirement 1:** OpenAI Codex organized the ten supplied job postings into a consistent report structure, drafted the job summaries and AI-impact analysis, and inserted the ten screenshots supplied by the student.
- **Requirement 2:** ChatGPT Web produced the initial short explanations of twenty defects. OpenAI Codex structured the report fields and revised the content using the student's source-review findings.
- **Requirement 3:** GPT Web drafted fifteen baseline fan test cases. OpenAI Codex incorporated the student's device information, actual results, videos, edge cases, defect evidence, and later report edits.
- **Mindmap and audit artifacts:** OpenAI Codex generated the Mermaid mindmap and assisted with `prompt_log.md`, `AI-02-Audit-Report.md`, and the final report structure.
- **Completed without AI:** collecting the ten job links; taking the job screenshots; reviewing the twenty defect explanations against sources; identifying the fan; performing the physical tests; recording Actual/Verdict values and videos; finding the three edge cases and observed defects; and supplying the three ISTQB classification findings.

### 2.5 How I reviewed, revised, or verified AI output

The job content was checked against the supplied ITviec links and dated screenshots. The twenty defect explanations were compared with the linked vendor, government, and technical sources; unsupported scope, overstatements, and omissions were recorded and corrected in the report. The fan test cases were executed on the identified Senko LTS106A, and the Actual/Verdict fields were filled from observed results supported by videos and issue screenshots. The mindmap was compared with ISTQB CTFL Syllabus v4.0.1, which led to three documented classification findings. AI-generated statements not supported by the available evidence were not added as facts.

### 2.6 Citation

[1] OpenAI, “ChatGPT Web and Codex responses used for HW01,” conversation transcript, Sep. 25–28, 2026. See `HW01/prompt_log.md` and `HW01/ai-appendix/AI-02-Audit-Report.md`.

## 3. Statement of Honesty

By signing below, I confirm that the disclosure above is accurate and complete. I understand that undisclosed or false disclosure of AI use is treated as academic misconduct and may result in a zero grade for the assignment and disciplinary referral.

## Signature

| Field | Value |
|---|---|
| Student name | Nguyễn Đoàn Xuân Thu |
| Student ID | 23120170 |
| Class / Cohort | 23_31 / 2023 |
| Course | CSC130003 |
| Instructor | Dr. Lam Quang Vu; Dr. Tran Duy Hoang; MSc. Tran Thi Bich Hanh; MSc. Truong Phuoc Loc; MSc. Ho Tuan Thanh |
| Date | 28/09/2026 |
| Signature | Thu |

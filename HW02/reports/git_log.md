# Lịch sử Git — HW02

- Repository: `thu2005/Software-testing`
- Branch: `main`
- HEAD tại thời điểm xuất: `3890f48e382de4f14b28b08dadcdc294ceaa0100`
- Thời điểm xuất: `2026-10-17T22:12:36+07:00`
- Bộ lọc: chỉ các commit có subject bắt đầu bằng `[HW02]`
- Số commit: **53**

Lệnh truy xuất tương đương:

```text
git log --reverse --date=iso-strict --pretty=format:"%H%x09%ad%x09%an%x09%s" --grep="^\[HW02\]"
```

## Danh sách commit

```text
Commit                                   Date                       Author  Subject
c8109e790256d2a7e8def8339a985f577e13a437 2026-10-15T02:39:35+07:00  thu     [HW02]: create skills, file templates, update prompt log
48bdd73f50e2b673b89bd480b9fcc361d28ecb34 2026-10-16T16:36:01+07:00  thu     [HW02]: edit prompt log template
12dc9ce8eb7c566387bc9d96165c7b72f992faa7 2026-10-16T16:50:08+07:00  thu     [HW02][FR-01] capture requirements and isolate test runtime
cf93f88556ee92f8eae3b9915e79407068e4116a 2026-10-16T17:28:57+07:00  thu     [HW02][FR-01] design domain testing cases
ed9956a761c0e540cbd89b15bda82303fc3cee11 2026-10-16T17:29:01+07:00  thu     [HW02][FR-01] design boundary value cases
103443beb3741e7e3cc46e3d4acbf9763c9db69a 2026-10-16T17:29:28+07:00  thu     [HW02] log FR-01 DT and BVA design session
72a6d9f4dffcc263900201e830a544f325ab9ce2 2026-10-16T18:03:13+07:00  thu     [HW02][FR-01] reduce DT and BVA suite to 14 cases
46ef59f99cf1f4c611d4d4d263194dd746f4be54 2026-10-16T18:03:59+07:00  thu     [HW02] log FR-01 suite reduction
9655409758f01841c7e2d0d7b27e66d36e391117 2026-10-16T18:19:19+07:00  thu     [HW02][FR-01] review and refine test cases
ba28c68947d89905b3dcebc776c63825579592a8 2026-10-16T18:19:45+07:00  thu     [HW02] log FR-01 test case review
22333a0ef1733106049b3b789cf1a58281e74f3b 2026-10-16T18:44:01+07:00  thu     [HW02][FR-01] record student test case approval
8952c1adba84ea5543caf978e47e767848a830e8 2026-10-16T18:44:20+07:00  thu     [HW02] log FR-01 approval clarification
ee6feae69031eb987dbef5bb7b2470e7fb32d332 2026-10-16T20:10:46+07:00  thu     [HW02][FR-01] record test execution results
295da639047297f03835c1d8af41d7d14308b27d 2026-10-16T20:11:12+07:00  thu     [HW02] log FR-01 test execution
40ea4bf05a3ed750394704fed09fc1e74304479b 2026-10-16T20:43:59+07:00  thu     [HW02][FR-01] add execution evidence and bug reports
f1d50dc52df531e61e544e348985c55779592900 2026-10-16T20:44:21+07:00  thu     [HW02] log FR-01 evidence and bug reporting
fa0dee21d1b1cc6c6a8d9ee254beb66d6969702d 2026-10-16T21:45:37+07:00  thu     [HW02][FR-01] verify environment and issue evidence
f0a01e7a860035886e52ae4d7145d2de30fa7034 2026-10-16T21:46:10+07:00  thu     [HW02] log FR-01 completion review
650a418230004b0e6158c2916060b0a2d360a001 2026-10-16T21:49:22+07:00  thu     [HW02][FR-01] keep execution notes student-authored
b4104445a83927b36947c5e64f1c81dd49300792 2026-10-16T21:49:42+07:00  thu     [HW02] log FR-01 execution ownership correction
711b7132efc6eedfcd9ab23bc2dd383d5bfec95e 2026-10-16T21:54:34+07:00  thu     [HW02] remove redundant files and update prompt log template
639d273417e437e81e7fe85a65adc164355f174d 2026-10-16T21:59:12+07:00  thu     [HW02][FR-01] remove tester-owned execution note
f7c0ab68f9ecb60b567c2a83f8425b9c2d05c782 2026-10-16T21:59:35+07:00  thu     [HW02] log FR-01 gap assessment
411802d1189596c5409c4fb7a02490f031eb71c9 2026-10-16T22:06:35+07:00  thu     [HW02][FR-07] design domain and boundary test cases
79b0910567872693dbb475f66f69af3345ed538a 2026-10-16T22:08:50+07:00  thu     [HW02][FR-07] review and refine test cases
28d5c543cbe03839f291774d8e210aca961d8a22 2026-10-16T22:09:21+07:00  thu     [HW02] log FR-07 test design and review
79cb3ff1ced6394309f6b9ca9ef7c870c1c13876 2026-10-17T17:13:08+07:00  thu     [HW02][FR-07] record execution and bug drafts
e0fd86814ec2842ff60eba92e785cf05d5057fa9 2026-10-17T17:13:38+07:00  thu     [HW02] log FR-07 execution and bug reporting
8c4d30ba5d52ca23789267d1ef292554575e3dde 2026-10-17T17:36:24+07:00  thu     [HW02][FR-07] link GitHub issues and finalize artifacts
036461017bdb36c8143384df6dbab948aa28e6e3 2026-10-17T17:36:57+07:00  thu     [HW02] log FR-07 completion verification
5e51c6196889a31cc641dc54aeda4c06545f0915 2026-10-17T17:44:22+07:00  thu     [HW02][FR-07] document confirmed AI gaps
79c960a2626d537d6fd42c88c19350f8f1fd1a49 2026-10-17T17:44:36+07:00  thu     [HW02] log FR-07 AI gap analysis
048ee78aef1ed0866ec4bc75fe9175150fb8f539 2026-10-17T18:10:58+07:00  thu     [HW02] limit scope of ai gap analysis
7f8a92df45c771b8db7c51883a2fc3759f663b3b 2026-10-17T18:15:14+07:00  thu     [HW02][FR-14] add domain testing design
68af3b61f52fb4220ef02a79435993992f9b10d2 2026-10-17T18:16:14+07:00  thu     [HW02][FR-14] add boundary value analysis
faef8e9cd162b661f9b6a1744df6591391586601 2026-10-17T18:18:15+07:00  thu     [HW02][FR-14] review and refine test cases
f5f84b38e77706327239fffaf364ce372a4794b5 2026-10-17T18:18:32+07:00  thu     [HW02] log FR-14 test design and review
a33f350b375ae24a6ba8034cb0b50e40f7b2b57b 2026-10-17T18:35:43+07:00  thu     [HW02]
673a59b7896f9765228013e43c6750d62a8432f9 2026-10-17T18:36:19+07:00  thu     [HW02]
29624b757262507cbb3d170a9c0cd15ab58f79dc 2026-10-17T19:15:20+07:00  thu     [HW02] bug report and github issue
71cbc1662b567bcc71afc7ce2e0115431283ae2e 2026-10-17T19:29:02+07:00  thu     [HW02] record FR-14 AI gap
8714c69ab96fad46276f2302fd69d63b5c181c69 2026-10-17T19:29:33+07:00  thu     [HW02] append FR-14 gap review prompt log
4a56409dd87c6c42ca383bc9867cfac5bb4f264f 2026-10-17T19:48:42+07:00  thu     [HW02]: ai-gap-analysis and update related bug
b8b96d1fd63627e6800be65f01c7b756a6d4cb6f 2026-10-17T19:59:11+07:00  thu     [HW02] add FR-06 Mobile domain testing
4bfa0c6430c9ce985080f5d878557ec43724991f 2026-10-17T19:59:57+07:00  thu     [HW02] add FR-06 Mobile boundary value analysis
e9b439a9af638d5cdc72aa874f57403939f2c8a0 2026-10-17T20:01:31+07:00  thu     [HW02] review FR-06 Mobile test cases
e3b6a1e38b83e12dc44e23faf77f798f36552818 2026-10-17T20:02:00+07:00  thu     [HW02] append FR-06 Mobile design prompt log
27a353a060d3ea7496330f6baf1e869db360add0 2026-10-17T20:57:06+07:00  thu     [HW02] record FR-06 Mobile execution and bugs
ea26515f8fff500247317bba64395271b5434baa 2026-10-17T20:57:41+07:00  thu     [HW02] append FR-06 Mobile execution prompt log
d1d80b4b23b9248ed236387340fc0eb2b91a07c8 2026-10-17T21:10:31+07:00  thu     [HW02] github issue and bug reports updated
499456e20cf8ab4e3c556e060d20be06b2a0711a 2026-10-17T21:12:04+07:00  thu     [HW02] log FR-06 AI gap review
bcdd437141f6e85fab057567b2e7fe1dfc56b806 2026-10-17T22:08:36+07:00  thu     [HW02] update report
3890f48e382de4f14b28b08dadcdc294ceaa0100 2026-10-17T22:11:01+07:00  thu     [HW02] update report pdf
```

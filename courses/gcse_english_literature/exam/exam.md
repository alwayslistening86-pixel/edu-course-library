# GCSE English Literature (AQA 8702) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile.

## Format
This is a cumulative, original mock covering the whole qualification, sat as two timed papers.

**Paper 1: Shakespeare and the 19th-century novel (1 hour 45 minutes, 64 marks, 40% of the GCSE).** Section A: one extract-based question on Macbeth, requiring analysis of the printed extract and reference to the play as a whole (34 marks: 30 across AO1/AO2/AO3, plus 4 separate AO4 marks for technical accuracy). Section B: one extract-based question on A Christmas Carol, requiring analysis of the printed extract and reference to the novella as a whole (30 marks, AO1/AO2/AO3, no separate AO4).

**Paper 2: Modern texts and poetry (2 hours 15 minutes, 96 marks, 60% of the GCSE).** Section A: a choice of one essay from two options on An Inspector Calls, without a printed extract, requiring reference across the whole play (34 marks: 30 across AO1/AO2/AO3, plus 4 separate AO4 marks). Section B: one named Power and Conflict poem, printed on the paper, compared with a second poem from the same cluster chosen by the learner (30 marks, AO1/AO2/AO3). Section C: unseen poetry, two poems never studied before -- Question 1 responds to and analyses the first poem alone (24 marks, AO1+AO2), Question 2 briefly compares the two poems' methods (8 marks, AO2 only, no personal response or context marks).

Both papers are marked out of their own totals and combined into the 160-mark qualification total (64 + 96); AQA sets exact grade boundaries per exam series rather than a fixed mark-to-grade table, so no such table is used here. There is no non-exam assessment, coursework or spoken-language component in English Literature 8702 (unlike English Language 8700) -- the qualification is assessed entirely through these two written papers.

**Running the mock.** Present an original invented extract from Macbeth (short quotation is fine, this text is public domain) for Paper 1 Section A, and an original invented extract from A Christmas Carol (short quotation is fine, this text is public domain) for Section B. For Paper 2 Section A, set an original essay question on An Inspector Calls (paraphrase only in any model material, since this text is in copyright). For Section B, print one Power and Conflict poem's title and ask the learner to compare it with a self-chosen second poem from the cluster (respecting each poem's copyright status when quoting). For Section C, present two short original invented poems, never studied, written in a style and difficulty comparable to real unseen-poetry exam choices, and set both questions. Use entirely original extracts, essay prompts and unseen poems -- never real AQA past-paper material, and never a real, whole in-copyright poem reproduced in full.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. Grade each essay on its own six-level ladder (or the appropriate AO1/AO2 split for unseen poetry Question 1, and the AO2-only descriptor for Question 2), and grade AO4 technical accuracy separately on the Shakespeare and modern-text questions.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the paper(s) and question(s) that broke down (for example "Paper 2 Section B comparison did not sustain the comparison throughout; revisit S11-S13's comparison practice"), offer targeted review of the relevant stage(s), then a fresh original retry paper covering the same question types.

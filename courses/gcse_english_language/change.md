# Change log — gcse_english_language

## 2026-09-23 — live recheck (course-runner)

**Source:** AQA, "GCSE English Language 8700 — 2026 updates" (https://www.aqa.org.uk/english-language-changes); specification-at-a-glance page (cover dated 20 Mar 2026). First assessed: **summer 2026**.

**Unchanged (confirmed):** paper structure, number of questions, marks per question and per paper, AO allocation per question, timings. Spoken Language endorsement unchanged (0% weighting, separately reported).

**Changed — not reflected in this course's lessons or rubric (built from the June 2021 P1 / June 2022 P2 mark schemes):**

| Paper / Q | Old (as taught here) | New (from summer 2026) | Affected stages |
|---|---|---|---|
| P1 Q1 (4 marks, AO1) | List four things from a set part of the extract | Multiple-choice: shade the circles by the correct statements | S01 (description), S07 |
| P1 Q3 (8 marks, AO2) | How has the writer structured the text to interest you as a reader (range of structural features) | Focus narrowed to analysing one named structural effect | S01 (description), S12 |
| P1 Q4 (20 marks, AO4) | "A student said…" statement; agree/disagree | No "student" framing; revised methods bullet; may agree and/or disagree; question names the section of the extract; added evaluative support wording | S14 |
| P1 Q5 (40 marks) | Narrative option = full story | Narrative option may be the opening of a story; picture prompt need not be depicted literally | S18 |
| P2 Q2 (8 marks, AO1) | Summary of differences | Reworded for clarity (task unchanged in substance) | S09 |
| P2 Q4 (16 marks, AO3) | Methods bullet | Methods bullet reworded | S15 |
| Mark schemes (both papers) | 2021/2022 schemes | Refined marking guidance; level structure and marks unchanged | all graded reading/writing stages |

**Graded criteria:** S01's rubric (paper lengths, marks, AOs, levels, endorsement) is **not invalidated** — marks and AOs are unchanged. No stage has a recorded pass yet for any learner reviewed here, so no pass is invalidated.

**Also found (content error, not a spec change):** S01 lesson.md, item 2.NEA, says Spoken Language is taught in "stages S28 and S29"; the ladder has S22 and S23.

**Action:** `/audit` recommended to re-sync lessons, practice, tests and rubric entries for S07, S09, S12, S14, S15, S18 (and S01 wording) with the summer-2026 question formats and the current mark schemes.

## 2026-09-26 — /audit

**Fixed:** S01 lesson.md now says Spoken Language is taught in stages S22 and S23 (it previously said S28 and S29).
**Re-confirmed live:** AQA's summer-2026 question changes (https://www.aqa.org.uk/english-language-changes) still stand. **Still outstanding:** S07, S09, S12, S14, S15, S18 (and S01's paper descriptions) have not been updated for the new P1 Q1/Q3/Q4/Q5 and P2 Q2/Q4 formats. The audit does not write teaching content. The remedy is expanding those stages in place. Coverage stays `full`, because the spec items are unchanged and only the question formats changed.
**Provenance note:** the cited filestore PDF (AQA-8700-SP-2015.PDF) still serves Version 1.5 (Oct 2021). The Version 1.6 (Mar 2026) recorded here comes from AQA's web specification pages.

## 2026-09-28 — 2026 format remediation

**Fixed:** the outstanding remediation identified in the two entries above is now complete. S01 (paper descriptions), S07 (P1 Q1 rewritten to the 2026 shade-the-boxes format, with practice/test scenarios and rubric criteria rewritten to match), S09 (P2 Q2 wording note), S12 (P1 Q3 rewritten to the 2026 named-effect format, with practice/test/rubric updated), S14 (P1 Q4 "a student said" framing removed, "agree and/or disagree" made explicit), S15 (P2 Q4 wording note), and S18 (P1 Q5 descriptive-imagination and narrative-opening wording) all now teach and test the 2026 question formats. `curriculum_map.json`'s P1.Q1 and P1.Q3 syllabus-item titles updated to match. A `learner_notices` entry (`aqa_2026_format_update`) summarises the changes and their sourcing for the learner/tutor.

**Source:** confirmed directly from AQA's own published change page (https://www.aqa.org.uk/english-language-changes), cross-checked against several independent GCSE revision publishers (Save My Exams, Think Smart Academy, Uplevel Academy, Satchel Learning) who independently describe the same substance. Marks, AOs, timings and paper structure remain unchanged throughout, confirmed both by AQA's page and by this course's own rubric/exam structure, which did not need to change.

**Coverage:** unchanged at `full` -- this was a question-format and wording update, not a syllabus-content change.

**Post-update verification fix (same day):** independent verification found `S07/test.md`'s Part 2 (the pre-existing, unchanged Paper 2 Q1 practice scenario) actually had five true statements among its eight (B, C, E, F, H), not four, because statement F ("they stop at the top of the hill") was true rather than a distractor -- an inconsistency that predates this update but was only surfaced by it. Fixed by changing F to "They stop at the bottom of the hill" (now false) and adding the missing "(Correct: B, C, E, H.)" answer key, matching Part 1's style. Revalidated clean.

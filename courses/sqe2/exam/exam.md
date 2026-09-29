# SQE2 (Solicitors Qualifying Examination, Stage 2) — Practical Legal Skills - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile (all six skills' core-technique and worked-scenario stages).

## Format
Reflects the real SQE2 assessment, which is split into oral and written sittings held over multiple half-day sessions, sampling the five practice-area contexts (Criminal Practice, Dispute Resolution, Property Practice, Wills and Intestacy/Probate Administration and Practice, and Business Organisations Rules and Procedures):

**Oral sitting (two half-days, four assessments, live or recorded before an assessor):**
- One Advocacy assessment (45 minutes' preparation, 15-minute presentation) in one practice-area context
- One Advocacy assessment in a second practice-area context
- One Client Interview and attendance note assessment (25-minute interview with 10 minutes' preparation, plus 25 minutes to write the attendance note) in a third practice-area context
- One Client Interview and attendance note assessment in a fourth practice-area context

**Written sitting (three half-days, twelve assessments, computer-based):**
- Case and Matter Analysis (60 minutes), Legal Research (60 minutes), Legal Writing (30 minutes) and Legal Drafting (45 minutes) tasks, set across the five practice-area contexts over the three half-days, such that by the end of the written sitting every one of the four written skills has been assessed at least twice, in different contexts, and Business Organisations Rules and Procedures is covered on its own half-day alongside the other four contexts elsewhere in the sitting

The exact skill-to-context pairing on any candidate's paper is set by the SRA per sitting and is not fixed; this course simulates a representative full spread by running one assessment per skill per practice-area context (30 assessments total: 6 skills x 5 contexts), which is broader than any single real sitting but ensures every combination taught in the course has been tested at least once before the course is marked complete.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. For the oral component, assess live delivery: structure, technique (questioning or submission), and etiquette/conduct, plus (for interviewing) the attendance note produced afterwards. For the written component, assess the submitted document or analysis against the same criteria used in the stage tests: correct method, accurate content, clear structure, and a usable, client-focused conclusion or product.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the specific skill(s) and/or practice-area context(s) that broke down, offer targeted review of that stage, then a fresh retry with a new original scenario in the same skill/context combination.

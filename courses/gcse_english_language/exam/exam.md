# GCSE English Language (AQA 8700) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile.

## Format
This is a cumulative, original mock covering the whole qualification, sat as two timed papers (or in one combined sitting if the learner prefers, noting the split below).

**Paper 1: Explorations in Creative Reading and Writing (1 hour 45 minutes, 80 marks, 50% of the GCSE).** One unseen, substantial extract of 20th- or 21st-century literature fiction. Section A (reading, 40 marks): Q1 shade four true statements (4 marks, AO1 -- shade-the-boxes format from 2026, replacing the earlier free-response 'list four things'); Q2 language analysis of a short extract (8 marks, AO2); Q3 how the whole source is structured, naming a single effect to track such as suspense or tension (8 marks, AO2 -- named-effect wording from 2026); Q4 evaluate a given statement about part of the source with judicious quotation (20 marks, AO4 -- from 2026 the statement is given directly, without the earlier 'a student said' framing). Section B (writing, 40 marks): Q5, a choice of one descriptive task (which from 2026 explicitly invites going beyond the literal picture) or one narrative task (which from 2026 explicitly accepts just the opening of a story) from an image and/or title (24 marks AO5, 16 marks AO6).

**Paper 2: Writers' Viewpoints and Perspectives (1 hour 45 minutes, 80 marks, 50% of the GCSE).** Two linked non-fiction/literary non-fiction sources, one 19th-century and one 20th/21st-century, on a shared theme. Section A (reading, 40 marks): Q1 choose four true statements (4 marks, AO1, unchanged for 2026); Q2 summarise differences/similarities between the sources, based on inference (8 marks, AO1 -- 'based on inference' made explicit in the 2026 wording); Q3 language analysis of one specified source (12 marks, AO2); Q4 compare both sources' perspectives and methods, with sharper 2026 wording on finding supporting quotations (16 marks, AO3). Section B (writing, 40 marks): Q5, one viewpoint writing task in a specified real-world form responding to the theme (24 marks AO5, 16 marks AO6).

Each paper is marked out of 80 raw marks; both are weighted equally (no scaling factor beyond combining the two 80s into a 160-mark total), and grade boundaries for 9-1 are set by AQA per exam series, so no fixed mark-to-grade table is used here.

**Spoken Language endorsement (non-exam assessment, separately reported).** Not part of this timed mock: the endorsement is a one-off, centre-assessed prepared talk with follow-up questions, graded Pass/Merit/Distinction/Not Classified, and does not contribute marks to, or combine with, the Paper 1/Paper 2 grade. If the learner has not already completed S22-S23's spoken practice, the tutor should note this as outstanding but must not block the written exam on it, since AQA reports it independently.

**Running the mock.** Present an original unseen fiction extract for Paper 1 and set Q1-Q5 in order, timed at roughly 1h45 total (or untimed with a note that timing was waived, if the learner needs that). Then present two original linked non-fiction extracts (one written in a deliberately 19th-century register, one contemporary) for Paper 2 and set Q1-Q5 in order, similarly timed. Use entirely original extracts and questions -- never real AQA past-paper material -- built in the same style, length and difficulty as the board's own papers.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. Grade each of the ten questions (five per paper) against the levels-of-response or AO6 grid it belongs to, using the same level descriptors taught in the stage tests, and grade the two writing questions on both the AO5 and AO6 grids separately as AQA does.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the paper(s) and question(s) that broke down (for example "Paper 2 Q4 comparison stayed at Level 2; revisit S15"), offer targeted review of the relevant stage(s), then a fresh original retry paper covering the same question types.

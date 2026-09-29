# GCSE French (AQA 8652) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile.

## Format
A written simulation of all four AQA 8652 papers, each equally weighted at 25%:
1. **Listening simulation**: a comprehension exercise (5 questions) plus a dictation (Foundation 20+ words, Higher 30+ words) read aloud by the tutor.
2. **Speaking simulation, written**: a five-task role-play response, a short reading-aloud passage with two follow-up question answers, and a two-photo description with detail, opinion and personal link for each photo.
3. **Reading and translation**: a comprehension exercise (5 questions) plus a French-to-English translation (Foundation 35+ words, Higher 50+ words).
4. **Writing simulation**: Foundation sits a five-bullet task, a five-item gap-fill, and an English-to-French translation; Higher sits a three-bullet task and a 150-word open-ended task with two bullets. Content is drawn from at least two different themes across the four papers, so no single topic's vocabulary can carry the whole exam.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. This is a course-level indicator of GCSE-standard performance across the four skills, not an official AQA grade, since AQA combines all four papers against grade boundaries set each year after the live series.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the paper(s)/stage(s) that broke down, offer targeted review of the relevant topic or paper stage, then a fresh retry paper.

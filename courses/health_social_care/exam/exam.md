# Health and Social Care (OCR Cambridge National Level 1/2, J835) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile.

## Format
This qualification is assessed by one externally examined written paper and two non-exam assessment (NEA) units, matching OCR's real structure (all figures per the J835 specification, section 5):
- **R032 Principles of care in health and social care settings** (mandatory, externally examined): 1 hour 15 minutes, 70 marks (80 UMS), 40% of the qualification. Six compulsory questions mixing short/medium answer and extended-response formats, with three questions set in a scenario, up to two six-mark extended-response questions and one eight-mark extended-response question assessing PO3 (discussion/evaluation). No calculator is used. OCR's rule is that the exam is sat in the candidate's final assessment series.
- **R033 Supporting individuals through life events** (mandatory, NEA): an OCR-set assignment, 60 marks (60 UMS), 20% of the qualification, centre-assessed and OCR-moderated, covering research into life stages, PIES development, an authenticated interview with a consenting individual about real life events, and evidence against the Task 1 and Task 2 marking criteria.
- **R035 Health promotion campaigns** (the optional unit selected for this course, NEA): an OCR-set assignment, 60 marks (60 UMS), 20% of the qualification, centre-assessed and OCR-moderated, covering research and choice of a public health challenge, a campaign plan, a teacher-observed live delivery (suggested 10 to 20 minutes) and a written self-evaluation, against the Task 1 to Task 4 marking criteria.
- Overall qualification: 200 UMS available for a candidate taking R032, R033 and R035 (the excluded optional unit R034 is not built in this course, per `declared_exclusions`). Grades run Distinction* and Distinction, Merit and Pass at Level 2, and Distinction, Merit and Pass at Level 1, using UMS thresholds OCR publishes for each series rather than a single fixed table.

## Example structure
Because this micro-profile has no way to run a live 1 hour 15 minute timed paper or a real observed campaign delivery, the exam stage combines a written paper simulation and an NEA-evidence simulation, both cumulative across every stage taught:
1. **R032 paper simulation**: six original questions in OCR's real mix (short/medium answer plus two six-mark and one eight-mark extended-response question, at least one scenario-based), drawing on J835-SYN, R032-1.1 to R032-4.5 and R032-X1 to R032-X5, marked against the paraphrased levels of response from S10.
2. **R033 NEA evidence check**: original prompts covering life stages and PIES development, factors and life events, the interview and authentication rules, and Task 2a/2b evidence requirements, drawing on the R033 items across S11 to S16.
3. **R035 NEA evidence check**: original prompts covering public health issues, factors and barriers, campaign planning, delivery and evaluation, and the Task 1 to Task 4 evidence requirements, drawing on the R035 items across S17 to S22.
No real past-paper or live set-assignment text is used anywhere in this stage; all questions and scenarios are original.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. A pass requires Level 3/MB3-consistent performance held across all three units under mixed, cumulative conditions, not just within a single stage.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the stage(s) or unit(s) that broke down, offer targeted review or a fresh retry paper.

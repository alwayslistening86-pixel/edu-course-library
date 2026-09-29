# Creative iMedia (OCR Cambridge National Level 1/2, J834) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` (S01-S29) shows a passed test in the micro-profile.

## Format
J834's real assessment is not a single sitting: it is one externally examined paper plus two centre-assessed, OCR-moderated non-exam assessment (NEA) units, all cumulative on everything taught across S01-S29.
- **R093 (external assessment)**: one written paper, 1 hour 30 minutes, 70 marks, sat under exam conditions in the learner's final series (the terminal assessment rule, J834-STRUCT). Section A: approximately 10 marks of short, closed recall questions drawing on any R093 Topic Area (S01-S12). Section B: approximately 60 marks of scenario-based questions built around a single fictional media product/client, including three extended-response questions (two testing analysis/evaluation, one testing recall and application), using OCR's command words (Appendix B, S12).
- **R094 (NEA)**: a set assignment of two tasks across six strands (50 marks/50 UMS), producing a visual identity and a digital graphic for a stated client and audience (S13-S19).
- **R097 (NEA)**: a set assignment of three tasks across eight strands (70 marks/70 UMS), planning, creating and reviewing an interactive digital media product for a stated client and audience (S20-S28).
This course's cumulative exam simulates all three components together in one sitting, since the learner has now covered every stage: an R093-style timed paper, followed by two original NEA-style set-assignment briefs (one visual-identity brief, one interactive-media brief) completed under the same independence rules taught in S29 (J834-NEA). No part of this reuses real OCR set assignments or past papers; all scenarios are original.

## Example structure
Part 1 (R093-style paper, 45 minutes for this simulation): Section A, five short recall questions drawn from any of S01-S12; Section B, one scenario with three extended responses (one analysis, one evaluation, one recall-and-application) built around a single fictional media product, requiring the audience, research, media codes, planning documents, legal/regulatory and file-format knowledge from S01-S12.
Part 2 (R094-style brief): one short original client brief; the learner produces a design concept, justification and planning documentation (Task 1 style, drawing on S13-S16) and describes/evidences the creation and export decisions they would make (Task 2 style, drawing on S17-S19).
Part 3 (R097-style brief): one short original client brief; the learner produces planning documentation including a wireframe, asset table and navigation diagram (Task 1 style, drawing on S20-S24), describes the build, saving and export decisions (Task 2 style, drawing on S25-S27), and writes a test plan plus a review with prioritised recommendations (Task 3 style, drawing on S28).
Throughout, the learner should apply J834-PO's four performance objectives, J834-GRADE's UMS/grading logic when asked to interpret marks, and J834-SYN's synoptic links between R093 and the NEA units.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. For Part 1, mark Section A questions for accurate recall and Section B extended responses for structure, use of the correct command word, and coverage of both sides of an analysis/evaluation question. For Parts 2 and 3, mark each strand-style response against the three OCR mark bands (MB1 limited/basic, MB2 adequate/sound, MB3 effective/fully suitable/comprehensive) exactly as taught in S13 and S20, with no MB1 evidence in a task scoring zero for that task.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the stage(s) that broke down (for example weak Section B extended responses pointing back to S01-S12, or thin NEA planning pointing back to S16 or S23-S24), and offer targeted review or a fresh retry paper with new original scenarios.

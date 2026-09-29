# Engineering Design (OCR Cambridge National Level 1/2, J822) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` (S01-S10) shows a passed test in the micro-profile.

## Format
J822's real assessment is not a single sitting: it is one externally examined paper plus two centre-assessed, OCR-moderated non-exam assessment (NEA) units, all cumulative on everything taught across S01-S10.
- **R038 (external assessment)**: one written paper, 1 hour 15 minutes, 70 marks, sat under exam conditions in the learner's final series (the terminal assessment rule, J822-STRUCT). It mixes multiple choice questions, short answer questions (single-mark list items up to two-or-more-mark developed responses) and extended response questions marked on OCR's three-level-of-response scheme, drawing on any of R038's four Topic Areas (S01-S04) and using the command words in Appendix B (S05).
- **R039 (NEA)**: a set assignment of four tasks (60 marks/60 UMS), producing freehand design proposals, a developed proposal, orthographic/assembly drawings and CAD presentation drawings for a set brief (S06-S07).
- **R040 (NEA)**: a set assignment of six tasks (60 marks/60 UMS), analysing, disassembling, virtually modelling, planning, manufacturing and evaluating a prototype for a set brief (S07-S10).
This course's cumulative exam simulates all three components together in one sitting, since the learner has now covered every stage: an R038-style timed paper, followed by two original NEA-style set-assignment briefs (one communicating-designs brief, one design-evaluation-and-modelling brief) completed under the same independence rules taught in S10 (J822-NEA). No part of this reuses real OCR set assignments or past papers; all scenarios are original.

## Example structure
Part 1 (R038-style paper, 40 minutes for this simulation): five short recall/short-answer questions drawn from any of S01-S04, plus one extended response question requiring discussion and weighing of alternatives (for example comparing two design strategies, or discussing a manufacturing consideration), marked on the three-level-of-response scheme from S05.
Part 2 (R039-style brief): one short original product brief; the learner produces (or fully describes) two freehand design proposals with rendering and annotation, develops one further, produces a conventioned orthographic/assembly drawing, and describes the CAD presentation evidence they would produce (drawing on S06-S07).
Part 3 (R040-style brief): one short original product brief; the learner analyses an existing product with ACCESS FM and a comparison matrix, describes a disassembly with hazards and safety controls, describes a 3D CAD model, writes a production plan with a risk assessment, describes photographic-diary evidence for manufacture, and evaluates a finished prototype with justified improvements (drawing on S08-S10).
Throughout, the learner should apply J822-PO's four performance objectives, J822-GRADE's UMS/grading logic when asked to interpret marks, and J822-SYN's synoptic links between R038 and the NEA units.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. For Part 1, mark short answer/recall questions for accuracy and the extended response for structure, correct terminology, and genuine development of two or more points to Level 3 standard. For Parts 2 and 3, mark each task-style response against OCR's three mark bands (MB1 limited/basic, MB2 adequate/sound, MB3 comprehensive/effective) exactly as taught in S06 and S07, with no MB1 evidence in a task scoring zero for that task.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the stage(s) that broke down (for example a weak extended response pointing back to S05, or thin production planning pointing back to S09), and offer targeted review or a fresh retry paper with new original scenarios.

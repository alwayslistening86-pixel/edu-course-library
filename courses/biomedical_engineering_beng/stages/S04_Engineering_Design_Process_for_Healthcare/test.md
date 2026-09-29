# S04_Engineering_Design_Process_for_Healthcare - Test: Engineering Design Process for Healthcare

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Outline the engineering design process from initial user-needs research through to prototyping and iteration, naming at least six distinct stages in order, and explain why the process is described as iterative rather than strictly linear. [4 marks]
2. Construct a simple weighted decision matrix (in words: name the rows, columns and scoring method) to choose between three concepts for a home blood-pressure monitor against the criteria accuracy, cost and ease of use, where accuracy is twice as important as the other two criteria. [4 marks]
3. Which of the following are examples of designing to prevent a use error by the device's physical form, rather than by instructions alone (a human-factors principle)? Choose every correct option.
   A. A connector shaped so it can only be attached one way round
   B. A warning label printed in the instructions manual
   C. A drug cartridge that will not fit into the wrong device model
   D. A verbal training session for new users
4. Explain why a design specification requirement such as 'the device must comply with relevant medical device regulation' needs to be made specific and testable at the specification stage rather than left general, referencing the evaluation/Pugh-matrix method from this stage. [3 marks]
5. A design team is choosing between an injection-moulded polymer housing and a machined aluminium housing for a low-cost home medical device expected to sell in large volumes. Using DFMA principles, give one reason favouring each option. [2 marks]

## Answer key (for the tutor only)
1. [4] B3 (up to 3 marks for stages, at least six of: research/needs -> specification -> concept generation -> evaluation -> development/detailing -> communication/CAD -> manufacture planning -> prototype/test -> evaluate/iterate); B1 iterative because evaluation at any stage can send the process back to revise an earlier stage, rather than proceeding strictly forwards.
2. [4] B1 rows = the three concepts (one, a datum, may be an existing product); B1 columns = the criteria, each with a weight (accuracy weight 2, cost weight 1, ease of use weight 1); B1 each concept scored per criterion (e.g. against the datum: better/same/worse, or a numeric scale), each score multiplied by its criterion's weight; B1 weighted scores summed per concept; the highest weighted total is selected.
3. Correct: A, C (exactly these options, no others)
4. [3] B1 a vague requirement cannot be scored consistently in a weighted decision matrix, since 'better' or 'worse' compliance cannot be judged without a concrete criterion; B1 it should instead name the specific regulatory classification/standard the device must meet (linking forward to the medical device regulation content in S13); B1 a testable requirement can be checked and evidenced later, which matters if the design decision is scrutinised as part of regulatory evidence.
5. [2] B1 injection moulding: very low per-unit cost at high volume once tooling is paid for, and can combine several features into one moulded part (reducing part count); B1 machined aluminium: no tooling investment needed, so favoured for low volumes or where high strength/stiffness or heat dissipation is required.

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Engineering_Design_Process_for_Healthcare` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Biomechanics_I_Statics_and_Musculoskeletal_Mechanics.

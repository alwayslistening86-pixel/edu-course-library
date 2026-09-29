# S20_Boolean_Logic - Test: Boolean logic: truth tables, gates and circuits

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Construct the full truth table for a two-input OR gate. [2 marks]
2. Construct the full truth table for the Boolean expression NOT A AND B. [4 marks]
3. Write the Boolean expression for a circuit where the output is 1 only if input A is 1 and input B is 0. [2 marks]
4. A circuit's output is 1 in every row of its truth table except when both A and B are 0. Identify which single logic gate this describes. [1 mark]
5. Which logic gate's output is 1 only when its two inputs differ from each other? Choose every correct option.
   A. `XOR`
   B. `AND`
   C. `OR`
   D. `NOT`

## Answer key (for the tutor only)
1. [2] B2 all four rows correct: 0,0->0; 0,1->1; 1,0->1; 1,1->1 (1 mark for 3-4 correct, full marks for all 4 correct with headers).
2. [4] M1 correctly evaluates NOT A for each row; M1 correctly ANDs with B for each row; A2 all four rows correct: A=0,B=0->0; A=0,B=1->1; A=1,B=0->0; A=1,B=1->0.
3. [2] B1 correctly identifies AND combined with a NOT on B; B1 A AND (NOT B).
4. [1] B1 OR.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S20_Boolean_Logic` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S21_Programming_Languages_and_Translators.

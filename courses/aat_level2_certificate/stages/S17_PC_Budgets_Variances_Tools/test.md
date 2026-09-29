# S17_PC_Budgets_Variances_Tools - Test: Budgets, variances and spreadsheet tools

## How to run this
A real checkpoint in AAT's own style: numeric gap-fill calculations, journal/ledger-entry questions and multiple-choice items, with marks shown. Give the whole test at once, with no hints and a calculator allowed (as in the real assessment). Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A fixed budget assumes £12,000 fixed costs and £5 variable cost per unit at a budgeted output of 800 units. Actual output was 1,000 units. Calculate the flexed budget at the actual output level. [3 marks]
2. Budgeted income is £40,000; actual income is £37,600. Calculate the variance in £ and as a percentage, and state whether it is adverse or favourable, explaining your reasoning. [4 marks]
3. Explain what exception reporting is, and why a business would use it rather than reporting on every variance found. [3 marks]
4. Write the correct spreadsheet formula to add the values in cells B2 to B8, and explain what is wrong with the alternative =SUM(B2,B8). [2 marks]
5. Which of these is an acceptable spreadsheet formula for subtracting cell B11 from cell C11? Choose every correct option.
   A. =C11-B11
   B. =+C11-B11
   C. =SUM(C11-B11)
   D. =PRODUCT(C11-B11)

## Answer key (for the tutor only)
1. [3] M1 flexed budget = 12,000 + (5x1,000); A1 £17,000; B1 correct method (fixed costs unchanged; variable cost scaled to actual output, not budgeted output).
2. [4] M1 variance = 37,600-40,000 = -£2,400, i.e. £2,400; A1 percentage = 2,400/40,000 x100 = 6.0%; B1 adverse; B1 reasoning: actual income is lower than budgeted, which makes profit worse, so a shortfall in income is an adverse variance (the opposite of a cost variance, where a lower actual figure is favourable).
3. [3] B1 exception reporting means only reporting variances that are significant against the organisation's own policy (e.g. a set threshold); B1 it focuses management's limited time and attention on the variances that matter most, rather than being swamped by minor/insignificant differences; B1 the report should include the potential cause(s) and effect(s) of each significant variance, not just its size.
4. [2] B1 correct: =SUM(B2:B8); B1 =SUM(B2,B8) uses an unnecessary comma and would add only B2 and B8 together, not the whole range B2 to B8.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S17_PC_Budgets_Variances_Tools` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 10 (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S18_BE_Contract_Law.

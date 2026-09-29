# S24_Non_Parametric_Tests - Test: Non-parametric tests

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The resting pulse rates of 8 people before and after a fitness course are: before [72, 68, 75, 80, 66, 71, 78, 69], after [70, 65, 76, 74, 63, 70, 72, 64]. Use a Wilcoxon matched-pairs signed-rank test at the 5% level to test whether pulse rates have decreased. (The one-tailed 5% critical value for n = 8 is 5.) [7 marks]
2. A sample of 12 values has 10 above the claimed median of 20 and 2 below. Carry out a sign test at 5% for H1: median > 20. [4 marks]
3. State one advantage and one disadvantage of the Wilcoxon signed-rank test compared with the sign test. [2 marks]

## Answer key (for the tutor only)
1. [7] B1 H0: median difference 0, H1: median before - after > 0; M1 differences [2, 3, -1, 6, 3, 1, 6, 5]; M1 ranks the absolute differences (ties averaged); A1 W+ = 34.5, W- = 1.5; A1 T = 1.5; M1 compares with 5; A1 reject H0: evidence pulse rates have decreased.
2. [4] B1 X ~ B(12, 0.5); M1 P(X ≥ 10); A1 0.0193; A1 < 0.05, reject H0: evidence the median exceeds 20.
3. [2] B1 advantage: it uses the size of the differences, so it is more powerful; B1 disadvantage: it assumes a symmetric distribution.

## Grading
Apply `rubric.json`'s `stage_rubrics.S24_Non_Parametric_Tests` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S25_Correlation_and_Regression.

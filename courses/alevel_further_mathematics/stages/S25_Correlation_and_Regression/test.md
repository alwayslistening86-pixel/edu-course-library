# S25_Correlation_and_Regression - Test: Correlation and regression

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. x: [1.2, 2.0, 2.9, 3.8, 4.5, 5.1, 6.3, 7.0]; y: [3.1, 4.0, 5.2, 5.9, 7.1, 7.4, 8.8, 9.5]. (a) Calculate the PMCC. (b) Test at 5% for positive correlation (critical value for n = 8 is 0.6215). (c) Find the regression line of y on x and estimate y when x = 4. [8 marks]
2. Two judges rank 8 entries: judge A [1, 2, 3, 4, 5, 6, 7, 8], judge B [2, 1, 4, 3, 6, 5, 8, 7]. Calculate Spearman's coefficient and test for positive association at 5% (critical value 0.6429). [5 marks]
3. A scatter diagram shows a curved but always increasing relationship. Which correlation coefficient is more appropriate and why? [2 marks]

## Answer key (for the tutor only)
1. [8] M1 calculates S_xx, S_yy, S_xy; A1 r = 0.9980; B1 H0: ρ = 0, H1: ρ > 0; A1 r > 0.6215, reject H0: evidence of positive correlation; M1 b = S_xy/S_xx; A1 b = 1.1040; A1 a = 1.8487; A1 y ≈ 6.26.
2. [5] M1 d values all ±1; M1 Σd^2 = 8; A1 r_s = 1 - 48/504 = 0.9048; M1 compares with 0.6429; A1 reject H0: evidence of agreement between the judges.
3. [2] B1 Spearman's; B1 it measures monotonic association, not linearity.

## Grading
Apply `rubric.json`'s `stage_rubrics.S25_Correlation_and_Regression` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S26_Dimensional_Analysis.

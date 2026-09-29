# S22_Linear_Combinations_Estimation_and_Tests - Test: Linear combinations, estimation, tests and confidence intervals

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Bags of flour are N(1010, 8^2) g and the empty boxes N(150, 5^2) g, independently. A box holds 6 bags. Find the probability that a full box weighs more than 6250 g. [5 marks]
2. A sample of 50 batteries has Σx = 1024 hours and Σx^2 = 21580. Find unbiased estimates of the mean and variance, and a 95% confidence interval for the mean lifetime. [6 marks]
3. A manufacturer claims the mean lifetime is 21 hours. Using the previous sample, test at 5% whether the mean is less than 21. [5 marks]
4. X has variance 4. Find Var(X1 + X2 + X3) and Var(3X), where X1, X2, X3 are independent observations of X, and explain the difference. [3 marks]

## Answer key (for the tutor only)
1. [5] M1 total mean 6 x 1010 + 150 = 6210; M1 variance 6 x 64 + 25 = 409; A1 N(6210, 409); M1 P(T > 6250); A1 0.0240.
2. [6] B1 x̄ = 20.48; M1 s^2 = (21580 - 1024^2/50)/49; A1 s^2 = 12.418; M1 x̄ ± 1.96 s/root50; A1 interval (19.50, 21.46); B1 CLT justifies normality with n = 50.
3. [5] B1 H0: μ = 21, H1: μ < 21; M1 z = (20.48 - 21)/(s/root50); A1 z = -1.043; M1 compares with -1.645; A1 do not reject H0: insufficient evidence that the mean is below 21 hours.
4. [3] B1 12; B1 36; B1 three separate observations vary independently, whereas 3X scales one observation.

## Grading
Apply `rubric.json`'s `stage_rubrics.S22_Linear_Combinations_Estimation_and_Tests` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S23_Chi_Squared_Tests.

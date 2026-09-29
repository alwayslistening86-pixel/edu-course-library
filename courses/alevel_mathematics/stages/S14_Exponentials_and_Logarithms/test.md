# S14_Exponentials_and_Logarithms - Test: Exponentials and logarithms

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Solve log_3(2x + 5) - log_3(x - 1) = 2. [4 marks]
2. Solve e^(2x) - 5e^x + 6 = 0, giving exact answers. [3 marks]
3. The value of a car is modelled by V = 18000e^(-0.15t), where t is its age in years. Find (a) its initial value, (b) its value after 4 years, (c) when it first falls below £5000. [5 marks]
4. Data are thought to follow y = ax^n. A graph of log10 y against log10 x is a straight line through (0.5, 1.6) and (2.0, 4.6). Find n and a. [4 marks]
5. Sketch y = e^(x) - 3, giving the equation of the asymptote and the coordinates of the axis intercepts. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 log_3((2x + 5)/(x - 1)) = 2; M1 (2x + 5)/(x - 1) = 9; A1 2x + 5 = 9x - 9; A1 x = 2.
2. [3] M1 (e^x - 2)(e^x - 3) = 0; A1 x = ln 2; A1 x = ln 3.
3. [5] B1 £18000; M1 18000e^(-0.6); A1 £9,879; M1 -0.15t = ln(5/18); A1 t = 8.54 years.
4. [4] M1 gradient (4.6 - 1.6)/(2.0 - 0.5); A1 n = 2; M1 intercept 1.6 - 2(0.5) = 0.6; A1 a = 10^0.6 ≈ 3.98.
5. [3] B1 shape; B1 asymptote y = -3; B1 (0, -2) and (ln 3, 0).

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Exponentials_and_Logarithms` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Differentiation_Basics.

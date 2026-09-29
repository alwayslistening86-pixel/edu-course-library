# S12_Series - Test: Summation of series and the method of differences

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Show that Σ (r = 1 to n) (2r - 1)^2 = n(2n - 1)(2n + 1)/3. [4 marks]
2. (a) Express 1/((2r - 1)(2r + 1)) in partial fractions. (b) Hence find Σ (r = 1 to n) 1/((2r - 1)(2r + 1)). (c) Find the sum to infinity. [6 marks]
3. Find Σ (r = 11 to 20) r^2. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 expands 4r^2 - 4r + 1; M1 uses standard results; A1 (2n(n + 1)(2n + 1)/3) - 2n(n + 1) + n; A1 factorises to the result.
2. [6] B1 (1/2)(1/(2r - 1) - 1/(2r + 1)); M1 writes out terms; M1 cancels; A1 (1/2)(1 - 1/(2n + 1)); A1 = n/(2n + 1); B1 1/2.
3. [2] M1 Σ(1 to 20) - Σ(1 to 10) = 2870 - 385; A1 2485.

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Series` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Hyperbolic_Functions.

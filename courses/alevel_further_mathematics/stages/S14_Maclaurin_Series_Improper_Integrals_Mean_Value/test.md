# S14_Maclaurin_Series_Improper_Integrals_Mean_Value - Test: Maclaurin series, improper integrals and mean value

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the first three non-zero terms of the Maclaurin series of e^x cos x, and hence estimate ∫ (0 to 0.2) e^x cos x dx. [5 marks]
2. Evaluate ∫ (0 to ∞) x e^(-2x) dx, showing the limiting process. [4 marks]
3. Explain why ∫ (0 to 1) 1/x dx does not exist. [2 marks]
4. Find the mean value of y = x^2 + 1 on [0, 3]. [2 marks]

## Answer key (for the tutor only)
1. [5] M1 multiplies series; A1 1 + x - x^3/3 (terms up to x^3); M1 integrates term by term; A1 estimate 0.21987; B1 compared with the exact 0.21986.
2. [4] M1 parts: -xe^(-2x)/2 - e^(-2x)/4; M1 limits 0 to a; M1 uses a e^(-2a) → 0; A1 1/4.
3. [2] M1 ∫ (b to 1) = -ln b; A1 → ∞ as b → 0+, so the integral diverges.
4. [2] M1 (1/3)∫(x^2 + 1) dx; A1 (1/3)(9 + 3) = 4.

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Maclaurin_Series_Improper_Integrals_Mean_Value` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Volumes_and_Further_Integration.

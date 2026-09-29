# S08_Parametric_Equations - Test: Parametric equations

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A curve has parametric equations x = t^2 - 1, y = 2t + 3. (a) Find the cartesian equation. (b) Find the points where the curve meets the line y = x + 2. [6 marks]
2. x = 1 + 2cos t, y = 3 + 2sin t, 0 ≤ t < 2 pi. Identify the curve fully. [3 marks]
3. A stone's position t seconds after it is thrown is x = 15t, y = 1.8 + 10t - 4.9t^2 (metres), with ground level y = 0. Find the horizontal distance travelled before it lands, to 3 significant figures. [4 marks]
4. x = t^2, y = t^3 for all real t. Find the cartesian equation and explain why y can be negative though x cannot. [3 marks]

## Answer key (for the tutor only)
1. [6] M1 t = (y - 3)/2; A1 x = ((y - 3)/2)^2 - 1; M1 substitutes: 2t + 3 = t^2 - 1 + 2; A1 t^2 - 2t - 2 = 0, so t = 1 ± root 3; A1 x = t^2 - 1 = 3 ± 2 root 3; A1 points (3 + 2 root 3, 5 + 2 root 3) and (3 - 2 root 3, 5 - 2 root 3).
2. [3] M1 cos t = (x - 1)/2, sin t = (y - 3)/2; A1 (x - 1)^2 + (y - 3)^2 = 4; A1 circle, centre (1, 3), radius 2.
3. [4] M1 sets y = 0; M1 uses the formula: t = (10 + root(100 + 35.28))/9.8; A1 t = 2.2072; A1 x = 33.1 m.
4. [3] M1 t = y^(1/3) or x^3 = t^6 = y^2; A1 y^2 = x^3; B1 x = t^2 ≥ 0 for all t, but y = t^3 < 0 when t < 0.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Parametric_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Binomial_Expansion.

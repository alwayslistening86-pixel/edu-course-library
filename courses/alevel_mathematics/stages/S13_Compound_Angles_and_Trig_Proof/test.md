# S13_Compound_Angles_and_Trig_Proof - Test: Compound and double angles, R-form, trig proof and context

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Express 5sin x - 12cos x in the form R sin(x - α), R > 0, 0 < α < 90°. Hence find the maximum value of 1/(20 + 5sin x - 12cos x). [6 marks]
2. Prove that (cos 2x)/(cos x + sin x) = cos x - sin x. [3 marks]
3. Solve cos 2x + 3sin x = 2 for 0 ≤ x < 2π. [5 marks]
4. Show that sin(x + 60°) + sin(x - 60°) = sin x. [3 marks]
5. Use the diagram-based proof, or the compound-angle formula, to show that cos(90° - A) = sin A. [2 marks]
6. The height of a point on a big wheel is h = 20 - 18cos(πt/15) metres at t minutes. Find the greatest height, the time it first occurs, and the period. [3 marks]

## Answer key (for the tutor only)
1. [6] M1 R cos α = 5, R sin α = 12; A1 R = 13; A1 α = 67.38°; M1 minimum of the denominator is 20 - 13 = 7; A1 maximum 1/7; B1 correct reasoning that the fraction is largest when the denominator is smallest.
2. [3] M1 cos 2x = cos^2 x - sin^2 x; M1 factorises as (cos x - sin x)(cos x + sin x); A1 cancels to the RHS.
3. [5] M1 cos 2x = 1 - 2sin^2 x; A1 2sin^2 x - 3sin x + 1 = 0; M1 (2sin x - 1)(sin x - 1) = 0; A1 x = π/6, 5π/6; A1 x = π/2.
4. [3] M1 expands both; M1 the cos x sin 60° terms cancel; A1 2sin x cos 60° = sin x.
5. [2] M1 cos 90° cos A + sin 90° sin A; A1 = sin A.
6. [3] B1 38 m; B1 t = 15 minutes; B1 period 30 minutes.

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Compound_Angles_and_Trig_Proof` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 22 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Exponentials_and_Logarithms.

# S05_Exponential_Form_and_de_Moivre - Test: Exponential form, de Moivre's theorem and roots of unity

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Use de Moivre's theorem to show that sin 5θ = 16sin^5 θ - 20sin^3 θ + 5sin θ. [6 marks]
2. Solve z^4 = -16, giving the roots in the form a + bi, and describe their positions on an Argand diagram. [5 marks]
3. Express cos^3 θ in terms of cos 3θ and cos θ using z = e^(iθ). [4 marks]
4. ω = e^(2πi/5). Show that 1 + ω + ω^2 + ω^3 + ω^4 = 0. [3 marks]

## Answer key (for the tutor only)
1. [6] M1 expands (c + is)^5; M1 takes the imaginary part: 5c^4 s - 10c^2 s^3 + s^5; M1 c^2 = 1 - s^2; A1 5(1 - s^2)^2 s - 10(1 - s^2)s^3 + s^5; M1 expands; A1 correct result.
2. [5] M1 16e^(iπ); M1 z = 2e^(i(π + 2πk)/4); A1 root2 ± i root2; A1 -root2 ± i root2; B1 vertices of a square, radius 2, centred at O.
3. [4] M1 (z + 1/z)^3 = 8cos^3 θ; M1 z^3 + 1/z^3 + 3(z + 1/z); A1 2cos 3θ + 6cos θ; A1 cos^3 θ = (cos 3θ + 3cos θ)/4.
4. [3] M1 geometric series (1 - ω^5)/(1 - ω); M1 ω^5 = 1; A1 sum 0 since ω ≠ 1.

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Exponential_Form_and_de_Moivre` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Matrices_and_Transformations.

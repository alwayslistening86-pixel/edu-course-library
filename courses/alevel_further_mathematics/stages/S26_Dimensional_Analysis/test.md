# S26_Dimensional_Analysis - Test: Dimensional analysis

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The drag force F on a sphere is modelled as F = k ρ^a v^b r^c, where ρ is the fluid's density, v the speed and r the radius, and k is dimensionless. Find a, b and c. [5 marks]
2. Show that E = mc^2 is dimensionally consistent. [2 marks]
3. A student claims the height reached by a ball thrown up at speed u is h = u^2/g^2. Use dimensions to show this is wrong, and suggest a consistent form. [3 marks]

## Answer key (for the tutor only)
1. [5] M1 M L T^-2 = (M L^-3)^a (L T^-1)^b L^c; A1 M: a = 1; A1 T: b = 2; M1 L: -3a + b + c = 1; A1 c = 2.
2. [2] M1 [M][L T^-1]^2; A1 = M L^2 T^-2, the dimensions of energy.
3. [3] M1 u^2/g^2 has dimensions (L^2 T^-2)/(L^2 T^-4) = T^2; A1 not a length, so wrong; B1 h = k u^2/g.

## Grading
Apply `rubric.json`'s `stage_rubrics.S26_Dimensional_Analysis` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S27_Work_Energy_and_Power.

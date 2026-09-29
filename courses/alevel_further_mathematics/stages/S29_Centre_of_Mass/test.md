# S29_Centre_of_Mass - Test: Centre of mass

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A uniform lamina is a 6 cm by 4 cm rectangle with a 2 cm by 2 cm square removed from one corner. Taking the full rectangle's corners at (0, 0), (6, 0), (6, 4), (0, 4) and the removed square at the corner (6, 4), find the centre of mass. It is then suspended from (0, 0); find the angle between the side along the x-axis and the vertical. [7 marks]
2. Find the centre of mass of the uniform lamina bounded by y = root x, the x-axis and x = 4. [5 marks]
3. A uniform cuboid 2 m high with a square base of side 0.8 m stands on a rough plane whose inclination is slowly increased. μ = 0.5. Does it slide or topple first? Justify. [4 marks]

## Answer key (for the tutor only)
1. [7] M1 areas 24 and 4, remaining 20; M1 x̄: 24(3) - 4(5) = 20x̄; A1 x̄ = 2.6; M1 ȳ: 24(2) - 4(3) = 20ȳ; A1 ȳ = 1.8; M1 G hangs vertically below (0, 0), so the line from (0, 0) to G is vertical and makes angle arctan(1.8/2.6) with the x-axis side; A1 the x-axis side makes 34.7° with the vertical.
2. [5] M1 area ∫root x dx = 16/3; M1 ∫x root x dx = 64/5; A1 x̄ = 12/5; M1 ∫x/2 dx = 4; A1 ȳ = 4/(16/3) = 3/4.
3. [4] M1 slides when tan α = 0.5; M1 topples when tan α = 0.4/1 = 0.4; A1 0.4 < 0.5; A1 it topples first (at α = 21.8°).

## Grading
Apply `rubric.json`'s `stage_rubrics.S29_Centre_of_Mass` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S30_Circular_Motion_and_Variable_Force.

# S11_Roots_of_Polynomials_and_Partial_Fractions - Test: Roots of polynomials and further partial fractions

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The roots of 2x^3 + 5x^2 - x + 3 = 0 are α, β, γ. Find a cubic equation with integer coefficients whose roots are α + 2, β + 2, γ + 2. [4 marks]
2. For the quartic x^4 - 2x^3 + 3x^2 + x - 1 = 0 with roots α, β, γ, δ, find Σα, Σαβ, αβγδ and Σ1/α. [4 marks]
3. Express (2x^2 - x + 7)/((x - 2)(x^2 + 3)) in partial fractions. [4 marks]

## Answer key (for the tutor only)
1. [4] M1 x = w - 2; M1 expands 2(w - 2)^3 + 5(w - 2)^2 - (w - 2) + 3; A1 correct terms; A1 2x^3 - 7x^2 + 3x + 9 = 0.
2. [4] B1 Σα = 2; B1 Σαβ = 3; B1 αβγδ = -1; B1 Σ1/α = Σαβγ/αβγδ = (-1)/(-1) = 1.
3. [4] M1 form A/(x - 2) + (Bx + C)/(x^2 + 3); M1 x = 2 gives A; A1 A = 13/7; A1 (x - 5)/(7(x^2 + 3)) + 13/(7(x - 2)).

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Roots_of_Polynomials_and_Partial_Fractions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Series.

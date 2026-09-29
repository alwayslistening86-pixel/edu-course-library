# S13_Hyperbolic_Functions - Test: Hyperbolic functions

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove that cosh^2 x - sinh^2 x = 1 from the definitions. [3 marks]
2. Solve 4cosh x - sinh x = 4, giving answers in exact form. [4 marks]
3. Show that arsinh x = ln(x + root(x^2 + 1)). [4 marks]
4. Differentiate y = x cosh 3x and find ∫ sinh^2 x dx. [4 marks]

## Answer key (for the tutor only)
1. [3] M1 squares both; M1 (e^(2x) + 2 + e^(-2x))/4 - (e^(2x) - 2 + e^(-2x))/4; A1 = 1.
2. [4] M1 2(e^x + e^(-x)) - (e^x - e^(-x))/2 = 4; M1 3e^x + 5e^(-x) = 8, so 3e^(2x) - 8e^x + 5 = 0; A1 e^x = 1 or 5/3; A1 x = 0 or ln(5/3).
3. [4] M1 x = sinh y = (e^y - e^(-y))/2; M1 e^(2y) - 2xe^y - 1 = 0; M1 quadratic in e^y; A1 rejects the negative root since e^y > 0.
4. [4] B1 cosh 3x + 3x sinh 3x; M1 sinh^2 x = (cosh 2x - 1)/2; A1 sinh 2x/4; A1 - x/2 + c.

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Hyperbolic_Functions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Maclaurin_Series_Improper_Integrals_Mean_Value.

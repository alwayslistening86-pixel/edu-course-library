# S04_Polynomials_Rational_Expressions_Partial_Fractions - Test: Polynomials, rational expressions and partial fractions

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. f(x) = 2x^3 - 3x^2 - 11x + 6. (a) Show that (x - 3) is a factor of f(x). (b) Hence factorise f(x) completely. (c) Solve f(x) = 0. [6 marks]
2. Find the remainder when x^4 - 3x^2 + 5 is divided by (x + 2). [2 marks]
3. Simplify fully (2x^2 + 5x - 3)/(4x^2 - 1). [3 marks]
4. Express (x + 9)/((x - 1)(x + 3)^2) in partial fractions. [5 marks]
5. Given that f(x) = x^3 + ax^2 + bx - 6 has factors (x - 1) and (x + 2), find a and b. [4 marks]

## Answer key (for the tutor only)
1. [6] B1 f(3) = 54 - 27 - 33 + 6 = 0; M1 divides; A1 2x^2 + 3x - 2; A1 f(x) = (x - 3)(x + 2)(2x - 1); B1 x = 3, x = -2; B1 x = 1/2.
2. [2] M1 evaluates f(-2); A1 16 - 12 + 5 = 9.
3. [3] M1 numerator (2x - 1)(x + 3); M1 denominator (2x - 1)(2x + 1); A1 (x + 3)/(2x + 1).
4. [5] M1 correct form A/(x - 1) + B/(x + 3) + C/(x + 3)^2; M1 x + 9 = A(x + 3)^2 + B(x - 1)(x + 3) + C(x - 1); A1 A = 5/8 (x = 1); A1 C = -3/2 (x = -3); A1 B = -5/8. Result: -5/(8(x + 3)) - 3/(2(x + 3)^2) + 5/(8(x - 1)).
5. [4] M1 f(1) = 0: 1 + a + b - 6 = 0, so a + b = 5; M1 f(-2) = 0: -8 + 4a - 2b - 6 = 0, so 2a - b = 7; M1 solves; A1 a = 4, b = 1.

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Polynomials_Rational_Expressions_Partial_Fractions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 20 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Graphs_and_Curve_Sketching.

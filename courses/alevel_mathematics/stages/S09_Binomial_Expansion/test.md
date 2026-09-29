# S09_Binomial_Expansion - Test: The binomial expansion

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the coefficient of x^4 in the expansion of (2 - x/2)^9. [3 marks]
2. Expand (8 + 3x)^(1/3) in ascending powers of x up to and including the x^2 term, simplifying coefficients. State the values of x for which it is valid. [5 marks]
3. Hence, by choosing a suitable x, estimate the cube root of 8.3 to 5 decimal places. [2 marks]
4. Find the expansion of (1 + x)/(1 - x)^2 up to and including the x^3 term. [4 marks]
5. In the expansion of (1 + ax)^n, n a positive integer, the coefficient of x is 12 and the coefficient of x^2 is 60. Find a and n. [5 marks]

## Answer key (for the tutor only)
1. [3] M1 9C4 (2)^5 (-1/2)^4 term; A1 126 × 32 × 1/16; A1 252.
2. [5] M1 takes out 8^(1/3) = 2: 2(1 + 3x/8)^(1/3); M1 binomial with n = 1/3; A1 2 + x/4; A1 - x^2/32; B1 |x| < 8/3.
3. [2] M1 x = 0.1; A1 2.02469.
4. [4] M1 (1 - x)^(-2) = 1 + 2x + 3x^2 + 4x^3; M1 multiplies by (1 + x); A1 1 + 3x + 5x^2; A1 + 7x^3.
5. [5] M1 na = 12; M1 n(n - 1)a^2/2 = 60; M1 divides or substitutes: (n - 1)a/2 = 5, so na - a = 10; A1 a = 2; A1 n = 6.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Binomial_Expansion` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Sequences_and_Series.

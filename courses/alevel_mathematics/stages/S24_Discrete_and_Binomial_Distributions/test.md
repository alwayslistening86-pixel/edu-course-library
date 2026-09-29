# S24_Discrete_and_Binomial_Distributions - Test: Discrete and binomial distributions

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The random variable Y has P(Y = y) = c(5 - y) for y = 1, 2, 3, 4. Find c and P(Y ≤ 2). [3 marks]
2. 15% of a type of seed fail to germinate. 20 seeds are planted. (a) State two assumptions for a binomial model, in context. (b) Find P(exactly 3 fail). (c) Find P(at least 5 fail). [6 marks]
3. X ~ B(30, 0.25). Find P(5 < X < 10). [3 marks]
4. X ~ B(n, 0.2). Find the least n such that P(X ≥ 1) > 0.95. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 c(4 + 3 + 2 + 1) = 1; A1 c = 1/10; A1 0.7.
2. [6] B1 each seed fails independently; B1 the probability of failing is 0.15 for every seed; M1 B(20, 0.15); A1 0.2428; M1 1 - P(X ≤ 4); A1 0.1702.
3. [3] M1 P(X ≤ 9) - P(X ≤ 5); A1 correct values; A1 0.6008.
4. [3] M1 1 - 0.8^n > 0.95; M1 n > ln 0.05/ln 0.8 = 13.43; A1 n = 14.

## Grading
Apply `rubric.json`'s `stage_rubrics.S24_Discrete_and_Binomial_Distributions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S25_Normal_Distribution.

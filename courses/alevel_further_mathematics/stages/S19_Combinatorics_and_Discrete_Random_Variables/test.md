# S19_Combinatorics_and_Discrete_Random_Variables - Test: Combinatorial probability and discrete random variables

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A committee of 4 is chosen at random from 6 teachers and 5 students. Find the probability that it contains at least one student. [3 marks]
2. X has P(X = x) = kx^2 for x = 1, 2, 3. Find k, E(X), Var(X) and E(1/X). [6 marks]
3. Y = 3X - 2 where E(X) = 4 and Var(X) = 1.5. Find E(Y) and Var(Y). [2 marks]
4. Seven people sit in a row at random. Find the probability that two particular people, A and B, do not sit next to each other. [3 marks]
5. A fair spinner has sides numbered 1 to 10. Find the mean and variance of the score. [2 marks]

## Answer key (for the tutor only)
1. [3] M1 1 - P(no students); M1 6C4/11C4 = 15/330; A1 21/22.
2. [6] M1 k(1 + 4 + 9) = 1; A1 k = 1/14; A1 E(X) = (1 + 8 + 27)/14 = 18/7; M1 E(X^2) = (1 + 16 + 81)/14 = 7; A1 Var(X) = 7 - (18/7)^2 = 19/49; B1 E(1/X) = (1 + 2 + 3)/14 = 3/7.
3. [2] B1 10; B1 13.5.
4. [3] M1 together: 2 x 6!; M1 1 - 2(6!)/7!; A1 5/7.
5. [2] B1 5.5; B1 99/12 = 8.25.

## Grading
Apply `rubric.json`'s `stage_rubrics.S19_Combinatorics_and_Discrete_Random_Variables` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S20_Geometric_and_Poisson_Distributions.

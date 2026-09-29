# S10_Sequences_and_Series - Test: Sequences and series

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A sequence is defined by u1 = 4, u_(n+1) = 2u_n - 3. Find u2, u3 and u4, and Σ (r = 1 to 4) u_r. [3 marks]
2. The sequence u_(n+1) = 3 - u_n, u1 = 1 is periodic. State its order and find Σ (r = 1 to 25) u_r. [3 marks]
3. The 3rd term of an arithmetic series is 13 and the sum of the first 10 terms is 200. Find the first term and the common difference. [4 marks]
4. A geometric series has second term 24 and fifth term 81. Find the common ratio, the first term, and the least n for which S_n > 1000. [6 marks]
5. Find the values of x for which the geometric series 1 + (x - 2) + (x - 2)^2 + ... converges, and its sum when x = 2.5. [3 marks]
6. A firm's profits are £40 000 in year 1 and are modelled as falling by 5% each year. Find the total profit over the first 10 years, to the nearest pound, and criticise the model. [4 marks]

## Answer key (for the tutor only)
1. [3] B1 u2 = 5, u3 = 7; B1 u4 = 11; B1 sum 27.
2. [3] B1 terms 1, 2, 1, 2, ... order 2; M1 12 pairs summing to 3, plus u25 = 1; A1 37.
3. [4] M1 a + 2d = 13; M1 5(2a + 9d) = 200, so 2a + 9d = 40; M1 solves (2a + 4d = 26, so 5d = 14); A1 d = 2.8 and a = 7.4.
4. [6] M1 ar = 24, ar^4 = 81; A1 r^3 = 27/8, r = 3/2; A1 a = 16; M1 16(1.5^n - 1)/0.5 > 1000; M1 1.5^n > 32.25, n > log(32.25)/log(1.5) = 8.57; A1 n = 9.
5. [3] M1 |x - 2| < 1; A1 1 < x < 3; A1 1/(1 - 0.5) = 2.
6. [4] M1 a = 40000, r = 0.95; M1 S_10 = 40000(1 - 0.95^10)/0.05; A1 £321,010; B1 e.g. profits unlikely to fall by exactly the same percentage every year.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Sequences_and_Series` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 23 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Trigonometry_Foundations.

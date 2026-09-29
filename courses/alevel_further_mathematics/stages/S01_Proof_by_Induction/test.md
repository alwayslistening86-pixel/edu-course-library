# S01_Proof_by_Induction - Test: Proof by induction

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove by induction that 5^n + 3 is divisible by 4 for all positive integers n. [5 marks]
2. Prove by induction that Σ (r = 1 to n) r(r + 2) = n(n + 1)(2n + 7)/6. [6 marks]
3. M = [[3, -2], [1, 0]]. Prove by induction that M^n = [[2^(n+1) - 1, 2 - 2^(n+1)], [2^n - 1, 2 - 2^n]]. [6 marks]
4. A sequence has u1 = 3 and u_(n+1) = 2u_n - 1. Find u2, u3, u4, conjecture a formula for u_n and prove it by induction. [6 marks]

## Answer key (for the tutor only)
1. [5] B1 n = 1: 8; M1 assumes 5^k + 3 = 4m; M1 5^(k+1) + 3 = 5(5^k + 3) - 12; A1 = 20m - 12 = 4(5m - 3); A1 conclusion.
2. [6] B1 n = 1: 3 = 1(2)(9)/6; M1 assumption; M1 adds (k + 1)(k + 3); M1 factorises (k + 1)/6 out; A1 (k + 1)(2k^2 + 13k + 18)/6 = (k + 1)(k + 2)(2k + 9)/6; A1 conclusion.
3. [6] B1 n = 1 gives [[3, -2], [1, 0]]; M1 assumes for k; M1 multiplies M^k M; A1 top row 3(2^(k+1) - 1) + (2 - 2^(k+1)) = 2^(k+2) - 1 and -2(2^(k+1) - 1) = 2 - 2^(k+2); A1 bottom row 2^(k+1) - 1, 2 - 2^(k+1); A1 conclusion.
4. [6] B1 5, 9, 17; B1 u_n = 2^n + 1; B1 basis; M1 2(2^k + 1) - 1; A1 = 2^(k+1) + 1; A1 conclusion.

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Proof_by_Induction` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 23 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Complex_Numbers_Basics.

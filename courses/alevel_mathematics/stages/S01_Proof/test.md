# S01_Proof - Test: Proof

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove by exhaustion that for all integers n, n^2 leaves remainder 0 or 1 when divided by 3. [4 marks]
2. Insert the correct symbol (=>, <= or <=>) between each pair, where x is real: (a) x = 2 ... x^2 = 4; (b) x^3 = 8 ... x = 2; (c) x > 3 ... x^2 > 9. [3 marks]
3. Disprove the statement: 'if a and b are irrational, then ab is irrational'. [2 marks]
4. Prove by contradiction that there is no largest even number. [3 marks]
5. Prove by contradiction that if n^2 is odd then n is odd (n an integer). [4 marks]
6. Which statements are true for real numbers x? Choose every correct option.
   A. `x = -1 => x^2 = 1`
   B. `x^2 = 1 => x = -1`
   C. `x^2 > 0 <=> x ≠ 0`
   D. `x > 1 <=> x^2 > 1`

## Answer key (for the tutor only)
1. [4] M1 considers n = 3m, 3m + 1 and 3m + 2; A1 9m^2 = 3(3m^2), remainder 0; A1 (3m + 1)^2 = 3(3m^2 + 2m) + 1 and (3m + 2)^2 = 3(3m^2 + 4m + 1) + 1, remainder 1; A1 conclusion covering all cases.
2. [3] B1 (a) =>; B1 (b) <=> (the real cube root is unique); B1 (c) => (x = -4 gives x^2 > 9 without x > 3).
3. [2] M1 chooses a counter-example; A1 e.g. a = b = root 2, both irrational, ab = 2 which is rational.
4. [3] M1 assume a largest even number N exists; M1 N + 2 is even and greater than N; A1 contradiction stated, so no largest even number exists.
5. [4] M1 assume n^2 is odd and n is even; M1 n = 2k; M1 n^2 = 4k^2 = 2(2k^2), which is even; A1 contradicts n^2 odd, so n is odd.
6. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Proof` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Indices_Surds_and_Quadratics.

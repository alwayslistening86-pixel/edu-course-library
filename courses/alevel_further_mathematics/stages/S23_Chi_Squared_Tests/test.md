# S23_Chi_Squared_Tests - Test: Chi-squared tests

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A spinner with four sectors is claimed to be fair. In 100 spins the results are 18, 25, 30, 27. Test the claim at the 5% level. [6 marks]
2. In a survey, 200 people are classified by age (under 40 / 40 and over) and preference (A / B / C): under 40: 40, 35, 25; 40 and over: 20, 40, 40. Test for association at 5%. [7 marks]
3. Explain why, when fitting a Poisson distribution whose mean is estimated from the data, the degrees of freedom are reduced by 2 from the number of cells. [2 marks]

## Answer key (for the tutor only)
1. [6] B1 H0: fair (each probability 1/4); B1 E = 25 each; M1 X^2 = Σ(O - E)^2/E; A1 X^2 = 3.12; M1 ν = 3, critical value 7.815; A1 do not reject H0: insufficient evidence that the spinner is unfair.
2. [7] B1 H0: age and preference independent; M1 expected frequencies from totals; A1 E: 30, 37.5, 32.5 in each row; M1 X^2; A1 X^2 = 10.46; M1 ν = 2, critical value 5.991; A1 reject H0: evidence of association. Interpretation: the under-40s favour A more than expected.
3. [2] B1 one for the total being fixed; B1 one for the estimated parameter λ.

## Grading
Apply `rubric.json`'s `stage_rubrics.S23_Chi_Squared_Tests` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S24_Non_Parametric_Tests.

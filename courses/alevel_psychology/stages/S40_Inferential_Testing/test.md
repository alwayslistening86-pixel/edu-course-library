# S40_Inferential_Testing - Test: Introduction to inferential testing

## How to run this
A real checkpoint in AQA's style: short-answer, calculation and levels-marked extended-writing questions at the real tariffs used in the actual papers (1-16 marks), with marks shown. Give the whole test at once, with no hints, under rough time pressure (allow about 1.5 minutes per mark, matching AQA's papers). Then mark short/calculation items against the mark schemes below, and extended-writing items using AQA's levels-of-response descriptors (also below), together with this stage's entry in `rubric.json`.

## Test items
1. A researcher uses a repeated measures design to test whether a new revision technique improves exam scores for 8 students, comparing their scores before and after using the technique. 7 students' scores improved (+) and 1 student's score got worse (-), with no ties. Calculate S for a sign test on this data, and state, using the critical value of 1 (n=8, one-tailed, p<=0.05), whether the result is significant. [4 marks]
2. Explain which inferential test should be used for a study testing the correlation between two variables measured at the ordinal level, and why. [3 marks]
3. Explain why using a very strict significance level, such as p <= 0.01 instead of p <= 0.05, increases the risk of a Type II error. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 S is the number of signs in the less frequent direction; A1 S = 1 (one participant showed a decrease, against seven increases); A1 the critical value for n=8, one-tailed, p<=0.05 is 1; A1 since the calculated S (1) is equal to the critical value (1), the result is statistically significant (the sign test requires the calculated value to be equal to or less than the critical value).
2. [3] B1 Spearman's rho should be used; B1 because the study tests a correlation/association, not a difference; B1 and the data is at the ordinal level (Spearman's rho is suitable for at least ordinal-level correlational data, whereas Pearson's r requires interval-level, normally distributed data).
3. [3] B1 a stricter significance level requires stronger evidence before a result is declared significant; B1 this makes it harder to detect a genuine effect that does actually exist in the population; B1 increasing the chance of failing to reject a null hypothesis that is actually false, i.e. a Type II error.

## Grading
Apply `rubric.json`'s `stage_rubrics.S40_Inferential_Testing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S41_Gender_Culture_Free_Will_and_Determinism.

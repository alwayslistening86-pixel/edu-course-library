# S23_Probability - Test: Probability

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A bag has 5 red and 3 blue counters. Two are taken without replacement. Find P(both the same colour) and P(second is red | first is blue). [4 marks]
2. In a group of 80 people, 45 like tea, 30 like coffee, and 12 like both. A person is chosen at random. Find P(likes tea or coffee), P(likes neither) and P(likes coffee | likes tea). [4 marks]
3. P(A) = 0.4 and P(B | A) = 0.25, P(B | A') = 0.5. Find P(B) and P(A | B). [4 marks]
4. A model assumes each of a footballer's penalties is scored independently with probability 0.8. Give one reason the model might be unrealistic. [1 mark]

## Answer key (for the tutor only)
1. [4] M1 (5/8)(4/7) + (3/8)(2/7); A1 26/56 = 13/28; M1 conditional on first blue: 5 red of 7 left; A1 5/7.
2. [4] M1 Venn: 33, 12, 18; A1 63/80; A1 17/80; A1 12/45 = 4/15.
3. [4] M1 0.4 × 0.25 + 0.6 × 0.5; A1 0.4; M1 0.1/0.4; A1 0.25.
4. [1] B1 e.g. independence may fail (confidence or fatigue), or the probability varies with the goalkeeper.

## Grading
Apply `rubric.json`'s `stage_rubrics.S23_Probability` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S24_Discrete_and_Binomial_Distributions.

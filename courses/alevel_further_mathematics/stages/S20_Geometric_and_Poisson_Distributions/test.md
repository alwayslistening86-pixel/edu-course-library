# S20_Geometric_and_Poisson_Distributions - Test: Geometric and Poisson distributions

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A basketball player scores each free throw independently with probability 0.7. X is the number of throws up to and including the first miss. State the distribution of X and find P(X = 4), P(X > 5) and E(X). [5 marks]
2. Emails arrive at a rate of 6 per hour, modelled by a Poisson distribution. Find (a) P(exactly 4 in an hour), (b) P(at most 2 in 20 minutes), (c) P(more than 10 in 90 minutes). [6 marks]
3. State two conditions needed for the Poisson model in the previous question to be valid, in context. [2 marks]
4. Faults in cable A occur at 0.8 per 100 m and in cable B at 1.2 per 100 m, independently, both as Poisson variables. Find the probability of at least 3 faults in total in 100 m of each. [3 marks]
5. A sample of counts has mean 4.1 and variance 7.8. Comment on the suitability of a Poisson model. [2 marks]

## Answer key (for the tutor only)
1. [5] B1 X ~ Geo(0.3); M1 0.7^3 x 0.3; A1 0.1029; A1 P(X > 5) = 0.7^5 = 0.1681; B1 E(X) = 1/0.3 = 10/3.
2. [6] M1 Po(6); A1 0.1339; M1 Po(2); A1 0.6767; M1 Po(9); A1 0.2940.
3. [2] B1 emails arrive independently of one another; B1 at a constant average rate (and singly).
4. [3] M1 Po(2); M1 1 - P(≤ 2); A1 0.3233.
5. [2] M1 compares mean and variance; A1 variance much larger than mean, so a Poisson model is unlikely to be suitable.

## Grading
Apply `rubric.json`'s `stage_rubrics.S20_Geometric_and_Poisson_Distributions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S21_Continuous_Random_Variables.

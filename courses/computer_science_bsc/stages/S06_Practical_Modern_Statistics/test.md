# S06_Practical_Modern_Statistics - Test: Practical modern statistics

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
from math import exp, factorial
lam = 4
for k in range(0, 3):
    print(k, round(lam**k * exp(-lam) / factorial(k), 4))
```
2. A/B testing a new webpage design: 40 out of 500 visitors to the old design convert (buy something); 55 out of 500 visitors to the new design convert. A two-proportion test gives p-value 0.09. Using alpha=0.05, state the conclusion and explain what a Type II error would mean here if the new design genuinely is better. [4 marks]
3. A server's requests per minute average 6 (Poisson-distributed). Compute the probability of exactly 4 requests in a given minute, showing your working. [4 marks]
4. A sample of 64 page-load times has mean 3.2s and sample standard deviation 0.8s. Construct a 95% confidence interval for the true mean load time and state, in words, what this interval means. [5 marks]
5. For a dataset with correlation coefficient r=0.85 between hours studied and exam score, a student claims 'studying more causes higher scores, and this proves it'. Critique this claim using the concept of R-squared and the distinction between correlation and causation. [3 marks]
6. Which statements about hypothesis testing are correct? Choose every correct option.
   A. A p-value is the probability that the null hypothesis is true
   B. A Type I error is rejecting a true null hypothesis
   C. A smaller p-value than alpha leads to rejecting the null hypothesis
   D. Failing to reject the null hypothesis proves it is true

## Answer key (for the tutor only)
1. Actual result (from running it):
```
0 0.0183
1 0.0733
2 0.1465
```
2. [4] M1 p-value (0.09) > alpha (0.05); A1 conclusion: fail to reject H0 -- insufficient evidence at the 5% level that the new design's conversion rate differs from the old; A1 a Type II error here means failing to detect a real improvement (accepting H0 when the new design genuinely converts better); A1 explains the practical consequence: the company might discard a genuinely better design because the test lacked the power/sample size to detect the true effect.
3. [4] M1 identifies Poisson formula P(X=k)=lambda^k e^{-lambda}/k!; M1 substitutes lambda=6, k=4; A2 P(X=4) = 6^4 e^{-6} / 4! -- correct numeric value to at least 3 dp (approximately 0.1339).
4. [5] M1 standard error = 0.8/root(64) = 0.1; M1 margin = 1.96 x 0.1 = 0.196; A1 interval (3.004, 3.396) (accept rounding); A2 correct interpretation: if this sampling process were repeated many times, about 95% of the resulting intervals would contain the true population mean load time -- not 'a 95% chance the true mean is in this specific interval' (1 mark for the repeated-sampling framing, 1 mark for explicitly rejecting the common misinterpretation).
5. [3] B1 R^2 = 0.85^2 = 0.7225, so about 72% of the variance in exam score is associated with (explained by) hours studied -- a strong but not perfect linear association; B1 correlation alone does not establish causation: a third/confounding variable (e.g. general motivation or prior ability) could drive both hours studied and exam score; B1 a controlled experiment (or at least ruling out plausible confounders), not an observed correlation, would be needed to support a causal claim.
6. Correct: B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Practical_Modern_Statistics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Algorithms_and_Data_Structures.

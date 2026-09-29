# S02_Mathematical_and_Statistical_Methods_for_Bioengineering - Test: Mathematical and Statistical Methods for Bioengineering

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A tracer's plasma concentration follows C(t) = C0 e^(-kt) with C0 = 8.0 mg/L and k = 0.12 per hour. Find the concentration after 6 hours and the half-life. [3 marks]
2. A sample of 25 patients has mean systolic pressure 128 mmHg and sample standard deviation 14 mmHg. Calculate the SEM and a 95% confidence interval for the population mean. [4 marks]
3. A force of 40 N and a force of 30 N act perpendicular to each other on a bone fragment. Calculate the resultant force magnitude and the moment of the resultant about a point 0.05 m away along its own line of action. [3 marks]
4. Which statements about a p-value from a two-sample t-test are correct? Choose every correct option.
   A. A p-value below 0.05 is conventionally called statistically significant
   B. A p-value is the probability the null hypothesis is true
   C. Statistical significance always implies practical/engineering significance
   D. A very large sample can make a small, unimportant difference statistically significant
5. Experimental data (x = time in minutes, y = ln of drug concentration) has least-squares gradient m = -0.084 per minute (from linearising C = C0 e^(-kt)). State the value of the rate constant k and its half-life. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 C(6) = 8.0 e^(-0.12x6); A1 = 3.89 mg/L; A1 half-life = ln2/0.12 = 5.78 hours.
2. [4] M1 SEM = 14/root(25) = 2.8; M1 95% CI = mean +/- 1.96 x SEM; A1 lower = 122.51; A1 upper = 133.49 mmHg.
3. [3] M1 resultant = root(40^2+30^2) = 50.0 N; A1 direction theta = atan(30/40) = 36.9 degrees from the 40 N force; B1 moment about a point on the line of action is zero (perpendicular distance = 0).
4. Correct: A, D (exactly these options, no others)
5. [3] B1 k = -m = 0.084 per min (gradient of ln C vs t is -k); M1 half-life = ln2/k; A1 = 8.25 minutes.

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Mathematical_and_Statistical_Methods_for_Bioengineering` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Introductory_Materials_Science_for_Engineers.

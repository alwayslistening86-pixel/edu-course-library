# S08_Data_Analysis_and_Modelling_for_Bioengineers - Test: Data Analysis and Modelling for Bioengineers

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Plasma drug concentration data give ln(C) against time t a least-squares gradient of -0.045 per hour and intercept ln(C0) = 2.30. Find k, C0 and the drug's half-life. [4 marks]
2. Clearance CL = k x Vd, with k measured as 0.06 +/- 5% per hour and Vd measured as 35 +/- 6% L. Calculate CL and its propagated percentage and absolute uncertainty. [4 marks]
3. Which observations from a residual plot (measured minus model-predicted value, against time) would suggest the fitted single-exponential model form is wrong, rather than just ordinary measurement noise? Choose every correct option.
   A. Residuals scattered randomly around zero with no pattern
   B. Residuals that trend from positive to negative to positive again over time
   C. A clear systematic curve in the residuals
   D. All residuals exactly zero
4. Basal metabolic rate scales with body mass as BMR = a M^0.75 (allometric scaling). If a reference adult of mass 70 kg has BMR = 1600 kcal/day, estimate the BMR of a patient of mass 100 kg, assuming the same scaling constant a. [3 marks]
5. Explain why checking dimensional homogeneity is a useful first step before fitting any physiological model to data, giving one concrete example of an error it would catch. [3 marks]

## Answer key (for the tutor only)
1. [4] B1 k = 0.045 per hour (negative of gradient); M1 C0 = e^2.30; A1 = 9.97 mg/L; A1 half-life = ln2/k = 15.40 hours.
2. [4] M1 CL = 0.06 x 35 = 2.10 L/h; M1 percentage uncertainty = 5% + 6% (product rule) = 11%; A1 absolute uncertainty = 0.11 x 2.10; A1 = 0.231 L/h, so CL = 2.10 +/- 0.23 L/h.
3. Correct: B, C (exactly these options, no others)
4. [3] M1 a = 1600/70^0.75; M1 BMR(100) = a x 100^0.75 = 1600 x (100/70)^0.75; A1 = 2091 kcal/day.
5. [3] B1 both sides of a correctly formed physiological equation must have the same physical dimensions/units, so checking this is a quick way to catch an algebraic or unit-conversion error before doing any numerical work; B1 e.g. it would catch mistakenly writing clearance CL (units volume/time) as equal to a rate constant k alone (units 1/time), which are dimensionally inconsistent; B1 it does not guarantee the model is scientifically correct, only that it is not obviously ill-formed.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Data_Analysis_and_Modelling_for_Bioengineers` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Biochemistry_and_Cell_Biology_for_Engineers.

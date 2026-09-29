# S14_Rate_Equations - Test: Rate equations, orders, the Arrhenius equation and mechanisms

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator, the Periodic Table and the data sheet. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. For A + B → C: experiment 1 [A] 0.10, [B] 0.10, rate 1.2 x 10^-3; experiment 2 [A] 0.20, [B] 0.10, rate 2.4 x 10^-3; experiment 3 [A] 0.20, [B] 0.30, rate 2.16 x 10^-2 (concentrations in mol dm^-3, rates in mol dm^-3 s^-1). Deduce the rate equation and calculate k with units. [5 marks]
2. A graph of ln k against 1/T has a gradient of -9.2 x 10^3 K. Calculate the activation energy in kJ mol^-1. [2 marks]
3. The rate equation for 2NO + O2 → 2NO2 is rate = k[NO]^2[O2]. Which species, and how many of each, are involved in (or before) the rate-determining step? [2 marks]
4. Hydrolysis of 2-bromo-2-methylpropane: rate = k[(CH3)3CBr]. Suggest a two-step mechanism and identify the rate-determining step. [3 marks]
5. Use the Arrhenius equation to calculate the ratio k(310 K)/k(300 K) for Ea = 50 kJ mol^-1. [2 marks]
6. In an iodine clock reaction, explain why 1/t can be used as a measure of the initial rate. [2 marks]

## Answer key (for the tutor only)
1. [5] B1 first order in A (doubling [A] doubles the rate); B1 second order in B (tripling [B] increases rate 9 times); B1 rate = k[A][B]^2; M1 k = 1.2 x 10^-3/(0.10 x 0.10^2); A1 1.2 mol^-2 dm^6 s^-1.
2. [2] M1 Ea = -gradient x R; A1 76.5 kJ mol^-1.
3. [2] B1 two molecules of NO; B1 one molecule of O2.
4. [3] B1 step 1 (slow): (CH3)3CBr → (CH3)3C+ + Br-; B1 step 2 (fast): (CH3)3C+ + OH- → (CH3)3COH; B1 step 1 is rate-determining, as OH- is not in the rate equation.
5. [2] M1 exp[(Ea/R)(1/300 - 1/310)]; A1 1.91.
6. [2] B1 the same fixed amount of product (iodine) forms before the colour appears each time; B1 rate = amount/time, so rate ∝ 1/t (and the reaction has not progressed far, so it is close to the initial rate).

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Rate_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Kp.

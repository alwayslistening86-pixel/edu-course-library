# S16_Capacitance - Test: Capacitance and exponential change

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator and the data booklet. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A 2200 μF capacitor charged to 15 V discharges through a 2.0 kΩ resistor. Calculate the time constant, the pd after 10 s and the energy released in that time. [5 marks]
2. Explain why inserting a dielectric between the plates of an isolated charged capacitor reduces the pd across it. [3 marks]
3. In required practical 9, a graph of ln V (V in volts) against t has gradient -0.125 s^-1 and R = 100 kΩ. Calculate C. [2 marks]
4. A capacitor is charged through a 5.0 kΩ resistor from a 12 V supply. Its capacitance is 470 μF. Find the pd across it after 3.0 s. [2 marks]
5. Two parallel plates 0.20 m x 0.20 m are 2.0 mm apart with a material of εr = 2.5 between them. Calculate the capacitance. [2 marks]
6. Data suggest y = ax^n. Explain how a graph can test this and find n. [3 marks]

## Answer key (for the tutor only)
1. [5] B1 RC = 4.4 s; M1 V = 15e^(-10/4.4); A1 1.55 V; M1 energy difference (1/2)C(V0^2 - V^2); A1 0.245 J.
2. [3] B1 polar molecules rotate to align with the field; B1 they create an opposing field, reducing the net field; B1 V = Ed falls (Q unchanged, so C increases).
3. [2] M1 gradient = -1/RC; A1 80 μF.
4. [2] M1 V = 12(1 - e^(-3/2.35)); A1 8.65 V.
5. [2] M1 Aε0εr/d; A1 443 pF.
6. [3] B1 plot log y against log x (or ln against ln); B1 a straight line confirms the power law; B1 gradient = n (intercept log a).

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_Capacitance` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S17_Magnetic_Fields_and_Induction.

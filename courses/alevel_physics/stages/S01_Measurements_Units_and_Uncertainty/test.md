# S01_Measurements_Units_and_Uncertainty - Test: Measurements, units, uncertainty and numerical skills

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator and the data booklet. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Show that the equation v^2 = u^2 + 2as is homogeneous with respect to units. [2 marks]
2. The period of a pendulum is found by timing 20 oscillations: 28.4 s with a stopwatch reading to 0.01 s, and a human reaction time uncertainty of ± 0.2 s. Find the period with its absolute uncertainty, and explain why timing 20 oscillations is better than timing one. [4 marks]
3. The kinetic energy E = (1/2)mv^2. m = 0.50 ± 0.01 kg and v = 3.2 ± 0.1 m s^-1. Find E and its absolute uncertainty. [4 marks]
4. Estimate the order of magnitude of the number of atoms in a 1 kg iron bar (molar mass 56 g mol^-1, N_A = 6.02 x 10^23). [2 marks]
5. Which of the following are systematic errors? Choose every correct option.
   A. A newton meter reading 0.2 N with nothing attached
   B. Reading a scale from above rather than at eye level every time
   C. Timings scattered by variable reaction time
   D. A thermometer that reads 1 °C high throughout
6. Convert: (a) 350 nm to m, (b) 4.5 GHz to Hz, (c) 2.0 kWh to J. [3 marks]

## Answer key (for the tutor only)
1. [2] M1 v^2 and u^2: m^2 s^-2; A1 2as: (m s^-2)(m) = m^2 s^-2, so every term matches.
2. [4] M1 T = 28.4/20 = 1.42 s; M1 uncertainty 0.2/20; A1 1.42 ± 0.01 s; B1 the fixed reaction-time uncertainty is spread over 20 oscillations, reducing the percentage uncertainty.
3. [4] M1 E = 2.56 J; M1 % uncertainty in m = 2%, in v = 3.1%; M1 total = 2 + 2 x 3.1 = 8.2%; A1 E = 2.56 ± 0.21 J (≈ 2.6 ± 0.2 J).
4. [2] M1 1000/56 x 6.02 x 10^23 = 1.08 x 10^25; A1 order 10^25.
5. Correct: A, B, D (exactly these options, no others)
6. [3] B1 3.5 x 10^-7 m; B1 4.5 x 10^9 Hz; B1 7.2 x 10^6 J.

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Measurements_Units_and_Uncertainty` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Particles.

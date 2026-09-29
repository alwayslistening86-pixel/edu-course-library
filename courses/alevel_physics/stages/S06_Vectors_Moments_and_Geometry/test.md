# S06_Vectors_Moments_and_Geometry - Test: Scalars, vectors, moments and geometry skills

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator and the data booklet. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A uniform beam of weight 200 N and length 4.0 m is supported at each end. A 500 N load is 1.0 m from the left end. Calculate the support forces. [4 marks]
2. A 5.0 kg block rests on a smooth slope inclined at 25°, held by a rope parallel to the slope. Calculate the tension and the normal reaction. [3 marks]
3. Define a couple and calculate the torque of two 15 N forces 0.30 m apart. [2 marks]
4. Calculate the volume of a steel sphere of diameter 12 mm, and its mass (density 7800 kg m^-3). [3 marks]
5. Convert 25° to radians and use a small-angle approximation to estimate sin(0.05 rad). [2 marks]

## Answer key (for the tutor only)
1. [4] M1 moments about the left end: R_R x 4.0 = 200 x 2.0 + 500 x 1.0; A1 R_R = 225 N; M1 R_L = 700 - 225; A1 475 N.
2. [3] M1 resolves along the slope; A1 T = 5.0 x 9.81 sin 25° = 20.7 N; A1 R = 5.0 x 9.81 cos 25° = 44.5 N.
3. [2] B1 two equal, opposite parallel forces not in the same line; B1 4.5 N m.
4. [3] M1 (4/3)π(6.0 x 10^-3)^3; A1 9.05 x 10^-7 m^3; A1 0.00706 kg.
5. [2] B1 0.436 rad; B1 0.05.

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Vectors_Moments_and_Geometry` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Motion_and_Projectiles.

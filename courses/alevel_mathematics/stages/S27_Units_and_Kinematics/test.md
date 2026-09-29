# S27_Units_and_Kinematics - Test: Units and kinematics in a straight line

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A stone is thrown vertically upwards at 21 m/s from a point 3 m above the ground. Using g = 9.8 m s^-2, find (a) its greatest height above the ground, (b) the time it takes to hit the ground. [6 marks]
2. A train's velocity-time graph: from rest it accelerates uniformly for 40 s to V m/s, travels at V for 3 minutes, then decelerates uniformly to rest in 60 s. The total distance is 11.2 km. Find V. [4 marks]
3. A particle moves in a straight line with v = t^2 - 5t + 4 m/s. Find (a) its acceleration when t = 3, (b) the total distance travelled from t = 0 to t = 4. [6 marks]
4. Convert 54 km/h to m/s and state the SI unit of acceleration. [2 marks]

## Answer key (for the tutor only)
1. [6] M1 v^2 = u^2 + 2as with v = 0; A1 s = 22.5 m, so 25.5 m above the ground; M1 -3 = 21t - 4.9t^2; M1 solves the quadratic; A1 t = 4.42 s; B1 rejects the negative root.
2. [4] M1 area of trapezium; A1 (1/2)(40)V + 180V + (1/2)(60)V = 230V; M1 230V = 11200; A1 V = 48.7 m/s (3 s.f.).
3. [6] B1 a = 2t - 5 = 1 m s^-2; M1 rest at t = 1 and 4; M1 integrates: t^3/3 - 5t^2/2 + 4t; A1 ∫ (0 to 1) = 11/6; A1 ∫ (1 to 4) = -9/2; A1 total distance 19/3 m.
4. [2] B1 15 m s^-1; B1 m s^-2.

## Grading
Apply `rubric.json`'s `stage_rubrics.S27_Units_and_Kinematics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S28_Kinematics_in_2D_and_Projectiles.

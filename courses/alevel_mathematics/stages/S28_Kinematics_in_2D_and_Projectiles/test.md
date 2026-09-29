# S28_Kinematics_in_2D_and_Projectiles - Test: Kinematics in two dimensions and projectiles

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A particle has velocity v = (6t - 2)i + (3 - t^2)j m/s. At t = 0 it is at the origin. Find (a) its acceleration at t = 2, (b) its position at t = 3, (c) when it moves parallel to i. [6 marks]
2. A ball is thrown from the top of a 15 m cliff at 12 m/s at 30° above the horizontal (g = 9.8). Find the time it takes to reach the sea and its horizontal distance from the cliff. [6 marks]
3. A particle starts from rest at 2i + j m with constant acceleration (3i - 4j) m/s^2. Find its distance from the origin after 2 s. [3 marks]
4. State two limitations of the projectile model. [2 marks]

## Answer key (for the tutor only)
1. [6] M1 differentiates; A1 a = 6i - 4j; M1 integrates with r(0) = 0; A1 r = (3t^2 - 2t)i + (3t - t^3/3)j, at t = 3: 21i + 0j; M1 j-component zero: 3 - t^2 = 0; A1 t = root 3.
2. [6] M1 vertical: -15 = 6t - 4.9t^2; M1 4.9t^2 - 6t - 15 = 0; A1 t = 2.47 s; M1 horizontal velocity 12cos 30°; A1 distance 25.6 m; B1 negative root rejected.
3. [3] M1 r = r0 + (1/2)at^2; A1 8i - 7j; A1 root 113 ≈ 10.6 m.
4. [2] B1 air resistance ignored; B1 ball treated as a particle (no spin or size), or g assumed constant.

## Grading
Apply `rubric.json`'s `stage_rubrics.S28_Kinematics_in_2D_and_Projectiles` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S29_Forces_and_Newtons_Laws.

# A Level Further Mathematics (OCR A, H245): Pure Core with Statistics and Mechanics - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Four papers of 75 marks and 90 minutes each, ideally on different days: Pure Core 1 and Pure Core 2 (both drawing on S01-S18), Statistics (S19-S25) and Mechanics (S26-S30). Questions are original and in OCR's style; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest.

## 9 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Pure Core] Prove by induction that Σ (r = 1 to n) r(r!) = (n + 1)! - 1. [5 marks]
2. [Pure Core] Find the cube roots of 4 + 4i root3, giving them in the form re^(iθ) with -π < θ ≤ π. [5 marks]
3. [Pure Core] Find the shortest distance between the lines r = (1, 0, 2) + λ(2, 1, -1) and r = (0, 3, 1) + μ(1, 0, 1). [5 marks]
4. [Pure Core] Solve d^2y/dx^2 - 4dy/dx + 4y = 8x, given y = 0 and dy/dx = 0 when x = 0. [7 marks]
5. [Pure Core] Find the area enclosed by the curve r = 2 + cos θ, 0 ≤ θ < 2π. [4 marks]
6. [Statistics] The number of cars passing a checkpoint in a minute is modelled by Po(2.4). Find the probability that in a 5-minute period more than 15 cars pass, and give one reason why the model might fail. [4 marks]
7. [Statistics] A random sample of 60 has x̄ = 31.2 and s = 5.4. Find a 99% confidence interval for the population mean. [3 marks]
8. [Mechanics] A car of mass 1500 kg climbs a slope of 1 in 20 (sin α = 1/20) against a resistance of 500 N. Its engine works at 36 kW. Find its acceleration when its speed is 15 m/s. [4 marks]
9. [Mechanics] Two smooth spheres, A of mass 2m moving at 3u and B of mass m moving at u in the same direction, collide directly. The coefficient of restitution is 1/2. Find their speeds after the collision. [5 marks]

## Answer key for the ready-made items (tutor only)
1. [5] B1 n = 1: 1 = 2! - 1; M1 assumes for k; M1 adds (k + 1)(k + 1)!; A1 (k + 1)! - 1 + (k + 1)(k + 1)! = (k + 2)(k + 1)! - 1 = (k + 2)! - 1; A1 conclusion.
2. [5] M1 8e^(iπ/3); M1 r = 2; M1 θ = (π/3 + 2πk)/3; A1 2e^(iπ/9), 2e^(i7π/9); A1 2e^(-i5π/9).
3. [5] M1 n = (2, 1, -1) x (1, 0, 1) = (1, -3, -1); M1 b - a = (-1, 3, -1); M1 projection; A1 |-9|/root11; A1 9 root(11)/11.
4. [7] M1 auxiliary (m - 2)^2 = 0; A1 CF (A + Bx)e^(2x); M1 PI y = px + q; A1 PI 2x + 2; M1 y(0) = 0 gives A = -2; M1 y'(0) = 0 gives B = 2; A1 y = 2x + 2(x - 1) e^(2x) + 2.
5. [4] M1 (1/2)∫(2 + cos θ)^2 dθ; M1 expands and uses cos^2 = (1 + cos 2θ)/2; A1 correct integration; A1 9pi/2.
6. [4] M1 Po(12); M1 1 - P(X ≤ 15); A1 0.1556; B1 e.g. cars travel in clusters (not independent), or the rate varies with the time of day.
7. [3] M1 31.2 ± 2.576 x 5.4/root60; A1 (29.40, 33.00); B1 CLT justifies normality (n = 60 is large).
8. [4] M1 driving force 36000/15 = 2400 N; M1 2400 - 500 - 1500g/20 = 1500a; A1 correct equation; A1 a = 0.777 m s^-2.
9. [5] M1 momentum 6mu + mu = 2mv_A + mv_B; M1 v_B - v_A = (1/2)(3u - u) = u; A1 3v_A = 6u; A1 v_A = 2u; A1 v_B = 3u.

## Grading
Mark every question against a written mark scheme. A pass needs at least 50% of the 300 marks overall and at least 40% on each paper. Report the total, the percentage per paper and the weakest topic areas. OCR's grade boundaries change every series, so the course does not claim a predicted grade.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.

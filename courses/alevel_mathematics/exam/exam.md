# A Level Mathematics (OCR A, H240) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Three papers of 100 marks and 2 hours each, sat under timed conditions on different days if possible. Paper 1 covers Pure Mathematics (S01-S21); Paper 2 has a Pure section and a Statistics section (S22-S26); Paper 3 has a Pure section and a Mechanics section (S27-S31). Questions are original and in OCR's style; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest.

## 10 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Paper 1] Prove that n^3 - n is divisible by 6 for every integer n. [4 marks]
2. [Paper 1] (a) Express 2cos x - 3sin x in the form R cos(x + α), R > 0, 0 < α < π/2. (b) Hence solve 2cos x - 3sin x = 1 for 0 ≤ x < 2π. [7 marks]
3. [Paper 1] Find ∫ (0 to 1) x e^(-2x) dx, giving an exact answer. [5 marks]
4. [Paper 1] The curve y = x ln x - 2x has one stationary point. Find its exact coordinates and determine its nature. [5 marks]
5. [Paper 1] The first three terms of a geometric series are k + 4, k and 2k - 15, where k is positive. Find k, the common ratio and the sum to infinity. [6 marks]
6. [Paper 2, Statistics] The heights of a plant species are normally distributed with mean 42 cm and standard deviation 5 cm. After a new fertiliser, a random sample of 20 plants has mean height 44.1 cm. Test at the 5% level whether the mean height has increased. [6 marks]
7. [Paper 2, Statistics] 35% of a town's households have a smart meter. In a random sample of 40 households, find P(fewer than 10 have one) and P(between 12 and 18 inclusive have one). [4 marks]
8. [Paper 3, Mechanics] A particle P moves so that its displacement from O at time t seconds is s = t^3 - 9t^2 + 24t metres. Find the times when P is at rest and the total distance travelled in the first 5 seconds. [6 marks]
9. [Paper 3, Mechanics] A block of mass 3 kg on a rough plane inclined at 25° (μ = 0.3) is connected by a light inextensible string over a smooth pulley at the top of the plane to a hanging particle of mass 3 kg. The system is released from rest. Show that the system moves, and find the acceleration and the tension (g = 9.8). [8 marks]
10. [Paper 3, Mechanics] A projectile is launched from ground level at 30 m/s at 50° above the horizontal (g = 9.8). Find the greatest height and the horizontal range, and state one modelling assumption. [5 marks]

## Answer key for the ready-made items (tutor only)
1. [4] M1 factorises: (n - 1)n(n + 1); M1 three consecutive integers include a multiple of 2 and a multiple of 3; A1 so the product is divisible by 2 and by 3; A1 conclusion: divisible by 6 since 2 and 3 are coprime.
2. [7] M1 R cos α = 2, R sin α = 3; A1 R = root 13; A1 α = 0.9828; M1 cos(x + α) = 1/root 13; A1 principal value 1.2898; A1 x = 4.011; A1 x = 0.307.
3. [5] M1 parts with u = x; A1 -(x/2)e^(-2x) + ∫(1/2)e^(-2x) dx; A1 -(x/2)e^(-2x) - (1/4)e^(-2x); M1 limits; A1 (-3 + e^(2)) e^(-2)/4.
4. [5] M1 dy/dx = ln x + 1 - 2 = ln x - 1; A1 x = e; A1 y = e - 2e = -e; M1 d^2y/dx^2 = 1/x > 0; A1 minimum at (e, -e).
5. [6] M1 k/(k + 4) = (2k - 15)/k; A1 k^2 = (2k - 15)(k + 4), so k^2 - 7k - 60 = 0; A1 k = 12 (k > 0); A1 r = 12/16 = 3/4; M1 S = 16/(1 - 3/4); A1 64.
6. [6] B1 H0: μ = 42, H1: μ > 42; M1 X̄ ~ N(42, 25/20); M1 P(X̄ ≥ 44.1) = 0.0302; A1 compares with 0.05; A1 reject H0; A1 evidence at the 5% level that the mean height has increased.
7. [4] M1 B(40, 0.35); A1 P(X ≤ 9) = 0.0644; M1 P(X ≤ 18) - P(X ≤ 11); A1 0.7248.
8. [6] M1 v = 3t^2 - 18t + 24; A1 t = 2 and t = 4; M1 s(0) = 0, s(2) = 20, s(4) = 16, s(5) = 20; M1 distance = 20 + 4 + 4; A1 28 m; B1 accounts for the change in direction.
9. [8] M1 R = 3g cos 25°; A1 limiting friction 0.3R = 7.99 N; B1 the pull 3g - 3g sin 25° = 16.98 N exceeds it, so the system moves (block up the slope); M1 hanging: 3g - T = 3a; M1 block: T - 3g sin 25° - F = 3a; M1 adds: 3g - 3g sin 25° - F = 6a; A1 a = 1.497 m s^-2; A1 T = 24.91 N.
10. [5] M1 vertical component 30 sin 50°; A1 greatest height 26.9 m; M1 time of flight 60 sin 50°/9.8; A1 range 90.4 m; B1 e.g. no air resistance.

## Grading
Mark every question against a written mark scheme (M, A and B marks). A pass needs at least 50% of the 300 marks overall and at least 40% on each paper. Report the total, the percentage per paper and the weakest topic areas. OCR's own grade boundaries change every series, so the course does not claim a predicted grade.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.

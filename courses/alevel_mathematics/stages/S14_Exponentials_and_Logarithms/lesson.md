# S14_Exponentials_and_Logarithms - Lesson: Exponentials and logarithms

## Goal
The learner uses a^x, e^x, ln x and log_a x with their graphs and laws, solves exponential equations, estimates parameters from log graphs, and models growth and decay.

## Syllabus items taught here
- 1.06a - The function a^x and its graph (a > 0)
- 1.06b - The gradient of e^(kx) is k e^(kx); why exponential models are widely used
- 1.06c - log_a x as the inverse of a^x
- 1.06d - The function ln x and its graph
- 1.06e - ln x as the inverse of e^x
- 1.06f - Laws of logarithms
- 1.06g - Solving equations of the form a^x = b
- 1.06h - Logarithmic graphs to estimate parameters in y = ax^n and y = kb^x
- 1.06i - Exponential growth and decay in modelling, including limitations

## How to teach this
Ask what makes e special among all the possible bases, looking at the gradient of y = a^x at x = 0. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.06a The function a^x and its graph (a > 0)
For a > 0, y = a^x passes through (0, 1), is always positive, and has the x-axis as an asymptote; it increases if a > 1 and decreases if 0 < a < 1 (e.g. (1/2)^x = 2^(-x)).

#### 1.06b The gradient of e^(kx) is k e^(kx); why exponential models are widely used
e ≈ 2.71828 is the base for which the gradient of y = e^x equals its value: d/dx(e^x) = e^x, and d/dx(e^(kx)) = ke^(kx). So a quantity whose rate of change is proportional to its size (dN/dt = kN) follows an exponential model N = Ae^(kt): populations, radioactive decay, cooling, compound interest.

#### 1.06c log_a x as the inverse of a^x
log_a x = y means a^y = x (for a > 0, a ≠ 1, x > 0). It is the inverse of a^x, so log_a(a^x) = x and a^(log_a x) = x. *Example:* log_2 32 = 5; log_9 3 = 1/2; log_a 1 = 0.

#### 1.06d The function ln x and its graph
ln x = log_e x. y = ln x passes through (1, 0), exists only for x > 0, has the y-axis as an asymptote, and increases slowly. It is the reflection of y = e^x in y = x.

#### 1.06e ln x as the inverse of e^x
e^(ln x) = x (x > 0) and ln(e^x) = x. *Example:* solve e^(2x) = 7: 2x = ln 7, x = (ln 7)/2. Solve ln(3x - 1) = 2: 3x - 1 = e^2, x = (e^2 + 1)/3.

#### 1.06f Laws of logarithms
log_a x + log_a y = log_a(xy); log_a x - log_a y = log_a(x/y); k log_a x = log_a(x^k); log_a(1/x) = -log_a x; log_a a = 1. *Example:* 2 log 3 + log 4 - log 6 = log(9 × 4/6) = log 6. *Example:* solve log_2(x + 2) + log_2 x = 3: log_2(x(x + 2)) = 3, x^2 + 2x - 8 = 0, x = 2 (x = -4 is rejected because log_2(-4) is undefined).

#### 1.06g Solving equations of the form a^x = b
Take logs of both sides. *Example:* 3^x = 20: x = ln 20 / ln 3 = 2.727. *Example:* 2^(2x - 1) = 5^x: (2x - 1) ln 2 = x ln 5, x(2 ln 2 - ln 5) = ln 2, x = ln 2/(ln 4 - ln 5) = -3.106. Disguised quadratics: 9^x - 4(3^x) + 3 = 0 with u = 3^x gives u = 1 or 3, so x = 0 or 1.

#### 1.06h Logarithmic graphs to estimate parameters in y = ax^n and y = kb^x
If y = ax^n then log y = n log x + log a: plotting log y against log x gives a straight line with gradient n and intercept log a. If y = kb^x then log y = x log b + log k: plotting log y against x gives gradient log b and intercept log k. *Example:* a line of log y against x has gradient 0.3 and intercept 1.2 (base-10 logs): b = 10^0.3 ≈ 2.00 and k = 10^1.2 ≈ 15.8, so y ≈ 15.8 × 2^x.

#### 1.06i Exponential growth and decay in modelling, including limitations
Growth: N = N0 e^(kt), k > 0; decay: k < 0. *Example:* a culture of 500 bacteria doubles every 3 hours: 1000 = 500e^(3k), k = (ln 2)/3; after 10 hours N = 500e^(10k) = 5040. The rate of growth dN/dt = kN. Limitations: real populations are limited by food and space, so exponential growth cannot continue indefinitely; a refined model might level off.

## Explicitly not here
Differentiating and integrating exponentials are S16 and S18.

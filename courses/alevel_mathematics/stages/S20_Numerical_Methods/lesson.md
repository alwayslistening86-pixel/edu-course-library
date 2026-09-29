# S20_Numerical_Methods - Lesson: Numerical methods

## Goal
The learner locates roots by change of sign, uses fixed-point iteration and Newton-Raphson, recognises when each fails, applies the trapezium rule and judges over- or under-estimates, and uses numerical methods in context.

## Syllabus items taught here
- 1.09a - Locating roots by change of sign
- 1.09b - How change-of-sign methods can fail
- 1.09c - Iteration x(n+1) = g(x(n)); cobweb and staircase diagrams
- 1.09d - The Newton-Raphson method
- 1.09e - How iterative methods can fail
- 1.09f - Numerical integration: the trapezium rule, over- and under-estimates
- 1.09g - Using numerical methods to solve problems in context

## How to teach this
Ask how a calculator could find the root of x^3 + 2x - 5 = 0 when there's no formula to hand. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.09a Locating roots by change of sign
If f is continuous on [a, b] and f(a), f(b) have opposite signs, there is at least one root between a and b. *Example:* f(x) = x^3 + 2x - 5: f(1) = -2, f(2) = 7, so a root lies in (1, 2). To show a root is 1.33 to 2 d.p., check f(1.325) = -0.0238 and f(1.335) = 0.0493: the sign change confirms it (the root is 1.32827).

#### 1.09b How change-of-sign methods can fail
Change of sign can fail: an even number of roots in the interval gives no sign change (f(x) = x^2 - 0.01 on [-1, 1]); a repeated root touches without changing sign; a discontinuity (f(x) = 1/x on [-1, 1]) changes sign without a root. So always state that f is continuous on the interval.

#### 1.09c Iteration x(n+1) = g(x(n)); cobweb and staircase diagrams
Rearrange f(x) = 0 as x = g(x) and iterate x(n+1) = g(x(n)). *Example:* x^3 + 2x - 5 = 0 as x = cube root(5 - 2x), x1 = 1.3: x2 = 1.3389, x3 = 1.3243, x4 = 1.3298, x5 = 1.3277, converging (oscillating) to the root. On a diagram of y = x and y = g(x), a **staircase** shows monotonic convergence (0 < g' < 1) and a **cobweb** shows oscillating convergence (-1 < g' < 0). The iteration converges if |g'(x)| < 1 near the root.

#### 1.09d The Newton-Raphson method
x(n+1) = x(n) - f(x(n))/f'(x(n)): follow the tangent at x(n) to the x-axis. *Example:* f(x) = x^3 + 2x - 5, f'(x) = 3x^2 + 2, x1 = 1.5: x2 = 1.34286, x3 = 1.32838, x4 = 1.32827. It converges very fast when the start is close to the root.

#### 1.09e How iterative methods can fail
Iteration x = g(x) diverges if |g'(x)| > 1 near the root (then try a different rearrangement). Newton-Raphson fails if f'(x(n)) = 0 (a horizontal tangent: division by zero) and can jump to a different root, or diverge, if the starting point is near a stationary point.

#### 1.09f Numerical integration: the trapezium rule, over- and under-estimates
Trapezium rule with n strips of width h = (b - a)/n: ∫ (a to b) y dx ≈ (h/2)(y0 + 2(y1 + ... + y(n-1)) + yn). *Example:* ∫ (0 to 2) root(1 + x^2) dx with 4 strips (h = 0.5): ≈ 0.25(1 + 2(root1.25 + root2 + root3.25) + root5) = 2.9765; the exact value is 2.9579. If the curve is convex (bends upwards) the trapezia lie above it and the rule **over-estimates**; concave means an under-estimate. More strips improve the accuracy. You may also bound an integral between the sums of lower and upper rectangles.

#### 1.09g Using numerical methods to solve problems in context
Use numerical methods when an equation or integral cannot be solved exactly in context: e.g. the time when two models give equal values, or the area under a velocity-time curve from data. Give answers to a sensible accuracy and interpret them in context.

## Explicitly not here
Vectors are S21.

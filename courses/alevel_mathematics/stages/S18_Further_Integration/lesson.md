# S18_Further_Integration - Lesson: Further integration

## Goal
The learner integrates exponential, reciprocal and trig functions, finds areas between curves, understands integration as the limit of a sum, and integrates by substitution, by parts and using partial fractions.

## Syllabus items taught here
- 1.08c - Integrating e^(kx), 1/x, sin kx and cos kx
- 1.08f - Area between two curves
- 1.08g - Integration as the limit of a sum
- 1.08h - Integration by substitution
- 1.08i - Integration by parts
- 1.08j - Integrating using partial fractions with linear denominators

## How to teach this
Ask what ∫ 1/x dx should be, given that x^0/0 is meaningless. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.08c Integrating e^(kx), 1/x, sin kx and cos kx
∫e^(kx) dx = (1/k)e^(kx) + c; ∫(1/x) dx = ln|x| + c; ∫sin kx dx = -(1/k)cos kx + c; ∫cos kx dx = (1/k)sin kx + c. Also ∫f'(x)/f(x) dx = ln|f(x)| + c: ∫2x/(x^2 + 3) dx = ln(x^2 + 3) + c; ∫tan x dx = -ln|cos x| + c = ln|sec x| + c. *Example:* ∫ (0 to π/2) cos 2x dx = [sin 2x/2] = 0.

#### 1.08f Area between two curves
Area between y = f(x) and y = g(x) from x = a to x = b (with f ≥ g) is ∫ (a to b) (f(x) - g(x)) dx; find a and b from the intersections. *Example:* y = 4 - x^2 and y = x + 2 meet where x^2 + x - 2 = 0, x = -2 and 1: area = ∫ (-2 to 1) (2 - x - x^2) dx = 9/2.

#### 1.08g Integration as the limit of a sum
The area under a curve is the limit of the sum of thin rectangles: ∫ (a to b) f(x) dx = lim (δx → 0) Σ f(x) δx. This is why integrals give totals (distance from velocity, volume from cross-sectional area) and why the trapezium rule approximates an integral.

#### 1.08h Integration by substitution
Substitution: choose u, find du in terms of dx, change everything (including limits) to u. *Example:* ∫x(x^2 + 1)^5 dx: u = x^2 + 1, du = 2x dx, giving (1/2)∫u^5 du = (x^2 + 1)^6/12 + c. *Example:* ∫ (0 to 3) x root(x + 1) dx with u = x + 1 (limits 1 to 4): ∫ (1 to 4) (u - 1)u^(1/2) du = 116/15. Recognising the reverse chain rule is a shortcut: ∫cos x sin^4 x dx = sin^5 x/5 + c.

#### 1.08i Integration by parts
∫u (dv/dx) dx = uv - ∫v (du/dx) dx. Choose u to become simpler when differentiated (a power of x, or ln x). *Example:* ∫x e^(2x) dx: u = x, dv/dx = e^(2x): = (x/2)e^(2x) - ∫(1/2)e^(2x) dx = (x/2)e^(2x) - (1/4)e^(2x) + c. *Example:* ∫ln x dx = x ln x - x + c (take u = ln x, dv/dx = 1). Sometimes parts is needed twice (∫x^2 sin x dx).

#### 1.08j Integrating using partial fractions with linear denominators
Split into partial fractions, then integrate each term as a log (or a power for repeated factors). *Example:* ∫ (2 to 4) 5/((x - 1)(x + 4)) dx = ∫ (1/(x - 1) - 1/(x + 4)) dx = [ln|x - 1| - ln|x + 4|] = ln(3/8) - ln(1/6) = ln(9/4).

## Explicitly not here
Differential equations are S19.

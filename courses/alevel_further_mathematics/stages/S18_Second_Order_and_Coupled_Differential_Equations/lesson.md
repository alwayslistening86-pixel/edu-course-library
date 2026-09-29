# S18_Second_Order_and_Coupled_Differential_Equations - Lesson: Second-order and coupled differential equations

## Goal
The learner solves second-order linear equations with constant coefficients (homogeneous and with a particular integral), models simple harmonic motion and damped oscillations, and solves coupled first-order systems by elimination.

## Syllabus items taught here
- 4.10d - Second-order homogeneous equations y'' + ay' + by = 0 via the auxiliary equation
- 4.10e - Second-order non-homogeneous equations: complementary function plus particular integral
- 4.10f - Simple harmonic motion x'' = -ω^2 x and its solution
- 4.10g - Damped oscillations modelled by second-order differential equations
- 4.10h - Coupled first-order linear differential equations (e.g. predator-prey), solved by elimination

## How to teach this
Ask what function stays the same shape when you differentiate it twice and add multiples of it, and why e^(mx) is the natural guess. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.10d Second-order homogeneous equations y'' + ay' + by = 0 via the auxiliary equation
y'' + ay' + by = 0: try y = e^(mx): the **auxiliary equation** m^2 + am + b = 0. Distinct real roots m1, m2: y = Ae^(m1 x) + Be^(m2 x). Repeated root m: y = (A + Bx)e^(mx). Complex roots p ± qi: y = e^(px)(A cos qx + B sin qx). *Example:* y'' + 4y' + 13y = 0: m = -2 ± 3i, y = e^(-2x)(A cos 3x + B sin 3x).

#### 4.10e Second-order non-homogeneous equations: complementary function plus particular integral
General solution = complementary function (CF, solving the homogeneous case) + particular integral (PI). Try a PI of the same form as f(x): polynomial → polynomial of the same degree; ke^(px) → λe^(px) (if p is a root of the auxiliary equation, try λxe^(px)); sin or cos → λ cos + μ sin. *Example:* y'' - 5y' + 6y = 12x: CF Ae^(2x) + Be^(3x); PI y = px + q: -5p + 6px + 6q = 12x gives p = 2, q = 5/3. General solution y = Ae^(2x) + Be^(3x) + 2x + 5/3. Apply two conditions to find A and B.

#### 4.10f Simple harmonic motion x'' = -ω^2 x and its solution
Simple harmonic motion: x'' = -ω^2 x, solution x = A cos ωt + B sin ωt = R sin(ωt + α). Period 2π/ω, amplitude R. Velocity v^2 = ω^2(R^2 - x^2), maximum speed Rω at the centre.

#### 4.10g Damped oscillations modelled by second-order differential equations
Damped oscillation: x'' + kx' + ω^2 x = 0. Discriminant k^2 - 4ω^2 < 0: light damping (oscillations decaying like e^(-kt/2)); = 0: critical damping (returns fastest without oscillating); > 0: heavy damping. A forcing term gives forced oscillations (CF + PI); as t → ∞ the CF decays and the PI remains.

#### 4.10h Coupled first-order linear differential equations (e.g. predator-prey), solved by elimination
Coupled systems dx/dt = ax + by + f(t), dy/dt = cx + dy + g(t): differentiate the first, substitute y and dy/dt from the equations to get one second-order equation in x, solve it, then find y from the first equation (not by solving again, which would introduce new constants). *Example:* dx/dt = 3x - 2y, dy/dt = x: x'' = 3x' - 2y' = 3x' - 2x, so x'' - 3x' + 2x = 0, x = Ae^t + Be^(2t); y = (3x - x')/2 = Ae^t + (1/2)Be^(2t). Predator-prey and mixing models use this; interpret the solution in context (what happens as t increases, when does a population die out).

## Explicitly not here
Statistics begins in S19.

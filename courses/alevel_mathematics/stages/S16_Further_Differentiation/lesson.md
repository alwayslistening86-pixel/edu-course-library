# S16_Further_Differentiation - Lesson: Further differentiation

## Goal
The learner differentiates exponentials, logs and trig functions (including from first principles for sin and cos), uses the product, quotient and chain rules, differentiates implicitly and parametrically, uses the second derivative for concavity and inflection, and forms differential equations.

## Syllabus items taught here
- 1.07f - Second derivative, convex and concave sections, and points of inflection
- 1.07h - Differentiation from first principles for sin x and cos x
- 1.07j - Differentiating e^(kx) and a^(kx)
- 1.07k - Differentiating sin kx, cos kx and tan kx
- 1.07l - The derivative of ln x
- 1.07p - Finding points of inflection
- 1.07q - The product and quotient rules
- 1.07r - The chain rule, including connected rates of change and inverse functions
- 1.07s - Implicit and parametric differentiation (first derivative)
- 1.07t - Constructing simple differential equations in pure mathematics and in context

## How to teach this
Ask how to differentiate (3x + 1)^10 without expanding, and why the answer is not 10(3x + 1)^9. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.07f Second derivative, convex and concave sections, and points of inflection
Where f''(x) > 0 the curve is **convex** (bends upwards, lies above its tangents); where f''(x) < 0 it is **concave**. A point of inflection is where the curve changes between convex and concave, so f'' changes sign there. *Example:* y = x^3: f''(x) = 6x changes sign at 0, so (0, 0) is a point of inflection. f''(a) = 0 alone is not enough: y = x^4 has f''(0) = 0 but no inflection.

#### 1.07h Differentiation from first principles for sin x and cos x
Using sin(x + h) = sin x cos h + cos x sin h and the small-angle results sin h/h → 1 and (cos h - 1)/h → 0: (sin(x + h) - sin x)/h = sin x (cos h - 1)/h + cos x (sin h)/h → cos x. Similarly d/dx(cos x) = -sin x. Angles must be in radians.

#### 1.07j Differentiating e^(kx) and a^(kx)
d/dx(e^(kx)) = ke^(kx); d/dx(a^(kx)) = k(ln a)a^(kx), since a^(kx) = e^(kx ln a). *Example:* d/dx(5^(2x)) = 2 ln 5 × 5^(2x).

#### 1.07k Differentiating sin kx, cos kx and tan kx
d/dx(sin kx) = k cos kx; d/dx(cos kx) = -k sin kx; d/dx(tan kx) = k sec^2 kx. *Example:* d/dx(3sin 2x - cos 4x) = 6cos 2x + 4sin 4x.

#### 1.07l The derivative of ln x
d/dx(ln x) = 1/x; d/dx(ln kx) = 1/x too (since ln kx = ln k + ln x). With the chain rule, d/dx(ln f(x)) = f'(x)/f(x): d/dx(ln(x^2 + 1)) = 2x/(x^2 + 1).

#### 1.07p Finding points of inflection
Find where f''(x) = 0 and check that f'' changes sign. *Example:* y = x^4 - 6x^2: f''(x) = 12x^2 - 12 = 0 at x = ±1; f'' changes sign at each, so (1, -5) and (-1, -5) are points of inflection. If f'(a) = 0 as well, it is a stationary point of inflection.

#### 1.07q The product and quotient rules
Product rule: d/dx(uv) = u'v + uv'. Quotient rule: d/dx(u/v) = (u'v - uv')/v^2. *Example:* y = x^2 e^(3x): dy/dx = 2xe^(3x) + 3x^2 e^(3x) = xe^(3x)(2 + 3x). *Example:* y = sin x/x: dy/dx = (x cos x - sin x)/x^2. tan x = sin x/cos x by the quotient rule gives sec^2 x.

#### 1.07r The chain rule, including connected rates of change and inverse functions
Chain rule: dy/dx = dy/du × du/dx. *Example:* y = (3x + 1)^10: dy/dx = 10(3x + 1)^9 × 3 = 30(3x + 1)^9. y = e^(x^2): dy/dx = 2xe^(x^2). **Connected rates of change:** dV/dt = dV/dr × dr/dt. *Example:* a spherical balloon's radius grows at 0.5 cm/s; when r = 10, dV/dt = 4πr^2 × 0.5 = 200π cm^3/s. **Inverse functions:** dx/dy = 1/(dy/dx); e.g. x = y^3 + y gives dy/dx = 1/(3y^2 + 1).

#### 1.07s Implicit and parametric differentiation (first derivative)
Implicit: differentiate every term with respect to x, treating y as a function of x, so d/dx(y^2) = 2y dy/dx and d/dx(xy) = y + x dy/dx; then collect dy/dx. *Example:* x^2 + xy + y^2 = 7 at (1, 2): 2x + y + x dy/dx + 2y dy/dx = 0, so dy/dx = -(2x + y)/(x + 2y) = -4/5. Parametric: dy/dx = (dy/dt)/(dx/dt). *Example:* x = t^2, y = 2t: dy/dx = 2/(2t) = 1/t. Also d/dx(a^x) = a^x ln a, from ln y = x ln a.

#### 1.07t Constructing simple differential equations in pure mathematics and in context
A differential equation relates a function to its derivatives. Translate words into symbols: "the rate of decrease of temperature T is proportional to the excess temperature over the room's 20°C" gives dT/dt = -k(T - 20), k > 0. "The gradient at any point is the product of its coordinates" gives dy/dx = xy. State what the constant of proportionality means and its sign.

## Explicitly not here
Solving differential equations is S19.

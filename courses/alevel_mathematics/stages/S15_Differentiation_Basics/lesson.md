# S15_Differentiation_Basics - Lesson: Differentiation: principles, tangents and stationary points

## Goal
The learner understands the derivative as a gradient and a limit, differentiates from first principles and x^n, uses second derivatives, and finds tangents, normals, stationary points and intervals of increase.

## Syllabus items taught here
- 1.07a - The derivative as the gradient of the tangent at a general point
- 1.07b - The gradient of the tangent as a limit; the derivative as a rate of change
- 1.07c - Sketching the gradient function of a given curve
- 1.07d - Second derivatives
- 1.07e - The second derivative as the rate of change of gradient
- 1.07g - Differentiation from first principles for small positive integer powers of x
- 1.07i - Differentiating x^n for rational n, with constant multiples, sums and differences
- 1.07m - Gradients, tangents and normals
- 1.07n - Finding and classifying stationary points as maxima or minima
- 1.07o - Increasing and decreasing functions

## How to teach this
Ask the learner to estimate the gradient of y = x^2 at x = 3 using chords to x = 3.1, 3.01 and 3.001. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.07a The derivative as the gradient of the tangent at a general point
The derivative f'(x) (or dy/dx) gives the gradient of the tangent to y = f(x) at the point (x, f(x)). At a specific point, substitute: for y = x^2, dy/dx = 2x, so the gradient at (3, 9) is 6.

#### 1.07b The gradient of the tangent as a limit; the derivative as a rate of change
The gradient of the tangent at x = a is the limit of chord gradients: f'(a) = lim (h → 0) (f(a + h) - f(a))/h. It measures the rate of change of y with respect to x: if s is distance and t time, ds/dt is velocity. *Example:* the chord gradients of y = x^2 from x = 3 to 3 + h are 6 + h, tending to 6.

#### 1.07c Sketching the gradient function of a given curve
Sketch y = f'(x) from y = f(x): where f has a stationary point, f' = 0 (crosses the x-axis); where f is increasing, f' > 0 (above the axis); decreasing, f' < 0. A cubic's gradient function is a quadratic; a quadratic's is a straight line. A point of inflection on f is a turning point of f'.

#### 1.07d Second derivatives
Differentiate twice: f''(x) or d^2y/dx^2. *Example:* y = 2x^4 - 3x^2: dy/dx = 8x^3 - 6x, d^2y/dx^2 = 24x^2 - 6.

#### 1.07e The second derivative as the rate of change of gradient
d^2y/dx^2 measures how fast the gradient itself changes. If s is displacement, ds/dt is velocity and d^2s/dt^2 acceleration. Where d^2y/dx^2 > 0 the gradient is increasing (the curve bends upwards).

#### 1.07g Differentiation from first principles for small positive integer powers of x
For f(x) = x^2: (f(x + h) - f(x))/h = (x^2 + 2xh + h^2 - x^2)/h = 2x + h → 2x as h → 0. For x^3: ((x + h)^3 - x^3)/h = 3x^2 + 3xh + h^2 → 3x^2. Write the limit statement clearly and show that h cancels before letting h → 0. The same method proves d/dx(ax^2 + bx) = 2ax + b.

#### 1.07i Differentiating x^n for rational n, with constant multiples, sums and differences
d/dx(x^n) = nx^(n-1) for any rational n; constants differentiate to 0; differentiate term by term. Rewrite first: y = 3/x^2 + 4root x = 3x^(-2) + 4x^(1/2), so dy/dx = -6x^(-3) + 2x^(-1/2). Expand brackets and split fractions before differentiating: (x^2 + 5)/x = x + 5x^(-1).

#### 1.07m Gradients, tangents and normals
Tangent at (a, f(a)): gradient m = f'(a); equation y - f(a) = m(x - a). Normal: perpendicular to the tangent, gradient -1/m. *Example:* y = x^3 - 2x at x = 1: y = -1, dy/dx = 3x^2 - 2 = 1, tangent y = x - 2, normal y = -x.

#### 1.07n Finding and classifying stationary points as maxima or minima
Stationary points are where dy/dx = 0. Classify with d^2y/dx^2: positive → minimum, negative → maximum (zero → use another method, e.g. gradient either side). *Example:* y = x^3 - 6x^2 + 9x + 1: dy/dx = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 at x = 1, 3. d^2y/dx^2 = 6x - 12: at x = 1 it is -6 (maximum, y = 5); at x = 3 it is 6 (minimum, y = 1). Optimisation problems: form an expression in one variable, differentiate, set to zero, check it is a max or min, and answer the question asked.

#### 1.07o Increasing and decreasing functions
f is increasing where f'(x) > 0 and decreasing where f'(x) < 0. *Example:* for y = x^3 - 6x^2 + 9x + 1, 3(x - 1)(x - 3) < 0 for 1 < x < 3, so the function is decreasing on that interval and increasing for x < 1 and x > 3. To show a function is increasing everywhere, show f'(x) > 0 for all x, e.g. by completing the square.

## Explicitly not here
Product, quotient and chain rules are S16.

# S06_Functions_Modulus_and_Transformations - Lesson: Functions, modulus and transformations

## Goal
The learner uses function notation with domains and ranges, forms composite and inverse functions, works with the modulus function algebraically and graphically, applies single and combined transformations, and models with functions.

## Syllabus items taught here
- 1.02l - The modulus function and its properties
- 1.02s - Sketching the graph of the modulus of a linear function
- 1.02t - Solving equations and inequalities involving the modulus function graphically
- 1.02u - The definition of a function: domain and range, one-one and many-one
- 1.02v - Inverse functions and their graphs; composite functions
- 1.02w - Effect of single transformations on y = f(x): translations, stretches and reflections
- 1.02x - Combinations of transformations on y = f(x)
- 1.02z - Using functions in modelling, including limitations and refinements

## How to teach this
Ask why f(x) = x^2 has no inverse unless its domain is restricted, and what restriction works. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.02l The modulus function and its properties
|x| is the distance of x from 0: |x| = x if x ≥ 0, -x if x < 0. Properties: |a| = |b| <=> a^2 = b^2; |x - a| < b <=> a - b < x < a + b. *Example:* |2x - 3| = 5 gives 2x - 3 = 5 or 2x - 3 = -5, so x = 4 or x = -1. *Example:* |x - 2| < 3 gives -1 < x < 5. *Example:* |x + 1| = |2x - 4|: square both sides, x^2 + 2x + 1 = 4x^2 - 16x + 16, 3x^2 - 18x + 15 = 0, x = 1 or x = 5.

#### 1.02s Sketching the graph of the modulus of a linear function
y = |ax + b|: sketch the line, then reflect any part below the x-axis in the x-axis, giving a V shape with its vertex on the x-axis at x = -b/a. *Example:* y = |2x - 4| has vertex (2, 0) and y-intercept 4. (y = |f(x)| reflects negative parts up; y = f(|x|) reflects the right-hand half into the left.)

#### 1.02t Solving equations and inequalities involving the modulus function graphically
Sketch both sides to see how many solutions exist and which branch each lies on, then solve algebraically. *Example:* |2x - 4| = x + 1: on the right branch 2x - 4 = x + 1, x = 5; on the left branch -(2x - 4) = x + 1, x = 1. Both valid (check x + 1 ≥ 0). *Example:* |2x - 4| < x + 1 holds between the intersections: 1 < x < 5.

#### 1.02u The definition of a function: domain and range, one-one and many-one
A **function** maps every element of the domain to exactly one element of the range. One-one: each output from exactly one input; many-one: some outputs come from more than one input (e.g. x^2 over all reals). *Example:* f(x) = x^2 + 3, x ∈ ℝ has range f(x) ≥ 3; g(x) = 1/(x - 2), x ≠ 2 has range g(x) ≠ 0. A mapping that sends one input to two outputs (like y = ±root x) is not a function.

#### 1.02v Inverse functions and their graphs; composite functions
Composite fg(x) = f(g(x)): apply g first. *Example:* f(x) = 2x + 1, g(x) = x^2: fg(x) = 2x^2 + 1, gf(x) = (2x + 1)^2. Only **one-one** functions have inverses. To find f^(-1): write y = f(x), swap x and y (or make x the subject), rearrange. The domain of f^(-1) is the range of f, and the graph of f^(-1) is the reflection of f in y = x. *Example:* f(x) = (x + 3)/(x - 1), x > 1: y(x - 1) = x + 3, x(y - 1) = y + 3, so f^(-1)(x) = (x + 3)/(x - 1) (this f is self-inverse), with domain x > 1. ff^(-1)(x) = x.

#### 1.02w Effect of single transformations on y = f(x): translations, stretches and reflections
y = f(x) + a: up a. y = f(x + a): left a (translation by the vector (-a, 0)). y = af(x): stretch parallel to the y-axis, scale factor a. y = f(ax): stretch parallel to the x-axis, scale factor 1/a. y = -f(x): reflection in the x-axis; y = f(-x): reflection in the y-axis. *Example:* the point (2, 5) on y = f(x) maps to (2, 8) on y = f(x) + 3, (-1, 5) on y = f(x + 3), (2, 10) on y = 2f(x) and (1, 5) on y = f(2x). Describe transformations in full ("translation by vector ...", "stretch parallel to the x-axis, scale factor ...").

#### 1.02x Combinations of transformations on y = f(x)
Apply transformations one at a time in a sensible order: inside the bracket (x changes) act on x in the reverse of the operations applied to x; outside act on y in the order written. *Example:* y = 2f(x - 1) + 3 from y = f(x): translate right 1, stretch vertically ×2, then up 3. The maximum (0, 4) of f maps to (1, 11). For y = f(2x + 6) = f(2(x + 3)): translate left 3, then stretch parallel to the x-axis, scale factor 1/2; (4, 0) maps to ((4 - 6)/2, 0) = (-1, 0).

#### 1.02z Using functions in modelling, including limitations and refinements
A function can model a real situation: state the variables and units, choose the function, fit parameters from data, then comment on its **limitations** (e.g. it predicts negative values, or is only valid over a restricted domain) and possible **refinements**. *Example:* the height of a ball h = 20t - 5t^2 (metres, t seconds) is valid for 0 ≤ t ≤ 4 only; it ignores air resistance, which would reduce the maximum height below 20 m.

## Explicitly not here
Trigonometric and exponential functions are S11-S14.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **GeoGebra Graphing Calculator** (https://www.geogebra.org/graphing) -- Plot f(x) alongside a transformed version (a slider for the transformation constant) to see the effect on the graph directly, rather than only reasoning about it algebraically.

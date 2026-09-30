# S17_Integration_Basics - Lesson: Integration: the basics and areas

## Goal
The learner understands integration as the reverse of differentiation, integrates x^n, evaluates definite integrals and finds areas between a curve and the x-axis.

## Syllabus items taught here
- 1.08a - The fundamental theorem of calculus
- 1.08b - Integrating x^n (n not -1), with sums, differences and constant multiples
- 1.08d - Evaluating definite integrals
- 1.08e - Area between a curve and the x-axis

## How to teach this
Ask for a function whose derivative is 6x^2, and whether it is the only one. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.08a The fundamental theorem of calculus
The fundamental theorem of calculus: integration reverses differentiation, and the definite integral of f from a to b equals F(b) - F(a) where F' = f. Indefinite integrals need + c because constants differentiate to zero. *Example:* if dy/dx = 6x^2 and the curve passes through (1, 5), then y = 2x^3 + c, c = 3.

#### 1.08b Integrating x^n (n not -1), with sums, differences and constant multiples
∫x^n dx = x^(n+1)/(n + 1) + c (n ≠ -1). Integrate term by term after rewriting as powers: ∫(4x^3 - 3/x^2 + root x) dx = x^4 + 3x^(-1) + (2/3)x^(3/2) + c.

#### 1.08d Evaluating definite integrals
Evaluate [F(x)] between the limits: ∫ (1 to 3) (3x^2 - 2x) dx = [x^3 - x^2] (1 to 3) = (27 - 9) - (1 - 1) = 18. No + c is needed. Swapping the limits changes the sign.

#### 1.08e Area between a curve and the x-axis
The area between y = f(x), the x-axis and x = a, x = b is ∫ (a to b) f(x) dx when the curve is above the axis. Parts below the axis give negative integrals: find the roots, integrate each part separately and add the magnitudes. *Example:* area between y = x(x - 2) and the x-axis is |∫ (0 to 2) (x^2 - 2x) dx| = |-4/3| = 4/3. *Example:* for y = x^3 - x from -1 to 1 the integral is 0, but the area is 2 × 1/4 = 1/2.

## Explicitly not here
Areas between two curves and harder integration are S18.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **GeoGebra Graphing Calculator** (https://www.geogebra.org/graphing) -- Use the built-in integral tool to shade the area under a curve between two limits and see the numerical value computed directly, as a check against a hand-calculated definite integral.

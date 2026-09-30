# S05_Graphs_and_Curve_Sketching - Lesson: Graphs, curve sketching and proportion

## Goal
The learner sketches polynomial and reciprocal curves with intercepts, roots and asymptotes, interprets algebraic solutions graphically, uses intersections to solve equations, and models proportion.

## Syllabus items taught here
- 1.02m - Using graphs of functions
- 1.02n - Sketching curves defined by simple equations, including polynomials
- 1.02o - Sketching y = a/x and y = a/x^2, including asymptotes
- 1.02p - Interpreting the algebraic solution of equations graphically
- 1.02q - Using intersection points of graphs to solve equations
- 1.02r - Proportional relationships and their graphs

## How to teach this
Ask what the graph of y = (x - 1)^2(x + 3) does at x = 1 compared with x = -3. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.02m Using graphs of functions
A graph shows every point (x, f(x)); reading it gives values, roots (where it meets the x-axis) and turning points. Key features to mark on any sketch: intercepts with both axes, turning points where known, asymptotes, and behaviour as x → ±∞. Use graphs to check an algebraic answer (a claimed root must be where the graph crosses the axis).

#### 1.02n Sketching curves defined by simple equations, including polynomials
For a polynomial in factorised form, the roots are where each factor is zero. A single root: the curve crosses. A repeated (squared) root: the curve touches the axis and turns. A cubed factor: a point of inflection on the axis. The leading term sets the ends: a positive cubic goes from bottom-left to top-right; a negative quartic points down at both ends. *Example:* y = (x - 1)^2(x + 3): crosses at x = -3, touches at x = 1, y-intercept (0 - 1)^2(0 + 3) = 3, bottom-left to top-right. *Example:* y = -x(x - 2)(x + 2)^2: roots at 0 and 2 (cross), -2 (touch); ends both down.

#### 1.02o Sketching y = a/x and y = a/x^2, including asymptotes
y = a/x (a > 0): two branches in the first and third quadrants, asymptotes x = 0 and y = 0. y = a/x^2 (a > 0): both branches above the x-axis (first and second quadrants), same asymptotes, symmetric about the y-axis. For a < 0 each graph is reflected in the x-axis. Mark asymptotes as dashed lines.

#### 1.02p Interpreting the algebraic solution of equations graphically
Solving f(x) = 0 algebraically gives the x-intercepts of y = f(x); a repeated root is a touching point; no real roots means the graph misses the axis. Solving f(x) = g(x) gives the x-coordinates where the two graphs meet. *Example:* x^2 - 4x + 5 = 0 has discriminant 16 - 20 < 0, so y = x^2 - 4x + 5 lies wholly above the x-axis.

#### 1.02q Using intersection points of graphs to solve equations
To show how many solutions an equation has, rearrange it as f(x) = g(x) with two sketchable graphs and count intersections. *Example:* how many real solutions has x^3 = 4 - x? Sketch y = x^3 and y = 4 - x: the cubic is increasing and the line decreasing, so they meet exactly once (between x = 1 and x = 2, since 1 < 3 and 8 > 2). *Example:* 1/x = x^2 - 3 has three solutions: the hyperbola meets the parabola once for x > 0 and twice for x < 0.

#### 1.02r Proportional relationships and their graphs
y ∝ x means y = kx (a straight line through the origin); y ∝ x^2 means y = kx^2; y ∝ 1/x means y = k/x (inverse proportion, a hyperbola). Find k from one pair of values. *Example:* the time T for a job is inversely proportional to the number of workers w; T = 12 hours when w = 5, so k = 60 and T = 60/w; with 8 workers T = 7.5 hours.

## Explicitly not here
Transformations of graphs are S06.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **GeoGebra Graphing Calculator** (https://www.geogebra.org/graphing) -- Type in any function and see it plotted instantly, with sliders for parameters -- useful for checking a hand-sketched curve (intercepts, turning points, asymptotes) against the real graph.

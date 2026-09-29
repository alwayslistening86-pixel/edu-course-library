# S03_Simultaneous_Equations_and_Inequalities - Lesson: Simultaneous equations and inequalities

## Goal
The learner solves linear/quadratic simultaneous equations, solves linear and quadratic inequalities, writes solution sets correctly, and shades regions for inequalities in two variables.

## Syllabus items taught here
- 1.02c - Simultaneous equations in two variables, including one linear and one quadratic
- 1.02g - Linear and quadratic inequalities in one variable, interpreted graphically
- 1.02h - Expressing solutions using 'and', 'or' and set notation
- 1.02i - Representing linear and quadratic inequalities in two variables graphically

## How to teach this
Ask how many times a line can meet a parabola, and how the discriminant would show it. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.02c Simultaneous equations in two variables, including one linear and one quadratic
Linear pairs: elimination or substitution. Linear with quadratic: rearrange the linear equation for one variable and **substitute into the quadratic**. *Example:* y = 2x - 1 and x^2 + y^2 = 13: x^2 + (2x - 1)^2 = 13, so 5x^2 - 4x - 12 = 0, (5x + 6)(x - 2) = 0, x = 2 or -6/5; then y = 3 or -17/5. Pair the values: (2, 3) and (-6/5, -17/5). The number of solutions tells you about intersection: substituting a line into a curve and getting a repeated root means the line is a **tangent**.

#### 1.02g Linear and quadratic inequalities in one variable, interpreted graphically
Linear inequalities: solve like equations, but reverse the sign when multiplying or dividing by a negative. *Example:* 5 - 2x < 11 gives -2x < 6, x > -3. Quadratic inequalities: find the critical values, then sketch. *Example:* x^2 - x - 6 > 0: (x - 3)(x + 2) > 0; the parabola is above the axis outside the roots, so x < -2 or x > 3. x^2 - x - 6 ≤ 0 gives -2 ≤ x ≤ 3. With fractions, multiply by a positive square (e.g. (x - 1)^2) rather than by a denominator whose sign is unknown.

#### 1.02h Expressing solutions using 'and', 'or' and set notation
Two separate intervals are joined by "or" (x < -2 or x > 3), which in set notation is {x : x < -2} ∪ {x : x > 3}. A single interval like -2 ≤ x ≤ 3 is "x ≥ -2 and x ≤ 3", i.e. {x : x ≥ -2} ∩ {x : x ≤ 3} or {x : -2 ≤ x ≤ 3}. Never write -2 > x > 3 for two separate regions (that says a number is both below -2 and above 3). Interval notation such as [-2, 3] may also be used.

#### 1.02i Representing linear and quadratic inequalities in two variables graphically
For an inequality in x and y, draw the boundary: solid for ≤ or ≥ (included), dashed for < or > (excluded). Test a point not on the boundary (the origin, if possible) to decide which side to shade. *Example:* the region y > x + 1 and y < 7 - x^2 lies above the dashed line y = x + 1 and inside (below) the dashed parabola y = 7 - x^2. The line and curve meet where x + 1 = 7 - x^2, x^2 + x - 6 = 0, x = 2 or x = -3, so the region lies between x = -3 and x = 2. Label the required region R as the question asks (OCR often asks to shade the region *not* required).

## Explicitly not here
Modulus inequalities are S06.

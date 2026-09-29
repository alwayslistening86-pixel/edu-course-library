# S07_Lines_and_Circles - Lesson: Coordinate geometry: lines and circles

## Goal
The learner writes equations of lines in all three forms, uses parallel and perpendicular gradients, models with straight lines, and finds and uses the equation, centre and radius of a circle with its chord, tangent and semicircle properties.

## Syllabus items taught here
- 1.03a - Equation of a straight line in the forms y = mx + c, y - y1 = m(x - x1) and ax + by + c = 0
- 1.03b - Gradient conditions for parallel and perpendicular lines
- 1.03c - Straight-line models in context
- 1.03d - Coordinate geometry of a circle: (x - a)^2 + (y - b)^2 = r^2
- 1.03e - Completing the square to find a circle's centre and radius
- 1.03f - Circle properties in coordinate geometry: angle in a semicircle, perpendicular bisector of a chord, tangent perpendicular to radius

## How to teach this
Ask how you could find a circle's centre if you only knew three points on it. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.03a Equation of a straight line in the forms y = mx + c, y - y1 = m(x - x1) and ax + by + c = 0
Gradient m = (y2 - y1)/(x2 - x1). Forms: y = mx + c; y - y1 = m(x - x1); ax + by + c = 0 (a, b, c integers is the usual request). *Example:* the line through (2, -1) and (5, 8): m = 9/3 = 3; y + 1 = 3(x - 2), so y = 3x - 7, or 3x - y - 7 = 0.

#### 1.03b Gradient conditions for parallel and perpendicular lines
Parallel lines have equal gradients; perpendicular lines have m1 m2 = -1 (so m2 = -1/m1). *Example:* the perpendicular to 2x + 3y = 6 (m = -2/3) through (4, 1) has gradient 3/2: y - 1 = (3/2)(x - 4), i.e. 3x - 2y - 10 = 0. The perpendicular bisector of AB passes through the midpoint of AB with the perpendicular gradient.

#### 1.03c Straight-line models in context
A straight-line model y = mx + c: m is the rate of change and c the initial value, both with units. *Example:* a candle is 24 cm tall and burns 1.5 cm per hour: h = 24 - 1.5t, valid for 0 ≤ t ≤ 16. Criticise models (does a constant rate make sense? what happens outside the data?) and interpret gradient and intercept in context.

#### 1.03d Coordinate geometry of a circle: (x - a)^2 + (y - b)^2 = r^2
A circle with centre (a, b) and radius r: (x - a)^2 + (y - b)^2 = r^2. *Example:* centre (3, -2) through (6, 2): r^2 = 3^2 + 4^2 = 25, so (x - 3)^2 + (y + 2)^2 = 25. To find where a line meets a circle, substitute; a repeated root means the line is a tangent, and no real roots means no intersection.

#### 1.03e Completing the square to find a circle's centre and radius
x^2 + y^2 + 2gx + 2fy + c = 0: complete the square in x and in y. *Example:* x^2 + y^2 - 6x + 4y - 12 = 0: (x - 3)^2 - 9 + (y + 2)^2 - 4 - 12 = 0, so (x - 3)^2 + (y + 2)^2 = 25, centre (3, -2), radius 5. If the right-hand side comes out ≤ 0 the equation is not a circle.

#### 1.03f Circle properties in coordinate geometry: angle in a semicircle, perpendicular bisector of a chord, tangent perpendicular to radius
(1) The angle in a semicircle is a right angle, so if AB is a diameter and C on the circle, AC ⊥ BC. (2) The perpendicular from the centre to a chord bisects the chord; the perpendicular bisector of a chord passes through the centre. (3) A tangent is perpendicular to the radius at the point of contact. *Example:* tangent to (x - 3)^2 + (y + 2)^2 = 25 at (6, 2): radius gradient (2 + 2)/(6 - 3) = 4/3, so the tangent gradient is -3/4: y - 2 = -(3/4)(x - 6), i.e. 3x + 4y - 26 = 0. Find a circle through three points by intersecting two perpendicular bisectors.

## Explicitly not here
Parametric curves are S08.

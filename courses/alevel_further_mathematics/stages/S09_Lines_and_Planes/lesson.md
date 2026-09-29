# S09_Lines_and_Planes - Lesson: Lines and planes

## Goal
The learner writes lines and planes in vector and cartesian forms, uses the scalar product for angles and perpendicularity, and finds angles between planes and between lines and planes, and intersections of lines with lines and with planes.

## Syllabus items taught here
- 4.04a - Equation of a line in 2-D and 3-D in cartesian and vector form
- 4.04b - Equation of a plane in cartesian and vector (including scalar product) form
- 4.04c - The scalar product: angles between vectors or lines, and perpendicularity
- 4.04d - Angle between two planes and between a line and a plane
- 4.04e - Point of intersection of two lines; skew lines
- 4.04f - Intersection of a line and a plane

## How to teach this
Ask how a single point plus a direction pins down a line, and what extra is needed to pin down a plane. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.04a Equation of a line in 2-D and 3-D in cartesian and vector form
Vector form r = a + λd (a: a point on the line, d: direction). Cartesian: (x - a1)/d1 = (y - a2)/d2 = (z - a3)/d3. *Example:* through (1, -2, 3) with direction (2, 1, -1): (x - 1)/2 = (y + 2)/1 = (z - 3)/(-1).

#### 4.04b Equation of a plane in cartesian and vector (including scalar product) form
A plane: r = a + λb + μc (a point and two directions), or r.n = a.n (n normal to the plane), or cartesian n1x + n2y + n3z = d. *Example:* through (1, 0, 2) with normal (3, -1, 2): 3x - y + 2z = 7.

#### 4.04c The scalar product: angles between vectors or lines, and perpendicularity
a.b = a1b1 + a2b2 + a3b3 = |a||b| cos θ. Perpendicular iff a.b = 0. The angle between two lines uses their direction vectors (take the acute angle). *Example:* directions (1, 2, 2) and (2, -1, 2): cos θ = 4/9, θ = 63.6°.

#### 4.04d Angle between two planes and between a line and a plane
Between two planes: the angle between their normals (acute). Between a line and a plane: 90° minus the angle between the line's direction and the normal, i.e. sin φ = |d.n|/(|d||n|). *Example:* line direction (1, 1, 0), plane normal (0, 1, 1): sin φ = 1/2, φ = 30°.

#### 4.04e Point of intersection of two lines; skew lines
Set the two vector equations equal and solve for λ and μ using two components; check the third. If it fails and the lines aren't parallel, they are **skew**. *Example:* r = (1, 0, 2) + λ(1, 1, 0) and r = (0, 3, 1) + μ(1, 0, 1): 1 + λ = μ, λ = 3, 2 = 1 + μ gives μ = 1 but then λ = 0, contradiction, so skew.

#### 4.04f Intersection of a line and a plane
Substitute the line's parametric coordinates into the plane's equation and solve for λ. *Example:* r = (2, 1, 0) + λ(1, -1, 3) meets x + 2y - z = 10 when 2 + λ + 2 - 2λ - 3λ = 10, λ = -3/2, at (1/2, 5/2, -9/2). If the direction is perpendicular to the normal, the line is parallel to the plane (it lies in it or never meets it).

## Explicitly not here
The vector product and distances are S10.

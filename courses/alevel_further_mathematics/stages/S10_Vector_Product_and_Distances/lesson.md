# S10_Vector_Product_and_Distances - Lesson: The vector product and shortest distances

## Goal
The learner uses the vector product to find normals, and finds shortest distances between parallel lines, skew lines, a point and a line, and a point and a plane.

## Syllabus items taught here
- 4.04g - The vector product to find a vector perpendicular to two given vectors
- 4.04h - Distance between parallel lines and shortest distance between skew lines
- 4.04i - Shortest distance between a point and a line
- 4.04j - Shortest distance between a point and a plane

## How to teach this
Ask how to find a direction perpendicular to two given directions without solving simultaneous equations. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.04g The vector product to find a vector perpendicular to two given vectors
a x b = (a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1), perpendicular to both a and b (its magnitude is |a||b| sin θ). *Example:* (1, 2, -1) x (3, 0, 2) = (4, -5, -6). Use it for the normal of a plane containing two directions.

#### 4.04h Distance between parallel lines and shortest distance between skew lines
Skew lines r = a + λd1 and r = b + μd2: n = d1 x d2 is perpendicular to both, and the shortest distance = |(b - a).n|/|n|. Parallel lines: the distance from a point on one line to the other line (4.04i). *Example:* r = (1, 0, 0) + λ(1, 1, 0) and r = (0, 1, 3) + μ(0, 1, 1): n = (1, 1, 0) x (0, 1, 1) = (1, -1, 1); b - a = (-1, 1, 3); distance = |(-1, 1, 3).(1, -1, 1)|/root3 = |-1 - 1 + 3|/root3 = 1/root3. If this calculation gives 0, the lines intersect.

#### 4.04i Shortest distance between a point and a line
Distance from P to the line r = a + λd: the foot F satisfies (a + λd - p).d = 0; the distance is |PF|. Or |(p - a) x d|/|d|. *Example:* P(1, 2, 3), line r = (0, 0, 0) + λ(1, 1, 1): λ = 2, F = (2, 2, 2), distance root2.

#### 4.04j Shortest distance between a point and a plane
Distance from P(x1, y1, z1) to the plane ax + by + cz = d: |ax1 + by1 + cz1 - d|/root(a^2 + b^2 + c^2). *Example:* (1, 2, 3) to 2x - y + 2z = 3: |2 - 2 + 6 - 3|/3 = 1.

## Explicitly not here
Roots of polynomials are S11.

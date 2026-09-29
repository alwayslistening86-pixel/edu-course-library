# S21_Vectors - Lesson: Vectors

## Goal
The learner works with vectors in two and three dimensions, finds magnitude and direction, adds and scales vectors geometrically, uses position vectors and distances, and applies vectors to geometry, forces and kinematics.

## Syllabus items taught here
- 1.10a - Vectors in two dimensions
- 1.10b - Vectors in three dimensions
- 1.10c - Magnitude and direction of a vector; converting between component and magnitude-direction form
- 1.10d - Adding vectors and multiplying by scalars, with geometrical interpretations
- 1.10e - Position vectors
- 1.10f - Distance between two points from position vectors
- 1.10g - Vectors to solve problems in pure mathematics and in context, including forces
- 1.10h - Vectors to solve problems in kinematics

## How to teach this
Ask how a single arrow can carry both 'how far' and 'which way'. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.10a Vectors in two dimensions
A 2D vector has components: a = 3i - 2j = (3, -2) as a column. Vectors are equal when their components match. Ordered pairs written as column vectors are used throughout.

#### 1.10b Vectors in three dimensions
In 3D, v = xi + yj + zk. *Example:* from A(1, 2, -1) to B(4, 0, 3): AB = 3i - 2j + 4k. |AB| = root(9 + 4 + 16) = root 29.

#### 1.10c Magnitude and direction of a vector; converting between component and magnitude-direction form
|a| = root(a1^2 + a2^2); direction: the angle with i is arctan(a2/a1), adjusting for the quadrant. *Example:* a = -4i + 3j: |a| = 5, direction 180° - 36.9° = 143.1° from i. A vector of magnitude 10 at 30° above i is 10cos 30° i + 10sin 30° j = 5root3 i + 5j. A unit vector: a/|a|.

#### 1.10d Adding vectors and multiplying by scalars, with geometrical interpretations
Add head to tail (the triangle or parallelogram law); subtract by adding the negative; λa is parallel to a with |λ| times the length (reversed if λ < 0). Two vectors are parallel if one is a scalar multiple of the other. *Example:* 2(3i - j) - (i + 4j) = 5i - 6j. Geometrical reasoning: in triangle OAB with OA = a, OB = b, the midpoint M of AB has OM = (a + b)/2.

#### 1.10e Position vectors
The position vector of point A is OA = a from the origin. AB = b - a. A point dividing AB in the ratio 2 : 1 has position vector a + (2/3)(b - a) = (a + 2b)/3.

#### 1.10f Distance between two points from position vectors
Distance AB = |b - a|. *Example:* A(2, -1, 5), B(-1, 3, 5): b - a = -3i + 4j + 0k, AB = 5. Collinear points: AB and BC parallel with a common point.

#### 1.10g Vectors to solve problems in pure mathematics and in context, including forces
Vectors show geometrical results (parallel sides, midpoints, parallelograms) and represent forces: the resultant of F1 = 3i + 4j and F2 = -i + 2j is 2i + 6j N, magnitude root 40 N. If a particle is in equilibrium under several forces, their vector sum is 0.

#### 1.10h Vectors to solve problems in kinematics
Position r, velocity v and acceleration a are vectors. For constant velocity, r = r0 + vt. *Example:* a ship at (2i + 3j) km moving with velocity (4i - j) km/h is at (2 + 4t)i + (3 - t)j after t hours; it is due east of the origin when 3 - t = 0, t = 3, at 14i. Two objects meet if their position vectors are equal at the same time.

## Explicitly not here
Vector kinematics with acceleration is S28.

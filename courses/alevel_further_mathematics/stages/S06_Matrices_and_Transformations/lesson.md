# S06_Matrices_and_Transformations - Lesson: Matrices and transformations

## Goal
The learner uses matrix language and arithmetic, knows that multiplication is associative but not commutative, represents 2-D and simple 3-D transformations and their compositions by matrices, and finds invariant points and lines.

## Syllabus items taught here
- 4.03a - The language of matrices: order, square, zero and identity matrices
- 4.03b - Adding, subtracting and multiplying conformable matrices; scalar multiplication
- 4.03c - Matrix multiplication is associative but not commutative
- 4.03d - Matrices for 2-D linear transformations: reflections, rotations, enlargements, stretches and shears
- 4.03e - Matrices for successive transformations
- 4.03f - Matrices for 3-D reflections in coordinate planes and rotations about coordinate axes
- 4.03g - Invariant points and invariant lines

## How to teach this
Ask where the unit vectors i and j go under a rotation of 90°, and how that builds the matrix. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.03a The language of matrices: order, square, zero and identity matrices
A matrix of order m x n has m rows and n columns. Square matrices have m = n; the zero matrix 0 has all entries 0; the identity I has 1s on the leading diagonal and 0s elsewhere, and AI = IA = A.

#### 4.03b Adding, subtracting and multiplying conformable matrices; scalar multiplication
Add or subtract matrices of the same order entry by entry; multiply by a scalar entry by entry. AB exists if A is m x n and B is n x p (the product is m x p); entry (i, j) is row i of A dotted with column j of B.

#### 4.03c Matrix multiplication is associative but not commutative
(AB)C = A(BC), so powers are well defined; but in general AB ≠ BA. *Example:* A = [[2, 1], [0, 3]], B = [[1, 0], [1, 1]]: AB = [[3, 1], [3, 3]], BA = [[2, 1], [2, 4]].

#### 4.03d Matrices for 2-D linear transformations: reflections, rotations, enlargements, stretches and shears
The columns of a transformation matrix are the images of i and j. Rotation by θ anticlockwise about O: [[cos θ, -sin θ], [sin θ, cos θ]]. Reflection in y = x: [[0, 1], [1, 0]]; in y = -x: [[0, -1], [-1, 0]]; in the x-axis: [[1, 0], [0, -1]]. Enlargement scale factor k: [[k, 0], [0, k]]. Stretch parallel to the x-axis, factor k (y-axis invariant): [[k, 0], [0, 1]]. Shear with the x-axis invariant: [[1, k], [0, 1]] (so (0, 1) goes to (k, 1)).

#### 4.03e Matrices for successive transformations
Applying A then B is the single transformation BA (the first transformation is on the right). *Example:* reflect in the x-axis, then rotate 90° anticlockwise: [[0, -1], [1, 0]][[1, 0], [0, -1]] = [[0, 1], [1, 0]], a reflection in y = x.

#### 4.03f Matrices for 3-D reflections in coordinate planes and rotations about coordinate axes
3-D: reflection in the plane z = 0: diag(1, 1, -1) (similarly for x = 0, y = 0). Rotation by θ about the z-axis: [[cos θ, -sin θ, 0], [sin θ, cos θ, 0], [0, 0, 1]] (anticlockwise looking towards O from the positive axis); about the x-axis the 1 is in the top-left, and about the y-axis [[cos θ, 0, sin θ], [0, 1, 0], [-sin θ, 0, cos θ]].

#### 4.03g Invariant points and invariant lines
An **invariant point** satisfies Mx = x. An **invariant line** maps onto itself (points may move along it); a **line of invariant points** has every point fixed. For lines through O, y = mx: apply M to (x, mx) and require the image (x', y') to satisfy y' = mx'. *Example:* M = [[3, 1], [2, 2]] gives (x', y') = (3x + mx, 2x + 2mx); so 2 + 2m = m(3 + m), m^2 + m - 2 = 0, m = 1 or m = -2: y = x and y = -2x are invariant lines. For y = mx + c with c ≠ 0, require the image to satisfy y' = mx' + c for every x.

## Explicitly not here
Determinants and inverses are S07.

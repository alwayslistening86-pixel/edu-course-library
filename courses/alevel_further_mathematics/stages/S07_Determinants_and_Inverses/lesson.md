# S07_Determinants_and_Inverses - Lesson: Determinants and inverses

## Goal
The learner calculates 2 x 2 and 3 x 3 determinants and interprets them as area/volume scale factors, recognises singular matrices, uses det(AB) = det A det B, finds inverses by hand and calculator, relates inverses to inverse transformations, and solves linear systems with inverse matrices.

## Syllabus items taught here
- 4.03h - Determinant of a 2 x 2 matrix
- 4.03i - The determinant as an area scale factor and its sign as orientation
- 4.03j - Determinant of a 3 x 3 matrix
- 4.03k - The 3 x 3 determinant as a volume scale factor and orientation
- 4.03l - Singular and non-singular matrices
- 4.03m - det(AB) = det(A) det(B)
- 4.03n - Inverse of a non-singular 2 x 2 matrix
- 4.03o - Inverse of a non-singular 3 x 3 matrix
- 4.03p - Properties of inverses, including (AB)^(-1) = B^(-1)A^(-1)
- 4.03q - Inverse matrices and inverse transformations
- 4.03r - Solving two or three simultaneous linear equations with an inverse matrix

## How to teach this
Ask what a transformation that squashes the plane onto a line would do to areas, and whether it could be undone. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.03h Determinant of a 2 x 2 matrix
det [[a, b], [c, d]] = ad - bc.

#### 4.03i The determinant as an area scale factor and its sign as orientation
|det M| is the area scale factor of the transformation M. A negative determinant means orientation is reversed (the image is a reflection of the shape's orientation). *Example:* [[2, 1], [1, 3]] has det 5: a triangle of area 4 maps to area 20.

#### 4.03j Determinant of a 3 x 3 matrix
Expand along the top row: det = a(ei - fh) - b(di - fg) + c(dh - eg) for [[a, b, c], [d, e, f], [g, h, i]]. *Example:* det [[1, 2, 0], [3, -1, 4], [2, 1, 1]] = 1(-1 - 4) - 2(3 - 8) + 0 = 5.

#### 4.03k The 3 x 3 determinant as a volume scale factor and orientation
|det M| for a 3 x 3 matrix is the volume scale factor; a negative value means the orientation (handedness) is reversed.

#### 4.03l Singular and non-singular matrices
M is singular if det M = 0 (no inverse: the transformation collapses area or volume to zero); otherwise non-singular. *Example:* [[k, 2], [3, k - 1]] is singular when k^2 - k - 6 = 0, k = 3 or k = -2.

#### 4.03m det(AB) = det(A) det(B)
det(AB) = det A x det B: the scale factors multiply.

#### 4.03n Inverse of a non-singular 2 x 2 matrix
[[a, b], [c, d]]^(-1) = (1/(ad - bc))[[d, -b], [-c, a]].

#### 4.03o Inverse of a non-singular 3 x 3 matrix
For 3 x 3: find the matrix of cofactors, transpose it (the adjugate), divide by the determinant. *Example:* for M = [[1, 2, 0], [3, -1, 4], [2, 1, 1]], det = 5 and M^(-1) = [[-1, -2/5, 8/5], [1, 1/5, -4/5], [1, 3/5, -7/5]]. A calculator may be used unless the question says otherwise (then show the cofactor method).

#### 4.03p Properties of inverses, including (AB)^(-1) = B^(-1)A^(-1)
(AB)^(-1) = B^(-1)A^(-1) (proof: (AB)(B^(-1)A^(-1)) = I); (A^(-1))^(-1) = A; det(A^(-1)) = 1/det A.

#### 4.03q Inverse matrices and inverse transformations
The inverse matrix represents the inverse transformation: it maps images back to objects. So the original shape is found from the image by applying M^(-1). The inverse of a rotation by θ is a rotation by -θ; a reflection is self-inverse.

#### 4.03r Solving two or three simultaneous linear equations with an inverse matrix
Write the system as Mx = b, so x = M^(-1)b when det M ≠ 0. *Example:* x + 2y = 7, 3x - y + 4z = 9, 2x + y + z = 7: using M^(-1) above, (x, y, z) = (3/5, 16/5, 13/5).

## Explicitly not here
Systems without a unique solution are S08.

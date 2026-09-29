# S03_Complex_Roots_and_Argand_Diagrams - Lesson: Complex roots of polynomials and Argand diagrams

## Goal
The learner uses the conjugate-pair property to solve real cubics and quartics, plots complex numbers on an Argand diagram, and interprets conjugation, addition, subtraction, multiplication and division geometrically.

## Syllabus items taught here
- 4.02g - Complex roots of real polynomials occur in conjugate pairs
- 4.02j - Solving and factorising real cubics and quartics using conjugate pairs and the factor theorem
- 4.02k - Argand diagrams
- 4.02l - Geometrical effect of conjugation and of adding and subtracting complex numbers
- 4.02m - Geometrical effect of multiplying and dividing complex numbers

## How to teach this
Ask why, if 2 + i is a root of a polynomial with real coefficients, 2 - i must be one too. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.02g Complex roots of real polynomials occur in conjugate pairs
If a polynomial has real coefficients, complex roots come in conjugate pairs: taking the conjugate of p(α) = 0 gives p(α*) = 0. So a real cubic has either three real roots or one real root and a conjugate pair.

#### 4.02j Solving and factorising real cubics and quartics using conjugate pairs and the factor theorem
*Example:* given 1 - 2i is a root of z^3 - z^2 + 3z + 5 = 0, then 1 + 2i is too, so (z - (1 - 2i))(z - (1 + 2i)) = z^2 - 2z + 5 is a factor. Dividing: z^3 - z^2 + 3z + 5 = (z^2 - 2z + 5)(z + 1); roots 1 ± 2i, -1. Quartics: two conjugate pairs, or one pair and two real roots.

#### 4.02k Argand diagrams
The Argand diagram plots z = x + iy as the point (x, y) (or the vector to it). The modulus is its distance from O; the argument is the angle from the positive real axis.

#### 4.02l Geometrical effect of conjugation and of adding and subtracting complex numbers
z* is the reflection of z in the real axis. z + w adds as vectors (parallelogram rule); z - w is the vector from w to z, so |z - w| is the distance between the points z and w.

#### 4.02m Geometrical effect of multiplying and dividing complex numbers
|zw| = |z||w| and arg(zw) = arg z + arg w: multiplying by w scales by |w| and rotates by arg w. |z/w| = |z|/|w| and arg(z/w) = arg z - arg w. Multiplying by i rotates by π/2. *Example:* z = 2(cos π/3 + i sin π/3), w = 3(cos π/4 + i sin π/4): zw = 6(cos 7π/12 + i sin 7π/12), z/w = (2/3)(cos π/12 + i sin π/12). Adjust sums of arguments back into the principal range.

## Explicitly not here
Loci are S04.

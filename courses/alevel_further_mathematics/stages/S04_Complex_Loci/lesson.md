# S04_Complex_Loci - Lesson: Loci and regions in the Argand diagram

## Goal
The learner sketches and describes loci and regions in the Argand diagram (circles, half-lines, perpendicular bisectors and horizontal/vertical lines) and uses set notation for them.

## Syllabus items taught here
- 4.02o - Loci and regions in the Argand diagram: circles, half-lines and perpendicular bisectors
- 4.02p - Set notation for loci

## How to teach this
Ask what set of points is exactly 2 units from 1 + i, and how to write that with a modulus. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.02o Loci and regions in the Argand diagram: circles, half-lines and perpendicular bisectors
|z - a| = k: circle, centre a, radius k (|z - a| < k is the inside). arg(z - a) = θ: a half-line from a (excluding a itself) at angle θ. |z - a| = |z - b|: the perpendicular bisector of the points a and b. Re z = k and Im z = k: vertical and horizontal lines. Use solid lines for boundaries included (≤) and dashed for excluded (<), and indicate the region clearly. *Example:* |z - 2 - i| ≤ 2 and 0 ≤ arg(z - 2 - i) ≤ π/4 is a sector of the circle. Find the greatest value of |z| on a circle as (distance from O to the centre) + radius.

#### 4.02p Set notation for loci
Loci as sets: {z : |z - 3i| = 2}; intersections with ∩ and unions with ∪, e.g. {z : |z| ≤ 3} ∩ {z : Re z > 1}. A point lies in a set if it satisfies the defining condition.

## Explicitly not here
De Moivre's theorem is S05.

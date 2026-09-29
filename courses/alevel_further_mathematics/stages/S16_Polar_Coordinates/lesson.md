# S16_Polar_Coordinates - Lesson: Polar coordinates

## Goal
The learner converts between polar and cartesian coordinates, sketches polar curves, and finds areas enclosed by polar curves.

## Syllabus items taught here
- 4.09a - Polar coordinates (r ≥ 0) and converting between polar and cartesian
- 4.09b - Sketching polar curves r = f(θ)
- 4.09c - Area enclosed by a polar curve: (1/2)∫r^2 dθ

## How to teach this
Ask how a lighthouse beam at angle θ and distance r describes a point differently from x and y. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.09a Polar coordinates (r ≥ 0) and converting between polar and cartesian
A point has polar coordinates (r, θ), r ≥ 0: x = r cos θ, y = r sin θ; r^2 = x^2 + y^2, tan θ = y/x (by quadrant). *Example:* r = 4cos θ: r^2 = 4r cos θ gives x^2 + y^2 = 4x, a circle centre (2, 0) radius 2. y = x^2 becomes r sin θ = r^2 cos^2 θ, r = sin θ/cos^2 θ.

#### 4.09b Sketching polar curves r = f(θ)
Tabulate r for key θ (0, π/6, π/4, ... ) and plot; note maximum and minimum r, symmetry (replacing θ by -θ), and where r = 0 (the curve meets the pole with tangent in that direction). Only plot where r ≥ 0. *Example:* r = a(1 + cos θ) is a cardioid: r = 2a at θ = 0, r = 0 at θ = π. r = a sin 2θ for 0 ≤ θ ≤ π/2 is one loop.

#### 4.09c Area enclosed by a polar curve: (1/2)∫r^2 dθ
Area = (1/2) ∫ r^2 dθ between the limits. *Example:* area inside the cardioid r = 1 + cos θ: (1/2) ∫ (0 to 2π) (1 + cos θ)^2 dθ = 3π/2. For regions between two curves, find the intersection angles and subtract.

## Explicitly not here
Differential equations are S17.

# S11_Trigonometry_Foundations - Lesson: Trigonometry: definitions, rules, graphs and radians

## Goal
The learner uses sin, cos and tan for any angle, applies the sine and cosine rules and the area formula, works in radians (arc length and sector area), knows exact values, and sketches the trig graphs with their symmetries.

## Syllabus items taught here
- 1.05a - Definitions of sine, cosine and tangent for all arguments
- 1.05b - The sine and cosine rules
- 1.05c - Area of a triangle: (1/2)ab sin C
- 1.05d - Radian measure, arc length and sector area
- 1.05f - Graphs, symmetries and periodicity of sin, cos and tan
- 1.05g - Exact values of sin, cos and tan for 0, pi/6, pi/4, pi/3, pi/2 and multiples

## How to teach this
Ask why sin 150° = sin 30°, using the unit circle rather than a rule. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.05a Definitions of sine, cosine and tangent for all arguments
For any angle θ measured anticlockwise from the positive x-axis, the point on the unit circle is (cos θ, sin θ), and tan θ = sin θ / cos θ. Signs by quadrant (the CAST diagram): all positive in the first quadrant, sin in the second, tan in the third, cos in the fourth. *Example:* sin 210° = -sin 30° = -1/2; cos 300° = cos 60° = 1/2; tan 135° = -1.

#### 1.05b The sine and cosine rules
Sine rule: a/sin A = b/sin B = c/sin C (for a side-angle pair plus one more). Cosine rule: a^2 = b^2 + c^2 - 2bc cos A (two sides and the included angle, or three sides). *Example:* b = 7, c = 5, A = 40°: a^2 = 49 + 25 - 70 cos 40°, a = 4.514. The **ambiguous case**: given two sides and a non-included angle, the sine rule can give two possible angles (θ and 180° - θ); check whether both fit (angles must sum to less than 180°). *Example:* a = 6, b = 8, A = 40°: sin B = 8 sin 40°/6 = 0.8571, so B = 59.0° or 121.0°; both are possible.

#### 1.05c Area of a triangle: (1/2)ab sin C
Area = (1/2)ab sin C, using two sides and the angle between them. *Example:* sides 6 cm and 9 cm with an included angle of 50°: area = 27 sin 50° = 20.68 cm^2. Rearrange to find an angle: if the area is 20 and the sides are 8 and 7, sin C = 40/56, so C = 45.6° or 134.4°.

#### 1.05d Radian measure, arc length and sector area
π radians = 180°, so 1 rad ≈ 57.3°. Arc length s = rθ; sector area A = (1/2)r^2 θ (θ in radians). Segment area = (1/2)r^2(θ - sin θ). *Example:* r = 6 cm, θ = 1.2 rad: arc = 7.2 cm, sector = 21.6 cm^2, segment = 18(1.2 - sin 1.2) = 4.823 cm^2. In calculus, angles are always in radians.

#### 1.05f Graphs, symmetries and periodicity of sin, cos and tan
y = sin x and y = cos x have period 360° (2π) and range -1 to 1; y = tan x has period 180° (π) and vertical asymptotes at x = 90° + 180°n. Symmetries: sin(180° - x) = sin x; cos(360° - x) = cos x; sin(-x) = -sin x (odd); cos(-x) = cos x (even); cos x = sin(90° - x). Use them to find all solutions from the principal value.

#### 1.05g Exact values of sin, cos and tan for 0, pi/6, pi/4, pi/3, pi/2 and multiples
Exact values (from the half-square and half-equilateral triangles): sin 30° = 1/2, cos 30° = root3/2, tan 30° = 1/root3; sin 45° = cos 45° = 1/root2, tan 45° = 1; sin 60° = root3/2, cos 60° = 1/2, tan 60° = root3; sin 0 = 0, cos 0 = 1; sin 90° = 1, cos 90° = 0, tan 90° undefined. In radians: π/6, π/4, π/3, π/2. *Example:* sin(2π/3) = root3/2; cos(5π/4) = -1/root2; tan(11π/6) = -1/root3.

## Explicitly not here
Trig identities and equations are S12.

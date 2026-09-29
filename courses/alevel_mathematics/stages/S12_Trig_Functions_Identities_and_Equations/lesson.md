# S12_Trig_Functions_Identities_and_Equations - Lesson: Reciprocal and inverse trig functions, identities and equations

## Goal
The learner uses small-angle approximations, the reciprocal and inverse trig functions with their graphs, domains and ranges, the Pythagorean identities, and solves trig equations in a given interval.

## Syllabus items taught here
- 1.05e - Small-angle approximations for sin, cos and tan
- 1.05h - Secant, cosecant and cotangent; arcsin, arccos and arctan
- 1.05i - Graphs, domains and ranges of sec, cosec, cot and the inverse trig functions
- 1.05j - Identities tan x = sin x / cos x and sin^2 x + cos^2 x = 1
- 1.05k - Identities sec^2 x = 1 + tan^2 x and cosec^2 x = 1 + cot^2 x
- 1.05o - Solving trigonometric equations in a given interval, including quadratics and multiple angles

## How to teach this
Ask why arcsin has range -π/2 to π/2 rather than all angles. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.05e Small-angle approximations for sin, cos and tan
For small θ in radians: sin θ ≈ θ, cos θ ≈ 1 - θ^2/2, tan θ ≈ θ. *Example:* approximate (1 - cos 2θ)/(θ tan θ) for small θ: 1 - (1 - (2θ)^2/2) = 2θ^2, and θ tan θ ≈ θ^2, so the expression ≈ 2. Check with θ = 0.1: (1 - cos 0.2)/(0.1 tan 0.1) ≈ 1.99. These only work in radians.

#### 1.05h Secant, cosecant and cotangent; arcsin, arccos and arctan
sec θ = 1/cos θ, cosec θ = 1/sin θ, cot θ = 1/tan θ = cos θ / sin θ. arcsin x, arccos x and arctan x are the inverses of sin, cos and tan on restricted domains: arcsin: domain -1 ≤ x ≤ 1, range -π/2 ≤ y ≤ π/2; arccos: domain -1 ≤ x ≤ 1, range 0 ≤ y ≤ π; arctan: domain all real x, range -π/2 < y < π/2. *Example:* arcsin(-1/2) = -π/6; arccos(-1/2) = 2π/3; sec(π/3) = 2.

#### 1.05i Graphs, domains and ranges of sec, cosec, cot and the inverse trig functions
y = sec x has the same period as cos x, is undefined where cos x = 0 (asymptotes at x = π/2 + nπ) and has range y ≤ -1 or y ≥ 1. y = cosec x has asymptotes at x = nπ and the same range. y = cot x has period π and asymptotes at x = nπ. The inverse functions' graphs are reflections of the restricted sin, cos and tan graphs in y = x: arctan x has horizontal asymptotes y = ±π/2.

#### 1.05j Identities tan x = sin x / cos x and sin^2 x + cos^2 x = 1
tan θ = sin θ / cos θ and sin^2 θ + cos^2 θ = 1 (from Pythagoras on the unit circle). *Example:* given sin θ = 3/5 with θ obtuse, cos θ = -4/5 and tan θ = -3/4. *Example:* show (1 - cos^2 θ)/cos θ = sin θ tan θ: LHS = sin^2 θ / cos θ = sin θ (sin θ / cos θ) = RHS. Use it to turn an equation into one function: 2sin^2 x + 3cos x = 3 becomes 2 - 2cos^2 x + 3cos x = 3.

#### 1.05k Identities sec^2 x = 1 + tan^2 x and cosec^2 x = 1 + cot^2 x
Divide sin^2 θ + cos^2 θ = 1 by cos^2 θ: tan^2 θ + 1 = sec^2 θ; divide by sin^2 θ: 1 + cot^2 θ = cosec^2 θ. *Example:* solve 2tan^2 θ - sec θ - 1 = 0 for 0 ≤ θ < 360°: 2(sec^2 θ - 1) - sec θ - 1 = 0, so 2sec^2 θ - sec θ - 3 = 0, (2sec θ - 3)(sec θ + 1) = 0, so cos θ = 2/3 or cos θ = -1: θ = 48.2°, 311.8° or 180°.

#### 1.05o Solving trigonometric equations in a given interval, including quadratics and multiple angles
Method: find the principal value from the calculator, then use the graph's symmetry to list every solution in the interval. *Example:* sin x = 0.4 for 0 ≤ x < 360°: x = 23.6° or 156.4°. Multiple angles: adjust the interval first. *Example:* cos 2x = 0.5 for 0 ≤ x < 360°: 0 ≤ 2x < 720°, so 2x = 60°, 300°, 420°, 660°, giving x = 30°, 150°, 210°, 330°. Quadratics: 2cos^2 x + 3cos x - 2 = 0 factorises as (2cos x - 1)(cos x + 2) = 0; cos x = -2 is impossible, so x = 60° or 300°. Never divide by a function that could be zero: in sin x cos x = sin x, factor out sin x instead (sin x = 0 or cos x = 1).

## Explicitly not here
Compound-angle identities are S13.

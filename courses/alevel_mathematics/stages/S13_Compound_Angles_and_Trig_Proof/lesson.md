# S13_Compound_Angles_and_Trig_Proof - Lesson: Compound and double angles, R-form, trig proof and context

## Goal
The learner uses compound- and double-angle formulae, knows their geometrical proofs, rewrites a cos x + b sin x in harmonic form, proves identities and applies trig in context.

## Syllabus items taught here
- 1.05l - Double-angle formulae and the compound-angle formulae for sin, cos and tan of (A +/- B)
- 1.05m - Geometrical proofs of the compound-angle formulae
- 1.05n - Expressing a cos x + b sin x as R cos(x +/- alpha) or R sin(x +/- alpha)
- 1.05p - Proofs involving trigonometric functions and identities
- 1.05q - Trigonometric functions in context (vectors, kinematics and forces)

## How to teach this
Ask whether sin(A + B) = sin A + sin B, and test it with A = B = 30°. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.05l Double-angle formulae and the compound-angle formulae for sin, cos and tan of (A +/- B)
sin(A ± B) = sin A cos B ± cos A sin B; cos(A ± B) = cos A cos B ∓ sin A sin B; tan(A ± B) = (tan A ± tan B)/(1 ∓ tan A tan B). Double angle: sin 2A = 2sin A cos A; cos 2A = cos^2 A - sin^2 A = 2cos^2 A - 1 = 1 - 2sin^2 A; tan 2A = 2tan A/(1 - tan^2 A). *Example:* sin 75° = sin(45° + 30°) = (root6 + root2)/4. *Example:* solve sin 2x = cos x for 0 ≤ x < 360°: 2sin x cos x - cos x = 0, cos x(2sin x - 1) = 0, so x = 90°, 270°, 30°, 150°.

#### 1.05m Geometrical proofs of the compound-angle formulae
The standard proof of sin(A + B) uses two right-angled triangles stacked: a triangle with angle A on top of one with angle B, hypotenuse 1. The opposite side of the combined angle is sin A cos B + cos A sin B, read off as the sum of two vertical lengths. cos(A + B) comes from the horizontal lengths. Other formulae follow by replacing B with -B and dividing sin by cos. You should be able to reproduce and explain one such diagram.

#### 1.05n Expressing a cos x + b sin x as R cos(x +/- alpha) or R sin(x +/- alpha)
a cos x + b sin x = R cos(x - α), where R = root(a^2 + b^2) and tan α = b/a (and similarly for R sin(x ± α)). Expand R cos(x - α) = R cos x cos α + R sin x sin α and compare coefficients: R cos α = a, R sin α = b. *Example:* 3cos x + 4sin x = 5cos(x - α) with tan α = 4/3, α = 53.13°. Its maximum is 5 (when x = α) and minimum -5. Solve 3cos x + 4sin x = 2: cos(x - 53.13°) = 0.4, so x - α = 66.42° or 293.58°, giving x = 119.6° or x = 346.7° (the second from x - α = 360° - 66.42°, which keeps x within 0° to 360°).

#### 1.05p Proofs involving trigonometric functions and identities
To prove an identity, start from one side (usually the more complicated) and transform it into the other, one justified step at a time; never work on both sides at once as if it were an equation. *Example:* prove (sin 2θ)/(1 + cos 2θ) = tan θ. LHS = 2sin θ cos θ/(1 + 2cos^2 θ - 1) = 2sin θ cos θ/(2cos^2 θ) = sin θ/cos θ = tan θ = RHS. Useful tactics: write everything in sin and cos, use double-angle forms that cancel the 1s, factorise.

#### 1.05q Trigonometric functions in context (vectors, kinematics and forces)
Trig appears across applied problems: resolving a force F at angle θ gives components F cos θ and F sin θ; a velocity v at angle θ gives horizontal v cos θ and vertical v sin θ; a harmonic form R sin(ωt + α) models tides and oscillations. *Example:* the depth of water is d = 6 + 2.5 sin(πt/6) metres, t hours after midnight: maximum depth 8.5 m when πt/6 = π/2, t = 3 (03:00); the period is 12 hours.

## Explicitly not here
Differentiating trig functions is S16.

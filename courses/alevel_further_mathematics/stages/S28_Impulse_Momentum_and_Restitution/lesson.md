# S28_Impulse_Momentum_and_Restitution - Lesson: Impulse, momentum and restitution

## Goal
The learner applies conservation of momentum and the impulse-momentum principle in one and two dimensions, including variable forces, and uses the coefficient of restitution with Newton's experimental law for direct and oblique impacts.

## Syllabus items taught here
- 6.03a - Linear momentum in one dimension
- 6.03b - Conservation of linear momentum in one dimension for two particles
- 6.03c - Momentum in two dimensions as a vector mv
- 6.03d - Conservation of linear momentum in two dimensions
- 6.03e - The impulse of a force
- 6.03f - Impulse equals change in momentum: I = mv - mu
- 6.03g - The impulse-momentum principle in two dimensions
- 6.03h - Impulse of a constant force (Ft) or a variable force (∫F dt)
- 6.03i - The coefficient of restitution, 0 ≤ e ≤ 1
- 6.03j - Perfectly elastic (e = 1) and inelastic (e = 0) collisions
- 6.03k - Newton's experimental law for direct impact in one dimension
- 6.03l - Newton's experimental law in two dimensions (oblique impact with a surface or sphere)

## How to teach this
Ask why a cricketer draws their hands back when catching a hard ball. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 6.03a Linear momentum in one dimension
Momentum = mass x velocity (N s or kg m/s), with sign for direction in one dimension.

#### 6.03b Conservation of linear momentum in one dimension for two particles
In a collision or explosion with no external impulse, total momentum is conserved: m1u1 + m2u2 = m1v1 + m2v2. If they coalesce, (m1 + m2)v = m1u1 + m2u2.

#### 6.03c Momentum in two dimensions as a vector mv
In two dimensions momentum is the vector mv.

#### 6.03d Conservation of linear momentum in two dimensions
Conserve momentum as a vector (or in each component). *Example:* 2 kg at (3i + j) m/s collides and coalesces with 1 kg at (-i + 4j) m/s: v = (6i + 2j - i + 4j)/3 = (5i + 6j)/3.

#### 6.03e The impulse of a force
Impulse is the effect of a force acting over time: I = Ft for a constant force (N s).

#### 6.03f Impulse equals change in momentum: I = mv - mu
Impulse = change in momentum: I = mv - mu. *Example:* a 0.15 kg ball hits a wall at 20 m/s and rebounds at 15 m/s: impulse = 0.15(15 - (-20)) = 5.25 N s away from the wall.

#### 6.03g The impulse-momentum principle in two dimensions
In 2D, I = mv - mu as vectors. *Example:* a 0.5 kg ball with velocity (8i - 6j) receives an impulse (-6i + 5j) N s: v = (8i - 6j) + 2(-6i + 5j) = (-4i + 4j) m/s.

#### 6.03h Impulse of a constant force (Ft) or a variable force (∫F dt)
Constant force: I = Ft; variable force in one dimension: I = ∫ F dt. *Example:* F = 6t^2 N from t = 0 to 2: I = 16 N s, so a 4 kg particle initially at rest reaches 4 m/s.

#### 6.03i The coefficient of restitution, 0 ≤ e ≤ 1
Coefficient of restitution e = (speed of separation)/(speed of approach), 0 ≤ e ≤ 1.

#### 6.03j Perfectly elastic (e = 1) and inelastic (e = 0) collisions
e = 1: perfectly elastic (no loss of kinetic energy); e = 0: inelastic (the bodies coalesce or move together). Kinetic energy is lost unless e = 1.

#### 6.03k Newton's experimental law for direct impact in one dimension
Newton's experimental law for direct impact: v2 - v1 = -e(u2 - u1). With momentum conservation this gives two equations. *Example:* A (2 kg, 5 m/s) hits B (3 kg, at rest), e = 0.5: 2(5) = 2v1 + 3v2 and v2 - v1 = 2.5: v2 = 3, v1 = 0.5 m/s. KE lost = 25 - (0.25 + 13.5) = 11.25 J. With a fixed wall: rebound speed = e x approach speed.

#### 6.03l Newton's experimental law in two dimensions (oblique impact with a surface or sphere)
Oblique impact with a smooth wall: the velocity component parallel to the wall is unchanged; the perpendicular component is reversed and multiplied by e. *Example:* a ball hits a smooth wall at 10 m/s at 60° to the wall, e = 0.5: parallel 10cos 60° = 5, perpendicular 10sin 60° = 8.66 becomes 4.33, so the speed afterwards is root(25 + 18.75) = 6.61 m/s at arctan(4.33/5) = 40.9° to the wall. Oblique collisions of smooth spheres: components along the line of centres obey the momentum and restitution laws; perpendicular components are unchanged.

## Explicitly not here
Centre of mass is S29.

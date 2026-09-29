# S30_Friction - Lesson: Friction

## Goal
The learner models friction with F ≤ μR, identifies limiting equilibrium, and solves static and dynamic problems on rough horizontal and inclined surfaces.

## Syllabus items taught here
- 3.03r - Frictional force given in vector or component form or as a magnitude
- 3.03s - Contact force between rough surfaces as normal and frictional components
- 3.03t - The coefficient of friction; F <= mu R; limiting friction
- 3.03u - Static and limiting equilibrium on a rough surface
- 3.03v - Motion of a body on a rough surface

## How to teach this
Ask why a box can sit still on a slightly tilted ramp but slides once the ramp is steep enough. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 3.03r Frictional force given in vector or component form or as a magnitude
Friction opposes (potential) sliding, acting along the surface. It may be given as a vector (-2i N), as components, or as a magnitude with a direction. Draw it opposing the motion, or the direction the body would move without it.

#### 3.03s Contact force between rough surfaces as normal and frictional components
The total contact force from a rough surface has two components: the normal reaction R (perpendicular) and friction F (along the surface). The resultant contact force is root(R^2 + F^2).

#### 3.03t The coefficient of friction; F <= mu R; limiting friction
F ≤ μR, where μ is the coefficient of friction. Friction takes whatever value (up to μR) is needed to prevent motion; when the body is on the point of moving (**limiting equilibrium**) or moving, F = μR. *Example:* a 10 kg box on a rough floor with μ = 0.3: the maximum friction is 0.3 × 10g = 29.4 N; a 20 N push doesn't move it (friction is 20 N), a 40 N push gives a = (40 - 29.4)/10 = 1.06 m s^-2.

#### 3.03u Static and limiting equilibrium on a rough surface
On a slope at α, a block of mass m at rest: R = mg cos α; friction up the slope F = mg sin α; it stays at rest if mg sin α ≤ μ mg cos α, i.e. tan α ≤ μ. *Example:* the least force parallel to a rough slope (α = 25°, μ = 0.4) to stop a 6 kg block sliding down: P + μR = mg sin α, P = 6g(sin 25° - 0.4cos 25°) = 3.53 N.

#### 3.03v Motion of a body on a rough surface
When the body moves, F = μR opposite to the motion. *Example:* a 2 kg block slides down a rough slope at 30° with μ = 0.2: a = g(sin 30° - 0.2cos 30°) = 3.20 m s^-2. Pulled up the slope by a force P at an angle to the slope, the normal reaction changes (R = mg cos α - P sin β), so the friction changes too.

## Explicitly not here
Moments are S31.

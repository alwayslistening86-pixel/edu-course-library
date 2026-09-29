# S28_Kinematics_in_2D_and_Projectiles - Lesson: Kinematics in two dimensions and projectiles

## Goal
The learner uses the constant-acceleration formulae and calculus with vectors in two dimensions, models motion under gravity with vectors, and solves projectile problems, stating the model's limitations.

## Syllabus items taught here
- 3.02e - Constant-acceleration formulae in two dimensions using vectors
- 3.02g - Calculus in kinematics in two dimensions using vectors
- 3.02h - Motion under gravity in a vertical plane using vectors
- 3.02i - Projectiles: modelling with constant acceleration and the model's limitations

## How to teach this
Ask why a ball thrown horizontally and one dropped from the same height hit the ground at the same time. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 3.02e Constant-acceleration formulae in two dimensions using vectors
In 2D with constant acceleration: v = u + at, r = r0 + ut + (1/2)at^2, where u, v, a and r are vectors. *Example:* u = (2i + 3j) m/s, a = (i - 2j) m/s^2: after 4 s, v = 6i - 5j, speed root 61; displacement 4u + 8a = 16i - 4j.

#### 3.02g Calculus in kinematics in two dimensions using vectors
r = f(t)i + g(t)j; v = dr/dt = f'(t)i + g'(t)j; a = dv/dt. Integrate the other way, with vector constants. *Example:* r = (t^3 - 3t)i + (4t^2)j: v = (3t^2 - 3)i + 8tj, a = 6ti + 8j. The particle moves parallel to j when the i-component of v is 0: t = 1.

#### 3.02h Motion under gravity in a vertical plane using vectors
Under gravity alone, a = -gj (j vertically upwards), so v = u - gtj and r = ut - (1/2)gt^2 j: the horizontal velocity is constant and the vertical motion is as in S27.

#### 3.02i Projectiles: modelling with constant acceleration and the model's limitations
A projectile launched at speed u at angle θ above horizontal: horizontal x = (u cos θ)t; vertical y = (u sin θ)t - (1/2)gt^2. Time of flight (level ground) 2u sin θ/g; range u^2 sin 2θ/g; greatest height (u sin θ)^2/(2g). *Example:* u = 25 m/s, θ = 35°: time of flight 2.926 s, range 59.9 m, greatest height 10.49 m. The trajectory is a parabola: y = x tan θ - gx^2/(2u^2 cos^2 θ). Limitations: air resistance is ignored, the object is a particle (no spin, no size), and g is constant.

## Explicitly not here
Forces are S29.

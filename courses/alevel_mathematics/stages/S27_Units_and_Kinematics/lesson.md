# S27_Units_and_Kinematics - Lesson: Units and kinematics in a straight line

## Goal
The learner uses SI units, the language and graphs of kinematics, the constant-acceleration formulae (including deriving them), and calculus for straight-line motion.

## Syllabus items taught here
- 3.01a - Fundamental SI quantities and units: length (m), time (s), mass (kg)
- 3.01b - Derived quantities and units: velocity, acceleration, force, weight
- 3.01c - The unit of moment (N m)
- 3.02a - Language of kinematics: position, displacement, distance, velocity, speed, acceleration
- 3.02b - Graphs in kinematics for straight-line motion
- 3.02c - Gradient and area of displacement-time and velocity-time graphs
- 3.02d - The constant-acceleration (suvat) formulae for straight-line motion, including derivation
- 3.02f - Calculus in kinematics for straight-line motion

## How to teach this
Ask what the area under a velocity-time graph represents, and why. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 3.01a Fundamental SI quantities and units: length (m), time (s), mass (kg)
The three fundamental SI quantities in this course are length (metre, m), time (second, s) and mass (kilogram, kg); they are independent of one another. Convert everything to these before calculating: 72 km/h = 72 000 m / 3600 s = 20 m/s.

#### 3.01b Derived quantities and units: velocity, acceleration, force, weight
Derived units: velocity m s^-1; acceleration m s^-2; force newton N = kg m s^-2; weight is a force (N), W = mg. Always attach units to answers.

#### 3.01c The unit of moment (N m)
The moment of a force (force × perpendicular distance) is measured in newton metres, N m (S31).

#### 3.02a Language of kinematics: position, displacement, distance, velocity, speed, acceleration
Position: where the particle is relative to a fixed origin. Displacement: change of position (a vector, with sign). Distance: total length travelled (a scalar). Velocity: rate of change of displacement (vector); speed: its magnitude. Acceleration: rate of change of velocity. *Example:* walking 5 m forward then 3 m back: displacement +2 m, distance 8 m.

#### 3.02b Graphs in kinematics for straight-line motion
Displacement-time and velocity-time graphs describe straight-line motion; sketch them from a description and describe motion from them (at rest, constant velocity, speeding up, slowing down, changing direction).

#### 3.02c Gradient and area of displacement-time and velocity-time graphs
The gradient of a displacement-time graph is velocity. The gradient of a velocity-time graph is acceleration, and the area under it is displacement (area below the axis counts negative). *Example:* a car accelerates from rest to 12 m/s in 8 s, cruises for 20 s, then decelerates to rest in 6 s: acceleration 1.5 m/s^2; distance = (1/2)(8)(12) + 20(12) + (1/2)(6)(12) = 48 + 240 + 36 = 324 m.

#### 3.02d The constant-acceleration (suvat) formulae for straight-line motion, including derivation
For constant acceleration: v = u + at; s = ut + (1/2)at^2; s = (1/2)(u + v)t; v^2 = u^2 + 2as; s = vt - (1/2)at^2. Derive them from the v-t graph (gradient a, area s). List s, u, v, a, t, mark the unknown and the one not needed, and choose the formula. *Example:* a ball thrown up at 14 m/s (g = 9.8): greatest height when v = 0: 0 = 196 - 19.6s, s = 10 m; time to return to the thrower: 0 = 14t - 4.9t^2, t = 20/7 ≈ 2.86 s. Take a positive direction and stick to it.

#### 3.02f Calculus in kinematics for straight-line motion
v = ds/dt, a = dv/dt = d^2s/dt^2; s = ∫v dt, v = ∫a dt (with a constant from initial conditions). Use these when acceleration is not constant. *Example:* v = 3t^2 - 12t + 9: a = 6t - 12; at rest when t = 1 or 3; the distance travelled in 0 ≤ t ≤ 3 is |∫ (0 to 1) v dt| + |∫ (1 to 3) v dt| = 4 + 4 = 8 m (the displacement is 0 m).

## Explicitly not here
Two-dimensional motion is S28.

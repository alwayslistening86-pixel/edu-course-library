# S30_Circular_Motion_and_Variable_Force - Lesson: Circular motion and variable forces

## Goal
The learner uses angular speed and the circular motion formulae, solves horizontal-circle problems (conical pendulums, banked tracks), handles variable-speed and vertical circular motion (including leaving the circle), resolves acceleration radially and tangentially, and solves straight-line motion under variable forces with differential equations.

## Syllabus items taught here
- 6.05a - Angular velocity, velocity, speed and acceleration for circular motion
- 6.05b - v = rω and a = rω^2 = v^2/r for uniform circular motion
- 6.05c - Motion in a horizontal circle (including conical pendulums and banked tracks)
- 6.05d - Circular motion with variable speed, using energy
- 6.05e - Radial and tangential components of acceleration
- 6.05f - Motion in a vertical circle, including leaving the circular path
- 6.06a - Straight-line motion under a variable force, solved by separation or an integrating factor

## How to teach this
Ask why you feel pushed outwards on a roundabout when the real force on you points inwards. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 6.05a Angular velocity, velocity, speed and acceleration for circular motion
Angular velocity ω = dθ/dt (rad/s). Speed v = rω. For uniform circular motion the velocity is tangential and the acceleration points to the centre.

#### 6.05b v = rω and a = rω^2 = v^2/r for uniform circular motion
a = rω^2 = v^2/r towards the centre; the resultant inward force is mv^2/r = mrω^2. *Example:* a 0.2 kg mass on a 0.5 m string whirled at 4 rad/s on a smooth table: tension 0.2 x 0.5 x 16 = 1.6 N.

#### 6.05c Motion in a horizontal circle (including conical pendulums and banked tracks)
**Conical pendulum:** string at angle θ to the vertical: T cos θ = mg, T sin θ = mrω^2 (r = l sin θ), so ω^2 = g/(l cos θ). **Banked track** at angle α with no friction: tan α = v^2/(rg). With friction, include it along the slope (up or down depending on whether the car is too slow or too fast). *Example:* the speed for no sideways friction on a track banked at 15° with radius 50 m: v = root(50 x 9.8 tan 15°) = 11.46 m/s.

#### 6.05d Circular motion with variable speed, using energy
In a vertical circle speed changes; use energy conservation to find speed at any point, then F = mv^2/r radially for tension or reaction. *Example:* a particle on a light rod of length 1 m released from rest horizontally: at the bottom, v^2 = 2g x 1 = 19.6.

#### 6.05e Radial and tangential components of acceleration
With variable speed, acceleration has a radial component v^2/r (towards the centre) and a tangential component dv/dt = rθ''. Resolve forces in both directions.

#### 6.05f Motion in a vertical circle, including leaving the circular path
For a particle on a string (or on the inside of a surface), it leaves the circle when the tension (or reaction) becomes zero; it then moves as a projectile. On a rod (or a bead on a wire) it can't leave, so it completes the circle if its speed at the top is ≥ 0; on a string it needs v^2 ≥ gr at the top. *Example:* a particle slides from rest at the top of a smooth sphere of radius a: it leaves when cos θ = 2/3 (θ measured from the vertical).

#### 6.06a Straight-line motion under a variable force, solved by separation or an integrating factor
F = ma with a = dv/dt or v dv/dx, where F depends on t, v or x; solve by separating variables or an integrating factor. *Example:* a 2 kg boat decelerates under a resistance of 4v N: 2 dv/dt = -4v, v = v0 e^(-2t). Using v dv/dx: 2v dv/dx = -4v, so v = v0 - 2x, and it travels v0/2 m before stopping (in infinite time). *Example:* resistance kv^2: m v dv/dx = -kv^2 gives v = v0 e^(-kx/m).

## Explicitly not here
This is the final content stage; the mock exam follows.

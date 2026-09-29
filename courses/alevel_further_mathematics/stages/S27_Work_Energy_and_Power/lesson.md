# S27_Work_Energy_and_Power - Lesson: Work, energy and power

## Goal
The learner calculates work done by constant and variable forces, kinetic, gravitational and elastic potential energy, applies the work-energy principle and conservation of energy (including elastic strings and springs), and uses power, including P = Fv.

## Syllabus items taught here
- 6.02a - The concept of work done by a force
- 6.02b - Work done by a constant force
- 6.02c - Work done by a constant force using vectors (F.x) or by a variable force ∫F dx
- 6.02d - Mechanical energy
- 6.02e - Gravitational potential energy mgh and kinetic energy (1/2)mv^2
- 6.02f - Kinetic energy with the scalar product (1/2)m v.v
- 6.02g - Hooke's law T = λx/l for elastic strings and springs
- 6.02h - Elastic potential energy λx^2/(2l)
- 6.02i - Conservation of mechanical energy and the work-energy principle
- 6.02j - Energy principles with elastic strings and springs
- 6.02k - Power as the rate of doing work
- 6.02l - Power, tractive force and velocity: P = Fv
- 6.02m - Power for a variable force in two dimensions: P = F.v

## How to teach this
Ask why a car climbing a hill at constant speed still needs its engine working. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 6.02a The concept of work done by a force
Work is done when a force moves its point of application in the direction of the force. It transfers energy and is measured in joules (J).

#### 6.02b Work done by a constant force
Work = force x distance moved in the direction of the force = Fd cos θ. Work done against gravity lifting mass m through height h: mgh. Work against friction: μR x d.

#### 6.02c Work done by a constant force using vectors (F.x) or by a variable force ∫F dx
In vectors, work = F.d. For a variable force in one dimension, W = ∫ F dx. *Example:* F = (3i + 4j) N moving the particle from (1, 0) to (4, 2): W = (3, 4).(3, 2) = 17 J. A spring force F = kx stretched from 0 to a: W = ka^2/2.

#### 6.02d Mechanical energy
Mechanical energy = kinetic energy + potential energies (gravitational, elastic). Energy is a scalar.

#### 6.02e Gravitational potential energy mgh and kinetic energy (1/2)mv^2
KE = (1/2)mv^2; GPE = mgh relative to a chosen level (only changes matter).

#### 6.02f Kinetic energy with the scalar product (1/2)m v.v
With velocity vectors: KE = (1/2)m v.v. *Example:* m = 2 kg, v = (3i - 4j) m/s: KE = (1/2)(2)(9 + 16) = 25 J. Also v.v = u.u + 2a.x for constant acceleration.

#### 6.02g Hooke's law T = λx/l for elastic strings and springs
Hooke's law: the tension in an elastic string or spring is T = λx/l, where λ is the modulus of elasticity (N), l the natural length and x the extension (compression for springs). A string goes slack when x ≤ 0; a spring can be compressed.

#### 6.02h Elastic potential energy λx^2/(2l)
Elastic potential energy stored = λx^2/(2l) (the area under the tension-extension graph).

#### 6.02i Conservation of mechanical energy and the work-energy principle
Work-energy principle: work done by non-conservative forces (engines, friction, resistance) = change in total mechanical energy. If only gravity (and elastic forces) do work, mechanical energy is conserved. *Example:* a 2 kg block slides 5 m down a rough slope at 30° (μ = 0.2) from rest: loss of GPE = 2g(5 sin 30°) = 49 J; work against friction = 0.2 x 2g cos 30° x 5 = 16.97 J; KE gained = 32.03 J, so v = 5.66 m/s.

#### 6.02j Energy principles with elastic strings and springs
Include elastic potential energy in the energy equation. *Example:* a 0.5 kg particle is attached to one end of a light elastic string of natural length 1 m and modulus 20 N, the other end fixed at O. It is released from rest at O. At its lowest point, with extension e, all the GPE lost has become EPE: 0.5g(1 + e) = 20e^2/2, so 10e^2 - 4.9e - 4.9 = 0 and e = 0.987 m. Its greatest speed occurs where the tension equals the weight (e = 0.245 m), not where the string becomes taut.

#### 6.02k Power as the rate of doing work
Power is the rate of doing work: P = dW/dt, in watts (J/s).

#### 6.02l Power, tractive force and velocity: P = Fv
P = Fv, where F is the driving (tractive) force. At maximum speed on a level road, the driving force equals the resistance. *Example:* a 1200 kg car's engine works at 30 kW against 800 N resistance: maximum speed 37.5 m/s; at 20 m/s, driving force 1500 N and a = 700/1200 = 0.583 m s^-2. Up a slope, include mg sin α.

#### 6.02m Power for a variable force in two dimensions: P = F.v
In two dimensions with a variable force, P = F.v. *Example:* F = (2t i + 3j) N, v = (i + t j) m/s: P = 2t + 3t = 5t W.

## Explicitly not here
Momentum and impulse are S28.

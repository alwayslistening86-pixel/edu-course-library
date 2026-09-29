# S31_Moments - Lesson: Moments

## Goal
The learner calculates moments about a point, applies the equilibrium conditions to rigid bodies, and solves beam, rod and ladder problems.

## Syllabus items taught here
- 3.04a - Moment of a force about a point
- 3.04b - Rigid body in equilibrium: resultant force and resultant moment are zero
- 3.04c - Moments in simple static contexts (beams, rods, ladders)

## How to teach this
Ask why it's easier to open a door by pushing near the handle than near the hinge. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 3.04a Moment of a force about a point
The moment of a force about a point = magnitude of the force × perpendicular distance from the point to the line of action (N m), clockwise or anticlockwise. For a force at an angle, use the perpendicular distance, or resolve the force and take the perpendicular component. *Example:* a 20 N force at 60° to a rod, 3 m from the pivot: moment 20 sin 60° x 3 = 52.0 N m.

#### 3.04b Rigid body in equilibrium: resultant force and resultant moment are zero
A rigid body is in equilibrium when the resultant force is zero (resolve in two directions) **and** the resultant moment about any point is zero. Take moments about a point where an unknown force acts, to eliminate it.

#### 3.04c Moments in simple static contexts (beams, rods, ladders)
*Beam:* a uniform 6 m plank of mass 20 kg rests on supports at A (1 m from one end) and B (1.5 m from the other end); a 50 kg person stands 2 m from that first end. Moments about A: R_B × 3.5 = 20g × 2 + 50g × 1, so R_B = 90g/3.5 = 252 N; resolving: R_A = 70g - 252 = 434 N. On the point of tipping about a support, the reaction at the other support is zero. *Ladder:* a uniform ladder against a smooth wall on rough ground: take moments about the foot; friction at the ground balances the wall's reaction. A non-uniform rod has its centre of mass not at the midpoint.

## Explicitly not here
This is the final content stage; the mock exam follows.

# S29_Forces_and_Newtons_Laws - Lesson: Forces and Newton's laws

## Goal
The learner models forces as vectors, applies Newton's three laws in one and two dimensions (resolving where needed), uses weight, normal reaction and smooth contacts, and solves equilibrium and connected-particle problems including pulleys and resultants.

## Syllabus items taught here
- 3.03a - Force and its vector nature
- 3.03b - Newton's first law
- 3.03c - Newton's second law F = ma in a straight line
- 3.03d - Newton's second law with forces given as 2D vectors
- 3.03e - Newton's second law with resolving forces in two dimensions
- 3.03f - Weight and motion in a straight line under gravity
- 3.03g - Gravitational acceleration g and its value to different accuracies
- 3.03h - Newton's third law
- 3.03i - Normal reaction force
- 3.03j - The 'smooth' model and its limitations
- 3.03k - Connected particles in a straight line; equilibrium; light inextensible strings and smooth pulleys
- 3.03l - Newton's third law where forces need resolving (two dimensions)
- 3.03m - Equilibrium: resolved parts in any direction sum to zero
- 3.03n - Equilibrium of forces on a particle in two dimensions, including connected particles
- 3.03o - Resolving forces for connected particles and smooth pulleys
- 3.03p - Resultant of two or more forces at a point
- 3.03q - Dynamics of a particle moving in a plane under forces

## How to teach this
Ask a learner to draw every force on a book resting on a table, and which force is the 'reaction' to its weight in Newton's third law. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 3.03a Force and its vector nature
A force has magnitude and direction (a vector), measured in newtons. Draw a force diagram with every force acting on the object, labelled.

#### 3.03b Newton's first law
Newton's first law: a body stays at rest or moves with constant velocity unless a resultant force acts on it. So constant velocity means the forces balance (equilibrium).

#### 3.03c Newton's second law F = ma in a straight line
Newton's second law: resultant force = mass × acceleration, F = ma, in the direction of the acceleration. *Example:* a 1200 kg car with driving force 3000 N and resistance 600 N: a = 2400/1200 = 2 m s^-2.

#### 3.03d Newton's second law with forces given as 2D vectors
With forces as vectors, F = ma component-wise. *Example:* forces (3i + 2j) N and (5i - 8j) N act on a 2 kg particle: resultant 8i - 6j, a = 4i - 3j, magnitude 5 m s^-2.

#### 3.03e Newton's second law with resolving forces in two dimensions
Resolve each force into components parallel and perpendicular to the motion and apply F = ma along the motion. *Example:* a 5 kg box pulled along a smooth floor by 20 N at 30° above horizontal: a = 20cos 30°/5 = 3.46 m s^-2; the normal reaction R = 5g - 20sin 30° = 39 N.

#### 3.03f Weight and motion in a straight line under gravity
Weight W = mg acts vertically down through the centre of mass. A body falling freely has a = g. A lift problem: for a 70 kg person in a lift accelerating upwards at 1.5 m s^-2, R - 70g = 70 × 1.5, so R = 791 N.

#### 3.03g Gravitational acceleration g and its value to different accuracies
g is the acceleration due to gravity, taken as 9.8 m s^-2 (OCR's default); 9.81 or 10 may be specified. Give answers to an accuracy consistent with g (usually 2 or 3 significant figures).

#### 3.03h Newton's third law
Newton's third law: if A exerts a force on B, B exerts an equal and opposite force on A (of the same type). The weight of a book and the table's reaction on it are *not* a third-law pair; the third-law partner of the table's push on the book is the book's push on the table.

#### 3.03i Normal reaction force
The normal reaction acts perpendicular to the surface of contact, away from the surface. It is not always equal to the weight: on a slope at angle α it is mg cos α (if nothing else acts perpendicular to the slope); it changes if other forces push or pull at an angle.

#### 3.03j The 'smooth' model and its limitations
A smooth surface exerts no friction: the contact force is only normal. A light string has no mass (tension the same throughout); an inextensible string means connected particles share the same acceleration; a smooth pulley doesn't change the tension. Limitations: real strings stretch, real pulleys have friction and mass.

#### 3.03k Connected particles in a straight line; equilibrium; light inextensible strings and smooth pulleys
Connected particles in a straight line: write F = ma for each particle separately (or for the whole system when finding the acceleration). *Example:* a 900 kg car tows a 300 kg trailer with a driving force of 2400 N, resistances 300 N (car) and 100 N (trailer): whole system: 2400 - 400 = 1200a, a = 1.67 m s^-2; trailer: T - 100 = 300a, T = 600 N. Pulley problems: 5 kg and 3 kg masses over a smooth pulley: 5g - T = 5a and T - 3g = 3a give a = 2g/8 = 2.45 m s^-2, T = 36.75 N.

#### 3.03l Newton's third law where forces need resolving (two dimensions)
Newton's third law with resolved forces: at a tow bar at an angle, the force on the car and the force on the trailer are equal and opposite, and each can be resolved into components; apply F = ma to each body using its components.

#### 3.03m Equilibrium: resolved parts in any direction sum to zero
A particle is in equilibrium if and only if the sum of the resolved parts of the forces in any direction is zero. Resolve in two perpendicular directions (horizontal and vertical, or along and perpendicular to a slope) and set each sum to zero.

#### 3.03n Equilibrium of forces on a particle in two dimensions, including connected particles
*Example:* a 4 kg mass hangs from two strings at 30° and 45° to the horizontal. Horizontally T1 cos 30° = T2 cos 45°; vertically T1 sin 30° + T2 sin 45° = 4g. Solving gives T1 = 28.7 N and T2 = 35.1 N. Alternatively use a triangle of forces with the sine rule.

#### 3.03o Resolving forces for connected particles and smooth pulleys
Harder pulleys: a particle on a smooth slope connected over a pulley to a hanging mass. *Example:* a 4 kg block on a smooth slope at 30°, attached to a hanging 3 kg mass: 3g - T = 3a; T - 4g sin 30° = 4a; adding gives 3g - 2g = 7a, so a = 1.4 m s^-2 and T = 25.2 N. The force on the pulley is the resultant of the two tensions.

#### 3.03p Resultant of two or more forces at a point
The resultant of several forces at a point is their vector sum. Find it by resolving: R_x = Σ F cos θ, R_y = Σ F sin θ; |R| = root(R_x^2 + R_y^2), direction arctan(R_y/R_x). *Example:* 10 N east and 6 N at 60° north of east: R = (13, 5.196), |R| = 14.0 N at 21.8° north of east.

#### 3.03q Dynamics of a particle moving in a plane under forces
Combine resolving with F = ma in a plane. *Example:* forces (4i + 6j) N and (2i - 2j) N act on a 2 kg particle starting from rest: a = 3i + 2j, and after 3 s its velocity is 9i + 6j m/s (speed 10.8 m/s).

## Explicitly not here
Friction is S30.

# S29_Centre_of_Mass - Lesson: Centre of mass

## Goal
The learner locates centres of mass by symmetry, for systems of particles and composite bodies, and by integration for laminas and solids of revolution, and solves equilibrium problems for rigid bodies including suspension and toppling.

## Syllabus items taught here
- 6.04a - Weight acting at the centre of mass
- 6.04b - Centre of mass of uniform bodies by symmetry
- 6.04c - Centre of mass of systems of particles and composite bodies
- 6.04d - Centre of mass of uniform laminas and solids of revolution by integration
- 6.04e - Equilibrium of a rigid body under coplanar forces, including suspension and toppling

## How to teach this
Ask where you'd have to hold an L-shaped piece of card to balance it on one finger. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 6.04a Weight acting at the centre of mass
The weight of a body acts as a single force at its centre of mass.

#### 6.04b Centre of mass of uniform bodies by symmetry
Uniform bodies: use symmetry (rectangle: the centre; circle: the centre). Standard results from the formula booklet: triangle: 2/3 of the way from vertex to the midpoint of the opposite side (the mean of the vertices); semicircular lamina: 4r/(3π) from the diameter; solid hemisphere: 3r/8; solid cone: h/4 from the base.

#### 6.04c Centre of mass of systems of particles and composite bodies
Σm x̄ = Σ(m_i x_i) (and likewise for y). *Example:* masses 2, 3, 5 kg at (1, 0), (4, 2), (0, 3): x̄ = (2 + 12 + 0)/10 = 1.4, ȳ = (0 + 6 + 15)/10 = 2.1. Composite laminas: use areas as masses; subtract removed parts (negative mass).

#### 6.04d Centre of mass of uniform laminas and solids of revolution by integration
Uniform lamina under y = f(x) from a to b: x̄ = ∫xy dx / ∫y dx and ȳ = ∫(1/2)y^2 dx / ∫y dx. Solid of revolution about the x-axis: x̄ = ∫πxy^2 dx / ∫πy^2 dx. *Example:* the lamina under y = x^2 from x = 0 to 2 has area 8/3; x̄ = (∫x^3 dx)/(8/3) = 4 ÷ (8/3) = 3/2 and ȳ = (∫x^4/2 dx)/(8/3) = (16/5) ÷ (8/3) = 6/5. *Example:* a solid cone formed by rotating y = rx/h about the x-axis (0 ≤ x ≤ h) has x̄ = 3h/4 from the vertex, i.e. h/4 from the base.

#### 6.04e Equilibrium of a rigid body under coplanar forces, including suspension and toppling
Equilibrium of a rigid body: resultant force zero and resultant moment zero about any point. A body **suspended** freely from a point hangs with its centre of mass vertically below that point: find the angle using the centre of mass's position. A body on an inclined plane **topples** if the vertical through its centre of mass falls outside the base (before it would slide if friction is large enough). Compare tan α with μ (sliding) and with (half base width)/(height of G) (toppling).

## Explicitly not here
Circular motion is S30.

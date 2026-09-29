# S08_Systems_of_Equations_and_Planes - Lesson: Systems of equations and their geometry

## Goal
The learner decides whether a linear system with no unique solution is consistent or inconsistent, and interprets three equations geometrically as arrangements of three planes.

## Syllabus items taught here
- 4.03s - Consistency: infinitely many or no solutions when no unique solution exists
- 4.03t - Geometrical interpretation of three linear equations as three planes

## How to teach this
Ask how three sheets of paper can be arranged so that they share no common point. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.03s Consistency: infinitely many or no solutions when no unique solution exists
If det M = 0 the system Mx = b has no unique solution. Eliminate to test: if you reach a true statement such as 0 = 0 the equations are **consistent** (infinitely many solutions); a contradiction such as 0 = 5 means **inconsistent** (no solutions). *Example:* x + y + z = 3, 2x + y - z = 1, 3x + 2y = k: adding the first two gives 3x + 2y = 4, so the system is consistent only when k = 4. (Finding the full solution set in the infinite case is not required.)

#### 4.03t Geometrical interpretation of three linear equations as three planes
Three planes: unique solution: meet at a single point (det ≠ 0). det = 0 and consistent: a **sheaf** (all three contain a common line) or all three coincide. det = 0 and inconsistent: a **prism** (planes meet in pairs in three parallel lines), or two (or three) parallel planes. Tell them apart by looking at normals: parallel normals mean parallel planes. In the example above with k ≠ 4, no two normals are parallel, so the planes form a prism.

## Explicitly not here
Lines and planes in vector form are S09.

# S08_Parametric_Equations - Lesson: Parametric equations

## Goal
The learner converts between parametric and cartesian forms, sketches parametric curves over given parameter ranges, and uses parametric equations in modelling.

## Syllabus items taught here
- 1.03g - Parametric equations: converting between cartesian and parametric forms
- 1.03h - Parametric equations in modelling

## How to teach this
Ask how x = 3cos t, y = 3sin t can describe a circle when neither equation mentions the other variable. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.03g Parametric equations: converting between cartesian and parametric forms
A curve can be given as x = f(t), y = g(t) for a parameter t. To convert to cartesian form, eliminate t: make t the subject of one equation and substitute, or use an identity. *Example:* x = t + 1, y = t^2: t = x - 1, so y = (x - 1)^2. *Example:* x = 3cos t, y = 3sin t: cos^2 t + sin^2 t = 1 gives x^2 + y^2 = 9. *Example:* x = 2 + sec t, y = tan t: sec^2 t - tan^2 t = 1 gives (x - 2)^2 - y^2 = 1. The parameter range restricts the curve: x = t^2, y = 2t for t ≥ 0 is only the upper half of y^2 = 4x. Find where a parametric curve meets a line by substituting x(t) and y(t) into the line's equation and solving for t.

#### 1.03h Parametric equations in modelling
Parametric equations model motion naturally, with t as time: x and y give horizontal and vertical position. *Example:* a ball's position is x = 12t, y = 16t - 5t^2 (metres). It lands when y = 0: t = 3.2 s, at x = 38.4 m. Maximum height when t = 1.6: y = 12.8 m. Converting: t = x/12, so y = (4/3)x - (5/144)x^2. Comment on the domain of validity (0 ≤ t ≤ 3.2) and assumptions (no air resistance). Related rates of change use dy/dx = (dy/dt)/(dx/dt) (S16).

## Explicitly not here
Parametric differentiation is S16.

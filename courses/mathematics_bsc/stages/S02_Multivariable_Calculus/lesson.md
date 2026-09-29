# S02_Multivariable_Calculus - Lesson: Multivariable calculus

## Goal
The learner computes partial derivatives and directional derivatives, finds and classifies stationary points of two-variable functions, applies the multivariable chain rule and implicit differentiation, and solves constrained optimisation problems with Lagrange multipliers.

## Syllabus items taught here
- 2a - Partial derivatives, the gradient vector and directional derivatives
- 2b - Stationary points of functions of two variables; classification via the Hessian/second-derivative test
- 2c - The multivariable chain rule and implicit differentiation
- 2d - Lagrange multipliers for constrained optimisation

## How to teach this
Ask how the slope of a hillside depends on which direction you walk, before defining the directional derivative. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 2a Partial derivatives, the gradient vector and directional derivatives
For f(x,y), the partial derivative f_x = df/dx treats y as constant (and symmetrically for f_y). The **gradient vector** grad f = (f_x, f_y) points in the direction of steepest ascent, with magnitude equal to the maximum rate of increase. The **directional derivative** of f at a point in the direction of a unit vector u is grad f . u (the dot product). *Example:* for f(x,y) = x^2 y + e^y, f_x = 2xy, f_y = x^2 + e^y; at (1,0), grad f = (0, 2), so f increases fastest in the direction (0,1), and the directional derivative towards (1,1)/root2 is (0,2).(1,1)/root2 = 2/root2 = root2.

#### 2b Stationary points of functions of two variables; classification via the Hessian/second-derivative test
A stationary point of f(x,y) has f_x = f_y = 0. Classify it using the **Hessian determinant** D = f_xx f_yy - (f_xy)^2 at that point: if D > 0 and f_xx > 0, a local minimum; if D > 0 and f_xx < 0, a local maximum; if D < 0, a saddle point; if D = 0, the test is inconclusive. *Example:* f(x,y) = x^3 - 3x + y^2 has f_x = 3x^2 - 3, f_y = 2y; solving simultaneously gives stationary points at ['(-1, 0)', '(1, 0)']. With f_xx = 6x, f_yy = 2, f_xy = 0: at (1,0), D = (6)(2) - 0 = 12 > 0 and f_xx = 6 > 0, a local minimum; at (-1,0), D = (-6)(2) - 0 = -12 < 0, a saddle point.

#### 2c The multivariable chain rule and implicit differentiation
The multivariable chain rule: if z = f(x,y) with x = x(t), y = y(t), then dz/dt = f_x (dx/dt) + f_y (dy/dt). More generally, for z = f(x,y) with x = x(u,v), y = y(u,v): dz/du = f_x x_u + f_y y_u. **Implicit differentiation**: if F(x,y) = 0 defines y as a function of x, then dy/dx = -F_x/F_y (found by differentiating F(x,y)=0 with respect to x and solving). *Example:* for x^2 + xy + y^2 = 7, F_x = 2x+y, F_y = x+2y, so dy/dx = -(2x+y)/(x+2y); at (2,1), dy/dx = -5/4.

#### 2d Lagrange multipliers for constrained optimisation
To optimise f(x,y) subject to a constraint g(x,y) = c, **Lagrange multipliers** solve grad f = lambda grad g together with g(x,y) = c: at an extremum, the gradients of f and g are parallel. *Example:* maximise f(x,y) = xy subject to x + y = 10. grad f = (y,x), grad g = (1,1), so y = lambda, x = lambda, giving x = y; with x+y=10, x=y=5, and f(5,5) = 25 is the maximum (by the constraint being a closed bounded curve segment / checking endpoints give smaller products, this is confirmed a maximum).

## Explicitly not here
Constrained optimisation in higher dimensions and inequality constraints (KKT conditions) are beyond this stage's scope.

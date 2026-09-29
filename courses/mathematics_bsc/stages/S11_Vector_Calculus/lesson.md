# S11_Vector_Calculus - Lesson: Vector calculus

## Goal
The learner computes grad/div/curl, evaluates line integrals of scalar and vector fields, evaluates surface integrals and flux, and applies the Divergence Theorem, Green's Theorem and Stokes' Theorem.

## Syllabus items taught here
- 11a - Scalar and vector fields; grad, div and curl
- 11b - Line integrals of scalar and vector fields; work done by a force field
- 11c - Surface integrals and flux; the Divergence Theorem
- 11d - Green's Theorem and Stokes' Theorem

## How to teach this
Ask what 'curl' physically means for a vector field describing water flow -- whether a small paddle wheel placed in the flow would spin -- before defining it formally. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 11a Scalar and vector fields; grad, div and curl
For scalar field f, **grad f** = (df/dx, df/dy, df/dz), pointing in the direction of steepest increase. For vector field F=(F1,F2,F3), **div F** = dF1/dx + dF2/dy + dF3/dz (a scalar, measuring net outward flux density -- source/sink strength). **curl F** = (dF3/dy - dF2/dz, dF1/dz - dF3/dx, dF2/dx - dF1/dy) (a vector, measuring local rotation). *Example:* F=(x^2,y^2,z^2) has div F = 2x + 2y + 2z = 2(x+y+z) (verified with sympy); F=(y,-x,0) (a rotational field) has curl F = Matrix([
[ 0],
[ 0],
[-2]]), i.e. (0,0,-2), confirming this field rotates (clockwise, viewed from +z) with constant angular rate.

#### 11b Line integrals of scalar and vector fields; work done by a force field
A **line integral** of a scalar field f along curve C parametrised by r(t), t in [a,b], is integral_a^b f(r(t)) |r'(t)| dt. For a vector field F, the line integral (work integral) is integral_C F.dr = integral_a^b F(r(t)).r'(t) dt. *Example:* the work done by F=(y,x) moving along r(t)=(cos t, sin t), t in [0,pi/2] (quarter circle): F(r(t)).r'(t) = (sin t)(-sin t) + (cos t)(cos t) = cos(2t); integral_0^{pi/2} cos(2t) dt = [sin(2t)/2]_0^{pi/2} = 0.

#### 11c Surface integrals and flux; the Divergence Theorem
A **surface integral** of a scalar field over surface S is integral_S f dS; **flux** of a vector field through S is integral_S F.n dS (n the outward unit normal). The **Divergence Theorem**: for a closed surface S bounding solid region V, integral_S F.n dS = integral_V div F dV (flux out of a closed surface equals the volume integral of the divergence inside). *Example:* for F=(x,y,z) (div F = 3) through the sphere of radius R centred at the origin: by the Divergence Theorem, flux = integral_V 3 dV = 3(4/3)pi R^3 = 4 pi R^3 -- far easier than a direct surface computation.

#### 11d Green's Theorem and Stokes' Theorem
**Green's Theorem** (in the plane): for a simple closed curve C bounding region D, integral_C (P dx + Q dy) = integral_D (dQ/dx - dP/dy) dA -- a 2D special case relating a line integral round the boundary to a double integral of a 'curl-like' quantity inside. **Stokes' Theorem** (3D): for a surface S with boundary curve C, integral_C F.dr = integral_S (curl F).n dS -- the circulation round the boundary equals the flux of the curl through any surface spanning it. *Example:* for F=(-y,x) round the unit circle (Green's): dQ/dx-dP/dy = 1-(-1)=2, so the line integral equals integral_D 2 dA = 2(pi) = 2pi, matching a direct parametric computation of integral_C (-y dx + x dy) round the unit circle.

## Explicitly not here
Curvilinear coordinate systems (cylindrical, spherical) applied to these theorems are covered at the level of worked examples only, not derived from first principles here.

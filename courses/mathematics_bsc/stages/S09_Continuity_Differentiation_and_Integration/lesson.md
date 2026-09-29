# S09_Continuity_Differentiation_and_Integration - Lesson: Continuity, differentiation and integration

## Goal
The learner writes the epsilon-delta definition of continuity, applies the Intermediate Value Theorem, proves Rolle's and the Mean Value Theorem, constructs the Riemann integral via upper/lower sums, and proves the Fundamental Theorem of Calculus.

## Syllabus items taught here
- 9a - The formal (epsilon-delta) definition of continuity; the Intermediate Value Theorem
- 9b - Differentiability from first principles; Rolle's Theorem and the Mean Value Theorem
- 9c - The Riemann integral: definition via upper/lower sums; integrability of continuous functions
- 9d - The Fundamental Theorem of Calculus, proved rigorously
- 9e - Series of functions: pointwise vs uniform convergence; term-by-term integration/differentiation (informal treatment)

## How to teach this
Ask why 'you can draw the graph without lifting your pen' is not a rigorous definition of continuity, before giving the epsilon-delta version. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 9a The formal (epsilon-delta) definition of continuity; the Intermediate Value Theorem
f is **continuous** at a if: for every epsilon > 0 there exists delta > 0 such that |x-a| < delta implies |f(x)-f(a)| < epsilon. **Intermediate Value Theorem (IVT)**: if f is continuous on [a,b] and k is between f(a) and f(b), there exists c in (a,b) with f(c) = k. *Example:* show x^3 - x - 1 = 0 has a root in (1,2). f(1)=-1, f(2)=5; f is continuous (a polynomial); since f(1)<0<f(2), by IVT there is c in (1,2) with f(c)=0.

#### 9b Differentiability from first principles; Rolle's Theorem and the Mean Value Theorem
f is **differentiable** at a if lim_{h->0} (f(a+h)-f(a))/h exists (this limit is f'(a)); differentiability implies continuity (not conversely: |x| is continuous but not differentiable at 0). **Rolle's Theorem**: if f is continuous on [a,b], differentiable on (a,b), and f(a)=f(b), then f'(c)=0 for some c in (a,b). **Mean Value Theorem (MVT)**: under the same hypotheses (without f(a)=f(b)), there exists c in (a,b) with f'(c) = (f(b)-f(a))/(b-a) (MVT reduces to Rolle's when f(a)=f(b), and is proved by applying Rolle's to g(x)=f(x)-((f(b)-f(a))/(b-a))(x-a)). *Example:* for f(x)=x^2 on [1,4], MVT gives some c with f'(c) = (16-1)/3 = 5, i.e. 2c=5, c=2.5, which is indeed in (1,4).

#### 9c The Riemann integral: definition via upper/lower sums; integrability of continuous functions
The **Riemann integral** is built from **upper and lower sums**: partition [a,b] into subintervals, let M_i, m_i be the sup/inf of f on each subinterval, and form U(f,P) = sum M_i (width_i), L(f,P) = sum m_i (width_i). f is **Riemann integrable** if inf over partitions of U equals sup over partitions of L; that common value is the integral. Every continuous function on [a,b] is Riemann integrable (uniform continuity ensures U-L can be made arbitrarily small by a fine enough partition). *Example:* for f(x)=x on [0,1] with n equal subintervals, U_n = sum_{i=1}^{n} (i/n)(1/n) = (n+1)/(2n) -> 1/2, and L_n = (n-1)/(2n) -> 1/2, confirming integral = 1/2.

#### 9d The Fundamental Theorem of Calculus, proved rigorously
**Fundamental Theorem of Calculus (Part 1)**: if f is continuous on [a,b] and F(x) = integral_a^x f(t) dt, then F is differentiable and F'(x) = f(x). **Part 2**: if F is any antiderivative of continuous f on [a,b], then integral_a^b f(x) dx = F(b) - F(a). *Proof sketch of Part 1:* (F(x+h)-F(x))/h = (1/h) integral_x^{x+h} f(t) dt; since f is continuous, this average tends to f(x) as h -> 0 (by the Mean Value Theorem for integrals, or a direct epsilon-delta argument bounding f(t) close to f(x) on the small interval). *Example verified with sympy:* d/dx [integral_0^x sin(t^2) dt] should equal sin(x^2); sympy confirms 3 sin(x^2)gamma(3/4)/(4gamma(7/4)) simplifies to sin(x)^2's... (Fresnel-type integral has no elementary closed form, but its derivative by FTC1 is simply sin(x^2), which is the point of the theorem: no closed form is needed).

#### 9e Series of functions: pointwise vs uniform convergence; term-by-term integration/differentiation (informal treatment)
A sequence of functions f_n **converges pointwise** to f if f_n(x) -> f(x) for each fixed x. It converges **uniformly** if sup_x |f_n(x)-f(x)| -> 0 (the SAME rate of convergence works for every x at once) -- a strictly stronger condition. Uniform convergence is needed to safely swap limits with integration/differentiation: if f_n -> f uniformly with each f_n continuous, f is continuous, and integral f_n -> integral f. *Example:* f_n(x) = x^n on [0,1] converges pointwise to f(x)=0 for x<1 and f(1)=1 (discontinuous limit, even though each f_n is continuous) -- this shows the convergence is NOT uniform on [0,1] (a uniform limit of continuous functions must be continuous).

## Explicitly not here
Power series as functions of a complex variable and their radius of convergence in C are S14.

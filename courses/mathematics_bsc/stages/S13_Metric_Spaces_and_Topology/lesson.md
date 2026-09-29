# S13_Metric_Spaces_and_Topology - Lesson: Metric spaces and topology

## Goal
The learner verifies the metric axioms for standard examples, determines whether sets are open/closed and finds interior/closure/boundary, proves continuity via the general metric-space definition, and reasons about compactness and completeness.

## Syllabus items taught here
- 13a - Metric spaces: definition, examples (Euclidean, discrete, sup-norm on C[a,b]) and metrics induced by a norm
- 13b - Open and closed sets; interior, closure and boundary in a metric space
- 13c - Convergence and continuity in a general metric space; equivalence with sequential continuity
- 13d - Compactness and completeness in a metric space; a continuous image of a compact set is compact

## How to teach this
Ask what 'distance' should mean for two continuous functions, not just two points in the plane -- motivating the sup-norm metric on C[a,b]. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 13a Metric spaces: definition, examples (Euclidean, discrete, sup-norm on C[a,b]) and metrics induced by a norm
A **metric** d on a set X satisfies: d(x,y)>=0 with equality iff x=y; d(x,y)=d(y,x); and the **triangle inequality** d(x,z)<=d(x,y)+d(y,z). *Examples:* the **Euclidean metric** on R^n, d(x,y)=root(sum(x_i-y_i)^2); the **discrete metric** on any set, d(x,y)=0 if x=y, 1 otherwise (satisfies all three axioms trivially, giving a very different topology); the **sup-norm metric** on C[a,b] (continuous functions), d(f,g) = sup_{x in [a,b]} |f(x)-g(x)|, measuring the largest vertical gap between two graphs. A metric induced by a norm ||.|| is d(x,y)=||x-y||; the Euclidean and sup-norm metrics both arise this way.

#### 13b Open and closed sets; interior, closure and boundary in a metric space
A set U is **open** if every point of U has some ball B(x,epsilon) = {y : d(x,y)<epsilon} entirely contained in U. A set is **closed** if its complement is open (equivalently, if it contains all its limit points). The **interior** of A is the largest open set contained in A; the **closure** is the smallest closed set containing A; the **boundary** is closure minus interior (points arbitrarily close to both A and its complement). *Example:* in R with the usual metric, (0,1) is open; [0,1] is closed, with interior (0,1), closure [0,1], boundary {0,1}. In the discrete metric, EVERY subset is both open and closed (since B(x,1/2)={x} is contained in any set containing x).

#### 13c Convergence and continuity in a general metric space; equivalence with sequential continuity
A sequence (x_n) in metric space (X,d) **converges** to L if d(x_n,L) -> 0 (exactly the real-number epsilon-N definition, with |.| replaced by d). f: X -> Y is **continuous** at a if the epsilon-delta condition holds using d_X and d_Y in place of absolute value; equivalently (and often easier to use), f is continuous at a iff for every sequence x_n -> a, f(x_n) -> f(a) (**sequential continuity**). *Example:* f: R^2 -> R, f(x,y)=x^2+y^2, is continuous everywhere: if (x_n,y_n) -> (a,b) in the Euclidean metric, then x_n->a, y_n->b (componentwise), so x_n^2+y_n^2 -> a^2+b^2 by the algebra of real limits.

#### 13d Compactness and completeness in a metric space; a continuous image of a compact set is compact
A subset K of a metric space is **compact** if every open cover of K has a finite subcover (equivalently, in R^n: K is compact iff K is closed and bounded, the Heine-Borel theorem). (X,d) is **complete** if every Cauchy sequence in X converges to a point OF X (R is complete; Q is not, as seen in S08). Key theorem: **a continuous image of a compact set is compact**, and hence a continuous real-valued function on a compact set attains its maximum and minimum (the Extreme Value Theorem, generalised from calculus). *Example:* [0,1] is compact in R (closed and bounded, Heine-Borel); (0,1) is NOT compact (bounded but not closed -- the open cover {(1/n, 1) : n>=2} has no finite subcover, since finitely many such intervals still miss points near 0).

## Explicitly not here
Compactness proofs using open covers directly (rather than via Heine-Borel in R^n) are sketched only, not required in full generality at this stage.

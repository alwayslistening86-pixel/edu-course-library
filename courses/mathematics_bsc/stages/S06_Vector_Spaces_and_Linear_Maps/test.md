# S06_Vector_Spaces_and_Linear_Maps - Test: Vector spaces and linear maps

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove that W = {(x,y,z) in R^3 : 2x-y+z=0} is a subspace of R^3. [5 marks]
2. Determine whether the polynomials 1+x, x+x^2, 1+x^2 span P_2 (polynomials of degree <=2). [5 marks]
3. For T: R^4 -> R^3 with matrix [[1,2,1,0],[0,1,1,1],[1,3,2,1]], find rank(T) and nullity(T), verifying Rank-Nullity. [6 marks]
4. With respect to the basis B={(1,0),(1,1)} of R^2, find the coordinates of v=(5,3), and hence write v as a linear combination of B. [4 marks]
5. Show that the map T: R^2 -> R^2, T(x,y) = (x^2, y) is NOT a linear transformation. [3 marks]
6. Let T: V -> W be linear with V finite-dimensional. Which are always true? Choose every correct option.
   A. `ker(T) is a subspace of V`
   B. `dim(V) = dim(ker T) + dim(im T)`
   C. `If T is injective, dim(ker T) = 0`
   D. `im(T) is a subspace of V`

## Answer key (for the tutor only)
1. [5] M1 shows 0=(0,0,0) satisfies 2(0)-0+0=0, so 0 in W (non-empty); M1 for u,v in W, checks 2(u1+v1)-(u2+v2)+(u3+v3) = (2u1-u2+u3)+(2v1-v2+v3) = 0+0=0; A1 so u+v in W; M1 for scalar c, 2(cu1)-(cu2)+(cu3)=c(0)=0; A1 so cu in W; conclusion the subspace test is satisfied.
2. [5] M1 sets up a1(1+x)+a2(x+x^2)+a3(1+x^2)=b0+b1x+b2x^2 for general target; M1 solves the resulting 3x3 linear system for a1,a2,a3 in terms of b0,b1,b2; A1 the coefficient matrix [[1,0,1],[1,1,0],[0,1,1]] has determinant 2, nonzero; A1 so a unique solution exists for every target; A1 the three polynomials span (and are a basis for) P_2.
3. [6] M1 row-reduces the matrix; A1 finds row 3 = row 1 + row 2, so rank = 2; M1 applies Rank-Nullity: dim(domain)=4; A1 nullity = 4-2 = 2; M1 confirms by finding the 2-dimensional solution space of the homogeneous system directly; A1 both methods agree, verifying the theorem.
4. [4] M1 sets a(1,0)+b(1,1)=(5,3); M1 solves b=3, a+3=5 so a=2; A1 coordinates (2,3) in B; A1 v = 2(1,0)+3(1,1).
5. [3] M1 tests additivity with a specific counter-example, e.g. u=(1,0), v=(1,0): T(u+v)=T(2,0)=(4,0); A1 T(u)+T(v)=(1,0)+(1,0)=(2,0), which differs from (4,0); A1 conclusion: T is not linear since T(u+v) ≠ T(u)+T(v) here.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Vector_Spaces_and_Linear_Maps` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 24 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Eigenvalues_Diagonalisation_and_Inner_Product_Spaces.

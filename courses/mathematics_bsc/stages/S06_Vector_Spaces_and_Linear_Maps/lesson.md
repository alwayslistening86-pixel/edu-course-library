# S06_Vector_Spaces_and_Linear_Maps - Lesson: Vector spaces and linear maps

## Goal
The learner verifies the vector space axioms, determines linear independence/spanning/basis/dimension, represents linear maps as matrices with respect to a basis, computes kernel/image via row reduction, and applies the Rank-Nullity theorem.

## Syllabus items taught here
- 6a - Vector spaces over R: axioms, subspaces, examples (R^n, polynomials, matrices, function spaces)
- 6b - Linear independence, spanning sets, basis and dimension
- 6c - Linear transformations; matrix representation with respect to a basis
- 6d - Kernel and image of a linear map; the Rank-Nullity Theorem
- 6e - Change of basis

## How to teach this
Ask whether the set of all polynomials of degree exactly 3 forms a vector space (it does not -- 0 is excluded and it isn't closed under addition), before defining the axioms. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 6a Vector spaces over R: axioms, subspaces, examples (R^n, polynomials, matrices, function spaces)
A **vector space** V over R is a set with addition and scalar multiplication satisfying: addition makes (V,+) an abelian group; scalar multiplication distributes over vector and scalar addition; (ab)v = a(bv); and 1v = v. *Examples:* R^n (n-tuples); P_n (polynomials of degree <= n, INCLUDING the zero polynomial); M_{{m,n}}(R) (m x n matrices); C[a,b] (continuous functions on [a,b]), all under the natural addition/scalar multiplication. A **subspace** W of V is a subset that is itself a vector space under V's operations; the subspace test: W is non-empty, and closed under addition and scalar multiplication. *Example:* {{(x,y,z) : x+y+z=0}} is a subspace of R^3 (a plane through the origin); {{(x,y,z) : x+y+z=1}} is not (fails closure and does not contain 0).

#### 6b Linear independence, spanning sets, basis and dimension
Vectors v_1,...,v_k are **linearly independent** if c_1v_1+...+c_kv_k=0 forces all c_i=0 (no non-trivial combination gives the zero vector). They **span** V if every vector in V is some linear combination of them. A **basis** is a linearly independent spanning set; every basis of V has the same size, called the **dimension** dim(V). *Example:* in R^3, are (1,2,1),(2,4,0),(3,6,1) linearly independent? Row-reducing the matrix with these as rows: Matrix([
[1, 2, 0],
[0, 0, 1],
[0, 0, 0]]) shows a row of zeros appears (rank 2 not 3), so they are linearly dependent (indeed row1 + row2 - row3 relation exists) -- they do not form a basis of R^3.

#### 6c Linear transformations; matrix representation with respect to a basis
A **linear transformation** T: V -> W satisfies T(u+v) = T(u)+T(v) and T(cv) = cT(v). Given a basis {{v_1,...,v_n}} of V and {{w_1,...,w_m}} of W, T is represented by an m x n **matrix** A whose j-th column is the coordinates of T(v_j) in the w-basis; then T(v) corresponds to Av (in coordinates). *Example:* T: R^2 -> R^2, T(x,y) = (2x+y, x-y), with respect to the standard basis has matrix [[2,1],[1,-1]] (columns are T(1,0)=(2,1) and T(0,1)=(1,-1)).

#### 6d Kernel and image of a linear map; the Rank-Nullity Theorem
The **kernel** ker(T) = {{v in V : T(v)=0}} is a subspace of V; the **image** im(T) = {{T(v) : v in V}} is a subspace of W. The **Rank-Nullity Theorem**: dim(V) = dim(ker T) + dim(im T), i.e. dim(V) = nullity(T) + rank(T). *Example:* for T: R^3 -> R^2 given by the matrix [[1,2,3],[2,4,6]] (rank 1, since row 2 = 2 x row 1), rank(T)=1, so by Rank-Nullity, nullity(T) = 3 - 1 = 2: the kernel is 2-dimensional (the plane x+2y+3z=0, or rather the solution space of the system, has dimension 2).

#### 6e Change of basis
A **change of basis** matrix P converts coordinates from one basis to another: if [v]_B is v's coordinate vector in basis B and B' is another basis, [v]_{{B'}} = P^{{-1}}[v]_B where P's columns are the B-coordinates of B''s vectors. If T has matrix A with respect to basis B, its matrix with respect to B' is P^{{-1}}AP. *Example:* in R^2, changing from the standard basis to B'={{(1,1),(1,-1)}}: P = [[1,1],[1,-1]], P^{{-1}} = (1/2)[[1,1],[1,-1]]; the vector (3,1) has B'-coordinates P^{{-1}}(3,1)^T = (2,1)^T, i.e. (3,1) = 2(1,1) + 1(1,-1).

## Explicitly not here
Diagonalisation via eigenvectors (a special, especially useful change of basis) is S07.

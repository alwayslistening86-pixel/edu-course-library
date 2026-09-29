# S07_Eigenvalues_Diagonalisation_and_Inner_Product_Spaces - Lesson: Eigenvalues, diagonalisation and inner product spaces

## Goal
The learner finds eigenvalues/eigenvectors via the characteristic polynomial, diagonalises a matrix when possible, works with inner products and orthonormal bases, and applies the spectral theorem to symmetric matrices.

## Syllabus items taught here
- 7a - Eigenvalues and eigenvectors; the characteristic polynomial
- 7b - Diagonalisation of a matrix; when diagonalisation is possible
- 7c - Inner product spaces; the Euclidean/standard inner product; orthogonality and orthonormal bases
- 7d - Symmetric matrices, orthogonal diagonalisation and the spectral theorem

## How to teach this
Ask what is special about a vector that a matrix simply stretches, without changing its direction -- introducing eigenvectors before any formula. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 7a Eigenvalues and eigenvectors; the characteristic polynomial
For a square matrix A, a nonzero vector v with Av = lambda v is an **eigenvector** with **eigenvalue** lambda. Eigenvalues are the roots of the **characteristic polynomial** det(A - lambda I) = 0. *Example:* A = Matrix([
[4, 1],
[2, 3]]) has characteristic polynomial det(A-lambda I) = lambda^2 - 7lambda + 10 = 0, giving eigenvalues ['2', '5']. For each eigenvalue, the eigenvectors are the nonzero solutions of (A-lambda I)v=0; sympy confirms the eigenvectors here are (spanned by) ['Matrix([[-1/2, 1]])', 'Matrix([[1, 1]])'].

#### 7b Diagonalisation of a matrix; when diagonalisation is possible
A is **diagonalisable** if there is an invertible P with P^{-1}AP = D diagonal; this happens exactly when A has n linearly independent eigenvectors (n = size of A), e.g. guaranteed if A has n distinct eigenvalues. The columns of P are the eigenvectors, and D's diagonal entries are the corresponding eigenvalues in the same order. *Example:* diagonalising A = Matrix([
[4, 1],
[2, 3]]) (distinct eigenvalues ['2', '5'], so diagonalisable): P = Matrix([
[-1, 1],
[ 2, 1]]), D = Matrix([
[2, 0],
[0, 5]]), and P^(-1) A P = D exactly (verified: Matrix([
[2, 0],
[0, 5]])).

#### 7c Inner product spaces; the Euclidean/standard inner product; orthogonality and orthonormal bases
An **inner product** <u,v> on a real vector space is a symmetric, bilinear, positive-definite pairing (the standard/Euclidean inner product on R^n is the dot product u.v = sum u_i v_i). It induces a norm ||v|| = root(<v,v>) and defines **orthogonality**: u,v are orthogonal if <u,v>=0. An **orthonormal basis** consists of mutually orthogonal unit vectors; the **Gram-Schmidt process** converts any basis into an orthonormal one by successively subtracting projections onto previous vectors. *Example:* starting from (1,1,0) and (1,0,1) in R^3: u1=(1,1,0)/root2 (normalised); u2 is (1,0,1) minus its projection onto u1, then normalised: proj = <(1,0,1),u1>u1 = (1/2,1/2,0), so (1,0,1)-(1/2,1/2,0) = (1/2,-1/2,1), normalised to (1,-1,2)/root6.

#### 7d Symmetric matrices, orthogonal diagonalisation and the spectral theorem
**Symmetric matrices** (A = A^T) have two special properties, together the **Spectral Theorem**: all eigenvalues are real, and eigenvectors for distinct eigenvalues are automatically orthogonal, so A can be **orthogonally diagonalised**: A = QDQ^T with Q orthogonal (Q^T = Q^{-1}) and D diagonal. *Example:* A = Matrix([
[2, 1],
[1, 2]]) (symmetric) has eigenvalues ['1', '3'] with eigenvectors ['Matrix([[-1, 1]])', 'Matrix([[1, 1]])']; normalising these orthogonal eigenvectors gives the columns of an orthogonal Q with Q^T A Q diagonal.

## Explicitly not here
Jordan normal form for non-diagonalisable matrices is beyond this stage's scope.

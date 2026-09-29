# S05_Homomorphisms_and_Quotient_Groups - Lesson: Homomorphisms and quotient groups

## Goal
The learner tests whether a map is a group homomorphism, computes kernels and images, identifies normal subgroups, constructs quotient groups, and applies the First Isomorphism Theorem.

## Syllabus items taught here
- 5a - Group homomorphisms and isomorphisms; kernel and image
- 5b - Normal subgroups
- 5c - Quotient groups
- 5d - The First Isomorphism Theorem

## How to teach this
Ask what it means for a map between groups to 'respect the operation', before defining a homomorphism formally. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 5a Group homomorphisms and isomorphisms; kernel and image
A map phi: G -> H between groups is a **homomorphism** if phi(a*b) = phi(a)*phi(b) for all a,b in G (necessarily phi(e_G)=e_H and phi(a^{-1})=phi(a)^{-1}). A **bijective** homomorphism is an **isomorphism**, written G ≅ H (the groups are structurally identical). The **kernel** ker(phi) = {g in G : phi(g) = e_H} and the **image** im(phi) = {phi(g) : g in G}; ker(phi) is always a subgroup of G and im(phi) always a subgroup of H. phi is injective iff ker(phi) = {e_G}. *Example:* phi: (Z,+) -> (Z_n,+), phi(k) = k mod n, is a homomorphism (phi(a+b) mod n = (phi(a)+phi(b)) mod n); ker(phi) = nZ = {..., -n, 0, n, 2n, ...}, im(phi) = all of Z_n.

#### 5b Normal subgroups
A subgroup N <= G is **normal** (written N ◁ G) if gNg^{-1} = N for every g in G, equivalently gN = Ng for every g (left and right cosets coincide). Every subgroup of an abelian group is normal. The kernel of any homomorphism is always a normal subgroup. *Example:* in S_3, the subgroup A_3 = {e, (123), (132)} (the even permutations) is normal, since conjugating a 3-cycle by any permutation gives another 3-cycle, staying in A_3; but the subgroup {e, (1 2)} is not normal, since conjugating (1 2) by (1 3) gives (2 3), which is not in {e,(1 2)}.

#### 5c Quotient groups
If N ◁ G, the **quotient group** G/N has elements the cosets gN, with operation (aN)(bN) = (ab)N (well-defined precisely because N is normal); its identity is N = eN, and |G/N| = |G|/|N| when G is finite. *Example:* for (Z, +) and N = 3Z, Z/3Z has three cosets 0+3Z, 1+3Z, 2+3Z, with addition mod 3 -- so Z/3Z ≅ Z_3. For S_3 and N = A_3, S_3/A_3 has two cosets (A_3 itself and the odd permutations), so S_3/A_3 ≅ Z_2.

#### 5d The First Isomorphism Theorem
**First Isomorphism Theorem**: if phi: G -> H is a homomorphism, then G/ker(phi) ≅ im(phi). Intuitively, quotienting out everything that maps to the identity recovers exactly the image, with no information lost. *Example:* for phi: (Z,+) -> (Z_n,+), phi(k)=k mod n, ker(phi)=nZ and im(phi)=Z_n, so the theorem confirms Z/nZ ≅ Z_n (matching the direct construction of Z_n as a quotient). *Example:* for the sign homomorphism sgn: S_n -> ({1,-1}, x), ker(sgn) = A_n and im(sgn) = {1,-1}, so S_n/A_n ≅ Z_2.

## Explicitly not here
Ring homomorphisms and the analogous First Isomorphism Theorem for rings are S12.

# S03_Discrete_Mathematics_for_Computing - Lesson: Discrete mathematics for computing

## Goal
The learner constructs truth tables and simplifies Boolean expressions using De Morgan's laws, applies set operations and classifies relations and functions, represents graphs and trees using adjacency matrices/lists, and writes proofs by induction and by contradiction for simple computing results.

## Syllabus items taught here
- 3a - Propositional logic: truth tables, logical equivalence, De Morgan's laws and Boolean circuit simplification
- 3b - Sets, relations and functions: set operations, relations (reflexive/symmetric/transitive), injective/surjective/bijective functions
- 3c - Graph theory fundamentals: graphs, trees, adjacency matrix/list representations
- 3d - Proof techniques: proof by induction and proof by contradiction, applied to a computing result

## How to teach this
Ask the learner whether NOT(A AND B) is the same as (NOT A) AND (NOT B), and to check with a truth table rather than guessing. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 3a Propositional logic: truth tables, logical equivalence, De Morgan's laws and Boolean circuit simplification
**Propositional logic.** A truth table enumerates every combination of truth values for a proposition's variables and the resulting truth value of the whole expression. **De Morgan's laws**: NOT(A AND B) = (NOT A) OR (NOT B), and NOT(A OR B) = (NOT A) AND (NOT B) -- essential for simplifying Boolean expressions (and hence logic circuits/conditional code).
```python
from itertools import product

def not_and(a, b):
    return not (a and b)

def or_of_nots(a, b):
    return (not a) or (not b)

for a, b in product([False, True], repeat=2):
    print(a, b, not_and(a, b), or_of_nots(a, b), not_and(a, b) == or_of_nots(a, b))
```
Output:
```
False False True True True
False True True True True
True False True True True
True True False False True
```
Two expressions are **logically equivalent** if they have identical truth tables for every input, as confirmed above for De Morgan's first law. This directly simplifies code: `if not (x > 0 and y > 0):` is equivalent to `if x <= 0 or y <= 0:`.

#### 3b Sets, relations and functions: set operations, relations (reflexive/symmetric/transitive), injective/surjective/bijective functions
**Sets, relations and functions.** Set operations: union (A union B), intersection (A intersect B), difference (A - B), the Cartesian product A x B (all ordered pairs (a,b) with a in A, b in B). A **relation** R on a set A is a subset of A x A; it is *reflexive* if (a,a) is in R for every a; *symmetric* if (a,b) in R implies (b,a) in R; *transitive* if (a,b) and (b,c) in R implies (a,c) in R. A relation that is reflexive, symmetric and transitive is an *equivalence relation*. A **function** f: A -> B is *injective* (one-to-one) if distinct inputs give distinct outputs; *surjective* (onto) if every element of B is the image of some element of A; *bijective* if both (so it has a well-defined inverse).
```python
def is_reflexive(rel, elems):
    return all((a, a) in rel for a in elems)

def is_symmetric(rel):
    return all((b, a) in rel for (a, b) in rel)

def is_transitive(rel):
    return all((a, c) in rel for (a, b1) in rel for (b2, c) in rel if b1 == b2)

R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
print("reflexive:", is_reflexive(R, {1, 2, 3}))
print("symmetric:", is_symmetric(R))
print("transitive:", is_transitive(R))
```
Output:
```
reflexive: True
symmetric: True
transitive: True
```

#### 3c Graph theory fundamentals: graphs, trees, adjacency matrix/list representations
**Graph theory fundamentals.** A graph G = (V, E) consists of vertices V and edges E connecting pairs of vertices; a graph is *directed* if edges have a direction, *undirected* otherwise, and *weighted* if edges carry a numeric cost. A **tree** is a connected, undirected, acyclic graph with n vertices and exactly n-1 edges; a *rooted tree* additionally designates one vertex as the root, giving every other vertex a well-defined parent. A graph can be represented as an **adjacency matrix** (an n x n matrix where entry (i,j) is 1/weight if an edge exists from i to j, else 0 -- O(n^2) space, O(1) edge lookup) or an **adjacency list** (each vertex stores a list of its neighbours -- O(V+E) space, better for sparse graphs).
```python
graph_adj_list = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
n = 4
adj_matrix = [[0]*n for _ in range(n)]
for u, neighbours in graph_adj_list.items():
    for v in neighbours:
        adj_matrix[u][v] = 1
for row in adj_matrix:
    print(row)
```
Output:
```
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
```

#### 3d Proof techniques: proof by induction and proof by contradiction, applied to a computing result
**Proof by induction.** To prove a statement P(n) holds for all integers n >= base: (1) *Base case* -- show P(base) is true; (2) *Inductive step* -- assume P(k) is true (the inductive hypothesis) and show this implies P(k+1) is true; conclude P(n) holds for all n >= base. *Example*: prove 1+2+...+n = n(n+1)/2 for all n>=1. Base: n=1 gives 1 = 1(2)/2 = 1, true. Inductive step: assume 1+...+k = k(k+1)/2; then 1+...+k+(k+1) = k(k+1)/2 + (k+1) = (k+1)(k/2+1) = (k+1)(k+2)/2, which is the formula at n=k+1. **Proof by contradiction.** Assume the negation of what is to be proved, derive a logical contradiction, and conclude the original statement must be true. *Example (a computing result)*: prove that no comparison-based sorting algorithm can sort n items using fewer than ceil(log2(n!)) comparisons in the worst case. Sketch: assume such an algorithm exists using fewer comparisons; a comparison-based sort's execution corresponds to a path in a binary decision tree with one leaf per possible output permutation (n! of them); a binary tree of depth d has at most 2^d leaves, so distinguishing all n! outcomes needs 2^d >= n!, i.e. d >= log2(n!) -- contradicting the assumption that fewer comparisons suffice, since fewer comparisons means a shallower tree with too few leaves.
```python
import math
n = 5
print("n! =", math.factorial(n))
print("lower bound on comparisons, ceil(log2(n!)) =", math.ceil(math.log2(math.factorial(n))))
```
Output:
```
n! = 120
lower bound on comparisons, ceil(log2(n!)) = 7
```

## Explicitly not here
Formal automata and computability proofs (the halting problem) are S08.

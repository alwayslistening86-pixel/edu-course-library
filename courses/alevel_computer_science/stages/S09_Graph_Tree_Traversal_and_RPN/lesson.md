# S09_Graph_Tree_Traversal_and_RPN - Lesson: Graph and tree traversal, and Reverse Polish notation

## Goal
The learner traces breadth-first and depth-first graph traversal, pre/in/post-order tree traversal, and converts between infix and Reverse Polish (postfix) notation.

## Syllabus items taught here
- 4.3.1.1 - Graph-traversal algorithms: breadth-first and depth-first search
- 4.3.2.1 - Tree-traversal algorithms: pre-order, in-order, post-order
- 4.3.3.1 - Reverse Polish notation

## How to teach this
Ask the learner how they would explore a maze two ways: check every room one step away before going further (breadth-first), or follow one corridor as far as possible before backtracking (depth-first). AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.3.1.1 Graph-traversal algorithms: breadth-first and depth-first search
**Breadth-first search (BFS)** explores a graph level by level: visit the start node, then all its unvisited neighbours, then all of their unvisited neighbours, and so on, using a **queue** to remember which node to visit next. **Depth-first search (DFS)** explores as far as possible along each branch before backtracking, using a **stack** (or recursion, which implicitly uses the call stack). *Worked trace* on the graph A-B, A-C, B-D, C-D, D-E (undirected, neighbours visited in alphabetical order): BFS from A visits A, B, C, D, E (A first; then its neighbours B, C; then their new neighbour D; then D's new neighbour E). DFS from A visits A, B, D, C, E (A, then follows B, then B's first unvisited neighbour D, then D's first unvisited neighbour C, backtracking once C's neighbours are all visited, then D's remaining neighbour E). BFS is typically used to find the shortest path (fewest edges) between two nodes; DFS is used for tasks like exploring all paths, cycle detection, or topological sorting.

#### 4.3.2.1 Tree-traversal algorithms: pre-order, in-order, post-order
A **tree traversal** visits every node of a tree in a defined order. **Pre-order**: visit the root, then traverse the left subtree, then the right subtree. **In-order**: traverse the left subtree, then visit the root, then the right subtree (on a binary search tree, this visits nodes in sorted order). **Post-order**: traverse the left subtree, then the right subtree, then visit the root. *Worked trace* on the tree with root F, F's children B and G, B's children A and D, D's children C and E, and G's child I: pre-order gives F, B, A, D, C, E, G, I; in-order gives A, B, C, D, E, F, G, I; post-order gives A, C, E, D, B, I, G, F.

#### 4.3.3.1 Reverse Polish notation
**Reverse Polish notation (RPN, postfix)** writes an expression with operators after their operands (e.g. `3 4 +` rather than `3 + 4`), removing the need for brackets or precedence rules. To **evaluate** RPN: scan left to right, pushing numbers onto a stack; when an operator is found, pop the required number of operands, apply the operator, and push the result back. *Example:* `3 4 + 2 *` (the postfix form of infix `(3 + 4) * 2`): push 3, push 4; `+` pops 4 and 3, pushes 7; push 2; `*` pops 2 and 7, pushes 14 -- result 14. Converting infix to RPN uses operator precedence (and brackets) to decide the order operators are written in; RPN is used by some calculators and compilers because it can be evaluated directly with a stack, without needing to track precedence or brackets at evaluation time.

## Explicitly not here
Specific searching and sorting algorithms are S10-S11.

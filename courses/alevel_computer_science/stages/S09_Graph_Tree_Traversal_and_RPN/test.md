# S09_Graph_Tree_Traversal_and_RPN - Test: Graph and tree traversal, and Reverse Polish notation

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. For the graph in the practice question (edges A-B, A-C, B-D, C-D, neighbours visited alphabetically), state the order nodes are visited by depth-first search starting at A, and explain how it differs from breadth-first search here. [3 marks]
2. For a binary tree with root R, left child L, right child M, and L's children P and Q, state the pre-order and post-order traversal sequences. [4 marks]
3. Convert the infix expression 3 + 4 * 2 to Reverse Polish notation, and evaluate it using a stack, showing the stack's contents at each step. [4 marks]
4. Which traversal of a binary search tree visits its nodes in ascending sorted order? Choose every correct option.
   A. `in-order`
   B. `pre-order`
   C. `post-order`
   D. `breadth-first`

## Answer key (for the tutor only)
1. [3] B1 DFS order: A, B, D, C (follows B, then B's unvisited neighbour D, then D's unvisited neighbour C); B1 BFS visits all of A's neighbours (B, C) before going further, DFS commits to one branch (B, then D) before backtracking; B1 both still visit every reachable node, just in a different order.
2. [4] M1 pre-order (root, left, right): R, L, P, Q, M; M1 post-order (left, right, root): P, Q, L, M, R; A1/A1 both fully correct as written.
3. [4] M1 correct postfix (multiplication binds tighter, so it is written first): 3 4 2 * +; M1 push 3, push 4, push 2; M1 '*' pops 2 and 4, pushes 8 (stack: 3, 8); A1 '+' pops 8 and 3, pushes 11 -- result 11.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Graph_Tree_Traversal_and_RPN` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Searching_Algorithms.

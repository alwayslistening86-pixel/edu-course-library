# S14_Complexity_and_Turing_Machines - Test: Algorithm complexity, Big-O notation, limits of computation and Turing machines

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Put the following Big-O classes in order from fastest-growing to slowest-growing: O(n), O(log n), O(n^2), O(1), O(n log n). [2 marks]
2. Explain the difference between a tractable and an intractable problem. [3 marks]
3. Explain what the halting problem is, and state what Alan Turing proved about it. [3 marks]
4. Describe, in general terms, the components of a Turing machine. [3 marks]
5. Which best describes a Universal Turing Machine? Choose every correct option.
   A. a Turing machine that can simulate any other Turing machine, given its description and input on the tape
   B. a Turing machine that can only add two numbers
   C. a physical machine every real computer is built directly from
   D. a Turing machine with an infinite number of states

## Answer key (for the tutor only)
1. [2] B1/B1 correct order: O(n^2), O(n log n), O(n), O(log n), O(1) (award 2 marks for the whole order correct, 1 mark if only one adjacent pair is swapped).
2. [3] B1 a tractable problem has an algorithm that solves it in polynomial time (O(n^k) for some constant k), feasible for large n; B1 an intractable problem has no known polynomial-time algorithm, only exponential-time (or worse) solutions, which become impractically slow as n grows; B1 both are still computable in principle -- the distinction is about practical feasibility, not whether a solution exists at all.
3. [3] B1 the halting problem asks whether a general algorithm can be written that, given any program and its input, always correctly decides whether that program halts or runs forever; B1 Turing proved this problem is non-computable: no such general algorithm can exist, for any program/input in general; B1 this means no tool can perfectly and automatically detect every possible infinite loop in every possible program.
4. [3] B1 an infinite tape divided into cells, each holding a symbol (or blank); B1 a read-write head that reads/writes the current cell and moves one cell left or right; B1 a finite set of states and a transition function deciding, from the current state and symbol read, what to write, which way to move, and which state to go to next.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Complexity_and_Turing_Machines` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Software_Development_Lifecycle.

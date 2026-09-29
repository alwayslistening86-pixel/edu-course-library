# S07_Queues_and_Stacks - Lesson: Queues and stacks

## Goal
The learner explains and traces the operations of queues (add, remove, test empty, test full) and stacks (push, pop, peek, test empty, test full).

## Syllabus items taught here
- 4.2.2.1 - Queues
- 4.2.3.1 - Stacks

## How to teach this
Ask the learner to compare a queue of people at a checkout (first in, first served) with a pile of plates being taken from the top (last on, first off). AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.2.2.1 Queues
A **queue** is a First-In-First-Out (FIFO) data structure. Operations: **add** an item (to the back/rear of the queue), **remove** an item (from the front of the queue), **test for an empty queue** (is there anything to remove?), **test for a full queue** (is there room to add, e.g. in a fixed-size array implementation?). *Worked trace:* start empty; add(A) -> [A]; add(B) -> [A, B]; remove() returns A, queue is now [B]; add(C) -> [B, C]; remove() returns B, queue is now [C].

#### 4.2.3.1 Stacks
A **stack** is a Last-In-First-Out (LIFO) data structure. Operations: **push** (add an item to the top), **pop** (remove and return the item from the top), **peek/top** (look at the top item without removing it), **test for an empty stack**, **test for a full stack**. *Worked trace:* start empty; push(A) -> [A]; push(B) -> [A, B] (B on top); push(C) -> [A, B, C]; pop() returns C, stack is now [A, B]; peek() returns B without removing it; stack is still [A, B]. Stacks are used for undo operations, expression evaluation (S09), and recursive-call bookkeeping (the call stack, S04).

## Explicitly not here
Graphs, trees, hash tables, dictionaries and vectors are S08.

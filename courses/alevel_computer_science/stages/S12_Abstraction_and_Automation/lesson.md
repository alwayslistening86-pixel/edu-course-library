# S12_Abstraction_and_Automation - Lesson: Problem-solving, abstraction and automation

## Goal
The learner explains problem-solving and algorithm development, the different forms of abstraction (representational, procedural, functional, data, problem abstraction/reduction), decomposition, composition, and automation.

## Syllabus items taught here
- 4.4.1.1 - Problem-solving and algorithms
- 4.4.1.3 - Abstraction: representational, procedural, functional and data abstraction; decomposition and composition
- 4.4.1.11 - Automation

## How to teach this
Ask the learner what a car's steering wheel lets a driver do without needing to know anything about how the steering mechanism actually works underneath -- that's abstraction. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.4.1.1 Problem-solving and algorithms
**Problem-solving** in computer science means developing an **algorithm** (a precise, ordered sequence of steps solving a problem) and checking that it is correct: express it as pseudo-code with sequence, assignment, selection and iteration; **hand-trace** it (work through it step by step with test values, as in the practice/test items throughout this course) to check its logic; convert pseudo-code into working high-level language code; and reason logically about whether the algorithm is both **correct** (produces the right answer for all valid inputs) and **efficient** (uses reasonable time/memory, S14).

#### 4.4.1.3 Abstraction: representational, procedural, functional and data abstraction; decomposition and composition
**Abstraction** removes unnecessary detail so only what matters for the task at hand remains, and takes several related forms. **Representational abstraction** models something in the real world by keeping only the details relevant to the problem (e.g. a tube map keeps stations/connections, not true geography). **Procedural abstraction** hides how a subroutine computes its result behind its name and interface (you call `sort(list)` without needing to know which sorting algorithm it uses). **Functional abstraction** similarly hides a function's internal computation behind what it returns for given inputs. **Data abstraction** hides how a data structure is actually represented internally behind the operations it exposes (as with an ADT, S06). **Problem abstraction/reduction** strips a problem down, removing detail, until it reduces to a already-solvable/recognisable form. **Decomposition** breaks a large problem into smaller, more manageable sub-problems, each easier to solve; **composition** is the reverse process of building up a solution to the whole problem by combining (composing) smaller procedures or smaller pieces of data into the larger structure.

#### 4.4.1.11 Automation
**Automation** is using a computer to carry out a process without needing a human to perform each step manually, once the algorithm has been designed. It ties together the earlier stages: create an algorithm to solve the problem, implement it as program code, implement any data it needs using suitable data structures, then execute the code so the computer performs the task automatically -- freeing the human from repeating the manual steps every time.

## Explicitly not here
Formal models used to study computation itself -- finite state machines, regular expressions, BNF -- are S13; algorithm complexity and the limits of computation are S14.

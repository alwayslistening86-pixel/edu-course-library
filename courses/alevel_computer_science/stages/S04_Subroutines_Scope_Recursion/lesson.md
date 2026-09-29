# S04_Subroutines_Scope_Recursion - Lesson: Subroutines, parameters and return values; scope, stack frames and recursion

## Goal
The learner uses subroutines with parameters and return values, explains local/global variable scope and the role of stack frames, and solves simple problems using recursion.

## Syllabus items taught here
- 4.1.1.10 - Subroutines (procedures and functions): parameters and returning values
- 4.1.1.13 - Local and global variables; the role of stack frames
- 4.1.1.16 - Recursive techniques

## How to teach this
Ask the learner to imagine several people each keeping their own private notebook (local variables) alongside one shared noticeboard everyone can read and write (a global variable) -- what could go wrong with the noticeboard approach? AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.1.1.10 Subroutines (procedures and functions): parameters and returning values
A **subroutine** (a **procedure**, which performs an action, or a **function**, which additionally returns a value) is a named, reusable block of code. **Parameters** let data be passed into a subroutine when it is called (e.g. `def area(width, height):`); the values passed in are called **arguments**. A function **returns a value** to the calling code with a `RETURN` statement, which can then be used in an expression, e.g. `total = area(3, 4) + area(5, 6)`. Using subroutines avoids repeating code, makes programs easier to read/test/maintain, and allows a problem to be decomposed into smaller, independently-testable pieces.

#### 4.1.1.13 Local and global variables; the role of stack frames
A **local variable** is declared inside a subroutine and exists (and is accessible) only while that subroutine is executing; each call gets its own fresh copy. A **global variable** is declared outside any subroutine and is accessible from anywhere in the program, including inside subroutines (in most languages) -- but relying on globals makes code harder to reason about and test, since any subroutine could change the value unexpectedly, so local variables and parameters are generally preferred. A **stack frame** is the block of memory created on the **call stack** each time a subroutine is called; it stores the subroutine's **return address** (where to resume execution in the calling code), its **parameters** and its **local variables**. When the subroutine finishes, its stack frame is removed (popped), and execution resumes at the return address using the values in the calling routine's own (now top-of-stack) frame.

#### 4.1.1.16 Recursive techniques
**Recursion** is when a subroutine calls itself to solve a smaller version of the same problem. Every recursive solution needs a **base case** (a simple case solved directly, without a further recursive call, which stops the recursion) and a **general (recursive) case** (which calls the subroutine again on a smaller version of the problem, moving towards the base case). *Example* -- factorial: `factorial(0)` = 1 (base case); `factorial(n)` = `n * factorial(n - 1)` for `n > 0` (general case). Each recursive call gets its own stack frame, so `factorial(5)` builds up 6 stack frames (for n=5,4,3,2,1,0) before the base case returns 1 and the calls unwind, multiplying as they go: 1, then 1*1=1, then 2*1=2, then 3*2=6, then 4*6=24, then 5*24=120.

## Explicitly not here
How different programming paradigms (procedural vs object-oriented) organise subroutines/methods into larger programs is S05.

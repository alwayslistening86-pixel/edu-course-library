# S04_Subroutines_Scope_Recursion - Test: Subroutines, parameters and return values; scope, stack frames and recursion

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a procedure and a function. [2 marks]
2. Explain the difference between a local variable and a global variable, and give one reason local variables are generally preferred. [3 marks]
3. Describe the role of a stack frame when a subroutine is called. [3 marks]
4. Write a recursive function that returns the sum of all integers from 1 to n, stating its base case. [3 marks]
5. What does a recursive subroutine need to guarantee it eventually terminates? Choose every correct option.
   A. a base case that is reached and does not make a further recursive call
   B. a global variable to count the calls
   C. at least two parameters
   D. a return type of Boolean

## Answer key (for the tutor only)
1. [2] B1 both are subroutines (named, reusable blocks of code); B1 a function returns a value to the code that called it, a procedure does not (it performs an action).
2. [3] B1 a local variable exists only during, and is only accessible within, the subroutine it is declared in; B1 a global variable is accessible from anywhere in the program; B1 relying on globals makes programs harder to test/reason about, since any subroutine could unexpectedly change a shared value.
3. [3] B1 a new stack frame is pushed onto the call stack for each call; B1 it stores the return address (where to resume in the calling code), the subroutine's parameters and its local variables; B1 the frame is popped (removed) when the subroutine finishes, and execution resumes at the stored return address.
4. [3] M1 base case: n == 1 (or n == 0) returns 1 (or 0); M1 general case: return n + sum_to(n - 1); A1 correct overall structure that terminates for any positive n.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Subroutines_Scope_Recursion` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Programming_Paradigms.

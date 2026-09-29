# S11_Subroutines_Structured_Programming - Lesson: Subroutines and structured programming

## Goal
The learner understands subroutines, their advantages, passing data via parameters, returning values, local variables and why they're good practice, and the structured approach to programming and its advantages.

## Syllabus items taught here
- 3.2.10 - Structured programming and subroutines

## How to teach this
Ask the learner why it's better to write one 'calculate area' subroutine and call it five times than to copy and paste the same three lines of code five times. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.10 Structured programming and subroutines
A **subroutine** is a named, reusable block of code that performs a specific task and can be called from elsewhere in a program; a **procedure** performs an action, a **function** additionally returns a value. Advantages: code can be reused (called many times without rewriting it), a large program can be broken into smaller, more manageable, independently testable pieces, and the same subroutine written once reduces the chance of introducing an error by copying code incorrectly. **Parameters** pass data into a subroutine when it is called, so the same subroutine can work on different values each time; a subroutine that **returns a value** sends a result back to the code that called it (via `return` in Python), which can then be stored, printed or used further. Subroutines can declare their own **local variables**, which exist only while that subroutine is running and cannot be accessed from outside it; using local variables is good practice because it stops one subroutine accidentally reading or overwriting a variable that another part of the program is using for something else. The **structured approach to programming** builds a solution from three basic constructs -- sequence, selection and iteration -- combined via decomposition into subroutines, avoiding unstructured jumps around the code; advantages include code that is easier to read, test, debug, reuse and maintain, and that is easier for teams to divide up and work on. *Example:*
```
def area_of_rectangle(width, height):
    return width * height

print(area_of_rectangle(4, 5))
```

## Explicitly not here
Testing and validating that code, and catching errors, is S12.

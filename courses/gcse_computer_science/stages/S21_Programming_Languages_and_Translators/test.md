# S21_Programming_Languages_and_Translators - Test: Programming languages and translators

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the main difference between a low-level language and a high-level language. [2 marks]
2. Explain the difference between machine code and assembly language. [2 marks]
3. Explain the main differences between an interpreter and a compiler. [4 marks]
4. A software company is about to release a finished, tested application to millions of customers who should not be able to see its source code. Suggest and justify whether an interpreter or a compiler is more suitable. [3 marks]
5. Which translator translates and executes a program one statement at a time, stopping at the first error it meets? Choose every correct option.
   A. an interpreter
   B. a compiler
   C. an assembler
   D. an operating system

## Answer key (for the tutor only)
1. [2] B1 low-level languages are close to the hardware's own instructions (hard for humans to read, precise hardware control); B1 high-level languages use English-like, human-readable keywords/structures, far removed from hardware detail, and are typically portable across different computers.
2. [2] B1 machine code is the binary pattern of instructions a processor executes directly, with no translation needed; B1 assembly language uses short mnemonics that map one-to-one to machine code instructions, needing an assembler to translate it.
3. [4] B1 an interpreter translates and executes a program one statement at a time; B1 a compiler translates the whole program into a machine-code executable before it is run; B1 an interpreter stops at the first error found, while a compiler reports all the syntax errors it finds before running anything; B1 code translated by a compiler then runs faster/without the source or translator present, while an interpreted program must be re-translated (and the interpreter present) every time it runs.
4. [3] B1 a compiler; B1 it produces a stand-alone executable that runs without the original source code (or a compiler/interpreter) present; B1 the compiled program also runs faster than an interpreted one, which matters at that scale.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S21_Programming_Languages_and_Translators` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S22_Systems_Architecture.

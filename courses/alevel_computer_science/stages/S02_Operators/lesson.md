# S02_Operators - Lesson: Arithmetic, relational and Boolean operators

## Goal
The learner uses arithmetic operators (including exponentiation, rounding and truncation), relational operators, and Boolean operators NOT/AND/OR/XOR.

## Syllabus items taught here
- 4.1.1.3 - Arithmetic operations: +, -, *, real and integer division (with remainder), exponentiation, rounding, truncation
- 4.1.1.4 - Relational operations
- 4.1.1.5 - Boolean operations: NOT, AND, OR, XOR

## How to teach this
Ask the learner what 2 to the power 10 is, and whether rounding 2.5 and truncating 2.9 give the same answer. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.1.1.3 Arithmetic operations: +, -, *, real and integer division (with remainder), exponentiation, rounding, truncation
**Arithmetic operators**: addition (`+`), subtraction (`-`), multiplication (`*`), **real/float division** (`/`, e.g. `17 / 5` = 3.4) and **integer division with remainder** (`//` and `%` in Python, e.g. `17 // 5` = 3, `17 % 5` = 2), **exponentiation** (`**` in Python, e.g. `2 ** 10` = 1024), **rounding** (to the nearest whole number or a given number of decimal places, e.g. round 2.5 to 3 using round-half-up, or to 2 using round-half-to-even depending on the rule used) and **truncation** (discarding everything after the decimal point without rounding, e.g. truncating 2.9 gives 2, and truncating -2.9 gives -2, not -3).

#### 4.1.1.4 Relational operations
**Relational (comparison) operators** produce a Boolean result: equal to (`==`), not equal to (`!=`), less than (`<`), greater than (`>`), less than or equal to (`<=`), greater than or equal to (`>=`).

#### 4.1.1.5 Boolean operations: NOT, AND, OR, XOR
**Boolean operators**: **NOT** inverts a value; **AND** is True only if both operands are True; **OR** is True if at least one operand is True; **XOR** (exclusive or) is True if exactly one operand is True, but False if both are True or both are False -- this is the key difference from OR. *Example:* `True XOR True` is `False`, but `True OR True` is `True`.

## Explicitly not here
Data structures (arrays, records, and A-level's further structures) are S06-S08.

# S06_Operators - Lesson: Arithmetic, relational and Boolean operators

## Goal
The learner uses arithmetic operators (including integer and real division), relational operators, and Boolean operators (NOT, AND, OR).

## Syllabus items taught here
- 3.2.3 - Arithmetic operations
- 3.2.4 - Relational operations
- 3.2.5 - Boolean operations

## How to teach this
Ask the learner what 17 divided by 5 is 'normally', and what it is if only whole apples can be shared out -- that's the difference between real and integer division. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.3 Arithmetic operations
**Arithmetic operators**: addition (`+`), subtraction (`-`), multiplication (`*`), **real division** (`/`, gives a decimal/fractional result, e.g. `17 / 5` = 3.4) and **integer division** (`//` in Python, sometimes called DIV, gives only the whole-number quotient and discards the remainder, e.g. `17 // 5` = 3); the related **modulus/remainder** operator (`%`, sometimes MOD) gives what integer division discards, e.g. `17 % 5` = 2.

#### 3.2.4 Relational operations
**Relational (comparison) operators** test a relationship between two values and produce a Boolean result: equal to (`==`), not equal to (`!=`), less than (`<`), greater than (`>`), less than or equal to (`<=`), greater than or equal to (`>=`). *Example:* `7 == 7` is True; `7 != 8` is True; `3 < 5` is True; `5 >= 5` is True.

#### 3.2.5 Boolean operations
**Boolean operators** combine or invert Boolean (True/False) values: **NOT** inverts a value (`NOT True` is `False`); **AND** is True only if both operands are True (`True AND False` is `False`); **OR** is True if at least one operand is True (`True OR False` is `True`). These combine naturally with relational operators to build compound conditions, e.g. `age >= 5 AND age <= 11` tests whether age is in the range 5 to 11 inclusive.

## Explicitly not here
Data structures (arrays, records) are S07.

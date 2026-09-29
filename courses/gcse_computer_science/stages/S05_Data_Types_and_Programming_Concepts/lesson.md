# S05_Data_Types_and_Programming_Concepts - Lesson: Data types and core programming concepts

## Goal
The learner uses the five core data types, and declares variables and constants, assigns values, uses definite and indefinite iteration, selection (including nested), subroutines, and meaningful identifier names.

## Syllabus items taught here
- 3.2.1 - Data types
- 3.2.2 - Programming concepts: variables, constants, selection, iteration, subroutines, identifiers

## How to teach this
Ask the learner what kind of value 'age', 'is_raining' and 'first_name' each hold, before naming the data types. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.1 Data types
A **data type** classifies what kind of value a piece of data holds and what can be done with it. The five core types: **integer** (a whole number, positive or negative, e.g. 7, -3), **real** (a number with a fractional/decimal part, e.g. 3.14; also called float), **Boolean** (only True or False), **character** (a single symbol, e.g. 'a'), **string** (a sequence of characters, e.g. "hello"). Choosing the right data type matters: it affects what operations are valid (e.g. `2 + 2` on integers gives 4, but `"2" + "2"` on strings concatenates to "22") and how much memory is used.

#### 3.2.2 Programming concepts: variables, constants, selection, iteration, subroutines, identifiers
A **variable** is a named location that stores a value which can change while the program runs; a **constant** is named similarly but its value is fixed once set and cannot change. **Declaration** introduces the name (and often its type); **assignment** (`=`) gives it a value. **Selection** chooses between different paths of execution based on a condition (`IF ... THEN ... ELSE ...`); selection can be **nested** (an IF inside another IF) to test more than one condition in sequence. **Iteration** repeats a block of statements: **definite (count-controlled)** iteration (`FOR`) repeats a known number of times; **indefinite (condition-controlled)** iteration (`WHILE`, or a post-condition `REPEAT ... UNTIL`) repeats until a condition changes, so the number of repeats is not fixed in advance; iteration can be nested (a loop inside another loop). A **subroutine** is a named, reusable block of code that performs a task and can be called from elsewhere in the program (procedures and functions; covered fully in S11). Using **meaningful identifier names** (e.g. `total_score` rather than `x`) matters because it makes code far easier for the programmer -- and anyone else reading it later -- to understand and maintain, and reduces the chance of using the wrong variable by mistake.

## Explicitly not here
The specific operators used inside conditions and expressions are S06.

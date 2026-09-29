# S03_Constants_Strings_Random_Exceptions - Lesson: Constants/variables, string handling, random numbers and exception handling

## Goal
The learner distinguishes constants from variables, uses string-handling operations, generates random numbers, and uses exception handling.

## Syllabus items taught here
- 4.1.1.6 - Constants and variables
- 4.1.1.7 - String-handling operations: length, position, substring, concatenation, character/string conversion
- 4.1.1.8 - Random number generation
- 4.1.1.9 - Exception handling

## How to teach this
Ask the learner what should happen if a program asks the user to enter a number, but they type letters instead -- crash, or handle it gracefully? AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.1.1.6 Constants and variables
A **constant** is named like a variable but its value is fixed once set and cannot change during execution; a **variable**'s value can change. Named constants (e.g. `VAT_RATE = 0.2`) make code clearer and easier to update safely (change it in one place) than a "magic number" scattered through the code.

#### 4.1.1.7 String-handling operations: length, position, substring, concatenation, character/string conversion
**String-handling operations**: **length** (`len(s)`), **position** (finding where a substring occurs, e.g. `s.find("lo")`), **substring** (extracting part of a string, e.g. `s[1:4]`), **concatenation** (joining strings with `+`), **character/code conversion** (converting a character to its numeric code and back, e.g. Python's `ord('A')` = 65 and `chr(65)` = 'A'), and **string conversion** (e.g. converting a number to a string with `str(42)`, or a numeric string to a number with `int("42")`).

#### 4.1.1.8 Random number generation
**Random number generation** produces (pseudo-)random values within a program, e.g. Python's `random.randint(1, 6)` for a die roll. It is used for simulations, games, testing with varied data, and cryptographic applications (where a cryptographically secure generator is needed, not a general-purpose one).

#### 4.1.1.9 Exception handling
**Exception handling** lets a program detect and respond to a runtime error (e.g. dividing by zero, converting non-numeric text to a number, opening a file that doesn't exist) without crashing. A `TRY ... CATCH` (or Python's `try ... except`) block attempts code that might fail, and runs alternative/recovery code if a specific exception is **raised** (thrown), e.g. re-prompting the user for valid input instead of terminating.

## Explicitly not here
Subroutines, and where variables live during a subroutine call, are S04.

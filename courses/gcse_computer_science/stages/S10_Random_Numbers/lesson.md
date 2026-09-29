# S10_Random_Numbers - Lesson: Random number generation

## Goal
The learner uses random number generation in a program.

## Syllabus items taught here
- 3.2.9 - Random number generation

## How to teach this
Ask the learner how a simple dice-rolling program could produce a different number each time it runs. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.9 Random number generation
**Random number generation** produces an unpredictable value within a given range each time a program runs, used for things like dice-rolling games, shuffling, simulations and generating test data. In Python, `random.randint(a, b)` returns a random whole number between `a` and `b` inclusive (both ends possible); the `random` module must be imported first (`import random`). *Example:* `random.randint(1, 6)` simulates rolling a standard six-sided die.

## Explicitly not here
Subroutines and structured programming are S11.

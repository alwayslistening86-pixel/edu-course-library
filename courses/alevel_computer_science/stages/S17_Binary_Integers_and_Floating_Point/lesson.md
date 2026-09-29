# S17_Binary_Integers_and_Floating_Point - Lesson: Unsigned and signed (two's complement) binary integers, and floating point

## Goal
The learner performs unsigned binary arithmetic, represents signed integers using two's complement, and explains floating-point representation, normalisation and its associated errors.

## Syllabus items taught here
- 4.5.4.1 - Unsigned binary and binary arithmetic
- 4.5.4.3 - Signed binary using two's complement
- 4.5.4.4 - Floating point: normalisation, range, precision, rounding, underflow and overflow

## How to teach this
Ask the learner how a computer, which only stores 0s and 1s, can represent a negative number at all -- there's no minus sign in binary. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.5.4.1 Unsigned binary and binary arithmetic
**Unsigned binary** represents only non-negative integers directly as their binary value (e.g. an 8-bit unsigned byte ranges 0 to 255). **Unsigned binary arithmetic** (addition) works like column addition in decimal, but carries at 2 rather than 10: *example*, 00000111 (7) + 00000101 (5): 111+101 = 1100 -> 00001100 (12). If an addition needs more bits than are available (a carry out of the leftmost bit), this is an **overflow** -- the result is wrong/wrapped, because it no longer fits in the available bits.

#### 4.5.4.3 Signed binary using two's complement
**Two's complement** represents signed integers so that the leftmost bit indicates sign (0 = non-negative, 1 = negative) and ordinary binary addition still works correctly for both positive and negative numbers, without needing separate subtraction logic. To negate a value: **invert every bit**, then **add 1**. *Example:* -58 in 8-bit two's complement: 58 = 00111010; invert -> 11000101; add 1 -> 11000110. To convert a two's complement pattern back to its signed decimal value, the leftmost bit's place value is negative: e.g. 11000110 = -128+64+4+2 = -58, confirming the conversion.

#### 4.5.4.4 Floating point: normalisation, range, precision, rounding, underflow and overflow
A **floating-point** representation stores a real (fractional) number as a **mantissa** (the significant digits) and an **exponent** (how far, and which way, to shift the binary point), unlike **fixed-point**, where the binary point's position is fixed in advance (limiting range or precision). **Normalisation** adjusts the mantissa/exponent pair to a standard form (e.g. so the mantissa starts `0.1...`) so every value has one unique representation. *Example:* 5.75 in binary is 101.11; normalised, this is written as mantissa 0.10111 with exponent +3 (0.10111 x 2^3 = 0.71875 x 8 = 5.75). A larger **range** (largest/smallest representable magnitude) needs more exponent bits; a finer **precision** (how close together representable values are) needs more mantissa bits -- for a fixed total number of bits, range and precision trade off against each other. **Rounding errors** occur because most real numbers cannot be represented exactly in a finite number of bits, so the stored value is only the closest representable one. **Underflow** occurs when a number is too small in magnitude to be represented (rounds to zero); **overflow** occurs when a number is too large in magnitude for the available exponent range to represent at all.

## Explicitly not here
How individual characters, images and sound are represented is S18-S19.

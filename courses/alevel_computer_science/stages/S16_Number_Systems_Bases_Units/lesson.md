# S16_Number_Systems_Bases_Units - Lesson: Number systems, number bases and units of information

## Goal
The learner classifies number systems (natural, integer, rational, irrational, real, ordinal), converts between number bases, and uses units of information.

## Syllabus items taught here
- 4.5.1.1 - Number systems: natural, integer, rational, irrational, real and ordinal numbers
- 4.5.2.1 - Number bases
- 4.5.3.1 - Units of information

## How to teach this
Ask the learner: is -3 a natural number? Is 1/2? Is the square root of 2? -- these questions sort numbers into different number systems. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.5.1.1 Number systems: natural, integer, rational, irrational, real and ordinal numbers
**Natural numbers** are the non-negative whole numbers used for counting (0, 1, 2, 3, ...; some definitions start at 1). **Integers** extend these to include negative whole numbers (..., -2, -1, 0, 1, 2, ...). **Rational numbers** are any number that can be written as a fraction of two integers (e.g. 1/2, -3, 0.75 = 3/4); **irrational numbers** cannot (e.g. pi, the square root of 2) -- their decimal expansion never terminates or repeats. **Real numbers** are all rational and irrational numbers together (every point on the number line). **Ordinal numbers** describe position/order in a sequence (1st, 2nd, 3rd, ...) rather than a quantity (a **cardinal** number, like 1, 2, 3, which is what "counting and measurement" normally means).

#### 4.5.2.1 Number bases
A **number base** is the number of distinct digits used before a column's place value increases, and how many units of one place equal one unit of the next. **Denary (base 10, decimal)** uses digits 0-9; **binary (base 2)** uses 0-1; **hexadecimal (base 16)** uses 0-9 then A-F (representing 10-15) -- one hex digit represents exactly four binary bits (a nibble), which is why hex is a compact, human-friendly way to write binary. *Example:* binary 01111011 = decimal 64+32+16+8+2+1 = 123; the same binary split into nibbles 0111 and 1011 gives hex 7 and B, i.e. 0x7B.

#### 4.5.3.1 Units of information
**Units of information**: a **bit** is a single binary digit (0 or 1); a **byte** is 8 bits. Larger (decimal/SI) units scale by 1,000: 1 kilobyte (kB) = 1,000 bytes, 1 megabyte (MB) = 1,000 kB, 1 gigabyte (GB) = 1,000 MB, 1 terabyte (TB) = 1,000 GB. (Binary-based units, kibibyte KiB = 1,024 bytes etc., also exist but are not the convention used by this course -- see the standing notice.)

## Explicitly not here
How integers are actually represented and manipulated in binary (unsigned arithmetic, two's complement, floating point) is S17.

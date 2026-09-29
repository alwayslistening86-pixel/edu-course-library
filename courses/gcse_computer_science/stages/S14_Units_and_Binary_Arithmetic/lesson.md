# S14_Units_and_Binary_Arithmetic - Lesson: Units of information and binary arithmetic

## Goal
The learner knows that a bit is the fundamental unit of information and a byte is 8 bits, uses the kilo/mega/giga/tera prefixes to compare quantities of bytes, adds up to three binary numbers, and applies and explains binary shifts.

## Syllabus items taught here
- 3.3.3 - Units of information
- 3.3.4 - Binary arithmetic and binary shifts

## How to teach this
Ask the learner: if a photo is 4 megabytes and a song is 4,500 kilobytes, which file is bigger? Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.3 Units of information
A **bit** (binary digit) is the fundamental, smallest unit of information a computer stores, either 0 or 1. A **byte** is a group of 8 bits. Larger quantities are described with prefixes, each 1,000 times the one before (AQA uses the standard decimal/SI values): 1 **kilobyte (KB)** = 1,000 bytes; 1 **megabyte (MB)** = 1,000 KB = 1,000,000 bytes; 1 **gigabyte (GB)** = 1,000 MB; 1 **terabyte (TB)** = 1,000 GB. To compare quantities given in different prefixes, convert them to the same unit first: *example:* 2 MB = 2,000 KB, which is larger than 1,900 KB.

#### 3.3.4 Binary arithmetic and binary shifts
**Binary addition**: add up to three binary numbers the same way as decimal column addition, carrying into the next column whenever a column's total reaches 2 or more. *Example:* 01101101 + 00111001 = 10100110 (i.e. 109 + 57 = 166); adding a third number, 00000101 + 00000011 + 00000010 = 00001010 (i.e. 5+3+2=10). If the true sum needs more bits than are available, an **overflow** occurs and the extra bit is lost, giving a wrong result -- this is why the number of bits available limits the largest value that can be stored. **Binary shifts** move every bit left or right by a set number of places, filling the vacated places with 0: a **left shift** by n places multiplies the (unsigned) value by 2^n, e.g. 00001101 shifted left 2 places gives 00110100, i.e. 13 x 4 = 52; a **right shift** by n places divides the value by 2^n (discarding any remainder), e.g. 00110100 shifted right 2 places gives 00001101, i.e. 52 / 4 = 13. Binary shifts are used for fast multiplication/division by powers of two, and for manipulating individual bits within a byte (e.g. extracting or packing data).

## Explicitly not here
How individual characters are encoded into binary is S15.

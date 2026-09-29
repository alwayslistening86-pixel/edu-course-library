# S13_Number_Bases_and_Conversion - Lesson: Number bases and conversion

## Goal
The learner understands decimal, binary and hexadecimal, explains why computers use binary and why hexadecimal is often used, and converts between binary, decimal and hexadecimal in both directions.

## Syllabus items taught here
- 3.3.1 - Number bases: decimal, binary and hexadecimal
- 3.3.2 - Converting between number bases

## How to teach this
Ask the learner to count on their fingers past 9 -- computers can't do that; they only ever have two 'fingers', off and on. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.1 Number bases: decimal, binary and hexadecimal
Humans normally count in **decimal (base 10)**, using ten digits (0-9), where each column's place value is a power of 10. Computers use **binary (base 2)**, using only two digits (0 and 1, called bits), because their electronic circuits only reliably distinguish two states (roughly: off/low voltage and on/high voltage); every kind of data and every instruction a computer handles is ultimately represented as binary. **Hexadecimal (base 16)** uses sixteen symbols (0-9, then A-F for ten to fifteen); it is used often in computer science as a compact, human-friendly way to write binary values, because each hexadecimal digit represents exactly 4 bits (a "nibble"), so a whole byte can be written with just two hex digits instead of eight binary digits -- e.g. memory addresses and colour codes are usually shown in hexadecimal because it is far easier for a person to read and less error-prone to copy than long strings of 1s and 0s.

#### 3.3.2 Converting between number bases
**Binary to decimal**: each bit position (from the right, starting at 0) has place value 2^position (1, 2, 4, 8, 16, 32, 64, 128 for an 8-bit number); add the place values where the bit is 1. *Example:* 01011010 = 64+16+8+2 = 90 in decimal. **Decimal to binary**: repeatedly find the largest power of 2 that fits, or repeatedly divide by 2 and record the remainders from last to first. *Example:* 205 in decimal: 205-128=77, 77-64=13, 13-8=5, 5-4=1, 1-1=0, so bits are set at 128,64,8,4,1, giving 11001101. **Binary to hexadecimal**: split the binary number into groups of 4 bits (nibbles) from the right, and convert each nibble to its hex digit. *Example:* 10110110 splits into 1011 and 0110, which are 11 and 6 in decimal, i.e. hex digits B and 6, so 10110110 = 0xB6. **Hexadecimal to binary** reverses this: convert each hex digit to its 4-bit binary group and join them. **Decimal to/from hexadecimal** can go via binary, or by repeatedly dividing by 16 and recording remainders (using A-F for remainders 10-15). *Example:* decimal 205 = 0xCD = binary 11001101.

## Explicitly not here
How much data those bits represent in total (bytes, kilobytes, ...) is S14.

# S18_Character_Coding_and_Error_Checking - Test: Character encoding and error checking/correction

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why Unicode was needed in addition to ASCII. [3 marks]
2. A byte is transmitted using odd parity. The received byte is 01100100. Determine whether a (single-bit) error has been detected, showing your working. [3 marks]
3. Explain the general idea behind a checksum, and one limitation of using a simple parity bit for error checking. [3 marks]
4. Why is UTF-8 described as backward-compatible with ASCII? Choose every correct option.
   A. the first 128 Unicode code points, encoded in UTF-8, use exactly the same single-byte values as ASCII
   B. UTF-8 only supports the English alphabet
   C. UTF-8 always uses exactly 4 bytes per character, the same as ASCII
   D. ASCII files cannot be opened by any Unicode-aware program

## Answer key (for the tutor only)
1. [3] B1 ASCII only represents a small, fixed set of characters (128 or 256), sufficient mainly for English text; B1 Unicode represents a vastly larger set, covering virtually every writing system and symbol (including emoji) in use; B1 Unicode's first 128 code points match ASCII, so existing ASCII text remains valid under Unicode.
2. [3] M1 count the 1-bits in 01100100: three 1-bits (0,1,1,0,0,1,0,0 -- three 1s), which is odd; M1 under odd-parity, an odd count of 1-bits (including the parity bit) is expected, i.e. no error signalled by this check; A1 no error detected by this parity check (though parity cannot detect an even number of bit-flips, e.g. two errors, so this is not a guarantee the byte is correct).
3. [3] B1 a checksum combines (e.g. sums) blocks of the data into a single check value sent alongside it; the receiver repeats the calculation and compares, detecting most transmission errors; B1 a simple parity bit only reliably detects an odd number of bit-flips -- an even number of flips (e.g. two) can cancel out and go undetected; B1 a parity bit also cannot say which bit is wrong, only that an error occurred (no correction, only detection).
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S18_Character_Coding_and_Error_Checking` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S19_Analogue_Digital_and_Multimedia.

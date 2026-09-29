# S13_Number_Bases_and_Conversion - Test: Number bases and conversion

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Convert the 8-bit binary number 10010110 to decimal, showing your working. [2 marks]
2. Convert 200 decimal to 8-bit binary, showing your working. [2 marks]
3. Convert 10101110 to hexadecimal, showing your working. [3 marks]
4. Convert hexadecimal 3F to decimal, showing your working. [2 marks]
5. Explain why computer scientists often use hexadecimal rather than binary when writing things like memory addresses or colour codes. [3 marks]
6. Why do computers represent all data using binary rather than decimal? Choose every correct option.
   A. their electronic circuits reliably distinguish only two states (off/on)
   B. binary numbers are shorter to write than decimal numbers
   C. hexadecimal cannot be converted to decimal
   D. binary is easier for humans to read

## Answer key (for the tutor only)
1. [2] M1 correct place values identified; A1 = 150.
2. [2] M1 valid method shown; A1 11001000.
3. [3] M1 splits into two 4-bit nibbles 1010 and 1110; M1 converts each to decimal 10 and 14; A1 0xAE.
4. [2] M1 3 x 16 + 15; A1 = 63.
5. [3] B1 a hex digit represents exactly 4 bits (a nibble), so a byte needs only 2 hex digits instead of 8 binary digits; B1 this is far shorter/easier for a person to read and write correctly; B1 it reduces the risk of transcription errors compared with long strings of 1s and 0s.
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Number_Bases_and_Conversion` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Units_and_Binary_Arithmetic.

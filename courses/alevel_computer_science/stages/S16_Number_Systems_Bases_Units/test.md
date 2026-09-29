# S16_Number_Systems_Bases_Units - Test: Number systems, number bases and units of information

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Convert 10110110 (binary) to decimal and to hexadecimal, showing your working. [3 marks]
2. Explain the difference between a rational number and an irrational number, with one example of each. [2 marks]
3. A file is stated as 4.2 GB. Using this course's decimal (SI) units, state how many MB this is, and how many kB. [2 marks]
4. Which correctly converts hexadecimal 0x2F to binary? Choose every correct option.
   A. `00101111`
   B. `00110010`
   C. `00101110`
   D. `01001111`

## Answer key (for the tutor only)
1. [3] M1 decimal: 128+32+16+4+2 = 182; M1 hex nibbles: 1011=B, 0110=6; A1 0xB6.
2. [2] B1 a rational number can be written as a fraction of two integers, e.g. 3/4; B1 an irrational number cannot, e.g. pi (its decimal expansion never terminates or repeats).
3. [2] B1 4.2 GB = 4,200 MB; B1 4,200 MB = 4,200,000 kB.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_Number_Systems_Bases_Units` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S17_Binary_Integers_and_Floating_Point.

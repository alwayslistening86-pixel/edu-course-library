# S20_Hardware_Software_Languages_Logic - Test: Hardware/software/the OS, language classification and translators, logic gates and Boolean algebra

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain two ways the operating system manages a computer's resources between multiple running programs. [2 marks]
2. Explain the difference between a compiler and an interpreter, including one advantage of each. [4 marks]
3. Draw the truth table for the XOR gate, and state the one row where XOR and OR give different outputs. [3 marks]
4. Using Boolean algebra (or a truth table), show that A + (A.B) simplifies to A. [3 marks]
5. Which logic gate's output is 1 only when both of its inputs are 0? Choose every correct option.
   A. `NOR`
   B. `NAND`
   C. `XOR`
   D. `AND`

## Answer key (for the tutor only)
1. [2] B1 any valid example, e.g. scheduling processor time between programs so each gets a fair share; B1 a second valid example, e.g. managing memory allocation, or arbitrating access to shared peripherals like a printer.
2. [4] B1 a compiler translates the whole program into machine code in advance, producing a standalone executable; B1 advantage: the compiled program runs fast, since translation is already done; B1 an interpreter translates and executes the program line by line at run time, with no separate executable produced; B1 advantage: faster to test/debug changes, since there is no separate compile step before running.
3. [3] B1 correct XOR truth table: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->0; B1 OR's truth table gives (1,1)->1, differing from XOR here; B1 correctly identifies (1,1) as the differing row (both inputs 1: OR gives 1, XOR gives 0).
4. [3] M1 truth table or algebraic approach set out; M1 all four combinations of A,B checked (or the absorption law A + (A.B) = A applied and justified); A1 correctly concludes A + (A.B) = A in every case.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S20_Hardware_Software_Languages_Logic` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S21_Components_Stored_Program_Processor.

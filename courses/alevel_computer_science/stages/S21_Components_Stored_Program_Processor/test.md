# S21_Components_Stored_Program_Processor - Test: Internal hardware components, the stored program concept and processor structure

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. State the role of the program counter and the current instruction register. [2 marks]
2. Explain the difference between a general-purpose register and a dedicated register, giving one example of each. [3 marks]
3. Explain the role of the control unit in the processor. [2 marks]
4. Explain why the stored program concept allows a single computer to run many different programs without being physically rewired. [2 marks]
5. Which register holds the data just read from (or about to be written to) the address currently being accessed? Choose every correct option.
   A. the memory buffer/data register
   B. the program counter
   C. the current instruction register
   D. the status register

## Answer key (for the tutor only)
1. [2] B1 the program counter holds the address of the next instruction to be fetched; B1 the current instruction register holds the instruction currently being decoded/executed.
2. [3] B1 a general-purpose register holds data/addresses temporarily for the ALU's use, for any purpose the running program needs; B1 a dedicated register has one specific, fixed role in the processor's own operation; B1 example of a dedicated register, e.g. the memory address register (holds the address currently being accessed).
3. [2] B1 it directs the fetch-execute cycle, decoding fetched instructions; B1 it generates the control signals needed to carry each instruction out, coordinating the other components (ALU, registers, buses).
4. [2] B1 both instructions and data live in the same main memory and are treated alike (as stored, fetchable binary values); B1 running a different program is just a matter of loading different instructions into memory, not changing the physical hardware.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S21_Components_Stored_Program_Processor` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S22_Fetch_Execute_Interrupts_External_Devices.

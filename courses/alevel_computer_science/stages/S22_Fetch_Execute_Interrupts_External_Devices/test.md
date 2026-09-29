# S22_Fetch_Execute_Interrupts_External_Devices - Test: The fetch-execute cycle, interrupts, processor performance and external devices

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe what happens during the fetch stage of the fetch-execute cycle. [3 marks]
2. Explain the difference between immediate addressing and direct addressing. [2 marks]
3. Describe what happens when a processor receives an interrupt while running a program. [4 marks]
4. Explain two factors, other than clock speed, that affect a processor's performance. [4 marks]
5. Which device is best suited to reading data from a contactless access card using radio signals? Choose every correct option.
   A. an RFID reader
   B. a laser printer
   C. a barcode reader
   D. `an optical (DVD/Blu-ray) drive`

## Answer key (for the tutor only)
1. [3] B1 the address in the program counter is copied to the memory address register; B1 the instruction at that address is read from memory into the memory buffer register (and then the current instruction register); B1 the program counter is incremented, ready to fetch the next instruction next time.
2. [2] B1 immediate addressing uses the operand's value directly as the data to use; B1 direct addressing uses the operand as a memory address, and the actual value is fetched from that address.
3. [4] B1 the interrupt is detected/checked for at the end of the current fetch-execute cycle; B1 the processor saves its current state (so it can resume correctly later); B1 an interrupt service routine (ISR) runs to handle the interrupt; B1 the processor restores its saved state and resumes the interrupted program where it left off.
4. [4] B1 number of cores: more cores allow genuinely simultaneous execution of multiple instruction streams; B1 correctly explained; B1 cache memory: small, very fast memory holding frequently/recently used data, avoiding slower main-memory access; B1 (or word length/bus width: more bits processed/transferred per cycle) correctly explained -- award any two of these factors, each fully explained.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S22_Fetch_Execute_Interrupts_External_Devices` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S23_Consequences_of_Computing.

# S22_Systems_Architecture - Test: Systems architecture: CPU, memory, storage, embedded systems

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe the four steps of the fetch-execute cycle. [4 marks]
2. Explain the effect of increasing cache size on CPU performance. [3 marks]
3. Explain why a computer needs secondary storage as well as RAM. [3 marks]
4. Compare solid-state storage with magnetic storage, giving one advantage and one disadvantage of solid-state storage relative to magnetic. [3 marks]
5. Explain what an embedded system is, giving an example, and how it differs from a general-purpose computer. [3 marks]
6. Which factor would most directly increase how many processing cycles a CPU can perform each second? Choose every correct option.
   A. increasing the clock speed
   B. increasing the amount of ROM
   C. increasing the size of secondary storage
   D. switching from magnetic to optical storage

## Answer key (for the tutor only)
1. [4] B1 fetch: the next instruction is fetched from the memory address held in the Program Counter; B1 the Program Counter is incremented to point to the next instruction; B1 decode: the fetched instruction is decoded (interpreted); B1 execute: the instruction is carried out (e.g. by the ALU), then the cycle repeats.
2. [3] B1 cache is small, very fast memory holding frequently/recently used data and instructions; B1 a larger cache means more of what the CPU needs is likely to be found there rather than fetched from slower main memory; B1 this reduces the time spent waiting for data, improving overall performance.
3. [3] B1 RAM is volatile -- its contents are lost when the power is removed; B1 RAM is also comparatively small/expensive for the amounts of data typically needed long-term; B1 secondary storage is non-volatile, so files/programs/the OS can be kept permanently even when the computer is switched off.
4. [3] B1 advantage: no moving parts, so faster access and more durable/shock-resistant; B1 disadvantage: more expensive per gigabyte (and each cell has a limited number of write cycles); B1 magnetic storage explained as the comparison (spinning disk/moving head, cheaper per GB, slower, parts can wear/fail).
5. [3] B1 a computer system built into a larger device to perform one specific, dedicated function; B1 example, e.g. a washing machine controller, a digital thermometer, engine management system; B1 unlike a general-purpose computer, it is not designed to run a wide range of different applications chosen by the user.
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S22_Systems_Architecture` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S23_Network_Fundamentals_and_Topologies.

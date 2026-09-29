# S19_Hardware_Software_Classification - Test: Hardware, software and software classification

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between hardware and software, and how they depend on each other. [3 marks]
2. Give one example of system software and one example of application software, and explain the difference between the two categories. [3 marks]
3. Describe two functions of an operating system. [4 marks]
4. Which of these is an example of a utility program? Choose every correct option.
   A. disk defragmentation software
   B. a web browser
   C. a spreadsheet application
   D. a computer game

## Answer key (for the tutor only)
1. [3] B1 hardware is the physical, tangible parts of a computer system; B1 software is the programs/instructions that run on it and cannot be touched; B1 hardware needs software to be told what to do, and software needs hardware to run on -- neither is useful alone.
2. [3] B1 system software example, e.g. an operating system or a utility program (antivirus, disk clean-up); B1 application software example, e.g. a word processor, browser or game; B1 system software manages/supports the computer itself so applications and the user can use it, while application software lets the user do a specific task/produce specific work.
3. [4] B2 manages the processor (deciding which program runs when); B2 manages memory (allocating/reclaiming RAM for running programs); B2 manages input/output devices (via drivers); B2 runs applications; B2 provides security (accounts/permissions/passwords) -- any 2 for full marks (2 marks each: named function plus brief explanation).
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S19_Hardware_Software_Classification` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S20_Boolean_Logic.

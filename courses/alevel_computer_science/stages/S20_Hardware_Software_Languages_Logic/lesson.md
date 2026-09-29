# S20_Hardware_Software_Languages_Logic - Lesson: Hardware/software/the OS, language classification and translators, logic gates and Boolean algebra

## Goal
The learner explains hardware/software/the operating system's role, classifies programming languages and translators, and uses logic gates and Boolean algebra.

## Syllabus items taught here
- 4.6.1.1 - Hardware, software and the operating system
- 4.6.2.1 - Classification of programming languages and translators
- 4.6.4.1 - Logic gates and Boolean algebra

## How to teach this
Ask the learner: when several programs are open at once, what decides which one gets to use the processor, the screen, or the printer right now? AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.6.1.1 Hardware, software and the operating system
**Hardware** is the physical components of a computer system; **software** is the programs that run on it -- hardware executes software's instructions, and software is meaningless without hardware to run it on. Software is classified as **system software** (manages the computer itself and supports other software, e.g. the operating system, utilities, device drivers, translators) or **application software** (lets the user perform specific tasks, e.g. a word processor, a game). The **operating system (OS)** is the key piece of system software: it manages hardware resources (processor time, memory, storage, peripherals) between competing demands from multiple running programs, provides a user interface, handles file storage/security, and offers a consistent set of services so application software doesn't need to control hardware directly.

#### 4.6.2.1 Classification of programming languages and translators
Programming languages are classified as **low-level** (machine code: raw binary instructions the processor executes directly; and assembly language: a human-readable mnemonic form of machine code, translated one-to-one) or **high-level** (closer to human/mathematical language, e.g. Python, more portable across different processor types, but needing translation before the processor can run it). A **translator** converts high-level (or assembly) code into a form the processor can execute: a **compiler** translates the whole program into machine code in advance, producing a standalone executable that runs fast but must be recompiled for a different platform; an **interpreter** translates and executes the program line by line at run time, without producing a separate executable, making testing/debugging faster but execution slower; an **assembler** translates assembly language directly into machine code.

#### 4.6.4.1 Logic gates and Boolean algebra
A **logic gate** implements one basic Boolean operation on binary inputs: **AND** (output 1 only if both inputs are 1), **OR** (output 1 if at least one input is 1), **NOT** (inverts a single input), **NAND** (AND then inverted), **NOR** (OR then inverted), **XOR** (1 only if inputs differ). A **truth table** lists every combination of inputs and the resulting output. **Boolean algebra** manipulates these operations symbolically (AND as `.`, OR as `+`, NOT as `'` or a bar) to simplify logic expressions/circuits; a key law is **absorption**: `(A.B) + (A.B') = A` (whatever B is, ANDing with A then combining both cases with OR always just gives A back) -- verified by checking all four input combinations for A and B give the same output as A alone.

## Explicitly not here
The internal hardware components and how the processor actually executes instructions are S21-S22.

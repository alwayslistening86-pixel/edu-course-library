# S21_Components_Stored_Program_Processor - Lesson: Internal hardware components, the stored program concept and processor structure

## Goal
The learner describes the internal hardware components of a computer system, the stored program concept, and the structure of the processor and its registers.

## Syllabus items taught here
- 4.7.1.1 - Internal hardware components and the stored program concept
- 4.7.3.1 - Processor structure: ALU, control unit, clock and registers

## How to teach this
Ask the learner: if instructions and data are both stored together in the same memory, how does the processor know which is which at any given moment? AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.7.1.1 Internal hardware components and the stored program concept
A computer's basic internal components: the **processor** (executes instructions), **main memory** (holds the currently running program's instructions and data), and **buses** connecting them -- the **address bus** (carries the memory address being accessed), the **data bus** (carries the actual data/instruction being transferred) and the **control bus** (carries control signals, e.g. read/write). **I/O controllers** manage communication between the processor/memory and peripheral devices. The **stored program concept**: both a program's machine-code instructions and the data it works on are held together in main memory, and instructions are fetched and executed **serially** (one after another) by the processor -- this is what allows a general-purpose computer to run any program, simply by loading different instructions into memory, rather than being physically rewired for each new task.

#### 4.7.3.1 Processor structure: ALU, control unit, clock and registers
The processor contains the **arithmetic logic unit (ALU)** (performs arithmetic and logical operations), the **control unit (CU)** (directs the fetch-execute cycle, decoding instructions and generating the control signals to carry them out) and a **clock** (generates regular pulses that synchronise the processor's operations). **General-purpose registers** hold data/addresses temporarily for the ALU to use. **Dedicated registers** each have one specific role: the **program counter (PC)** holds the address of the next instruction to be fetched; the **current instruction register (CIR)** holds the instruction currently being decoded/executed; the **memory address register (MAR)** holds the address currently being accessed in memory; the **memory buffer/data register (MBR/MDR)** holds the data just read from (or about to be written to) that address; the **status register** holds flag bits recording the outcome of the last operation (e.g. whether it produced zero, a carry, or overflow).

## Explicitly not here
How these components actually cooperate to fetch and execute a single instruction, plus interrupts and performance, is S22.

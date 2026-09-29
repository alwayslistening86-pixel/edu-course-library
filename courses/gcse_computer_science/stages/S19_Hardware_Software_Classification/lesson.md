# S19_Hardware_Software_Classification - Lesson: Hardware, software and software classification

## Goal
The learner defines hardware and software and their relationship, and explains system software vs application software (including the need for, and functions of, operating systems and utility programs).

## Syllabus items taught here
- 3.4.1 - Hardware and software
- 3.4.3 - Software classification: system and application software

## How to teach this
Ask the learner: if you drop a laptop, what breaks -- and is that the same thing as the programs installed on it? Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.4.1 Hardware and software
**Hardware** is the physical, tangible parts of a computer system that can be touched (e.g. the CPU, RAM, hard disk, keyboard, monitor). **Software** is the programs and instructions that run on that hardware and tell it what to do; it cannot be touched. The two depend on each other: hardware is useless without software to give it instructions, and software cannot run without hardware to execute it on.

#### 3.4.3 Software classification: system and application software
**System software** manages and supports the computer system itself, so that application software and the user can work with the hardware, e.g. the operating system and utility programs. **Application software** lets a user carry out a specific task or produce specific work, e.g. a word processor, a web browser, a game. An **operating system (OS)** (e.g. Windows, macOS, Linux, Android) manages the computer's resources and provides a way for the user and applications to interact with the hardware: it manages the **processor** (deciding which program gets CPU time and when), **memory** (allocating RAM to running programs and reclaiming it when they close), **input/output devices** (via device drivers, so software doesn't need to know the exact hardware details), runs **applications** (loading, running and closing programs), and handles **security** (user accounts, permissions, passwords). **Utility programs** are system software that carry out specific maintenance or support tasks rather than user tasks, e.g. anti-virus software, disk defragmentation/clean-up tools, file compression tools, backup software.

## Explicitly not here
How circuits inside that hardware make logical decisions is S20.

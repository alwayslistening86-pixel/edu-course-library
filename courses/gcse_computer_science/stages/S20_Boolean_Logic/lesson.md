# S20_Boolean_Logic - Lesson: Boolean logic: truth tables, gates and circuits

## Goal
The learner constructs and interprets truth tables for NOT, AND, OR and XOR gates and simple combinations of them, and creates and interprets simple logic circuit diagrams and Boolean expressions, converting between the two.

## Syllabus items taught here
- 3.4.2 - Boolean logic: truth tables, logic gates and circuits

## How to teach this
Ask the learner: a porch light should switch on if it's dark AND (a motion sensor triggers OR a manual switch is pressed) -- how would a circuit decide that? Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.4.2 Boolean logic: truth tables, logic gates and circuits
A **logic gate** is a circuit that takes one or more binary (0/1, i.e. False/True) inputs and produces a single binary output according to a fixed rule; a **truth table** lists the output for every possible combination of inputs. **NOT** (one input, inverts it): `A=0 -> out 1`, `A=1 -> out 0`. **AND** (output 1 only if both inputs are 1): `A=0,B=0->0`; `A=0,B=1->0`; `A=1,B=0->0`; `A=1,B=1->1`. **OR** (output 1 if at least one input is 1): `A=0,B=0->0`; `A=0,B=1->1`; `A=1,B=0->1`; `A=1,B=1->1`. **XOR** (exclusive or; output 1 only if the inputs differ): `A=0,B=0->0`; `A=0,B=1->1`; `A=1,B=0->1`; `A=1,B=1->0`. Gates can be combined into **logic circuits**, and every circuit corresponds to a **Boolean expression** (e.g. AND written as `.`, OR as `+`, NOT as a bar or `NOT`), so a circuit can be converted to an expression (trace the wiring through each gate) and an expression can be converted to a circuit (draw one gate per operator, wiring outputs to the next gate's inputs) -- and either can be used to build the combined truth table. *Worked example:* the expression `(A AND B) OR (NOT C)` for all 8 combinations of A, B, C: `A=0,B=0,C=0: (0)OR(1)=1`; `A=0,B=0,C=1: (0)OR(0)=0`; `A=0,B=1,C=0: (0)OR(1)=1`; `A=0,B=1,C=1: (0)OR(0)=0`; `A=1,B=0,C=0: (0)OR(1)=1`; `A=1,B=0,C=1: (0)OR(0)=0`; `A=1,B=1,C=0: (1)OR(1)=1`; `A=1,B=1,C=1: (1)OR(0)=1`.

## Explicitly not here
Software classification is S19; how instructions like these are actually written and translated for a real computer is S21.

## Further resources (optional)

These are optional, hand-picked, externally hosted resources -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **AQA GCSE (8525) SLR11 - 3.4 Truth tables (Craig'n'Dave)** (https://www.youtube.com/watch?v=ElCMxOKNJUw) -- Board-matched to AQA 8525. Builds truth tables for AND/OR/NOT step by step -- useful for checking a hand-built truth table against a worked one.

# S15_Software_Development_Lifecycle - Lesson: The systematic approach to problem solving: analysis, design, implementation, testing, evaluation

## Goal
The learner explains the systematic approach to problem solving: analysis, design, implementation, testing and evaluation, including where an iterative/agile approach fits.

## Syllabus items taught here
- 4.13.1.1 - Analysis
- 4.13.1.2 - Design
- 4.13.1.3 - Implementation
- 4.13.1.4 - Testing
- 4.13.1.5 - Evaluation

## How to teach this
Ask the learner what could go wrong if a team started writing code before agreeing what the program actually needs to do. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.13.1.1 Analysis
**Analysis**: before a problem can be solved, it must be clearly defined and the requirements of the system that will solve it established, usually by interacting directly with its intended users; a **data model** of the information involved is created. Requirements may be clarified iteratively through **prototyping** or an **agile approach** (building and refining a rough working version with the users, rather than trying to specify everything perfectly up front).

#### 4.13.1.2 Design
**Design**: before building the solution, it is planned and specified -- designing the data structures for the data model, designing the algorithms that will process that data, designing an appropriate modular structure for the whole solution (e.g. breaking it into subroutines/classes), and designing the human-computer interface. Like analysis, design can itself be iterative, using prototyping/an agile approach rather than a single fixed design produced once.

#### 4.13.1.3 Implementation
**Implementation**: the designed models and algorithms are turned into actual data structures and code that a computer can run. The final solution may also be reached iteratively, using prototyping/an agile approach, with a focus on solving the **critical path** (the core, most important functionality) first, before less essential features.

#### 4.13.1.4 Testing
**Testing**: the implementation is tested for errors, using carefully selected **test data** covering **normal** (typical, expected) data, **boundary** (data right at the edge of what's valid) data, and **erroneous** (invalid) data, to check the program behaves correctly in each case. It should also undergo **acceptance testing** with the system's intended users, to check the finished solution genuinely meets what was specified during analysis.

#### 4.13.1.5 Evaluation
**Evaluation**: the finished system is judged against criteria such as whether it meets the original requirements, is efficient (in time/space), is usable, is robust (handles errors/invalid input gracefully), and is maintainable (easy for someone else to understand and later modify). Evaluation may lead back into further analysis/design/implementation if shortcomings are found -- the whole process (4.13.1.1-4.13.1.5) is not always strictly one-way, especially where an iterative/agile approach is used throughout.

## Explicitly not here
This is the last Paper 1 stage; S16 begins Paper 2's data representation content.

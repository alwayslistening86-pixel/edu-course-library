# S08_Input_Output - Lesson: Input and output

## Goal
The learner obtains user input from the keyboard and outputs data and information from a program.

## Syllabus items taught here
- 3.2.7 - Input/output

## How to teach this
Ask the learner: if a program needs to know the user's name before greeting them, where does that name come from, and where does the greeting go? Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.7 Input/output
**Input** brings data into a running program, typically from the keyboard (Python's `input()` reads a line of text typed by the user and always returns it as a string, so it usually needs converting, e.g. `int(input(...))`, before it can be used in arithmetic). **Output** sends data or information out of the program, typically to the screen (Python's `print()`), so the user can see results.

## Explicitly not here
Turning that text into other data types, and manipulating strings, is S09.

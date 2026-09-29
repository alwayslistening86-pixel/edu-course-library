# S12_Robust_Secure_Programming - Lesson: Robust and secure programming: validation, authentication, testing

## Goal
The learner writes data validation and authentication routines, understands testing, corrects errors, distinguishes normal/boundary/erroneous test data and syntax/logic errors, and selects and justifies suitable test data.

## Syllabus items taught here
- 3.2.11 - Robust and secure programming: validation, authentication, testing, errors

## How to teach this
Ask the learner what should happen if a program asking for an age between 0 and 120 is instead given -5, or the word 'banana'. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.11 Robust and secure programming: validation, authentication, testing, errors
**Validation** is an automatic check, done by the program itself, that input data is reasonable/sensible before it is used (it does not guarantee the data is correct, only that it is plausible), e.g. a **range check** (is a mark between 0 and 100?), a **presence check** (was anything entered at all?), a **type check** (is it actually a number?), a **length check** (is a password long enough?). **Authentication** confirms a user is who they claim to be, e.g. checking an entered username and password match a stored, correct pair before granting access. **Testing** runs a program (or part of it) with chosen input to check it behaves correctly and to find errors; **test data** is chosen deliberately to check specific behaviour: **normal (typical)** data that a sensible user would enter (should be accepted and processed correctly), **boundary (extreme)** data right at the edge of what should be accepted (e.g. exactly 0 and exactly 100 for a 0-100 range check, since these are the values most likely to reveal an off-by-one error), and **erroneous** data that should be rejected (e.g. -5, or "abc" for a numeric field). Good test data is chosen and justified to cover all three categories, not just data that is expected to work. Errors are categorised as **syntax errors** (the code breaks the rules of the language's grammar, so it cannot even run/compile, e.g. a missing colon or mismatched bracket) or **logic errors** (the code runs without crashing but produces the wrong result, because the algorithm itself is flawed, e.g. using `+` where `-` was needed); correcting errors means first identifying which category an error falls into, then locating and fixing the specific cause.

## Explicitly not here
This is the last programming stage; S13 begins data representation.

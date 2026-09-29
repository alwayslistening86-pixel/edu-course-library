# S09_String_Handling - Lesson: String handling operations

## Goal
The learner uses string handling operations: length, position, substring, concatenation, character-to-code and code-to-character conversion, and converts strings to/from numbers.

## Syllabus items taught here
- 3.2.8 - String handling operations

## How to teach this
Ask the learner how many letters are in their own first name, and what the third letter is -- that's length and position. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.8 String handling operations
String handling operations: **length** (`len(s)`) counts the characters in a string; **position** finds where a substring starts within a string (Python's `.find()`); **substring** extracts part of a string by position (Python's slicing, `s[start:end]`); **concatenation** (`+`) joins strings end to end. **Character code conversion**: every character has a numeric code (see S15/3.3.5); `ord(c)` converts a character to its code, `chr(n)` converts a code back to a character, e.g. `ord('A')` is 65, `chr(97)` is 'a'. **String conversion**: numbers can be converted to and from strings, e.g. `str(42)` gives "42" (a string), `int("42")` gives 42 (an integer), `float("3.5")` gives 3.5 (a real number); this is needed because keyboard input arrives as a string.

## Explicitly not here
Random numbers are S10.

# S15_Character_Encoding - Lesson: Character encoding: ASCII and Unicode

## Goal
The learner describes 7-bit ASCII and Unicode as character sets, converts between characters and codes using an encoding table, and explains the purpose and advantages of Unicode over ASCII.

## Syllabus items taught here
- 3.3.5 - Character encoding: ASCII and Unicode

## How to teach this
Ask the learner how a computer, which only stores numbers, manages to store and display the letters of a text message. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.5 Character encoding: ASCII and Unicode
A **character set** is the complete collection of characters a computer system can represent, each assigned a unique numeric code. **7-bit ASCII** assigns a unique number from 0 to 127 to each character; it covers the basic Latin alphabet (upper and lower case), digits 0-9, common punctuation and control characters, but only 128 possible codes, so it cannot represent characters from most other alphabets or symbols such as emoji. Character codes are grouped in sequence (e.g. 'A' to 'Z' run as consecutive codes, as do 'a' to 'z' and '0' to '9'), which makes conversions between related characters straightforward: to convert a character to its code, look it up in the character set (or use `ord()` in Python); to convert a code back to a character, look up the number (or use `chr()`). **Unicode** is a much larger character set (able to represent well over a million characters) designed to cover every writing system in the world, as well as symbols and emoji; its first 128 codes (0-127) deliberately match 7-bit ASCII exactly, so any ASCII text is automatically valid Unicode text too. The purpose of Unicode is to let every language and symbol be represented consistently by every computer system worldwide; its main advantage over ASCII is that it can represent vastly more characters (essentially every character in use globally, not just basic English), avoiding the garbled text ('mojibake') that happens when a document uses characters its character set cannot represent.

## Explicitly not here
Representing images (rather than text) is S16.

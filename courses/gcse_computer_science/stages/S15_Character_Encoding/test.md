# S15_Character_Encoding - Test: Character encoding: ASCII and Unicode

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why 7-bit ASCII can only represent 128 different characters. [2 marks]
2. Given that 'a' is ASCII code 97, state the character represented by code 100. [1 mark]
3. Explain the purpose of Unicode and state one advantage it has over ASCII. [3 marks]
4. Explain why Unicode's first 128 codes are identical to 7-bit ASCII's codes. [2 marks]
5. Which is true of character codes within a character set such as ASCII? Choose every correct option.
   A. related characters (e.g. 'A' to 'Z') are grouped and run in sequence
   B. every character set uses exactly the same codes for the same characters
   C. codes must always be written in hexadecimal
   D. a character's code changes depending on where it appears in a string

## Answer key (for the tutor only)
1. [2] B1 7 bits gives 2^7 possible combinations; B1 = 128, so only 128 distinct codes/characters are possible.
2. [1] B1 'd' (100 is 3 more than 97, and codes for lower-case letters run in sequence).
3. [3] B1 purpose: to represent every character from every world language (plus symbols/emoji) consistently across computer systems; B1 advantage: can represent vastly more characters than ASCII's 128; B1 (or) avoids characters being unrepresentable/displaying incorrectly in other languages.
4. [2] B1 so that any existing ASCII text is automatically valid, correctly-represented Unicode text; B1 giving backwards compatibility between the two character sets.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Character_Encoding` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 9 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S16_Representing_Images.

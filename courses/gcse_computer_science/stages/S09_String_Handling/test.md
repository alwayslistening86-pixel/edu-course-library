# S09_String_Handling - Test: String handling operations

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
s = "hello world"
print(s.find("world"))
print(s[6:])
```
2. Explain what the string operations length and concatenation each do, using "cat" and "fish" as an example. [3 marks]
3. What does this print? (If it raises an error, name it.)
```python
n = str(17) + str(3)
print(n)
```
4. A program reads a person's age as text from the keyboard and needs to add 1 to it. Name the conversion needed and write the line of code that performs it, storing the result in age. [2 marks]
5. What does ord('a') return? Choose every correct option.
   A. `the character code (number) for 'a'`
   B. `the character 'a' itself`
   C. `the length of the string 'a'`
   D. the position of 'a' in the alphabet counting from 1

## Answer key (for the tutor only)
1. Actual result (from running it):
```
6
world
```
2. [3] B1 length counts the characters, e.g. len("cat") is 3; B1 concatenation joins strings end to end; B1 e.g. "cat" + "fish" gives "catfish".
3. Actual result (from running it):
```
173
```
4. [2] B1 converts string to integer; B1 e.g. age = int(input()).
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_String_Handling` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Random_Numbers.

# S05_Characters_and_String_Operations - Practice: Characters, encodings and string operations

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
print(ord('0'), chr(ord('0') + 5), len('\u00e9t\u00e9'))
```
2. What does this print? (If it raises an error, name it.)
```python
print('abc' < 'abd', 'abc' < 'ab', 'Abc' == 'abc', 'b' * 2 + 'a' in 'bbad')
```
3. Which are true? Choose every correct option.
   A. UTF-8 stores every character in exactly one byte
   B. An ASCII character is stored the same way in UTF-8
   C. A code point is the number Unicode assigns to a character
   D. Python 3 str holds bytes

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
48 5 3
```
2. Actual result (from running it):
```
True False False True
```
3. Correct: B, C (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

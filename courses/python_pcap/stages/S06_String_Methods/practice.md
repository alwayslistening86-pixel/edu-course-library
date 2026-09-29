# S06_String_Methods - Practice: String methods and sorting strings

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
print('Hello'.isalpha(), 'Hello1'.isalnum(), '3.5'.isdigit(), ''.isalpha())
```
2. What does this print? (If it raises an error, name it.)
```python
print('a b  c'.split(), 'a b  c'.split(' '), ' x '.strip() + '|')
```
3. What does this print? (If it raises an error, name it.)
```python
print('mississippi'.find('ss'), 'mississippi'.rfind('ss'), 'mississippi'.find('ss', 3))
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
True True False False
```
2. Actual result (from running it):
```
['a', 'b', 'c'] ['a', 'b', '', 'c'] x|
```
3. Actual result (from running it):
```
2 5 5
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

# S10_Comprehensions_Lambdas_Closures - Practice: Comprehensions, lambdas, map/filter and closures

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
print([x for x in 'banana' if x != 'a'], [[i, j] for i in range(2) for j in 'ab'])
```
2. What does this print? (If it raises an error, name it.)
```python
print(list(map(lambda s: s[::-1], ['ab', 'cd'])), list(filter(None, [0, 1, '', 'x'])))
```
3. What does this print? (If it raises an error, name it.)
```python
def outer():
    msg = 'kept'
    def inner():
        return msg
    return inner
f = outer()
print(f())
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
['b', 'n', 'n'] [[0, 'a'], [0, 'b'], [1, 'a'], [1, 'b']]
```
2. Actual result (from running it):
```
['ba', 'dc'] [1, 'x']
```
3. Actual result (from running it):
```
kept
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

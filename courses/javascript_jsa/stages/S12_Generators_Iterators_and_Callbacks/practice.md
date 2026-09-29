# S12_Generators_Iterators_and_Callbacks - Practice: Generators, iterators and asynchronous callbacks

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
function* g() { yield 1; yield 2; return 3; }
console.log([...g()], g().next());
```
2. What does this log? (If it throws, name the error.)
```javascript
function later(cb) { setTimeout(() => cb(null, 'data'), 1); }
later((err, d) => console.log(err, d));
console.log('first');
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
[ 1, 2 ] { value: 1, done: false }
```
2. Actual result (from running it):
```
first
null data
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

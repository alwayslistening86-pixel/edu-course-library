# S13_Promises_Async_Await_and_Fetch - Practice: Promises, async/await and network requests

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
Promise.resolve(1).then(v => v + 1).then(v => console.log(v));
console.log('sync');
```
2. What does this log? (If it throws, name the error.)
```javascript
async function f() { return 5; }
f().then(v => console.log(v, f() instanceof Promise));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
sync
2
```
2. Actual result (from running it):
```
5 true
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

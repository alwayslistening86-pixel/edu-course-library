# S11_Errors_Exceptions_and_Debugging - Practice: Errors, exceptions and debugging

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
try {
  undefinedFunction();
} catch (e) {
  console.log(e.name);
} finally {
  console.log('done');
}
```
2. What does this log? (If it throws, name the error.)
```javascript
try {
  throw new Error('custom');
} catch (e) {
  console.log(e.message, e instanceof Error);
}
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
ReferenceError
done
```
2. Actual result (from running it):
```
custom true
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

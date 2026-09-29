# S07_Number_String_and_Date - Practice: Number, String and Date

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
console.log((12.345).toFixed(1), parseInt('0x1F'), parseInt('1F', 16), Number('1e3'));
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log('Data'.padStart(6, '*'), ' x '.trim().length, 'a-b-c'.replaceAll('-', '+'));
```
3. What does this log? (If it throws, name the error.)
```javascript
const d = new Date(Date.UTC(2026, 0, 31));
d.setUTCMonth(1);
console.log(d.toISOString().slice(0, 10));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
12.3 31 31 1000
```
2. Actual result (from running it):
```
**Data 1 a+b+c
```
3. Actual result (from running it):
```
2026-03-03
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

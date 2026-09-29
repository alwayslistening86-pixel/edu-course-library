# S08_Loops - Practice: Loops: while, do-while, for, for-in and for-of

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
let s = '';
for (let i = 0; i < 5; i += 2) s += i;
console.log(s);
```
2. What does this log? (If it throws, name the error.)
```javascript
const o = { x: 1, y: 2 };
for (const k in o) console.log(k);
for (const v of [7, 8]) console.log(v);
```
3. What does this log? (If it throws, name the error.)
```javascript
let n = 5;
do {
  n--;
} while (n > 10);
console.log(n);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
024
```
2. Actual result (from running it):
```
x
y
7
8
```
3. Actual result (from running it):
```
4
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

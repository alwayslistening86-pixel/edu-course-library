# S01_Object_Literals_and_Properties - Practice: Object literals and properties

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const k = 'size';
const o = { [k]: 3, 'a b': 1 };
o.size++;
delete o['a b'];
console.log(o, o.k);
```
2. What does this log? (If it throws, name the error.)
```javascript
const cfg = { db: { host: 'h' } };
console.log(cfg.db?.host, cfg.cache?.ttl, cfg.cache?.ttl ?? 60);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
{ size: 4 } undefined
```
2. Actual result (from running it):
```
h undefined 60
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

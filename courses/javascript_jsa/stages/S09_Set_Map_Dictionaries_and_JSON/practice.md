# S09_Set_Map_Dictionaries_and_JSON - Practice: Set, Map, objects as dictionaries, and JSON

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this log? (If it throws, name the error.)
```javascript
const s = new Set(['a', 'b', 'a']);
s.add('c');
console.log(s.size, [...s].join(''));
```
2. What does this log? (If it throws, name the error.)
```javascript
const m = new Map();
m.set('x', 1).set('y', 2);
m.delete('x');
console.log(m.size, m.get('y'), [...m.keys()]);
```
3. What does this log? (If it throws, name the error.)
```javascript
console.log(JSON.stringify({ a: [1, 'two', null], b: true }));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
3 abc
```
2. Actual result (from running it):
```
1 2 [ 'y' ]
```
3. Actual result (from running it):
```
{"a":[1,"two",null],"b":true}
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.

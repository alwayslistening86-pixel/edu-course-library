# JavaScript: JSA-41-01 Certified Associate JavaScript Programmer (JS Institute) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
40 items in JSA's real proportions: 11 from S01-S04, 7 from S05-S06, 12 from S07-S10 and 10 from S11-S13. Mix single-select, multiple-select and code-output items, in non-sequential order. No running code until everything is answered. Suggested time: 65 minutes (the real exam's timing is set by the exam provider).

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What does this log? (If it throws, name the error.)
```javascript
const o = { a: 1, b: { c: 2 } };
const c = { ...o, a: 5 };
c.b.c = 9;
console.log(o.a, o.b.c);
```
2. What does this log? (If it throws, name the error.)
```javascript
class A { static s = 'S'; i = 'I'; }
const a = new A();
console.log(a.s, A.i, A.s, a.i);
```
3. What does this log? (If it throws, name the error.)
```javascript
const m = new Map([['k', [1]]]);
m.get('k').push(2);
console.log(m.get('k'), m.size);
```
4. What does this log? (If it throws, name the error.)
```javascript
console.log([5, 1, 10].sort(), [5, 1, 10].sort((a, b) => a - b));
```
5. What does this log? (If it throws, name the error.)
```javascript
function* g() { yield* [1, 2]; yield 3; }
console.log([...g()].reduce((a, b) => a * b));
```
6. What does this log? (If it throws, name the error.)
```javascript
const p = new Promise(r => { console.log('executor'); r('v'); });
p.then(v => console.log('then', v));
console.log('after');
```
7. What does this log? (If it throws, name the error.)
```javascript
function F(x) { this.x = x; }
F.prototype.get = function () { return this.x; };
const f = new F(4);
const g = f.get;
console.log(f.get(), g.call({ x: 8 }));
```
8. What does this log? (If it throws, name the error.)
```javascript
console.log(JSON.stringify([undefined, () => 1, 'x']), Object.keys('ab'));
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
1 9
```
2. Actual result (from running it):
```
undefined undefined S I
```
3. Actual result (from running it):
```
[ 1, 2 ] 1
```
4. Actual result (from running it):
```
[ 1, 10, 5 ] [ 1, 5, 10 ]
```
5. Actual result (from running it):
```
6
```
6. Actual result (from running it):
```
executor
after
then v
```
7. Actual result (from running it):
```
4 8
```
8. Actual result (from running it):
```
[null,null,"x"] [ '0', '1' ]
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 28 of 40 (70%) for a pass, and report the score per block.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest block, offer targeted review, and retry with a fresh paper.

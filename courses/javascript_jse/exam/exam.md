# JavaScript: JSE-40-01 Certified Entry-Level JavaScript Programmer (JS Institute) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
30 items in JSE's real proportions: 3 from S01, 6 from S02-S05, 5 from S06, 6 from S07-S08, 6 from S09-S10 and 4 from S11. Mix single-select, multiple-select and code-output items, in non-sequential order. No running code until everything is answered. Suggested time: 45 minutes (the real exam's timing is set by the exam provider).

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What does this log? (If it throws, name the error.)
```javascript
console.log(typeof null, typeof [], typeof undefined, typeof 1n);
```
2. What does this log? (If it throws, name the error.)
```javascript
let a = '3';
console.log(a + 1, a - 1, a * 1 + 1);
```
3. What does this log? (If it throws, name the error.)
```javascript
const arr = [1, 2, 3];
arr.unshift(arr.pop());
console.log(arr);
```
4. What does this log? (If it throws, name the error.)
```javascript
let r = '';
for (let i = 3; i > 0; i--) {
  if (i === 2) continue;
  r += i;
}
console.log(r);
```
5. What does this log? (If it throws, name the error.)
```javascript
const f = (x, y = x * 2) => x + y;
console.log(f(1), f(1, 1));
```
6. What does this log? (If it throws, name the error.)
```javascript
console.log(0 || '' || 'last', 1 && 2 && 0, null ?? 0 ?? 1);
```
7. What does this log? (If it throws, name the error.)
```javascript
let x = 1;
{
  let x = 2;
  x++;
}
console.log(x);
```
8. What does this log? (If it throws, name the error.)
```javascript
try {
  null.prop;
} catch (e) {
  console.log(e.name);
} finally {
  console.log('end');
}
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
object object undefined bigint
```
2. Actual result (from running it):
```
31 2 4
```
3. Actual result (from running it):
```
[ 3, 1, 2 ]
```
4. Actual result (from running it):
```
31
```
5. Actual result (from running it):
```
3 2
```
6. Actual result (from running it):
```
last 0 0
```
7. Actual result (from running it):
```
1
```
8. Actual result (from running it):
```
TypeError
end
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 21 of 30 (70%) for a pass, and report the score per block.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete, and it now satisfies the prerequisite for JSA (associate).
- **Not yet:** leave `exam_status: "available"`, name the weakest block, offer targeted review, and retry with a fresh paper.

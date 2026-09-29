# S08_Loops - Test: Loops: while, do-while, for, for-in and for-of

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
let c = 0;
while (c < 10) {
  c += 4;
}
console.log(c);
```
2. What does this log? (If it throws, name the error.)
```javascript
let out = '';
for (let i = 1; i <= 6; i++) {
  if (i % 2 === 0) continue;
  if (i > 4) break;
  out += i;
}
console.log(out);
```
3. What does this log? (If it throws, name the error.)
```javascript
const arr = ['a', 'b'];
let r = '';
for (const i in arr) r += i + typeof i[0] + ' ';
console.log(r.trim());
```
4. What does this log? (If it throws, name the error.)
```javascript
let s = 0;
for (const v of [1, 2, 3]) s += v;
for (const ch of 'ab') s += ch;
console.log(s);
```
5. What does this log? (If it throws, name the error.)
```javascript
let count = 0;
for (let i = 0; i < 3; i++)
  for (let j = i; j < 3; j++) count++;
console.log(count);
```
6. What does this log? (If it throws, name the error.)
```javascript
let k = 0;
do {
  k++;
} while (false);
console.log(k);
```
7. Which loop is the best choice to visit the values of an array? Choose every correct option.
   A. `for...of`
   B. `for...in`
   C. do...while with no counter
8. Write a loop that prints the numbers from 1 to 20 that are divisible by 3 but not by 2, using continue.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
12
```
2. Actual result (from running it):
```
13
```
3. Actual result (from running it):
```
0string 1string
```
4. Actual result (from running it):
```
6ab
```
5. Actual result (from running it):
```
6
```
6. Actual result (from running it):
```
1
```
7. Correct: A (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Prints 3, 9, 15; uses continue correctly.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Loops` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Functions_Scope_and_Recursion.

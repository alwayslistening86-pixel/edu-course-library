# S05_Objects_and_Arrays - Test: Objects and arrays

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const user = { name: 'Bo', tags: ['a'] };
user.tags.push('b');
user.age = 9;
console.log(user.tags.length, user['age'], user.email);
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = [4, 5];
const r = a.push(6, 7);
console.log(r, a.shift(), a);
```
3. What does this log? (If it throws, name the error.)
```javascript
const a = [1, 2, 3];
const b = a.reverse();
b.push(0);
console.log(a);
```
4. What does this log? (If it throws, name the error.)
```javascript
const a = ['p', 'q', 'r', 's'];
console.log(a.slice(-2), a.slice(1, -1), a.indexOf('x'));
```
5. What does this log? (If it throws, name the error.)
```javascript
const a = [];
a[3] = 'd';
console.log(a.length, a[0]);
```
6. What does this log? (If it throws, name the error.)
```javascript
const o = {};
try {
  console.log(o.x.y);
} catch (e) {
  console.log(e.name);
}
```
7. Which array methods change the original array? Choose every correct option.
   A. `push`
   B. `slice`
   C. `reverse`
   D. `concat`
   E. `shift`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2 9 undefined
```
2. Actual result (from running it):
```
4 4 [ 5, 6, 7 ]
```
3. Actual result (from running it):
```
[ 3, 2, 1, 0 ]
```
4. Actual result (from running it):
```
[ 'r', 's' ] [ 'q', 'r' ] -1
```
5. Actual result (from running it):
```
4 undefined
```
6. Actual result (from running it):
```
TypeError
```
7. Correct: A, C, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Objects_and_Arrays` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Operators_and_User_Interaction.

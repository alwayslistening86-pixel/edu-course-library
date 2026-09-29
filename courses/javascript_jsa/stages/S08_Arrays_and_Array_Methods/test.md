# S08_Arrays_and_Array_Methods - Test: Arrays and advanced array methods

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const a = ['a', 'b', 'c', 'd'];
const r = a.splice(1, 2);
console.log(a, r);
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = [3, 20, 100];
console.log(a.sort(), a.sort((x, y) => y - x));
```
3. What does this log? (If it throws, name the error.)
```javascript
const people = [{ n: 'A', age: 30 }, { n: 'B', age: 17 }, { n: 'C', age: 45 }];
console.log(people.find(p => p.age < 18).n, people.every(p => p.age > 10), people.some(p => p.age > 50));
```
4. What does this log? (If it throws, name the error.)
```javascript
const words = ['a', 'bb', 'a', 'ccc'];
const lens = words.reduce((acc, w) => { acc[w] = w.length; return acc; }, {});
console.log(lens);
```
5. What does this log? (If it throws, name the error.)
```javascript
const a = [1, 2];
const b = [...a, ...[3], 4];
const [first, ...others] = b;
console.log(b.length, first, others);
```
6. What does this log? (If it throws, name the error.)
```javascript
console.log([1, 2, 3].map((x, i) => x * i), [].reduce((a, b) => a + b, 'empty'));
```
7. What does this log? (If it throws, name the error.)
```javascript
try {
  [].reduce((a, b) => a + b);
} catch (e) {
  console.log(e.name);
}
```
8. Which methods return a new array and leave the original unchanged? Choose every correct option.
   A. `map`
   B. `filter`
   C. `sort`
   D. `splice`
   E. `slice`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
[ 'a', 'd' ] [ 'b', 'c' ]
```
2. Actual result (from running it):
```
[ 100, 20, 3 ] [ 100, 20, 3 ]
```
3. Actual result (from running it):
```
B true false
```
4. Actual result (from running it):
```
{ a: 1, bb: 2, ccc: 3 }
```
5. Actual result (from running it):
```
4 1 [ 2, 3, 4 ]
```
6. Actual result (from running it):
```
[ 0, 2, 6 ] empty
```
7. Actual result (from running it):
```
TypeError
```
8. Correct: A, B, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Arrays_and_Array_Methods` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Set_Map_Dictionaries_and_JSON.

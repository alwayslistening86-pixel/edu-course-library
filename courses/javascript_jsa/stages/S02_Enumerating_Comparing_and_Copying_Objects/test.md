# S02_Enumerating_Comparing_and_Copying_Objects - Test: Enumerating, comparing and copying objects

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const p = { inherited: true };
const o = Object.create(p);
o.own = 1;
console.log('inherited' in o, Object.hasOwn(o, 'inherited'), Object.keys(o));
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = [1, 2];
const b = [1, 2];
console.log(a == b, a === a, JSON.stringify(a) === JSON.stringify(b));
```
3. What does this log? (If it throws, name the error.)
```javascript
const o = { x: 1, nested: { y: 2 } };
const c = Object.assign({}, o);
c.x = 9;
c.nested.y = 9;
console.log(o.x, o.nested.y);
```
4. What does this log? (If it throws, name the error.)
```javascript
const o = { a: 1, nested: { b: 2 } };
const deep = structuredClone(o);
deep.nested.b = 5;
console.log(o.nested.b, deep.nested.b);
```
5. What does this log? (If it throws, name the error.)
```javascript
const o = { f: () => 1, u: undefined, n: null };
console.log(JSON.parse(JSON.stringify(o)));
```
6. What does this log? (If it throws, name the error.)
```javascript
const o = { b: 2, a: 1 };
let s = '';
for (const k in o) s += k;
console.log(s, Object.values(o).reduce((x, y) => x + y));
```
7. Which make an independent copy of the nested objects too? Choose every correct option.
   A. `{ ...obj }`
   B. `Object.assign({}, obj)`
   C. `structuredClone(obj)`
   D. `const copy = obj`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
true false [ 'own' ]
```
2. Actual result (from running it):
```
false true true
```
3. Actual result (from running it):
```
1 9
```
4. Actual result (from running it):
```
2 5
```
5. Actual result (from running it):
```
{ n: null }
```
6. Actual result (from running it):
```
ba 3
```
7. Correct: C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Enumerating_Comparing_and_Copying_Objects` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Methods_this_Accessors_and_Configuration.

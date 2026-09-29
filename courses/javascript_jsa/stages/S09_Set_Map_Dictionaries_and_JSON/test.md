# S09_Set_Map_Dictionaries_and_JSON - Test: Set, Map, objects as dictionaries, and JSON

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
const s = new Set([1, '1', 1, NaN, NaN]);
console.log(s.size, s.has('1'), s.has(NaN));
```
2. What does this log? (If it throws, name the error.)
```javascript
const a = new Set([1, 2, 3]), b = new Set([2, 3, 4]);
console.log([...a].filter(x => b.has(x)), [...new Set([...a, ...b])].length);
```
3. What does this log? (If it throws, name the error.)
```javascript
const k1 = {}, k2 = {};
const m = new Map([[k1, 'one']]);
m.set(k2, 'two');
console.log(m.get(k1), m.get({}), m.size);
```
4. What does this log? (If it throws, name the error.)
```javascript
const inv = { apples: 3 };
inv.pears = 2;
delete inv.apples;
console.log('apples' in inv, Object.entries(inv));
```
5. What does this log? (If it throws, name the error.)
```javascript
const text = JSON.stringify({ d: new Date(0), s: new Set([1]), n: NaN });
console.log(text);
```
6. What does this log? (If it throws, name the error.)
```javascript
const obj = JSON.parse('{"list":[1,2],"nested":{"ok":true}}');
console.log(obj.list.length, obj.nested.ok);
```
7. What does this log? (If it throws, name the error.)
```javascript
try {
  JSON.parse('[1, 2,]');
} catch (e) {
  console.log(e.name);
}
```
8. When is a Map a better choice than a plain object? Choose every correct option.
   A. When keys are objects
   B. `When insertion order and size() matter`
   C. When you want JSON.stringify to include the entries directly
   D. When keys are added and removed often

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3 true true
```
2. Actual result (from running it):
```
[ 2, 3 ] 4
```
3. Actual result (from running it):
```
one undefined 2
```
4. Actual result (from running it):
```
false [ [ 'pears', 2 ] ]
```
5. Actual result (from running it):
```
{"d":"1970-01-01T00:00:00.000Z","s":{},"n":null}
```
6. Actual result (from running it):
```
2 true
```
7. Actual result (from running it):
```
SyntaxError
```
8. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Set_Map_Dictionaries_and_JSON` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Math_RegExp_and_Extending_Builtins.

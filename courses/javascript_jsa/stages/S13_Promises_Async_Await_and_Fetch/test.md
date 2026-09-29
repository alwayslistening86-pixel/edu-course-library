# S13_Promises_Async_Await_and_Fetch - Test: Promises, async/await and network requests

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);
```
2. What does this log? (If it throws, name the error.)
```javascript
Promise.reject(new Error('x'))
  .then(() => console.log('then'))
  .catch(e => { console.log('catch', e.message); return 'recovered'; })
  .then(v => console.log(v))
  .finally(() => console.log('finally'));
```
3. What does this log? (If it throws, name the error.)
```javascript
const w = (ms, v) => new Promise(r => setTimeout(() => r(v), ms));
Promise.all([w(30, 'a'), w(10, 'b'), 'c']).then(v => console.log(v));
Promise.race([w(30, 'slow'), w(10, 'fast')]).then(v => console.log(v));
```
4. What does this log? (If it throws, name the error.)
```javascript
Promise.any([Promise.reject(new Error('1')), Promise.reject(new Error('2'))]).catch(e => console.log(e.name, e.errors.length));
```
5. What does this log? (If it throws, name the error.)
```javascript
async function f() {
  try {
    await Promise.reject(new Error('fail'));
    return 'ok';
  } catch (e) {
    return 'handled ' + e.message;
  }
}
f().then(console.log);
```
6. What does this log? (If it throws, name the error.)
```javascript
async function a() { console.log('a start'); await null; console.log('a end'); }
a();
console.log('outside');
```
7. When does a fetch() promise reject? Choose every correct option.
   A. When the server returns 404
   B. When the server returns 500
   C. When there is a network failure
   D. When response.ok is false
8. Write an async function getJSON(url) that fetches the URL, throws an Error including the status if response.ok is false, and otherwise returns the parsed JSON.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1
4
3
2
```
2. Actual result (from running it):
```
catch x
recovered
finally
```
3. Actual result (from running it):
```
fast
[ 'a', 'b', 'c' ]
```
4. Actual result (from running it):
```
AggregateError 2
```
5. Actual result (from running it):
```
handled fail
```
6. Actual result (from running it):
```
a start
outside
a end
```
7. Correct: C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Uses await fetch, checks response.ok, throws with status, returns await response.json().

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Promises_Async_Await_and_Fetch` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.

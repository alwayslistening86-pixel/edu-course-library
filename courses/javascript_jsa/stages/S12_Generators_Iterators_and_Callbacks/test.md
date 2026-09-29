# S12_Generators_Iterators_and_Callbacks - Test: Generators, iterators and asynchronous callbacks

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
function* evens() { let n = 0; while (true) { yield n; n += 2; } }
const it = evens();
it.next();
console.log(it.next().value, it.next().value);
```
2. What does this log? (If it throws, name the error.)
```javascript
function* g() { const x = yield 'first'; yield 'got ' + x; }
const it = g();
console.log(it.next().value, it.next(42).value, it.next().done);
```
3. What does this log? (If it throws, name the error.)
```javascript
const it = [10, 20][Symbol.iterator]();
console.log(it.next(), it.next(), it.next());
```
4. What does this log? (If it throws, name the error.)
```javascript
class Countdown {
  constructor(n) { this.n = n; }
  *[Symbol.iterator]() { for (let i = this.n; i > 0; i--) yield i; }
}
console.log([...new Countdown(3)], Math.max(...new Countdown(5)));
```
5. What does this log? (If it throws, name the error.)
```javascript
function task(n, cb) {
  setTimeout(() => (n % 2 ? cb(new Error('odd ' + n)) : cb(null, n * 10)), n);
}
for (const n of [2, 3]) task(n, (err, r) => console.log(err ? err.message : r));
```
6. What does this log? (If it throws, name the error.)
```javascript
try {
  setTimeout(() => { throw new Error('late'); }, 0);
  console.log('try block finished');
} catch (e) {
  console.log('caught', e.message);
}
process.on('uncaughtException', e => console.log('uncaught:', e.message));
```
7. What does an iterator's next() return? Choose every correct option.
   A. The next value only
   B. An object with value and done
   C. A promise
   D. undefined when finished

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2 4
```
2. Actual result (from running it):
```
first got 42 true
```
3. Actual result (from running it):
```
{ value: 10, done: false } { value: 20, done: false } { value: undefined, done: true }
```
4. Actual result (from running it):
```
[ 3, 2, 1 ] 5
```
5. Actual result (from running it):
```
20
odd 3
```
6. Actual result (from running it):
```
try block finished
uncaught: late
```
7. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Generators_Iterators_and_Callbacks` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Promises_Async_Await_and_Fetch.

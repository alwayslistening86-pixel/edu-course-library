# S10_Math_RegExp_and_Extending_Builtins - Test: Math, regular expressions and extending built-ins

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
console.log(Math.max(), Math.min(), Math.max(1, '5', 3), Math.abs('-2'));
```
2. What does this log? (If it throws, name the error.)
```javascript
console.log(Math.pow(2, -1), Math.sqrt(-1), Math.floor(Math.log10(12345)) + 1);
```
3. What does this log? (If it throws, name the error.)
```javascript
const m = 'Order #123 and #45'.match(/#(\d+)/);
console.log(m[0], m[1], m.index);
```
4. What does this log? (If it throws, name the error.)
```javascript
console.log('Order #123 and #45'.match(/#\d+/g), 'abc'.search(/z/));
```
5. What does this log? (If it throws, name the error.)
```javascript
const re = new RegExp('^[a-z]+$');
console.log(re.test('hello'), re.test('Hello'), re.test('hel lo'));
```
6. What does this log? (If it throws, name the error.)
```javascript
console.log('John Smith'.replace(/(\w+) (\w+)/, '$2, $1'));
```
7. Why is adding methods to Array.prototype risky? Choose every correct option.
   A. It affects every array in the program
   B. It can clash with methods added to the standard later
   C. It makes arrays slower to create
   D. Enumerable additions appear in for...in over arrays
8. Write an expression that gives a random whole number from 10 to 20 inclusive.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
-Infinity Infinity 5 2
```
2. Actual result (from running it):
```
0.5 NaN 5
```
3. Actual result (from running it):
```
#123 123 6
```
4. Actual result (from running it):
```
[ '#123', '#45' ] -1
```
5. Actual result (from running it):
```
true false false
```
6. Actual result (from running it):
```
Smith, John
```
7. Correct: A, B, D (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Math.floor(Math.random() * 11) + 10 (or equivalent); both ends reachable.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Math_RegExp_and_Extending_Builtins` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Parameters_Closures_Context_Decorators.

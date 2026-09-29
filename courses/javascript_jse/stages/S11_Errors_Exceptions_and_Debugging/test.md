# S11_Errors_Exceptions_and_Debugging - Test: Errors, exceptions and debugging

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this log? (If it throws, name the error.)
```javascript
function f() {
  try {
    return 'try';
  } finally {
    console.log('finally');
  }
}
console.log(f());
```
2. What does this log? (If it throws, name the error.)
```javascript
try {
  (123).toFixed(500);
} catch (e) {
  console.log(e.name);
}
```
3. What does this log? (If it throws, name the error.)
```javascript
try {
  const q = 1;
  q++;
} catch (e) {
  console.log(e.name);
}
```
4. What does this log? (If it throws, name the error.)
```javascript
try {
  throw 'plain string';
} catch (e) {
  console.log(typeof e, e);
}
```
5. What does this log? (If it throws, name the error.)
```javascript
function check(age) {
  if (age < 0) throw new RangeError('negative');
  return age;
}
try {
  check(5);
  check(-1);
  console.log('not reached');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
```
6. A program runs without error messages but prints the wrong total. What kind of error is this? Choose every correct option.
   A. Syntax error
   B. Logic error
   C. `ReferenceError`
   D. Runtime error
7. Which debugger actions exist? Choose every correct option.
   A. Step over
   B. Step into
   C. Watch an expression
   D. Undo the last executed line
8. Write a function safeParse(text) that returns the parsed JSON, or null if the text is invalid, and always logs 'parsed attempt'.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
finally
try
```
2. Actual result (from running it):
```
RangeError
```
3. Actual result (from running it):
```
TypeError
```
4. Actual result (from running it):
```
string plain string
```
5. Actual result (from running it):
```
RangeError: negative
```
6. Correct: B (exactly these options, no others)
7. Correct: A, B, C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Uses try/catch around JSON.parse (SyntaxError), returns null on failure, logs in finally.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Errors_Exceptions_and_Debugging` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.

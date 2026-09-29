# S01_JavaScript_and_Its_Environment - Test: JavaScript and its environment

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which describe an interpreter? Choose every correct option.
   A. Executes source code without a separate translation step first
   B. Produces a standalone executable before running
   C. Reports most errors only when the faulty code runs
2. Which tasks are typically server-side? Choose every correct option.
   A. Changing the colour of a button the user clicked
   B. Reading from a database and answering an HTTP request
   C. `Reading files on the server's disk`
   D. Showing an alert dialog
3. Which tool lets you pause a running script and inspect variables? Choose every correct option.
   A. The debugger
   B. `The code editor's syntax colouring`
   C. The HTML validator
4. Which are ways to include JavaScript in HTML? Choose every correct option.
   A. `An inline <script> element`
   B. `A <script> element with a src attribute`
   C. `A <style> element`
   D. `A <meta> element`
5. What does this log? (If it throws, name the error.)
```javascript
console.log(typeof console.log, 3 * 7)
```
6. Which are advantages of an online environment such as a web sandbox? Choose every correct option.
   A. No installation needed
   B. Easy to share code by link
   C. Works with no internet connection
   D. Best choice for large production projects

## Answer key (for the tutor only)
1. Correct: A, C (exactly these options, no others)
2. Correct: B, C (exactly these options, no others)
3. Correct: A (exactly these options, no others)
4. Correct: A, B (exactly these options, no others)
5. Actual result (from running it):
```
function 21
```
6. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_JavaScript_and_Its_Environment` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Variables_Scope_and_Hoisting.

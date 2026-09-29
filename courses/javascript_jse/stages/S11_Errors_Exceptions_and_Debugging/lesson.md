# S11_Errors_Exceptions_and_Debugging - Lesson: Errors, exceptions and debugging

## Goal
The learner classifies errors, names the built-in error types, handles and throws exceptions, and uses debugging tools to find faults.

## Syllabus items taught here
- 6.1a - Syntax, semantic, logic and runtime errors
- 6.2a - SyntaxError, ReferenceError, TypeError, RangeError
- 6.3a - try...catch...finally and throw
- 6.4a - Debugging: stepping, inspecting variables, timing code

## How to teach this
Ask which kind of error each is: a missing bracket, using an undeclared variable, adding when the task says multiply. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 6.1a Syntax, semantic, logic and runtime errors
A **syntax** error breaks the grammar, so the script doesn't run at all. A **runtime** error happens while running (calling something that isn't a function, for example). A **semantic** error is legal code that means something other than intended (such as using `=` where `===` was meant). A **logic** error is valid code with a wrong algorithm, giving wrong answers and no error message: the hardest kind to find.

#### 6.2a SyntaxError, ReferenceError, TypeError, RangeError
**SyntaxError**: invalid code (also thrown by `JSON.parse` on bad text). **ReferenceError**: using a name that doesn't exist (or a let before its line). **TypeError**: a value of the wrong kind, such as calling a non-function, reading a property of undefined or null, or assigning to a const. **RangeError**: a number out of its allowed range (`new Array(-1)`, `toFixed(200)`, too-deep recursion).
```javascript
const tests = [() => JSON.parse("{bad"), () => missingName, () => null.x, () => new Array(-1)];
for (const t of tests) {
  try { t(); } catch (e) { console.log(e.name); }
}
```
Output:
```
SyntaxError
ReferenceError
TypeError
RangeError
```

#### 6.3a try...catch...finally and throw
`try { ... } catch (e) { ... } finally { ... }`: catch runs if the try block throws, and receives the error object (`e.name`, `e.message`); finally runs **always**. `throw` raises any value, but throw Error objects (`throw new Error("msg")`, or `new RangeError(...)`). A thrown error travels up the call stack until something catches it.
```javascript
function withdraw(balance, amount) {
  if (amount > balance) throw new RangeError("insufficient funds");
  return balance - amount;
}
for (const amt of [30, 80]) {
  try {
    console.log("left:", withdraw(50, amt));
  } catch (e) {
    console.log(e.name, "-", e.message);
  } finally {
    console.log("finally for", amt);
  }
}
```
Output:
```
left: 20
finally for 30
RangeError - insufficient funds
finally for 80
```

#### 6.4a Debugging: stepping, inspecting variables, timing code
Debugging tools: a **breakpoint** (or the `debugger;` statement) pauses execution; **step over**, **step into** and **step out** run code a line or a call at a time; the scope panel and **watch expressions** show, and can modify, variable values; the **call stack** shows how you got there. `console.log` tracing is the simple version. `console.time(label)` and `console.timeEnd(label)` (or `performance.now()`) measure execution time.
```javascript
const t0 = performance.now();
let s = 0;
for (let i = 0; i < 1e6; i++) s += i;
const ms = performance.now() - t0;
console.log(s, ms >= 0 ? "measured a non-negative time" : "?");
```
Output:
```
499999500000 measured a non-negative time
```

## Explicitly not here
Custom error classes and async error handling belong to JSA.

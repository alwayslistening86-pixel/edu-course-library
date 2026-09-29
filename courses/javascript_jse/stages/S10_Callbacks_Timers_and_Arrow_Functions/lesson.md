# S10_Callbacks_Timers_and_Arrow_Functions - Lesson: Callbacks, timers and arrow functions

## Goal
The learner passes callbacks, predicts the order of synchronous and timer-based code, and writes arrow functions.

## Syllabus items taught here
- 5.5a - Synchronous and asynchronous callbacks; setTimeout and setInterval
- 5.6a - Arrow functions

## How to teach this
Ask what order these print in: console.log(1); setTimeout(() => console.log(2), 0); console.log(3); Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 5.5a Synchronous and asynchronous callbacks; setTimeout and setInterval
A **callback** is a function passed in to be called later. A **synchronous** callback runs immediately, during the call (like the function given to `forEach`). An **asynchronous** callback runs later: `setTimeout(fn, ms)` calls fn once after at least ms milliseconds; `setInterval(fn, ms)` calls it repeatedly until `clearInterval(id)`. Timer callbacks never interrupt running code: they wait until the current script has finished, even with a delay of 0.
```javascript
console.log("start");
setTimeout(() => console.log("timeout 0"), 0);
[1, 2].forEach(n => console.log("sync callback", n));
let ticks = 0;
const id = setInterval(() => {
  ticks++;
  console.log("tick", ticks);
  if (ticks === 3) clearInterval(id);
}, 10);
console.log("end of script");
```
Output:
```
start
sync callback 1
sync callback 2
end of script
timeout 0
tick 1
tick 2
tick 3
```

#### 5.6a Arrow functions
**Arrow functions**: `(a, b) => a + b`. With one parameter the brackets are optional (`n => n * 2`); with none, write `() => ...`. A concise body returns its expression automatically; a block body `{ ... }` needs an explicit `return`. To return an object literal, wrap it in parentheses. (Arrows also don't have their own `this`, which matters in JSA.)
```javascript
const double = n => n * 2;
const add = (a, b) => a + b;
const noReturn = n => { n * 2; };
const makeObj = n => ({ value: n });
console.log(double(4), add(2, 3), noReturn(4), makeObj(1), (() => "no args")());
```
Output:
```
8 5 undefined { value: 1 } no args
```

## Explicitly not here
Promises and async/await belong to JSA.

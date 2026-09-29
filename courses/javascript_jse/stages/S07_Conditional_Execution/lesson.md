# S07_Conditional_Execution - Lesson: if and switch

## Goal
The learner writes and traces if/else chains, nested conditions and switch statements, including fall-through.

## Syllabus items taught here
- 4.1a - if and if...else; multiple and nested conditions
- 4.2a - switch and case

## How to teach this
Ask what a switch prints for case 2 when case 2 has no break. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 4.1a if and if...else; multiple and nested conditions
`if (condition) { ... } else if (...) { ... } else { ... }`. The condition is converted to Boolean. Only the first true branch runs. Nest ifs for dependent decisions, or combine them with `&&` and `||`. Always use braces, even for one line.
```javascript
const temp = 12, raining = true;
if (temp > 20) {
  console.log("warm");
} else if (temp > 10) {
  if (raining) { console.log("mild and wet"); } else { console.log("mild"); }
} else {
  console.log("cold");
}
```
Output:
```
mild and wet
```

#### 4.2a switch and case
`switch (expr)` compares the value with each `case` using **strict equality** (`===`). Execution starts at the matching case and **falls through** into the following cases until a `break`. `default` runs when nothing matches, and can be anywhere in the list.
```javascript
function label(day) {
  switch (day) {
    case 6:
    case 7:
      return "weekend";
    case "1":
      return "string one";
    default:
      return "weekday";
  }
}
console.log(label(7), label(1), label("1"));
let out = "";
switch (2) { case 1: out += "a"; case 2: out += "b"; case 3: out += "c"; break; case 4: out += "d"; }
console.log(out);
```
Output:
```
weekend weekday string one
bc
```

## Explicitly not here
Loops are S08.

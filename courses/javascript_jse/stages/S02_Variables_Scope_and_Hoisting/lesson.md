# S02_Variables_Scope_and_Hoisting - Lesson: Variables, scope and hoisting

## Goal
The learner declares variables with let, const and var correctly, and predicts the effects of block scope, shadowing and hoisting.

## Syllabus items taught here
- 2.1a - Naming, declaring and initialising variables; updating values; constants
- 2.1b - Block scope, shadowing and hoisting

## How to teach this
Ask what `console.log(x); var x = 5;` prints, and what happens if var is replaced by let. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 2.1a Naming, declaring and initialising variables; updating values; constants
Declare with `let` (reassignable), `const` (a binding that can't be reassigned, and must be initialised) or the older `var`. Names may contain letters, digits, `_` and `$`; they can't start with a digit, can't be reserved words, and are case-sensitive. camelCase is the convention. `const` fixes the binding, not the contents: a const array can still be pushed to.
```javascript
let count = 1;
count = count + 1;
const LIMIT = 10;
const list = [1];
list.push(2);
console.log(count, LIMIT, list);
try { LIMIT = 11; } catch (e) { console.log(e.name + ": " + e.message); }
```
Output:
```
2 10 [ 1, 2 ]
TypeError: Assignment to constant variable.
```

#### 2.1b Block scope, shadowing and hoisting
`let` and `const` are **block-scoped**: they exist only inside the `{ }` where they're declared. `var` is function-scoped and ignores blocks. An inner declaration with the same name **shadows** the outer one. **Hoisting**: declarations are processed before the code runs. A `var` is hoisted and initialised to `undefined`; a `let` or `const` is hoisted but unusable until its line (the temporal dead zone, so accessing it early is a ReferenceError).
```javascript
console.log(early);
var early = 1;
{ let inner = 2; var leaks = 3; }
console.log(typeof inner, leaks);
let x = "outer";
{ let x = "inner"; console.log(x); }
console.log(x);
try { console.log(late); let late = 4; } catch (e) { console.log(e.name); }
```
Output:
```
undefined
undefined 3
inner
outer
ReferenceError
```

## Explicitly not here
Types of values are S03.

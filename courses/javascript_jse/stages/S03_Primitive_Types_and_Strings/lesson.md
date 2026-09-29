# S03_Primitive_Types_and_Strings - Lesson: Primitive types and strings

## Goal
The learner knows every primitive type, including number limits and BigInt, tells null from undefined, and writes and manipulates strings.

## Syllabus items taught here
- 2.2a - Numbers and BigInt: ranges and formats
- 2.2b - Boolean, null and undefined
- 2.3a - String literals, escapes and template interpolation
- 2.3b - String basics: length, charAt, slice, split

## How to teach this
Ask what 0.1 + 0.2 and 2 ** 53 + 1 display. Have the learner predict the result of every example before running it, in Node or in a browser console, and run code for real whenever they can.

#### 2.2a Numbers and BigInt: ranges and formats
`number` is a 64-bit float: integers are exact only up to `Number.MAX_SAFE_INTEGER` (2^53 - 1). Special values: `Infinity`, `-Infinity`, and `NaN` ("not a number", the result of invalid arithmetic, which isn't even equal to itself). Literals: `255`, `2.5`, `1e3`, `0xff`, `0o17`, `0b101`. **BigInt** (`123n`) holds integers of any size; you can't mix BigInt and number in arithmetic.
```javascript
console.log(0.1 + 0.2, Number.MAX_SAFE_INTEGER, 2 ** 53 + 1, 2n ** 53n + 1n);
console.log(1 / 0, -1 / 0, 0 / 0, NaN === NaN, 0xff, 1e3);
try { console.log(1n + 1); } catch (e) { console.log(e.name); }
```
Output:
```
0.30000000000000004 9007199254740991 9007199254740992 9007199254740993n
Infinity -Infinity NaN false 255 1000
TypeError
```

#### 2.2b Boolean, null and undefined
`boolean` is `true` or `false`. `undefined` means "not assigned yet": an unset variable, a missing property, a missing argument, or a function with no return value. `null` is an explicit "no value" that you assign yourself. `typeof null` is `"object"`, a long-standing quirk. `null == undefined` is true, but `null === undefined` is false.
```javascript
let a;
console.log(a, typeof a, typeof null, typeof true, null == undefined, null === undefined);
```
Output:
```
undefined undefined object boolean true false
```

#### 2.3a String literals, escapes and template interpolation
Strings use single or double quotes, or **backticks** for template literals, which allow `${expression}` interpolation and real line breaks. Escapes: `\n`, `\t`, `\\`, `\'`, `\"`.
```javascript
const name = "Ada", n = 3;
console.log(`Hi ${name}, ${n * 2} messages`, 'it\'s', "tab\there");
```
Output:
```
Hi Ada, 6 messages it's tab	here
```

#### 2.3b String basics: length, charAt, slice, split
`length` is a property, not a method. `charAt(i)` returns the character at i (an empty string if out of range; indexing with `str[i]` returns `undefined` instead). `slice(start, end)` extracts, with end excluded and negatives counting from the end. `split(sep)` returns an array. Strings are immutable: every method returns a new string.
```javascript
const s = "JavaScript";
console.log(s.length, s.charAt(4), s.charAt(99) === "", s[99], s.slice(0, 4), s.slice(-6), "a,b,c".split(","));
```
Output:
```
10 S true undefined Java Script [ 'a', 'b', 'c' ]
```

## Explicitly not here
Conversions between types are S04.

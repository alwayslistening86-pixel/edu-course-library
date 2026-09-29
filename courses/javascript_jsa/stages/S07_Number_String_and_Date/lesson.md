# S07_Number_String_and_Date - Lesson: Number, String and Date

## Goal
The learner converts and formats numbers, uses the common String methods, and creates, reads and compares dates correctly with time zones in mind.

## Syllabus items taught here
- 3.1a - Number: converting to and from numeric strings
- 3.1b - Number: static properties and methods; formatting (toFixed and others)
- 3.2a - String: case, split, find/replace, pad/trim and comparison
- 3.3a - Date: constructing, reading and writing components, elapsed time
- 3.3b - Date: local time versus UTC

## How to teach this
Ask what (0.1 + 0.2).toFixed(2) returns: a number or a string? Have the learner predict the result of every example before running it, and run code for real in Node or a browser console.

#### 3.1a Number: converting to and from numeric strings
`Number(str)` converts the whole string (NaN if any of it is invalid); `parseInt(str, radix)` and `parseFloat(str)` read a leading number and stop at junk. `num.toString(radix)` converts back, in any base from 2 to 36. Unary `+str` is shorthand for Number.
```javascript
console.log(Number("12.5"), parseInt("12.5px"), parseInt("ff", 16), parseFloat("3.14abc"), (255).toString(2), (255).toString(16), +"7");
```
Output:
```
12.5 12 255 3.14 11111111 ff 7
```

#### 3.1b Number: static properties and methods; formatting (toFixed and others)
Static members: `Number.MAX_SAFE_INTEGER`, `Number.EPSILON`, `Number.isInteger()`, `Number.isNaN()` (stricter than the global isNaN), `Number.isFinite()`. Formatting (each returns a **string**): `toFixed(digits)`, `toPrecision(n)`, `toExponential()` and `toLocaleString()`.
```javascript
console.log(Number.isInteger(5.0), Number.isNaN("abc"), isNaN("abc"), Number.isFinite(1 / 0));
console.log((3.14159).toFixed(2), typeof (3.14159).toFixed(2), (1234.5).toPrecision(2), (1500).toExponential(1), (1234567.891).toLocaleString("en-GB"));
```
Output:
```
true false true false
3.14 string 1.2e+3 1.5e+3 1,234,567.891
```

#### 3.2a String: case, split, find/replace, pad/trim and comparison
Useful String methods (all return new strings): `toUpperCase`, `toLowerCase`, `split`, `indexOf`, `includes`, `startsWith`, `endsWith`, `replace` (first match only, unless you use a global regex), `replaceAll`, `padStart` and `padEnd`, `trim`, `repeat`, `at(-1)`. Comparison `<` uses code units (capitals before lower case); `localeCompare` gives language-aware ordering, for sorting.
```javascript
const s = "  Hello World  ";
const t = s.trim();
console.log(t.toUpperCase(), t.indexOf("o"), t.includes("World"), t.replace("o", "0"), t.replaceAll("o", "0"));
console.log("7".padStart(3, "0"), "ab".padEnd(4, "."), "Zebra" < "apple", "Zebra".localeCompare("apple"), t.at(-1));
```
Output:
```
HELLO WORLD 4 true Hell0 World Hell0 W0rld
007 ab.. true 1 d
```

#### 3.3a Date: constructing, reading and writing components, elapsed time
`new Date()` is now; `new Date(ms)` counts milliseconds from 1 January 1970 UTC; `new Date(y, m, d)` uses **zero-based months** (0 = January) in local time; `new Date("2026-09-26")` parses an ISO string. Getters: `getFullYear`, `getMonth`, `getDate` (day of the month), `getDay` (weekday, 0 = Sunday), `getHours` and so on; each has a setter. Subtracting two dates gives milliseconds, for elapsed time; `Date.now()` gives the current timestamp.
```javascript
const d = new Date(Date.UTC(2026, 8, 26, 14, 30));
console.log(d.toISOString(), d.getUTCMonth(), d.getUTCDate(), d.getUTCDay());
const later = new Date(d.getTime());
later.setUTCDate(later.getUTCDate() + 10);
console.log(later.toISOString().slice(0, 10), (later - d) / (1000 * 60 * 60 * 24), "days");
```
Output:
```
2026-09-26T14:30:00.000Z 8 26 6
2026-10-06 10 days
```

#### 3.3b Date: local time versus UTC
A Date stores one moment (UTC milliseconds). The ordinary getters and setters (`getHours`, `setDate`) use the computer's **local** time zone; the `getUTC...` and `setUTC...` versions use UTC. So the same Date can show different hours on different machines. `toISOString()` always prints UTC (ending in `Z`). A date-only ISO string is parsed as UTC; a date-time string without a zone is parsed as local time.
```javascript
const d = new Date("2026-01-15T12:00:00Z");
console.log(d.toISOString(), d.getUTCHours(), d.getTimezoneOffset() === 0 ? "this machine runs on UTC" : "local zone differs from UTC");
```
Output:
```
2026-01-15T12:00:00.000Z 12 this machine runs on UTC
```

## Explicitly not here
Arrays are S08.

# S03_Console_Input_and_Output - Lesson: Console input and output

## Goal
The learner writes formatted console output with cout, cerr, endl and setw, and reads values with cin.

## Syllabus items taught here
- 1.7 - Basic I/O streams cin, cout, cerr and manipulators endl, setw

## How to teach this
Ask what `cout << setw(5) << 42 << 7;` prints, and whether setw applies to the 7. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.7 Basic I/O streams cin, cout, cerr and manipulators endl, setw
`cout << x << y;` writes to standard output; `cerr` writes to the unbuffered **error** stream (a separate stream, so it doesn't appear in normal output); `cin >> x;` reads whitespace-separated values into variables, converting to the variable's type. `endl` ends the line and flushes; `'\n'` just ends the line. `setw(n)` (from `<iomanip>`) sets a minimum width **for the next item only**, right-aligned by default; `left` and `right` choose the alignment, `setfill(c)` the padding character, and `fixed << setprecision(n)` the decimal places. `boolalpha` prints `true`/`false`.
```cpp
cout << "[" << setw(5) << 42 << "][" << 7 << "]" << endl;
cout << left << setw(6) << "ab" << "|" << right << setfill('*') << setw(4) << 9 << endl;
cout << fixed << setprecision(2) << 3.14159 << " " << boolalpha << true << endl;
cerr << "this goes to the error stream, not to cout" << endl;
// Reading: `int age; cin >> age;` waits for the user to type a number.
```
Output:
```
[   42][7]
ab    |***9
3.14 true
```

## Explicitly not here
File streams are not on the CPE syllabus.

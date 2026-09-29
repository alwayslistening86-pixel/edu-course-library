# S01_Program_Structure_Types_and_Literals - Lesson: Program structure, types and literals

## Goal
The learner reads and writes a complete small C++ program, knows the built-in types and their literals, and explains main() and its parameters.

## Syllabus items taught here
- 1.1 - Valid C++ syntax elements, keywords and code structure
- 1.2 - Built-in data types and their literals
- 1.3 - Structure and declaration of main() and its parameters

## How to teach this
Show the smallest legal C++ program, then add one line at a time, compiling after each. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.1 Valid C++ syntax elements, keywords and code structure
A program is a set of **declarations** and **statements**. Statements end with `;`, and blocks are grouped with `{ }`. `#include <iostream>` brings in library declarations; `using namespace std;` lets you write `cout` instead of `std::cout`. Keywords (`int`, `if`, `return`, `while`, `class`, `const`...) are reserved. Identifiers are case-sensitive, start with a letter or `_`, and contain letters, digits and `_`. Comments: `// line` and `/* block */`. (Examples in this course show declarations first, then the body of `main`; every example is compiled and run exactly as a complete program.)
```cpp
int answer = 42; // a global variable
// ---- main ----
    /* a block comment */
    int Answer = 1;
    cout << answer << " " << Answer << endl;
```
Output:
```
42 1
```

#### 1.2 Built-in data types and their literals
Fundamental types: `bool` (`true`/`false`), `char` (`'A'`, `'\n'`), `int` (`42`, `052` octal, `0x2A` hex, `0b101010` binary), `short`, `long` (`42L`), `long long` (`42LL`), unsigned variants (`42u`), `float` (`3.14f`), `double` (`3.14`, `1e-3`), `long double`. Sizes vary by platform; `sizeof` reports them. Integer division truncates; char is a small integer.
```cpp
cout << 052 << " " << 0x2A << " " << 0b101010 << " " << 7 / 2 << " " << 7.0 / 2 << endl;
char c = 'A';
cout << c + 1 << " " << char(c + 1) << " " << sizeof(char) << " " << boolalpha << (3 > 2) << endl;
```
Output:
```
42 42 42 3 3.5
66 B 1 true
```

#### 1.3 Structure and declaration of main() and its parameters
Every program has exactly one `main`, which returns `int`: `int main()` or `int main(int argc, char *argv[])`, where `argc` is the argument count (including the program name) and `argv` holds the arguments as C strings. Returning 0 means success; if control reaches the end of main, `return 0;` is implied (for main only).
```cpp
// this example's main takes no parameters; a program started as `app one two` would see argc == 3
int argc = 3;
const char *argv[] = {"app", "one", "two"};
for (int i = 0; i < argc; i++) cout << i << ":" << argv[i] << " ";
cout << endl;
```
Output:
```
0:app 1:one 2:two 
```

## Explicitly not here
Operators are S02; input and output formatting are S03.

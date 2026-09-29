# S11_Strings - Lesson: std::string

## Goal
The learner creates and changes std::string objects and uses the common string operations and comparisons.

## Syllabus items taught here
- 4.4 - Declaring, initialising and changing std::string objects
- 4.5 - Basic string operations and comparisons

## How to teach this
Ask what `string("10") < string("9")` gives, and why. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 4.4 Declaring, initialising and changing std::string objects
`#include <string>`; `std::string s = "text";`, `string t(3, 'x');` gives "xxx", and `string u = s;` copies. Unlike C strings, std::strings grow as needed and are **mutable**: `s[0] = 'T'`, `s += "!"`, `s.append(...)`, `s.insert(pos, str)`, `s.erase(pos, len)`, `s.replace(pos, len, str)`, `s.clear()`.
```cpp
string s = "hello";
string t(3, 'x');
s[0] = 'H';
s += " world";
s.insert(5, ",");
s.erase(0, 1);
s.replace(0, 4, "J");
cout << s << " " << t << " " << s.size() << endl;
```
Output:
```
J, world xxx 8
```

#### 4.5 Basic string operations and comparisons
Operations: `+` concatenates (at least one operand must be a std::string); `length()` or `size()`; `substr(pos, len)`; `find(str)` returns a position or `string::npos`; `at(i)` is a checked index. Comparisons `== != < >` compare **lexicographically** by character code (so `"Z" < "a"` and `"10" < "9"`). `to_string(n)` and `stoi(str)` convert numbers.
```cpp
string a = "apple", b = "banana";
cout << (a < b) << (string("Z") < "a") << (string("10") < "9") << " " << a + "-" + b << endl;
cout << b.substr(1, 3) << " " << b.find("na") << " " << (b.find("x") == string::npos) << " " << stoi("42") + 1 << " " << to_string(7) + "7" << endl;
```
Output:
```
111 apple-banana
ana 2 1 43 77
```

## Explicitly not here
C-style string functions (strlen, strcpy) are not on the CPE syllabus.

# S03_Strings_and_Aggregates - Lesson: Strings and aggregate types

## Goal
The learner manipulates std::string with escape sequences and operations, and uses vectors, arrays, structures, unions and enums.

## Syllabus items taught here
- 1.6 - std::string objects, escape sequences and string operations
- 1.7 - Aggregates: vectors, arrays, structures, unions and enums

## How to teach this
Ask what a union is for and what happens if you read the member you didn't write last. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.6 std::string objects, escape sequences and string operations
`std::string` supports `+` and `+=`, comparison operators, `size()`, `substr`, `find` (`string::npos` if not found), `insert`, `erase`, `replace`, `c_str()`, and indexing with `[]` or `at()`. Escape sequences inside literals: `\n \t \\ \" \' \0`, octal `\ooo` and hex `\xhh`; each is one character. Adjacent string literals are joined at compile time.
```cpp
string s = "Tab\there, quote \"x\"";
string t = "ab" "cd";
cout << s << " " << t << " " << t.size() << " " << string("a\0b").size() << endl;
t.replace(1, 2, "XYZ");
cout << t << " " << t.find("Z") << " " << (t.find("q") == string::npos) << endl;
```
Output:
```
Tab	here, quote "x" abcd 4 1
aXYZd 3 1
```

#### 1.7 Aggregates: vectors, arrays, structures, unions and enums
**Arrays** (`int a[3]`) have a fixed size; **vectors** grow. A **struct** groups members, which are public by default. A **union** stores its members in the *same* memory, so only the last one written is valid, and its size is that of the largest member. An **enum** names integer constants: an unscoped `enum Color { RED, GREEN }` converts to int, while a scoped `enum class Dir { Up, Down }` needs `Dir::Up` and an explicit cast.
```cpp
union Value { int i; float f; char c[4]; };
enum Color { RED, GREEN = 5, BLUE };
enum class Dir { Up, Down };
struct Pair { int a; double b; };
// ---- main ----
    Value v;
    v.i = 65;
    cout << sizeof(Value) << " " << v.c[0] << " " << RED << GREEN << BLUE << " " << static_cast<int>(Dir::Down) << endl;
    Pair p{1, 2.5};
    int arr[] = {1, 2, 3};
    vector<Pair> vp(2, p);
    cout << p.b << " " << sizeof(arr) / sizeof(arr[0]) << " " << vp[1].a << endl;
```
Output:
```
4 A 056 1
2.5 3 1
```

## Explicitly not here
Control flow is S04.

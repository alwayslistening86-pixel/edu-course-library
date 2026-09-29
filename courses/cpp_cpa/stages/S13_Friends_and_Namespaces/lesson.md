# S13_Friends_and_Namespaces - Lesson: Friends and namespaces

## Goal
The learner grants friend access where it's justified, and organises code with named, nested, anonymous and aliased namespaces.

## Syllabus items taught here
- 5.8 - Friend classes and functions
- 5.9 - Namespaces: anonymous, named, aliases and scope resolution

## How to teach this
Ask why operator<< for a class is usually declared a friend. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 5.8 Friend classes and functions
A class can declare a **friend function** or **friend class**, which may access its private and protected members. Friendship is granted, not taken: it isn't inherited and isn't mutual. It's typically used for operators like `<<` and for tightly coupled helper classes.
```cpp
class Box {
    int secret = 42;
    friend int peek(const Box &b);
    friend class Inspector;
};
int peek(const Box &b) { return b.secret; }
class Inspector { public: int look(const Box &b) { return b.secret + 1; } };
// ---- main ----
    Box b;
    cout << peek(b) << " " << Inspector().look(b) << endl;
```
Output:
```
42 43
```

#### 5.9 Namespaces: anonymous, named, aliases and scope resolution
`namespace name { ... }` groups declarations to avoid name clashes; refer to members with `name::member`, or bring them in with `using name::member;` or `using namespace name;`. Namespaces can be reopened and nested (`a::b::f`, or `namespace a::b` in C++17). An **anonymous** namespace makes names local to one file. An **alias**: `namespace short_name = very::long_name;`. A leading `::name` means the global name.
```cpp
int value = 1;
namespace geometry { const double PI = 3.14; namespace shapes { int sides(int n) { return n; } } }
namespace geometry { int value = 2; }
namespace { int hidden = 3; }
namespace gs = geometry::shapes;
// ---- main ----
    int value = 4;
    using geometry::PI;
    cout << PI << " " << gs::sides(6) << " " << geometry::value << " " << ::value << " " << value << " " << hidden << endl;
```
Output:
```
3.14 6 2 1 4 3
```

## Explicitly not here
Templates and the STL beyond vector and string are covered by CPP, not CPA.

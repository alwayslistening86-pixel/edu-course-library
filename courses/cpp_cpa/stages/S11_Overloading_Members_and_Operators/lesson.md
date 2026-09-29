# S11_Overloading_Members_and_Operators - Lesson: Overloading member functions and operators

## Goal
The learner overloads member functions (including const overloads) and operators, as members and as free functions.

## Syllabus items taught here
- 5.4 - Overloading member functions and operators

## How to teach this
Ask how `a + b` could work for two Money objects. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 5.4 Overloading member functions and operators
Member functions overload like free functions, and can also be overloaded on `const`: the const version is chosen for const objects. **Operator overloading** defines `operator+`, `operator==`, `operator<<`, `operator[]`, `operator++` and so on. A binary operator as a **member** takes one parameter (the left operand is `*this`); as a **free function** it takes two, and is needed when the left operand isn't your class (as with `ostream << obj`). Prefix `++` is `operator++()`; postfix is `operator++(int)`. The operators `::`, `.`, `.*`, `?:` and `sizeof` can't be overloaded.
```cpp
class Money {
    int pence;
public:
    Money(int p = 0) : pence(p) {}
    Money operator+(const Money &o) const { return Money(pence + o.pence); }
    bool operator==(const Money &o) const { return pence == o.pence; }
    Money &operator++() { pence += 100; return *this; }
    Money operator++(int) { Money old = *this; pence += 1; return old; }
    int value() const { return pence; }
    int value(int scale) const { return pence * scale; }
    friend ostream &operator<<(ostream &os, const Money &m) { return os << "£" << m.pence / 100 << "." << m.pence % 100; }
};
// ---- main ----
    Money a(250), b(75);
    Money c = a + b;
    Money old = c++;
    ++c;
    cout << c << " " << old << " " << (a + b == Money(325)) << " " << a.value(2) << endl;
```
Output:
```
£4.26 £3.25 1 500
```

## Explicitly not here
Inheritance is S12.

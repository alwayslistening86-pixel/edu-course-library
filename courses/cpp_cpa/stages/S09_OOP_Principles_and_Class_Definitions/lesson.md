# S09_OOP_Principles_and_Class_Definitions - Lesson: OOP principles and class definitions

## Goal
The learner explains the four OOP principles and defines classes with access control, member functions defined inside and outside the class, static members, and this.

## Syllabus items taught here
- 5.1 - OOP principles: inheritance, encapsulation, polymorphism, abstraction
- 5.2 - Defining classes; access specifiers; the :: operator and this

## How to teach this
Ask what the difference is between a struct and a class in C++. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 5.1 OOP principles: inheritance, encapsulation, polymorphism, abstraction
**Encapsulation**: bundle data with the functions that use it, and hide the details (private members). **Abstraction**: expose only what users need (a public interface; abstract classes). **Inheritance**: build new classes from existing ones. **Polymorphism**: one interface, many behaviours (virtual functions, overloading).

#### 5.2 Defining classes; access specifiers; the :: operator and this
`class Name { private: ... protected: ... public: ... };`. Class members are private by default (struct members public). Member functions can be defined inside the class (implicitly inline) or outside with the **scope resolution operator**: `ReturnType Class::method() { ... }`. `this` is a pointer to the current object, used to disambiguate or to return `*this` for chaining. `static` members belong to the class and are shared (`Class::count`); a static data member needs a definition outside the class (or `inline` in C++17).
```cpp
class Account {
    double balance = 0;
    static int count;
public:
    Account() { ++count; }
    Account &deposit(double balance);
    double get() const { return balance; }
    static int total() { return count; }
};
int Account::count = 0;
Account &Account::deposit(double balance) { this->balance += balance; return *this; }
// ---- main ----
    Account a, b;
    a.deposit(10).deposit(5);
    cout << a.get() << " " << Account::total() << endl;
```
Output:
```
15 2
```

## Explicitly not here
Constructors in depth are S10.

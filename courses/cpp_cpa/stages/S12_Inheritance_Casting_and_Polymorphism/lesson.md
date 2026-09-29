# S12_Inheritance_Casting_and_Polymorphism - Lesson: Inheritance, casting and polymorphism

## Goal
The learner builds single and multiple inheritance hierarchies with the right visibility, casts between related classes, and uses virtual functions, overriding and const correctly.

## Syllabus items taught here
- 5.5 - Single and multiple inheritance; managing visibility
- 5.6 - Class type compatibility and casting with static_cast and dynamic_cast
- 5.7 - Overriding; virtual and polymorphic functions; const members

## How to teach this
Ask what a Base* pointing to a Derived calls when the method isn't virtual. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 5.5 Single and multiple inheritance; managing visibility
`class D : public B` keeps B's public members public in D; `protected` inheritance makes them protected; `private` (the default for classes) makes them private. Private members of B are never accessible in D; protected ones are. **Multiple inheritance**: `class C : public A, public B`; base constructors run in the order the bases are **listed**, destructors in reverse.
```cpp
class A { public: A() { cout << "A "; } ~A() { cout << "~A "; } protected: int shared = 1; };
class B { public: B() { cout << "B "; } ~B() { cout << "~B "; } };
class C : public B, public A {
public:
    C() { cout << "C(" << shared << ") "; }
    ~C() { cout << "~C "; }
};
// ---- main ----
    { C c; }
    cout << endl;
```
Output:
```
B A C(1) ~C ~A ~B 
```

#### 5.6 Class type compatibility and casting with static_cast and dynamic_cast
A derived object can be used where a base is expected: `Base *p = &derived;` and `Base &r = derived;` are implicit upcasts. Assigning a derived object to a base *object* **slices** off the derived part. Downcasting needs `static_cast<Derived*>(p)` (unchecked) or `dynamic_cast<Derived*>(p)`, which is checked at run time for polymorphic classes: it returns nullptr for pointers, and throws `bad_cast` for references.
```cpp
#include <typeinfo>
struct Shape { virtual ~Shape() {} virtual string name() const { return "shape"; } };
struct Circle : Shape { string name() const override { return "circle"; } double r = 1; };
struct Square : Shape {};
// ---- main ----
    Circle c;
    Shape s = c;
    Shape *p = &c;
    cout << s.name() << " " << p->name() << " ";
    cout << (dynamic_cast<Circle*>(p) != nullptr) << (dynamic_cast<Square*>(p) == nullptr) << " ";
    try { Square &sq = dynamic_cast<Square&>(*p); } catch (const bad_cast &) { cout << "bad_cast"; }
    cout << endl;
```
Output:
```
shape circle 11 bad_cast
```

#### 5.7 Overriding; virtual and polymorphic functions; const members
A **virtual** function is chosen by the object's real (dynamic) type when called through a pointer or reference; a non-virtual one by the static type. `override` asks the compiler to check that you really override something. A **pure virtual** function (`= 0`) makes the class **abstract**, so it can't be instantiated. A base with virtual functions should have a virtual destructor. A `const` member function promises not to change the object, and is the only kind callable on const objects.
```cpp
class Animal {
public:
    virtual ~Animal() {}
    virtual string sound() const = 0;
    string describe() const { return "I say " + sound(); }
    string kind() const { return "animal"; }
};
class Dog : public Animal {
public:
    string sound() const override { return "woof"; }
    string kind() const { return "dog"; }
};
// ---- main ----
    Dog d;
    const Animal &a = d;
    cout << a.describe() << " " << a.kind() << " " << d.kind() << endl;
```
Output:
```
I say woof animal dog
```

## Explicitly not here
Friends and namespaces are S13.

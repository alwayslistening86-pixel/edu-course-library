# S12_Inheritance_Casting_and_Polymorphism - Test: Inheritance, casting and polymorphism

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
struct A { A() { cout << "A"; } ~A() { cout << "a"; } };
struct B : A { B() { cout << "B"; } ~B() { cout << "b"; } };
// ---- main ----
    { B obj; }
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct Base { string f() { return "base"; } };
struct Der : Base { string f() { return "der"; } };
// ---- main ----
    Der d;
    Base *p = &d;
    cout << p->f() << " " << d.f() << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
struct Shape { virtual double area() const = 0; virtual ~Shape() {} };
// ---- main ----
    Shape s;
```
4. What is the output? If it does not compile, say so and why.
```cpp
struct Shape { virtual double area() const = 0; virtual ~Shape() {} };
struct Sq : Shape { double s; Sq(double x) : s(x) {} double area() const override { return s * s; } };
struct Ci : Shape { double area() const override { return 3; } };
// ---- main ----
    vector<Shape*> v{new Sq(2), new Ci, new Sq(1)};
    double t = 0;
    for (Shape *s : v) { t += s->area(); delete s; }
    cout << t << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
struct B { virtual ~B() {} };
struct D : B {};
struct E : B {};
// ---- main ----
    B *p = new E;
    D *d = dynamic_cast<D*>(p);
    E *e = dynamic_cast<E*>(p);
    cout << (d == nullptr) << (e != nullptr) << endl;
    delete p;
```
6. What is the output? If it does not compile, say so and why.
```cpp
class Base { public: int x = 1; };
class Der : private Base { public: int get() { return x; } };
// ---- main ----
    Der d;
    cout << d.x;
```
7. What is the output? If it does not compile, say so and why.
```cpp
struct A { virtual void f() const { cout << "A"; } };
struct B : A { void f() override { cout << "B"; } };
// ---- main ----
    B b;
```
8. Which are true? Choose every correct option.
   A. A class with a pure virtual function cannot be instantiated
   B. Assigning a derived object to a base object slices it
   C. dynamic_cast on pointers returns nullptr when the cast fails
   D. Non-virtual functions are chosen by the dynamic type

## Answer key (for the tutor only)
1. Actual result (from running it):
```
ABba
```
2. Actual result (from running it):
```
base der
```
3. Actual result (from running it):
```
(does not compile: cannot declare variable ‘s’ to be of abstract type ‘Shape’)
```
4. Actual result (from running it):
```
8
```
5. Actual result (from running it):
```
11
```
6. Actual result (from running it):
```
(does not compile: ‘int Base::x’ is inaccessible within this context)
```
7. Actual result (from running it):
```
(does not compile: ‘void B::f()’ marked ‘override’, but does not override)
```
8. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Inheritance_Casting_and_Polymorphism` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Friends_and_Namespaces.

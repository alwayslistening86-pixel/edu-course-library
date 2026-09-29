# S09_Pointers_Casts_and_Dynamic_Memory - Lesson: Pointers, casts and dynamic memory

## Goal
The learner declares and uses pointers safely, converts between pointer types with static_cast and dynamic_cast, and manages heap memory without leaks.

## Syllabus items taught here
- 3.3 - Declaring and initialising pointers, including nullptr
- 3.4 - Dereferencing and the address-of operator &
- 3.5 - Pointer conversions with static_cast and dynamic_cast
- 3.6 - Dynamic memory with new, delete and delete[]

## How to teach this
Draw a variable box with an address label, then a pointer box holding that address. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 3.3 Declaring and initialising pointers, including nullptr
`int *p;` declares a pointer to int. Initialise it with an address (`int *p = &x;`) or with `nullptr` (meaning "points nowhere"; prefer it to `NULL` and `0`). An uninitialised pointer holds garbage. In `int *a, b;` only a is a pointer.
```cpp
int x = 5;
int *p = &x;
int *q = nullptr;
int *a, b = 0;
cout << (p != nullptr) << " " << (q == nullptr) << " " << sizeof(b) << endl;
```
Output:
```
1 1 4
```

#### 3.4 Dereferencing and the address-of operator &
`&x` gives x's address; `*p` **dereferences**, giving the object p points to, which you can read or assign. For a pointer to a struct or class, use `p->member`, short for `(*p).member`. Dereferencing nullptr is undefined behaviour.
```cpp
int x = 5;
int *p = &x;
*p = 8;
int **pp = &p;
**pp += 1;
cout << x << " " << *p << " " << (p == &x) << endl;
```
Output:
```
9 9 1
```

#### 3.5 Pointer conversions with static_cast and dynamic_cast
`static_cast<T>(v)` does compile-time-checked conversions: between numeric types, and up or down a class hierarchy with **no run-time check** (a wrong downcast is undefined behaviour). `dynamic_cast<Derived*>(basePtr)` checks at **run time**, and needs a polymorphic base (at least one virtual function): it returns nullptr if the object isn't really a Derived.
```cpp
struct Animal { virtual ~Animal() {} };
struct Dog : Animal { void bark() { cout << "woof" << endl; } };
struct Cat : Animal {};
// ---- main ----
    double d = 9.7;
    int i = static_cast<int>(d);
    Animal *a1 = new Dog, *a2 = new Cat;
    Dog *d1 = dynamic_cast<Dog*>(a1);
    Dog *d2 = dynamic_cast<Dog*>(a2);
    cout << i << " " << (d1 != nullptr) << " " << (d2 == nullptr) << endl;
    if (d1) d1->bark();
    delete a1; delete a2;
```
Output:
```
9 1 1
woof
```

#### 3.6 Dynamic memory with new, delete and delete[]
`new T` allocates one object on the heap and returns its address; `new T[n]` allocates an array. Every `new` needs exactly one matching `delete`, and every `new[]` a `delete[]`; mixing them is undefined behaviour, and forgetting them leaks memory. After deleting, set the pointer to nullptr to avoid dangling use. (Deleting nullptr is safe.)
```cpp
int *one = new int(42);
int *many = new int[3]{1, 2, 3};
cout << *one << " " << many[2] << endl;
delete one;
delete[] many;
one = nullptr;
delete one;
cout << "freed" << endl;
```
Output:
```
42 3
freed
```

## Explicitly not here
Smart pointers are not on the CPE syllabus.

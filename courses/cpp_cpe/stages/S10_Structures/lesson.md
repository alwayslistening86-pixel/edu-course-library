# S10_Structures - Lesson: Structures

## Goal
The learner declares structures, accesses their members, and processes vectors of structures.

## Syllabus items taught here
- 4.1 - Declaring and defining structures
- 4.2 - Accessing structure members with the dot operator
- 4.3 - Vectors of structures and their fields

## How to teach this
Ask how to keep a student's name, age and mark together in one variable. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 4.1 Declaring and defining structures
`struct Name { type member; ... };` (note the final semicolon) defines a new type grouping named members. Members can have default values. Create variables with brace initialisation: `Point p{1, 2};`.
```cpp
struct Point { int x = 0; int y = 0; };
struct Student { string name; int age; double mark; };
// ---- main ----
    Point origin;
    Student s{"Ann", 16, 71.5};
    cout << origin.x << origin.y << " " << s.name << " " << s.age << endl;
```
Output:
```
00 Ann 16
```

#### 4.2 Accessing structure members with the dot operator
The **dot** operator reaches a member of a structure variable (`s.mark`); for a pointer to a structure use `->` (`ptr->mark`). Structures can be copied as a whole by assignment, member by member.
```cpp
struct Box { int w, h; };
// ---- main ----
    Box a{2, 3};
    Box b = a;
    b.w = 10;
    Box *p = &a;
    p->h = 7;
    cout << a.w << "x" << a.h << " " << b.w << "x" << b.h << endl;
```
Output:
```
2x7 10x3
```

#### 4.3 Vectors of structures and their fields
`vector<Struct>` holds many records. Index it, then use the dot: `v[i].field`, or loop with `for (auto &s : v)` (a reference, to change them in place, or `const auto &` to read).
```cpp
struct Item { string name; double price; int qty; };
// ---- main ----
    vector<Item> cart = {{"pen", 1.5, 4}, {"pad", 3.0, 2}};
    cart.push_back({"ink", 8.25, 1});
    double total = 0;
    for (const auto &it : cart) total += it.price * it.qty;
    for (auto &it : cart) it.qty = 0;
    cout << cart.size() << " " << cart[2].name << " " << total << " " << cart[0].qty << endl;
```
Output:
```
3 ink 20.25 0
```

## Explicitly not here
Classes with private members and methods belong to CPA.

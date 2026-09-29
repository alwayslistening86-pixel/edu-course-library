# S10_Constructors_and_Destructors - Lesson: Constructors and destructors

## Goal
The learner writes default, parameterised, copy and explicit constructors with initialiser lists, and predicts constructor and destructor call order.

## Syllabus items taught here
- 5.3 - Constructors and destructors: default, copy and explicit

## How to teach this
Ask when a destructor runs for a local object, and in what order for several. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 5.3 Constructors and destructors: default, copy and explicit
A **constructor** has the class's name and no return type, and runs when an object is created. The **default constructor** takes no arguments (supplied automatically only if you declare no constructors at all). The **copy constructor** `T(const T &other)` runs when an object is initialised from another of its type, including pass-by-value. `explicit` stops a one-argument constructor being used for implicit conversions. Member **initialiser lists** (`: x(a), y(b)`) initialise members in their **declaration order**. The **destructor** `~T()` runs when the object's lifetime ends: local objects are destroyed in reverse order of construction.
```cpp
class Tag {
    string name;
public:
    Tag() : name("anon") { cout << "default(" << name << ") "; }
    explicit Tag(const string &n) : name(n) { cout << "make(" << name << ") "; }
    Tag(const Tag &o) : name(o.name + "'") { cout << "copy(" << name << ") "; }
    ~Tag() { cout << "~" << name << " "; }
};
void byValue(Tag t) {}
// ---- main ----
    {
        Tag a;
        Tag b("b");
        Tag c = b;
        byValue(c);
    }
    cout << endl;
```
Output:
```
default(anon) make(b) copy(b') copy(b'') ~b'' ~b' ~b ~anon 
```

## Explicitly not here
Operator overloading is S11.

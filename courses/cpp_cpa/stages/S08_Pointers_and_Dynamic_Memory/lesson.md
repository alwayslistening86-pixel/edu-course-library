# S08_Pointers_and_Dynamic_Memory - Lesson: Pointers and dynamic memory

## Goal
The learner declares pointers to every kind of target, dereferences them, uses pointer arithmetic and comparisons, and manages heap memory without leaks.

## Syllabus items taught here
- 4.1 - Pointers to variables, objects, functions and aggregates
- 4.2 - Dereferencing and the address-of operator
- 4.3 - Pointer arithmetic and comparisons
- 4.4 - Dynamic memory with new, delete and delete[]; avoiding leaks

## How to teach this
Ask what `p + 1` means when p is an int* versus a double*. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 4.1 Pointers to variables, objects, functions and aggregates
Pointers can point to variables (`int *p = &x`), to objects (`Point *pp = &pt;` then `pp->x`), to array elements (an array name decays to a pointer to its first element), and to **functions**: `int (*fp)(int) = square;` then `fp(3)`.
```cpp
struct Point { int x, y; };
int square(int n) { return n * n; }
// ---- main ----
    Point pt{2, 5};
    Point *pp = &pt;
    int arr[3] = {7, 8, 9};
    int *pa = arr;
    int (*fp)(int) = square;
    cout << pp->y << " " << *pa << " " << fp(4) << " " << (*fp)(5) << endl;
```
Output:
```
5 7 16 25
```

#### 4.2 Dereferencing and the address-of operator
`&x` gives an address; `*p` dereferences it (reading or writing the target); `p->m` is `(*p).m`. Pointer-to-pointer: `int **pp = &p`. A const can apply to the target (`const int *p`: can't change `*p`) or to the pointer itself (`int *const p`: can't re-point).
```cpp
int a = 1, b = 2;
const int *pc = &a;
pc = &b;
int *const cp = &a;
*cp = 10;
int *p = &b, **pp = &p;
**pp = 20;
cout << a << " " << b << " " << *pc << endl;
```
Output:
```
10 20 20
```

#### 4.3 Pointer arithmetic and comparisons
Adding n to a pointer moves n **elements** (n * sizeof(T) bytes). Subtracting two pointers into the same array gives the element distance. Comparisons (`== != < >`) are meaningful within the same array; `p[i]` is `*(p + i)`.
```cpp
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr, *q = &arr[4];
cout << *(p + 2) << " " << q - p << " " << (p < q) << " " << p[3] << " " << *(q - 1) << endl;
for (int *it = arr; it < arr + 5; it += 2) cout << *it << " ";
cout << endl;
```
Output:
```
30 4 1 40 40
10 30 50 
```

#### 4.4 Dynamic memory with new, delete and delete[]; avoiding leaks
`new T(args)` and `new T[n]` allocate on the heap; release with `delete` and `delete[]` respectively, exactly once. Leaks happen when the only pointer to a block is lost or overwritten, or when an exception skips the delete. After `delete`, the pointer dangles, so set it to nullptr. A failed `new` throws `bad_alloc`. (Modern code prefers `std::unique_ptr` and containers.)
```cpp
struct Node { int v; Node(int x) : v(x) { cout << "make" << v << " "; } ~Node() { cout << "free" << v << " "; } };
// ---- main ----
    Node *n = new Node(1);
    Node *arr = new Node[2]{Node(2), Node(3)};
    delete n;
    delete[] arr;
    n = nullptr;
    cout << endl;
```
Output:
```
make1 make2 make3 free1 free3 free2 
```

## Explicitly not here
Classes are S09 to S13.

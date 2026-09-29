# S08_Arrays_and_Vectors - Lesson: Arrays and vectors

## Goal
The learner declares, initialises and processes arrays (one- and multi-dimensional) and vectors, and uses data() to reach a vector's storage.

## Syllabus items taught here
- 3.1 - Vectors and arrays, including multidimensional arrays
- 3.2 - Accessing vector data through data()

## How to teach this
Ask what happens when you read a[5] from an array of 5 elements. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 3.1 Vectors and arrays, including multidimensional arrays
An **array** has a fixed size known at compile time: `int a[5] = {1, 2};` (the rest are zero-initialised); indices run from 0 to size-1, and there's **no bounds checking** (out of range is undefined behaviour). Multidimensional: `int m[2][3] = {{1,2,3},{4,5,6}};`, indexed `m[row][col]`. A `std::vector<T>` (from `<vector>`) is resizable: `push_back`, `pop_back`, `size()`, indexing with `[]` (unchecked) or `.at(i)` (checked; throws out_of_range), and `vector<vector<int>>` for 2D.
```cpp
int a[5] = {1, 2};
int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
cout << a[0] << a[1] << a[4] << " " << m[1][2] << " " << sizeof(a) / sizeof(a[0]) << endl;
vector<int> v = {10, 20};
v.push_back(30);
v.pop_back();
v.push_back(40);
cout << v.size() << " " << v[2] << " " << v.front() << " " << v.back() << endl;
vector<vector<int>> grid(2, vector<int>(3, 7));
grid[1][0] = 0;
cout << grid[1][0] << grid[1][1] << endl;
try { v.at(9); } catch (out_of_range &e) { cout << "out_of_range" << endl; }
```
Output:
```
120 6 5
3 40 10 40
07
out_of_range
```

#### 3.2 Accessing vector data through data()
`v.data()` returns a pointer to the vector's first element (its contiguous storage), usable wherever a raw array pointer is needed. It's valid only until the vector reallocates (for example after push_back grows it).
```cpp
vector<int> v = {5, 6, 7};
int *p = v.data();
p[1] = 60;
cout << *p << " " << *(p + 2) << " " << v[1] << " " << (p == &v[0]) << endl;
```
Output:
```
5 7 60 1
```

## Explicitly not here
Pointers in general are S09.

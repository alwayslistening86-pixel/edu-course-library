# S07_Algorithms_and_Data_Structures - Lesson: Algorithms and data structures

## Goal
The learner analyses the time/space complexity of code using Big-O/Omega/Theta, compares O(n^2) and O(n log n) sorting algorithms by tracing them, implements and analyses linked lists and hash tables including collision handling, and implements/traverses binary search trees while explaining the motivation for self-balancing trees.

## Syllabus items taught here
- 7a - Asymptotic analysis: Big-O, Big-Omega and Big-Theta; analysing the time and space complexity of code
- 7b - Sorting algorithms: bubble/insertion sort (O(n^2)) versus merge sort/quicksort (O(n log n))
- 7c - Data structures: linked lists, hash tables and collision handling, beyond A-level stacks/queues
- 7d - Trees: binary search trees, tree traversal (in-order/pre-order/post-order), the case for self-balancing trees

## How to teach this
Ask the learner to guess how much longer sorting 1,000,000 items takes than 1,000 items with bubble sort versus with merge sort, before showing the actual numbers. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 7a Asymptotic analysis: Big-O, Big-Omega and Big-Theta; analysing the time and space complexity of code
**Asymptotic analysis.** **Big-O** gives an asymptotic *upper bound* on growth (worst case, informally): f(n) is O(g(n)) if there exist constants c>0, n0 such that f(n) <= c.g(n) for all n>=n0. **Big-Omega** gives an asymptotic *lower bound* (best case); **Big-Theta** gives a *tight bound* (both upper and lower, i.e. the function's growth rate exactly, up to constants). Analysing code: a single loop over n items is O(n); a nested loop over n items (each iterating over n items) is O(n^2); halving the problem each step (e.g. binary search) is O(log n); a loop that calls an O(n) operation n times is O(n^2), not O(n) -- a very common student error.
```python
def is_big_o(f, g, n_values):
    # crude empirical check: does f(n)/g(n) stay bounded as n grows?
    ratios = [f(n) / g(n) for n in n_values]
    return ratios

def f(n):
    return 3 * n**2 + 5 * n

def g(n):
    return n**2

print([round(r, 2) for r in is_big_o(f, g, [10, 100, 1000, 10000])])
```
Output:
```
[3.5, 3.05, 3.0, 3.0]
```
The ratio settles towards the constant 3, confirming f(n) is Theta(n^2) (and hence O(n^2)).

#### 7b Sorting algorithms: bubble/insertion sort (O(n^2)) versus merge sort/quicksort (O(n log n))
**Sorting algorithms.** **Bubble sort** and **insertion sort** are O(n^2): bubble sort repeatedly swaps adjacent out-of-order elements, insertion sort repeatedly inserts each element into its correct position in an already-sorted prefix; both are simple but scale badly. **Merge sort** (divide the list in half recursively, sort each half, merge the two sorted halves in O(n)) and **quicksort** (choose a pivot, partition into smaller/larger, recursively sort each partition) both achieve O(n log n) average-case time by repeatedly halving the problem, the same logarithmic idea as binary search; quicksort's worst case is O(n^2) (a consistently bad pivot choice, e.g. an already-sorted list with a naive first-element pivot), but this is rare in practice with a good pivot strategy.
```python
import time, random

def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

random.seed(1)
data = random.sample(range(10000), 1500)
t0 = time.perf_counter(); bubble_sort(data); t1 = time.perf_counter()
t2 = time.perf_counter(); merge_sort(data); t3 = time.perf_counter()
print("bubble sort correct:", bubble_sort(data) == sorted(data))
print("merge sort correct:", merge_sort(data) == sorted(data))
print("bubble sort slower than merge sort by roughly a factor of", round((t1 - t0) / (t3 - t2), 1))
```
Output:
```
bubble sort correct: True
merge sort correct: True
bubble sort slower than merge sort by roughly a factor of 35.0
```

#### 7c Data structures: linked lists, hash tables and collision handling, beyond A-level stacks/queues
**Linked lists.** A singly linked list stores each element in a *node* holding a value and a reference to the next node; unlike an array, insertion/deletion at a known position is O(1) (no shifting needed), but access by index is O(n) (must follow references from the head). **Hash tables** map keys to array indices via a *hash function*, giving average-case O(1) insertion/lookup/deletion -- the key advantage over a linked list or array for lookup-heavy workloads. A **collision** occurs when two keys hash to the same index; *chaining* resolves it by storing a small linked list (or similar) at each index; *open addressing* (e.g. linear probing) resolves it by searching for the next free slot according to a fixed rule. A poor hash function (many collisions) degrades hash table performance towards O(n).
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out

def prepend(head, value):
    return Node(value, head)

head = None
for v in [3, 2, 1]:
    head = prepend(head, v)
print(to_list(head))

# simple chained hash table
table = [[] for _ in range(5)]
def put(key, value):
    table[hash(key) % 5].append((key, value))
def get(key):
    for k, v in table[hash(key) % 5]:
        if k == key:
            return v
    return None

put("a", 1); put("f", 6); put("k", 11)  # chosen so some collide on index (they may or may not, illustrative)
print(get("a"), get("f"), get("k"), get("missing"))
```
Output:
```
[1, 2, 3]
1 6 11 None
```

#### 7d Trees: binary search trees, tree traversal (in-order/pre-order/post-order), the case for self-balancing trees
**Trees.** A **binary search tree (BST)** stores comparable values so that, for every node, every value in its left subtree is smaller and every value in its right subtree is larger, giving O(log n) average-case search/insert/delete (following one path from root to a leaf) -- but O(n) worst case if the tree becomes a degenerate chain (e.g. inserting already-sorted data one at a time into a naive BST). **Traversal orders**: *in-order* (left, node, right) visits a BST's values in sorted order; *pre-order* (node, left, right) is useful for copying/serialising a tree; *post-order* (left, right, node) is useful for safely deleting a tree bottom-up. A **self-balancing tree** (e.g. AVL tree, which rebalances via rotations to keep left/right subtree heights within 1 of each other, or a B-tree, used heavily in databases/filesystems for its wide, shallow structure suited to disk access) guarantees O(log n) worst-case operations by preventing the degenerate-chain case a plain BST is vulnerable to.
```python
class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def in_order(root, out=None):
    if out is None:
        out = []
    if root:
        in_order(root.left, out)
        out.append(root.val)
        in_order(root.right, out)
    return out

root = None
for v in [8, 3, 10, 1, 6, 14, 4, 7]:
    root = insert(root, v)
print(in_order(root))
```
Output:
```
[1, 3, 4, 6, 7, 8, 10, 14]
```

## Explicitly not here
Formal computability limits on what algorithms can decide at all are S08.

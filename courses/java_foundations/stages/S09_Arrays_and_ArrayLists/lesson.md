# S09_Arrays_and_ArrayLists - Lesson: Arrays and ArrayLists

## Goal
The learner creates and uses one-dimensional arrays and ArrayLists, traverses ArrayLists in every way, and chooses between the two.

## Syllabus items taught here
- 11.1 - Use a one-dimensional array
- 11.2 - Create and manipulate an ArrayList
- 11.3 - Traverse the elements of an ArrayList using iterators and loops, including the enhanced for loop
- 11.4 - Compare an array and an ArrayList

## How to teach this
Ask why you can't add a fourth element to `new int[3]`. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 11.1 Use a one-dimensional array
An array has a **fixed length** set at creation and holds one type. Create with `int[] a = new int[5];` (elements default to 0, false, or null) or with an initialiser `int[] b = {3, 1, 4};`. Index from 0 to `length - 1` (`length` is a field, no parentheses); outside that range throws `ArrayIndexOutOfBoundsException`. Array variables are references: assigning one to another shares the array. `Arrays.toString` and `Arrays.sort` (in java.util) help.
```java
int[] a = new int[4];
a[0] = 7;
a[3] = a[0] * 2;
String[] names = {"Kim", "Al", "Bea"};
int[] alias = a;
alias[1] = 99;
Arrays.sort(names);
System.out.println(Arrays.toString(a) + " " + a.length + " " + Arrays.toString(names) + " " + new boolean[2][0]);
```
Output:
```
[7, 99, 0, 14] 4 [Al, Bea, Kim] [[Z@15db9742
```

#### 11.2 Create and manipulate an ArrayList
`ArrayList<Type>` (java.util) is a resizable list of objects. Primitives are stored via wrapper types (`ArrayList<Integer>`), with automatic boxing. Methods: `add(e)`, `add(index, e)` (shifts later elements right), `get(i)`, `set(i, e)` (returns the old value), `remove(index)` or `remove(object)`, `size()`, `contains(e)`, `indexOf(e)`, `isEmpty()`, `clear()`. For an `ArrayList<Integer>`, `remove(1)` removes at index 1; `remove(Integer.valueOf(1))` removes the value 1.
```java
ArrayList<String> list = new ArrayList<>();
list.add("b"); list.add("d"); list.add(0, "a"); list.add(2, "c");
String old = list.set(3, "D");
list.remove("b");
System.out.println(list + " " + list.size() + " " + old + " " + list.get(1) + " " + list.contains("d") + " " + list.indexOf("D"));
ArrayList<Integer> nums = new ArrayList<>();
nums.add(5); nums.add(1); nums.add(3);
nums.remove(1);
nums.remove(Integer.valueOf(5));
System.out.println(nums);
```
Output:
```
[a, c, D] 3 d c false 2
[3]
```

#### 11.3 Traverse the elements of an ArrayList using iterators and loops, including the enhanced for loop
Traverse with an index loop (`for (int i = 0; i < list.size(); i++) list.get(i)`), the enhanced for loop, or an `Iterator` (`list.iterator()`, then `hasNext()` / `next()`, and `remove()` to delete the current element safely). Removing through the list itself inside an enhanced for loop throws `ConcurrentModificationException`.
```java
ArrayList<Integer> nums = new ArrayList<>(List.of(4, 7, 10, 13));
for (int i = 0; i < nums.size(); i++) System.out.print(i + "=" + nums.get(i) + " ");
System.out.println();
int sum = 0;
for (int n : nums) sum += n;
Iterator<Integer> it = nums.iterator();
while (it.hasNext()) if (it.next() % 2 == 1) it.remove();
System.out.println(sum + " " + nums);
```
Output:
```
0=4 1=7 2=10 3=13 
34 [4, 10]
```
```java
ArrayList<String> xs = new ArrayList<>(List.of("a", "b", "c"));
for (String x : xs) if (x.equals("a")) xs.remove(x);
```
Output:
```
(throws ConcurrentModificationException)
```

#### 11.4 Compare an array and an ArrayList
| | Array | ArrayList |
|---|---|---|
| Size | fixed at creation | grows and shrinks |
| Element types | primitives or objects | objects only (wrappers for primitives) |
| Length | `arr.length` (field) | `list.size()` (method) |
| Access | `arr[i]` | `list.get(i)` / `list.set(i, e)` |
| Package | built into the language | `java.util` |
| Printing | `Arrays.toString(arr)` | `list` prints directly |
Arrays are slightly faster and simpler for fixed data; ArrayLists suit data whose size changes.
```java
int[] arr = {1, 2, 3};
ArrayList<Integer> list = new ArrayList<>(List.of(1, 2, 3));
list.add(4);
System.out.println(arr.length + " " + list.size() + " " + Arrays.toString(arr) + " " + list);
```
Output:
```
3 4 [1, 2, 3] [1, 2, 3, 4]
```
Printing an array directly (`System.out.println(arr)`) shows only a type-and-hash label such as `[I@1b6d3586`, which is why arrays need `Arrays.toString`.

## Explicitly not here
Two-dimensional arrays and the wider collections framework belong to java_se21_developer.

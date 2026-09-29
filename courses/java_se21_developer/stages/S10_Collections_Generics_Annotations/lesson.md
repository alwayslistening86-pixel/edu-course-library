# S10_Collections_Generics_Annotations - Lesson: Arrays, collections, generics and annotations

## Goal
The learner creates and manipulates arrays, Lists, Sets, Maps and Deques (including the Java 21 sequenced-collection methods), sorts with Comparable and Comparator, writes generic classes and methods with bounded wildcards, and applies the standard annotations correctly.

## Syllabus items taught here
- 5.1 - Create arrays, List, Set, Map and Deque collections, and add, remove, update, retrieve and sort their elements
- 11.2 - Use annotations such as Override, FunctionalInterface, Deprecated, SuppressWarnings and SafeVarargs
- 11.3 - Use generics, including wildcards

## How to teach this
Ask what `List.of(1, 2).add(3)` and `Arrays.asList(1, 2).set(0, 9)` each do, and why they differ. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 5.1 Create arrays, List, Set, Map and Deque collections, and add, remove, update, retrieve and sort their elements
**Arrays:** fixed length; `int[] a`, `int a[]`, `int[][] grid = new int[2][]` (ragged rows allowed); defaults 0/false/null. `Arrays.sort`, `Arrays.binarySearch` (sorted input only; a miss returns `-(insertionPoint) - 1`), `Arrays.fill`, `Arrays.equals` (contents) vs `==` (reference), `Arrays.compare` (lexicographic), `Arrays.mismatch` (first differing index, or -1).
```java
int[][] grid = new int[3][];
grid[0] = new int[]{1};
grid[1] = new int[]{2, 3};
int[] data = {5, 1, 4, 2};
Arrays.sort(data);
System.out.println(Arrays.deepToString(grid) + " " + Arrays.toString(data) + " " + Arrays.binarySearch(data, 4) + " " + Arrays.binarySearch(data, 3) + " " + Arrays.equals(new int[]{1}, new int[]{1}) + " " + Arrays.compare(new int[]{1, 2}, new int[]{1, 3}) + " " + Arrays.mismatch(new int[]{1, 2, 3}, new int[]{1, 9, 3}));
```
Output:
```
[[1], [2, 3], null] [1, 2, 4, 5] 2 -3 true -1 1
```
**Lists:** `ArrayList` (resizable array), `LinkedList` (also a Deque). `List.of(...)` and `List.copyOf` are **unmodifiable** and reject nulls; `Arrays.asList` is **fixed-size** but settable and writes through to the array. `remove(int)` removes by index, `remove(Object)` by value. Java 21 **sequenced collections** add `getFirst`, `getLast`, `addFirst`, `addLast`, `removeFirst`, `removeLast` and `reversed()` to List, Deque, LinkedHashSet, SortedSet (and `firstEntry`, `pollLastEntry`, `reversed` to LinkedHashMap and SortedMap).
```java
String[] arr = {"c", "a", "b"};
List<String> view = Arrays.asList(arr);
view.set(0, "z");
List<Integer> nums = new ArrayList<>(List.of(10, 20, 30, 40));
nums.remove(1);
nums.remove(Integer.valueOf(40));
nums.addFirst(5);
System.out.println(arr[0] + " " + nums + " " + nums.getLast() + " " + nums.reversed() + " " + nums.indexOf(30) + " " + nums.subList(1, 3));
try { view.add("q"); } catch (UnsupportedOperationException e) { System.out.print("asList can't grow; "); }
try { List.of(1).set(0, 2); } catch (UnsupportedOperationException e) { System.out.println("List.of can't change"); }
```
Output:
```
z [5, 10, 30] 30 [30, 10, 5] 2 [10, 30]
asList can't grow; List.of can't change
```
**Sets** have no duplicates (by `equals`/`hashCode`, or by `compareTo` for `TreeSet`): `HashSet` (no order), `LinkedHashSet` (insertion order), `TreeSet` (sorted; navigation methods `floor`, `ceiling`, `higher`, `lower`, `headSet`, `tailSet`). `add` returns false for a duplicate. **Maps** hold key-value pairs: `HashMap`, `LinkedHashMap`, `TreeMap` (sorted keys). `put` returns the old value; `get` returns null when absent; also `getOrDefault`, `putIfAbsent`, `merge`, `compute`, `computeIfAbsent`, `remove`, `keySet`, `values`, `entrySet`, `forEach`. `Map.of` is unmodifiable.
```java
TreeSet<Integer> ts = new TreeSet<>(List.of(40, 10, 30, 20));
Set<String> seen = new LinkedHashSet<>();
boolean added = seen.add("b") & seen.add("a") & seen.add("b");
System.out.println(ts + " " + ts.floor(25) + " " + ts.ceiling(25) + " " + ts.higher(40) + " " + ts.headSet(30) + " " + ts.descendingSet() + " " + seen + " " + added);
Map<String, Integer> counts = new TreeMap<>();
for (String w : "the cat and the hat and the bat".split(" ")) counts.merge(w, 1, Integer::sum);
Integer old = counts.put("cat", 9);
counts.putIfAbsent("cat", 100);
counts.computeIfAbsent("dog", k -> k.length());
counts.computeIfPresent("bat", (k, v) -> null);
System.out.println(counts + " " + old + " " + counts.get("cow") + " " + counts.getOrDefault("cow", 0) + " " + ((TreeMap<String, Integer>) counts).firstKey());
```
Output:
```
[10, 20, 30, 40] 20 30 null [10, 20] [40, 30, 20, 10] [b, a] false
{and=2, cat=9, dog=3, hat=1, the=3} 1 null 0 and
```
**Deques** (`ArrayDeque`, which rejects nulls, or `LinkedList`) work at both ends. As a **stack**: `push`/`pop`/`peek` (at the front). As a **queue**: `offer`/`poll`/`peek` (add at the back, take from the front). `poll` and `peek` return null when empty; `pop`, `remove` and `element` throw `NoSuchElementException`.
```java
Deque<String> dq = new ArrayDeque<>();
dq.push("a"); dq.push("b"); dq.offer("c"); dq.offerFirst("d"); dq.addLast("e");
System.out.println(dq + " " + dq.pop() + " " + dq.pollLast() + " " + dq.peek() + " " + dq.peekLast() + " " + dq);
Deque<Integer> empty = new ArrayDeque<>();
System.out.println(empty.poll() + " " + empty.peek());
empty.pop();
```
Output:
```
[d, b, a, c, e] d e b c [b, a, c]
null null
(throws NoSuchElementException)
```
**Sorting:** `Comparable<T>.compareTo` defines natural order (String alphabetical with uppercase first, numbers ascending); a `Comparator` gives other orders: `Comparator.comparing(key)`, `.thenComparing(...)`, `.reversed()`, `Comparator.naturalOrder()`, `reverseOrder()`, `nullsFirst`. `list.sort(c)`, `Collections.sort`, `Collections.reverse`, `Collections.max`. Sorting objects that are not Comparable without a comparator throws `ClassCastException` (TreeSet on the first add).
```java
record Emp(String name, String dept, int pay) { }
// ---- main ----
List<Emp> es = new ArrayList<>(List.of(new Emp("Ann", "IT", 50), new Emp("bob", "HR", 40), new Emp("Cy", "IT", 60), new Emp("Di", "HR", 40)));
es.sort(Comparator.comparing(Emp::dept).thenComparing(Emp::pay, Comparator.reverseOrder()).thenComparing(Emp::name));
System.out.println(es.stream().map(Emp::name).toList());
List<String> names = new ArrayList<>(List.of("bob", "Ann", "cy", "Di"));
Collections.sort(names);
System.out.print(names + " ");
names.sort(String.CASE_INSENSITIVE_ORDER.reversed());
System.out.println(names + " " + Collections.max(List.of(3, 9, 4)));
new TreeSet<Emp>().add(new Emp("x", "y", 1));
```
Output:
```
[Di, bob, Cy, Ann]
[Ann, Di, bob, cy] [Di, cy, bob, Ann] 9
(throws ClassCastException: class Emp cannot be cast to class java.lang.Comparable)
```

#### 11.2 Use annotations such as Override, FunctionalInterface, Deprecated, SuppressWarnings and SafeVarargs
**Standard annotations:** `@Override` makes the compiler check that the method really overrides or implements something. `@FunctionalInterface` checks for exactly one abstract method. `@Deprecated` (optional `since`, `forRemoval`) marks an API as discouraged: using it produces a compiler warning, not an error. `@SuppressWarnings("unchecked")`, `("deprecation")`, `("removal")` or `("rawtypes")` silence those warnings for the annotated element. `@SafeVarargs` asserts a generic varargs method doesn't abuse its array; it is allowed only on constructors and on `static`, `final` or `private` methods.
```java
class Old {
    @Deprecated(since = "2.0", forRemoval = true)
    static int legacy() { return 1; }
    @SafeVarargs
    static <T> List<T> listOf(T... items) { return new ArrayList<>(Arrays.asList(items)); }
    @SuppressWarnings({"unchecked", "rawtypes"})
    static List<String> raw() { List r = new ArrayList(); r.add("raw"); return r; }
}
// ---- main ----
@SuppressWarnings("removal")
int v = Old.legacy();
System.out.println(v + " " + Old.listOf("a", "b") + " " + Old.raw());
```
Output:
```
1 [a, b] [raw]
```
```java
class Pet {
    @Override
    public boolean equals(Pet other) { return true; }
}
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: method does not override or implement a method from a supertype)
```
```java
class Box<T> {
    @SafeVarargs
    void addAll(T... items) { }
}
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: Invalid SafeVarargs annotation. Instance method addAll(T...) is neither final nor private.)
```
```java
@FunctionalInterface
interface TwoWay { int a(); int b(); }
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: Unexpected @FunctionalInterface annotation)
```

#### 11.3 Use generics, including wildcards
**Generics** give compile-time type safety. A generic class `class Box<T>`; a generic method `static <T> T first(List<T> l)` (the type parameter goes before the return type); the diamond `new Box<>()` infers type arguments. **Bounds:** `<T extends Number & Comparable<T>>` lets you call those types' methods. **Type erasure:** type arguments don't exist at run time, so you can't do `new T()`, `instanceof List<String>`, create generic arrays, use primitives as type arguments, or overload methods that differ only in type arguments (name clash).

**Wildcards:** `List<?>` is a list of unknown type (read as Object, can add only null). `List<? extends Number>` accepts `List<Integer>`, `List<Double>`... and is safe to **read** as Number but you can't add (a producer). `List<? super Integer>` accepts `List<Integer>`, `List<Number>`, `List<Object>` and is safe to **add** Integers to, but reads as Object (a consumer): 'producer extends, consumer super'. Note `List<Integer>` is **not** a `List<Number>`.
```java
class Pair<A, B> {
    private final A a; private final B b;
    Pair(A a, B b) { this.a = a; this.b = b; }
    <C> Pair<A, C> withSecond(C c) { return new Pair<>(a, c); }
    public String toString() { return "(" + a + ", " + b + ")"; }
}
class Util {
    static <T extends Comparable<T>> T max(List<T> xs) { T best = xs.get(0); for (T x : xs) if (x.compareTo(best) > 0) best = x; return best; }
    static double sum(List<? extends Number> ns) { double s = 0; for (Number n : ns) s += n.doubleValue(); return s; }
    static void fill(List<? super Integer> sink, int n) { for (int i = 1; i <= n; i++) sink.add(i); }
    static int size(List<?> any) { return any.size(); }
}
// ---- main ----
Pair<String, Integer> p = new Pair<>("x", 1);
List<Number> sink = new ArrayList<>();
Util.fill(sink, 3);
sink.add(2.5);
System.out.println(p.withSecond(true) + " " + Util.max(List.of("pear", "apple", "zoo")) + " " + Util.sum(List.of(1, 2.5, 3L)) + " " + sink + " " + Util.size(List.of('a', 'b')));
```
Output:
```
(x, true) zoo 6.5 [1, 2, 3, 2.5] 2
```
```java
List<Integer> ints = new ArrayList<>();
List<Number> nums = ints;
```
Output:
```
(does not compile: incompatible types: List<Integer> cannot be converted to List<Number>)
```
```java
List<? extends Number> ro = new ArrayList<Integer>();
ro.add(1);
```
Output:
```
(does not compile: incompatible types: int cannot be converted to CAP#1)
```
```java
class Clash {
    void f(List<String> a) { }
    void f(List<Integer> b) { }
}
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: name clash: f(List<Integer>) and f(List<String>) have the same erasure)
```

## Explicitly not here
Streams over collections are S11; concurrent collections are S12.

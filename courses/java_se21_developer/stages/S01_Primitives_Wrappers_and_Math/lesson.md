# S01_Primitives_Wrappers_and_Math - Lesson: Primitives, wrappers, Math, conversions and casting

## Goal
The learner predicts the result of any expression mixing primitive types, wrappers, Math methods, promotion and casts, including overflow, integer caching and unboxing pitfalls.

## Syllabus items taught here
- 1.1 - Use primitives and wrapper classes; evaluate arithmetic and boolean expressions using the Math API, precedence rules, type conversions and casting

## How to teach this
Ask what `Integer a = 127, b = 127; a == b` gives, then the same with 128, and why. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 1.1 Use primitives and wrapper classes; evaluate arithmetic and boolean expressions using the Math API, precedence rules, type conversions and casting
**Numeric promotion:** in a binary operation, `byte`, `short` and `char` operands become `int`; if either operand is `long`, `float` or `double`, the other is widened to match. So `byte + byte` is an `int`, and assigning it back to a byte needs a cast, though compound assignment (`b += 1`) casts implicitly. A compile-time constant that fits is allowed in a narrowing assignment (`byte b = 10;`, `final int k = 5; byte c = k;`). `int` overflow wraps silently; `Math.addExact` throws instead.
```java
byte a = 10, b = 20;
int sum = a + b;
a += 300;
final int K = 5;
byte c = K;
int big = Integer.MAX_VALUE;
System.out.println(sum + " " + a + " " + c + " " + (big + 1) + " " + (long) big * 2 + " " + big * 2L);
char ch = 'a';
ch++;
System.out.println(ch + 1 + " " + (char) (ch + 1) + " " + ('a' + 'b') + " " + "" + 'a' + 'b');
```
Output:
```
30 54 5 -2147483648 4294967294 4294967294
99 c 195 ab
```
**Floating point and casts:** `(int)` truncates towards zero; casting a double beyond the int range gives `Integer.MAX_VALUE` or `MIN_VALUE`; floats are imprecise, so compare with a tolerance. Integer `/ 0` throws `ArithmeticException`, but `double / 0` is `Infinity` and `0.0 / 0` is `NaN` (and `NaN != NaN`).
```java
System.out.println((int) -7.9 + " " + (int) 1e20 + " " + (0.1 + 0.2) + " " + (0.1 + 0.2 == 0.3) + " " + 5.0 / 0 + " " + (0.0 / 0 == 0.0 / 0) + " " + Double.isNaN(0.0 / 0));
```
Output:
```
-7 2147483647 0.30000000000000004 false Infinity false true
```
**Precedence and evaluation:** operands are evaluated left to right, even when precedence groups them differently. `&&`/`||` short-circuit; `&`/`|` on booleans evaluate both sides; `^` is exclusive or. Postfix binds tighter than prefix, which binds tighter than `* / %`.
```java
int i = 2;
int r = i++ + i * --i;
boolean t = false;
boolean u = (t = true) | (i++ > 100);
boolean v = true ^ true || !false & false;
System.out.println(r + " " + i + " " + t + " " + u + " " + v + " " + (7 >> 1) + " " + (-8 >>> 28) + " " + (5 & 3 | 8));
```
Output:
```
8 3 true true false 3 15 9
```
**Wrappers:** each primitive has a wrapper (`Integer`, `Long`, `Double`, `Character`, `Boolean`...). Autoboxing and unboxing convert automatically; unboxing `null` throws `NullPointerException`. `Integer.valueOf` caches -128 to 127, so `==` on boxed values is unreliable: use `equals`. `parseInt` returns a primitive; `valueOf` returns a wrapper. `equals` also checks the type: `Long.valueOf(1).equals(1)` is false because 1 boxes to an Integer.
```java
Integer a = 127, b = 127, c = 128, d = 128;
System.out.println((a == b) + " " + (c == d) + " " + c.equals(d) + " " + Long.valueOf(1).equals(1) + " " + Integer.parseInt("-12") + Integer.valueOf("3") + " " + Integer.compare(3, 7) + " " + Character.getNumericValue('7') + " " + Double.valueOf("2.5e1"));
Integer none = null;
int n = none;
```
Output:
```
true false true false -123 -1 7 25.0
(throws NullPointerException: Cannot invoke "java.lang.Integer.intValue()" because "none" is null)
```
**Math API:** `Math.round` returns `long` for a double and `int` for a float, rounding .5 up (towards positive infinity); `Math.floor`/`ceil` return doubles; `Math.floorDiv` and `floorMod` round towards negative infinity, unlike `/` and `%`; `Math.abs(Integer.MIN_VALUE)` is still negative (overflow); `Math.clamp` is new in Java 21.
```java
System.out.println(Math.round(-2.5) + " " + Math.round(2.5f) + " " + Math.floorDiv(-7, 2) + " " + -7 / 2 + " " + Math.floorMod(-7, 3) + " " + -7 % 3 + " " + Math.abs(Integer.MIN_VALUE) + " " + Math.clamp(15, 0, 10) + " " + Math.hypot(3, 4) + " " + Math.cbrt(27));
```
Output:
```
-2 3 -4 -3 2 -1 -2147483648 10 5.0 3.0
```

## Explicitly not here
String arithmetic and StringBuilder are S02.

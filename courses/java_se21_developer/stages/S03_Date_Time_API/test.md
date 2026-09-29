# S03_Date_Time_API - Test: The Date-Time API and daylight saving time

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
LocalDate d = LocalDate.of(2023, 1, 31);
System.out.println(d.plusMonths(1) + " " + d.plusMonths(1).plusMonths(1) + " " + d.plusMonths(2) + " " + d.getDayOfWeek());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
ZoneId london = ZoneId.of("Europe/London");
ZonedDateTime z = ZonedDateTime.of(2024, 3, 31, 0, 30, 0, 0, london);
System.out.println(z.plusHours(1).toLocalTime() + " " + z.plusHours(2).toLocalTime() + " " + z.plusHours(2).getOffset());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
ZonedDateTime z = ZonedDateTime.of(LocalDateTime.of(2024, 3, 31, 1, 30), ZoneId.of("Europe/London"));
System.out.println(z.toLocalTime() + " " + z.getOffset());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
Period p = Period.ofMonths(14);
Duration d = Duration.ofSeconds(3725);
System.out.println(p + " " + p.normalized() + " " + d + " " + d.toMinutesPart() + " " + Period.of(0, 0, 0));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
LocalDateTime dt = LocalDateTime.of(2024, 1, 1, 12, 0);
System.out.println(dt.plus(Period.ofDays(1)) + " " + dt.plus(Duration.ofDays(1)));
LocalDate.of(2024, 1, 1).plus(Duration.ofHours(24));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
import java.time.format.*;
// ---- main ----
DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
LocalDateTime t = LocalDateTime.parse("2024-02-10 07:05", f);
System.out.println(t + " " + t.format(DateTimeFormatter.ofPattern("d/M/yy h:mm")) + " " + Instant.ofEpochSecond(86400 * 2));
```
7. Which are true? (choose two) Choose every correct option.
   A. LocalDate has a public constructor
   B. Instant represents a point on the UTC time-line
   C. Period.ofDays(1).ofWeeks(1) is a period of 8 days
   D. ZonedDateTime.plusHours works on the instant time-line, so it accounts for DST

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2023-02-28 2023-03-28 2023-03-31 TUESDAY
```
2. Actual result (from running it):
```
02:30 03:30 +01:00
```
3. Actual result (from running it):
```
02:30 +01:00
```
4. Actual result (from running it):
```
P14M P1Y2M PT1H2M5S 2 P0D
```
5. Actual result (from running it):
```
2024-01-02T12:00 2024-01-02T12:00
(throws UnsupportedTemporalTypeException: Unsupported unit: Seconds)
```
6. Actual result (from running it):
```
2024-02-10T07:05 10/2/24 7:05 1970-01-03T00:00:00Z
```
7. Correct: B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Date_Time_API` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Program_Flow.

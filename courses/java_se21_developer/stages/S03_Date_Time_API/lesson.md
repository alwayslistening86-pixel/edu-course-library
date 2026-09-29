# S03_Date_Time_API - Lesson: The Date-Time API and daylight saving time

## Goal
The learner creates and manipulates LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Instant, Period and Duration, formats and parses them, and predicts daylight-saving transitions.

## Syllabus items taught here
- 1.3 - Manipulate date, time, duration, period, instant and time-zone objects, including daylight saving time, using the Date-Time API

## How to teach this
Ask what 01:30 plus one hour is in New York on the night the clocks go forward. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 1.3 Manipulate date, time, duration, period, instant and time-zone objects, including daylight saving time, using the Date-Time API
**Local types** have no zone: `LocalDate`, `LocalTime`, `LocalDateTime`. Build with `of(...)` or `parse(...)` (there are no public constructors). They are immutable: `plusDays` etc. return new objects, so ignoring the result does nothing. Months are 1-based (`Month.MARCH` or 3). Invalid dates throw `DateTimeException`.
```java
import java.time.*;
import java.time.temporal.ChronoUnit;
// ---- main ----
LocalDate d = LocalDate.of(2024, 1, 31);
d.plusDays(1);
LocalDate e = d.plusMonths(1);
LocalDateTime dt = LocalDateTime.of(2024, Month.MARCH, 9, 23, 30).plusMinutes(45);
System.out.println(d + " " + e + " " + e.isLeapYear() + " " + dt + " " + dt.getDayOfWeek() + " " + d.withDayOfMonth(1).getDayOfYear() + " " + ChronoUnit.DAYS.between(d, e));
System.out.println(LocalTime.of(23, 50).plusMinutes(20) + " " + LocalDate.parse("2024-02-29").plusYears(1) + " " + d.isBefore(e));
LocalDate.of(2023, 2, 29);
```
Output:
```
2024-01-31 2024-02-29 true 2024-03-10T00:15 SUNDAY 1 29
00:10 2025-02-28 true
(throws DateTimeException: Invalid date 'February 29' as '2023' is not a leap year)
```
**Period** measures dates in years, months and days; **Duration** measures time in seconds and nanoseconds. `Period.of(1, 2, 3)` prints `P1Y2M3D`; `Duration.ofMinutes(90)` prints `PT1H30M`. Adding a Duration to a LocalDate throws `UnsupportedTemporalTypeException`. Period's `ofXxx` factories don't chain: `Period.ofYears(1).ofMonths(2)` is just 2 months (a static call via an instance).
```java
import java.time.*;
// ---- main ----
Period p = Period.between(LocalDate.of(2020, 5, 20), LocalDate.of(2024, 3, 10));
Duration du = Duration.between(LocalTime.of(9, 15), LocalTime.of(17, 5));
Period chain = Period.ofYears(1).ofMonths(2);
System.out.println(p + " " + du + " " + du.toMinutes() + " " + chain + " " + Period.ofWeeks(2) + " " + Duration.ofHours(25) + " " + LocalDate.of(2024, 1, 31).plus(Period.ofMonths(1)));
LocalDate.of(2024, 1, 1).plus(Duration.ofDays(1));
```
Output:
```
P3Y9M19D PT7H50M 470 P2M P14D PT25H 2024-02-29
(throws UnsupportedTemporalTypeException: Unsupported unit: Seconds)
```
**Instant** is a point on the UTC time-line (epoch seconds). **ZonedDateTime** is a local date-time plus a `ZoneId` and offset. When clocks go **forward** (a gap), a local time that doesn't exist is moved later by the gap length; when clocks go **back** (an overlap), the earlier offset is kept. Arithmetic with `plusHours` works on the instant time-line; `plusDays` keeps the local time.
```java
import java.time.*;
// ---- main ----
ZoneId ny = ZoneId.of("America/New_York");
ZonedDateTime before = ZonedDateTime.of(2024, 3, 10, 1, 30, 0, 0, ny);
System.out.println(before + " -> " + before.plusHours(1));
System.out.println(ZonedDateTime.of(LocalDateTime.of(2024, 3, 10, 2, 30), ny));
ZonedDateTime fall = ZonedDateTime.of(2024, 11, 3, 1, 30, 0, 0, ny);
System.out.println(fall + " -> " + fall.plusHours(1) + " | " + fall.plusDays(1));
Instant i = Instant.ofEpochSecond(0).plus(Duration.ofDays(1));
System.out.println(i + " " + i.atZone(ZoneId.of("Asia/Tokyo")).toLocalDateTime() + " " + Duration.between(before, before.plusDays(1)).toHours());
```
Output:
```
2024-03-10T01:30-05:00[America/New_York] -> 2024-03-10T03:30-04:00[America/New_York]
2024-03-10T03:30-04:00[America/New_York]
2024-11-03T01:30-04:00[America/New_York] -> 2024-11-03T01:30-05:00[America/New_York] | 2024-11-04T01:30-05:00[America/New_York]
1970-01-02T00:00:00Z 1970-01-02T09:00 23
```
**Formatting and parsing:** `DateTimeFormatter.ofPattern("dd MMM yyyy HH:mm")` (`M` month, `m` minute, `H` 0-23, `h` 1-12 with `a`, `E` day name, text in single quotes). Formatting a `LocalDate` with a time pattern throws. Predefined formatters include `ISO_LOCAL_DATE`.
```java
import java.time.*;
import java.time.format.*;
// ---- main ----
DateTimeFormatter f = DateTimeFormatter.ofPattern("EEE dd/MM/yyyy 'at' hh:mm a", Locale.UK);
LocalDateTime t = LocalDateTime.of(2024, 7, 4, 15, 5);
System.out.println(t.format(f) + " | " + LocalDate.parse("04-07-2024", DateTimeFormatter.ofPattern("dd-MM-yyyy")) + " | " + DateTimeFormatter.ISO_LOCAL_DATE.format(t));
LocalDate.of(2024, 7, 4).format(DateTimeFormatter.ofPattern("HH:mm"));
```
Output:
```
Thu 04/07/2024 at 03:05 pm | 2024-07-04 | 2024-07-04
(throws UnsupportedTemporalTypeException: Unsupported field: HourOfDay)
```

## Explicitly not here
Locale-specific date styles (FormatStyle) are in S14.

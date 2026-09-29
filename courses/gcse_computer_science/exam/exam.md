# GCSE Computer Science (AQA 8525) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Paper 1 covers algorithms and programming (S01-S12): multiple-choice, short-answer and longer programming/problem-solving questions, including code-tracing and writing short routines in AQA pseudo-code or Python. Paper 2 covers data representation, computer systems, networks, cyber security, databases/SQL and ethical/legal/environmental impacts (S13-S29): multiple-choice, short-answer, longer-answer, extended-response and SQL questions. Questions are original; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest, kept to each paper's real content split.

## 11 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Paper 1] Trace a linear search for the value 9 in [2, 5, 9, 14, 20]. State the number of comparisons made. [2 marks]
2. [Paper 1] Explain how binary search differs from linear search, and state the one precondition binary search requires. [3 marks]
3. What does this print? (If it raises an error, name it.)
```python
def is_even(n):
    return n % 2 == 0

for i in range(1, 6):
    if is_even(i):
        print(i, "is even")
    else:
        print(i, "is odd")
```
4. [Paper 1] A program needs to validate that an entered mark is a whole number from 0 to 100 inclusive. Suggest one normal, one boundary and one erroneous test value, and explain the purpose of each. [3 marks]
5. Which data structure groups several related fields, possibly of different types, about a single entity? Choose every correct option.
   A. a record
   B. an array
   C. a subroutine
   D. a Boolean
6. [Paper 2] Convert 01111011 (binary) to decimal and to hexadecimal, showing your working. [3 marks]
7. [Paper 2] A mono sound is sampled at 5,000 Hz with an 8-bit sample resolution, lasting 2 seconds. Calculate the file size in bytes. [3 marks]
8. In the fetch-execute cycle, which component holds the address of the next instruction to be fetched? Choose every correct option.
   A. the Program Counter
   B. the Accumulator
   C. the Control Unit
   D. the cache
9. [Paper 2] Explain the purpose of encryption on a network, and why HTTPS is preferred over HTTP for a login page. [3 marks]
10. [Paper 2] Given a Books table (id, title, author, price), write a SQL statement that returns the title and price of every book costing less than £10, cheapest first. [3 marks]
11. [Paper 2] Discuss the ethical and legal issues raised by storing personal data in cloud storage. [6 marks]

## Answer key for the ready-made items (tutor only)
1. [2] B1 checks index 0 (2), 1 (5), 2 (9) -- found; B1 3 comparisons.
2. [3] B1 binary search repeatedly halves the remaining section by comparing the target with the middle item, rather than checking items one by one; B1 it is far more efficient than linear search on large lists; B1 precondition: the list must already be sorted.
3. Actual result (from running it):
```
1 is odd
2 is even
3 is odd
4 is even
5 is odd
```
4. [3] B1 normal, e.g. 65 (a plausible in-range value that should be accepted); B1 boundary, e.g. 0 or 100 (tests the exact edge of the valid range); B1 erroneous, e.g. -1, 101 or 'abc' (should be rejected, testing the check correctly refuses invalid input).
5. Correct: A (exactly these options, no others)
6. [3] M1 decimal: 64+32+16+8+2+1 = 123; M1 hex nibbles 0111=7, 1011=B; A1 0x7B.
7. [3] M1 bits = 5,000 x 8 x 2 = 80,000; A1 bytes = 10,000; B1 correct method (rate x resolution x duration, then / 8).
8. Correct: A (exactly these options, no others)
9. [3] B1 encryption scrambles data so it is unreadable without the correct key, protecting it if intercepted; B1 HTTPS encrypts data sent between browser and server; B1 so a password sent over HTTPS (unlike plain HTTP) cannot be read even if intercepted in transit.
10. [3] M1 correct SELECT title, price FROM Books; M1 WHERE price < 10; A1 ORDER BY price ASC;
11. [6] Level 2 (4-6): balanced discussion covering legal issues (which jurisdiction's laws apply; who can be compelled to access the data), ethical issues (trust in a third party with personal data; user's lack of direct control), and a reasoned overall point. Level 1 (1-3): limited/one-sided discussion. 0: no relevant discussion.

## Grading
Mark short answers and multiple-choice against the mark schemes; mark calculations and conversions with method shown (a correct final answer with no valid method shown earns only what the mark scheme allows for a bare answer); mark the extended-response ethics/impact question by levels. A pass needs at least 50% of the 180 marks overall and at least 40% on each paper. Report the total, the percentage per paper and the weakest topic areas. AQA's grade boundaries change every series, so the course does not claim a predicted grade.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.

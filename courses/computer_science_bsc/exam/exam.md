# Computer Science (BSc Hons) -- Open University R88 module-framework structure, QAA Computing Benchmark graded - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
One paper covering every stage. Section A (S01-S10, programming, systems, maths, algorithms, theory, networks): structured questions, code traces and multiple-select items. Section B (S11-S15, AI, professional/ethical issues and the project strand): further structured questions plus at least one extended-response item marked on levels. Questions are original; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest.

## 5 ready-made items (write the rest fresh, never reusing stage-test items)
1. What does this print? (If it raises an error, name it.)
```python
def flatten(xs):
    return [y for x in xs for y in (flatten(x) if isinstance(x, list) else [x])]

print(flatten([1, [2, 3, [4, [5]]], 6]))
```
2. [Section A] A hash table of size 7 uses the hash function h(k) = k mod 7 and linear probing. Insert the keys 10, 17, 3, 24 in that order and state the final table (index: key). [5 marks]
3. [Section A] Convert the IP address 192.168.1.130 with subnet mask 255.255.255.192 (/26) to its network address and state the number of usable host addresses on that subnet. [5 marks]
4. [Section A] For f(n) = 3n^2 + 5n + 2, state its Big-O time complexity and justify your answer from the definition of Big-O. [3 marks]
5. [Section B] A recommendation system trained on historical hiring data is proposed to screen job applicants automatically, with human review only for applicants it rejects. Discuss the ethical and professional issues this raises, drawing on named ethical frameworks and the BCS Code of Conduct. [20 marks]

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
[1, 2, 3, 4, 5, 6]
```
2. [5] M1 h(10)=3, index 3 empty, place 10 at 3; M1 h(17)=3, occupied, probe to 4, place 17 at 4; M1 h(3)=3, occupied, probe 4 occupied, probe 5, place 3 at 5; M1 h(24)=3, occupied, probes 4,5 occupied, probe 6, place 24 at 6; A1 final table {3:10, 4:17, 5:3, 6:24}.
3. [5] M1 /26 gives a block size of 256-192=64 addresses per subnet; M1 subnets are .0, .64, .128, .192; A1 130 falls in the .128 subnet, so network address 192.168.1.128; M1 usable hosts = 2^(32-26)-2 = 62; A1 broadcast address 192.168.1.191 (not asked but confirms working).
4. [3] B1 O(n^2); B1 Big-O ignores lower-order terms and constant factors, valid since for n>=1, 3n^2+5n+2 <= 10n^2 (a constant c=10 and threshold n0=1 exist with f(n) <= c.n^2); B1 the n^2 term dominates growth as n becomes large.
5. [20] Mark out of 20 using honours-level (RQF Level 6) discursive levels, per the QAA Computing benchmark's expectation that graduates can 'engage with fundamental, legal, social, ethical and professional issues': Level 1 (1-4) states a position with little justification or named concept/framework; Level 2 (5-9) identifies relevant concepts/frameworks but applies them only descriptively, with limited weighing of alternatives; Level 3 (10-14) applies named concepts/frameworks (e.g. a specific ethical framework, professional code clause, or legal provision) accurately to the scenario and weighs at least one genuine counter-consideration; Level 4 (15-17) a well-structured argument that applies multiple relevant frameworks correctly, explicitly weighs competing considerations, and reaches a justified, nuanced conclusion; Level 5 (18-20) a sophisticated answer that additionally identifies tensions between frameworks or stakeholders the question does not spell out, and sustains a precise, fully justified judgement throughout. Credit specifically: the asymmetry of only human-reviewing rejections (which can entrench bias since accepted-but-wrongly-screened cases are never checked); bias risk from historical hiring data reflecting past discriminatory patterns; the BCS Code of Conduct's duties around public interest, professional competence and not misrepresenting a system's capabilities; a consequentialist framing (net benefit/harm to applicants and the employer) against a deontological framing (a duty of fairness/non-discrimination regardless of net benefit); UK Equality Act / GDPR-adjacent concerns about automated decision-making.

## Grading
Mark every question against a written mark scheme (M, A and B marks for calculation/code items, levels for the extended-response item, as in the stage tests). A pass needs at least 60% of the total marks, with at least 50% on each section. Report the total, the percentage per section and the weakest topic areas.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.

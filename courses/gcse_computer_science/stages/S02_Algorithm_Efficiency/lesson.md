# S02_Algorithm_Efficiency - Lesson: Efficiency of algorithms

## Goal
The learner recognises that multiple algorithms can solve the same problem, and compares algorithms' efficiency, explaining why one is more efficient than another.

## Syllabus items taught here
- 3.1.2 - Efficiency of algorithms

## How to teach this
Ask the learner to find a name in a phone book that's alphabetically sorted -- would they read every entry from the start, or open it near the middle first? Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.1.2 Efficiency of algorithms
More than one algorithm can correctly solve the same problem, but different algorithms can take very different amounts of time and use different amounts of memory to reach the same correct answer. **Efficiency** compares algorithms by roughly how many steps (time) or how much memory (space) they need, especially as the size of the input grows. One algorithm is more efficient than another if it reliably needs fewer steps/comparisons to solve the same size of problem: e.g. checking every entry in an unsorted list one by one is less efficient than a method that can rule out half the remaining entries at each step, because the second approach needs far fewer comparisons for a large list. Efficiency is usually judged by how the number of steps grows as the input gets bigger (a small list may make an inefficient algorithm look fine, but the difference becomes large for a big list), not just by timing one run on one machine.

## Explicitly not here
Two specific searching algorithms, compared directly, are S03.

# S18_Data_Compression - Lesson: Data compression: Huffman coding and RLE

## Goal
The learner explains what data compression is and why it is used, and explains and applies Huffman coding and run-length encoding (RLE), interpreting Huffman trees and calculating compressed sizes.

## Syllabus items taught here
- 3.3.8 - Data compression: Huffman coding and run-length encoding

## How to teach this
Ask the learner why it makes sense to give the most frequent letters in a text the shortest codes, and long strings of identical values a single count instead of repeating them. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.8 Data compression: Huffman coding and run-length encoding
**Data compression** reduces the number of bits needed to store or transmit data. It is used because compressed files take up less storage space and transfer faster over a network, at the cost of extra processing time to compress and decompress them (and, for lossy methods not required here, some quality). **Huffman coding** is a lossless method that assigns shorter binary codes to more frequently occurring symbols (characters) and longer codes to rarer ones, using a **Huffman tree** built by repeatedly combining the two least frequent items into a new node (whose frequency is their sum) until one tree remains; each symbol's code is read from the root to its leaf (e.g. left = 0, right = 1). *Worked example:* the string "AAAAABBBCCD" has frequencies A=5, B=3, C=2, D=1 (11 characters total). Building the tree: combine D(1) and C(2) into a node of frequency 3; combine that node with B(3) into a node of frequency 6; combine that node with A(5) to form the root (frequency 11). Reading the tree gives codes A=0 (1 bit), B=10 (2 bits), C=110 (3 bits), D=111 (3 bits); total Huffman-coded size = (5x1)+(3x2)+(2x3)+(1x3) = 20 bits, compared with 88 bits if every character used a fixed 8-bit ASCII code -- a substantial saving (about 77% smaller). **Run-length encoding (RLE)** is a lossless method suited to data with long runs of the same repeated value (such as some bitmap images): instead of storing each repeated value individually, it stores each run as a (value, count) pair. *Worked example:* the binary row "000001111100000" (15 bits: five 0s, then five 1s, then five 0s) is represented in RLE as the pairs (0,5), (1,5), (0,5), which is much shorter to store than 15 individual bits once a data set has many long runs.

## Explicitly not here
This is the last data-representation stage; S19 begins computer systems.

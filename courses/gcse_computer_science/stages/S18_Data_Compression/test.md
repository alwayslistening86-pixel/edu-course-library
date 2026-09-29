# S18_Data_Compression - Test: Data compression: Huffman coding and RLE

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what data compression is and state one advantage and one disadvantage of compressing a file. [3 marks]
2. A Huffman tree gives the codes: E=0, T=10, X=110, Q=111. Decode the bit string 010110111. [3 marks]
3. A run of pixels in a black-and-white image row is: 111111000000001111 (18 bits). Represent this using run-length encoding. [2 marks]
4. Explain why RLE would compress a scanned line drawing (mostly plain white with a few black lines) well, but would compress a photograph of a busy, colourful street scene poorly. [3 marks]
5. In Huffman coding, which characters are given the shortest binary codes? Choose every correct option.
   A. the most frequently occurring characters
   B. the least frequently occurring characters
   C. the characters earliest in the alphabet
   D. the characters with the smallest ASCII code

## Answer key (for the tutor only)
1. [3] B1 reducing the number of bits needed to store/transmit data; B1 advantage: e.g. takes up less storage space, or transfers faster over a network; B1 disadvantage: e.g. extra processing time/power needed to compress and decompress it.
2. [3] M1 splits correctly using the prefix-free codes: 0 | 10 | 110 | 111; A1 decodes as E, T, X, Q; B1 explains each code is read until a valid leaf/character is matched (no code is a prefix of another, so the split is unambiguous).
3. [2] B1 correctly counts each run: six 1s, eight 0s, four 1s; B1 (1,6),(0,8),(1,4).
4. [3] B1 RLE relies on long runs of the same repeated value; B1 the line drawing has large areas of a single repeated colour (long runs), so RLE saves a lot; B1 the photograph has pixel values that change frequently/rarely repeat in long runs, so RLE gives little or no saving (may even increase size).
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S18_Data_Compression` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S19_Hardware_Software_Classification.

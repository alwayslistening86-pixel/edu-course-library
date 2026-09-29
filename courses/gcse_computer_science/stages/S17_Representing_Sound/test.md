# S17_Representing_Sound - Test: Representing sound

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why an analogue sound signal must be sampled before it can be stored on a computer. [2 marks]
2. A mono sound is recorded at a sampling rate of 11000 Hz, with a sample resolution of 16 bits, lasting 4 seconds. Calculate the file size in bytes. [3 marks]
3. Explain the effect of increasing the sample resolution on both the accuracy of the recording and its file size. [2 marks]
4. Which change would increase a digital sound file's size, all else equal? Choose every correct option.
   A. increasing the sampling rate
   B. reducing the sampling rate
   C. reducing the duration of the recording
   D. reducing the sample resolution

## Answer key (for the tutor only)
1. [2] B1 a computer can only store discrete binary numbers, not a continuously varying (analogue) signal; B1 sampling measures the wave's amplitude at regular intervals so each measurement can be stored as a binary number, approximating the original wave.
2. [3] M1 bits = 11000 x 16 x 4 = 704,000; A1 bytes = 88,000; B1 correct method (rate x resolution x duration, then / 8) clearly shown.
3. [2] B1 a higher resolution can represent finer differences in amplitude, so the digital recording is a more accurate approximation of the original sound; B1 but each sample needs more bits, so the file size increases.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S17_Representing_Sound` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S18_Data_Compression.

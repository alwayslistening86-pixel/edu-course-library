# S17_Representing_Sound - Lesson: Representing sound

## Goal
The learner understands that sound is analogue and must be sampled to be stored digitally, describes sampling rate and sample resolution, and calculates sound file sizes.

## Syllabus items taught here
- 3.3.7 - Representing sound

## How to teach this
Ask the learner why a computer, which only stores numbers, has to take repeated 'snapshots' of a sound wave rather than storing the smooth wave directly. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.7 Representing sound
Real sound is an **analogue** signal: a continuously varying wave, with no fixed set of possible values. To store sound digitally, it must be **sampled**: the amplitude (height) of the analogue wave is measured at regular intervals, and each measurement is stored as a binary number, building up a digital approximation of the original wave. The **sampling rate** is how many samples are taken per second, measured in Hertz (Hz); a higher sampling rate captures the changing wave more accurately (closer to the original) but produces more data. The **sample resolution** (bit depth) is how many bits are used to store each individual sample's value; a higher resolution can represent finer differences in amplitude more accurately, but again produces more data. Sound file size is calculated as: **file size (bits) = sampling rate (Hz) x sample resolution (bits) x duration (seconds)**, dividing by 8 for bytes. *Worked example:* a mono recording sampled at 8000 Hz, with a resolution of 8 bits, lasting 5 seconds: file size = 8000 x 8 x 5 = 320,000 bits = 40,000 bytes = 40 KB.

## Explicitly not here
Reducing that file size through compression is S18.

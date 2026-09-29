# S19_Analogue_Digital_and_Multimedia - Test: Analogue/digital data, images, sound, compression and encryption

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what analogue-to-digital conversion does, and how sample rate and resolution each affect the accuracy of the digital result. [4 marks]
2. Explain the key difference between how MIDI represents music and how a sampled digital audio file (e.g. a WAV/MP3) represents it. [3 marks]
3. Run-length encode the string "CCCCCCDDAAAA", showing your working, and explain why RLE compresses this string well but would compress a string with no repeated characters poorly. [4 marks]
4. Explain the difference between lossless and lossy compression, and why lossy compression is often used for photographs. [3 marks]
5. Which statement about encryption is correct? Choose every correct option.
   A. it scrambles data using a key so it is unreadable without the correct key to reverse it, but does not by itself reduce data size
   B. encryption always makes data smaller in the same way lossless compression does
   C. encrypted data can be read normally by anyone without needing any key
   D. encryption and compression are the same technique with different names

## Answer key (for the tutor only)
1. [4] B1 samples an analogue signal at regular intervals, measuring (and quantising) its level at each point, storing the sequence digitally; B1 a higher sample rate takes measurements more often, capturing changes in the signal more accurately over time; B1 a higher resolution (more bits per sample) allows finer distinctions between levels, reducing quantisation error; B1 both increase storage requirements/file size.
2. [3] B1 MIDI stores instructions describing a performance (which note, how loud, how long, on which instrument), not the actual sound wave; B1 a sampled audio file stores the actual sampled sound wave itself; B1 as a result, MIDI files are far smaller and easily edited note-by-note, but the same MIDI file can sound different on different playback devices, unlike a fixed sampled recording.
3. [4] M1 identify runs: C(6), D(2), A(4); A1 RLE output: 6C2D4A; B1 RLE works well when data has long runs of the same repeated value, replacing many repeated symbols with one count+value pair; B1 with no repeated characters, every 'run' has length 1, so the RLE output would be no shorter (or even longer) than the original.
4. [3] B1 lossless compression can be perfectly reversed to recover the exact original data; B1 lossy compression discards some information judged least noticeable, so the original cannot be perfectly recovered, but achieves much greater size reduction; B1 photographs can often lose some detail without a viewer noticing much difference, so the large size saving from lossy compression is usually judged worth the small quality loss.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S19_Analogue_Digital_and_Multimedia` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S20_Hardware_Software_Languages_Logic.

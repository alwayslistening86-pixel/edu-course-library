# S19_Analogue_Digital_and_Multimedia - Lesson: Analogue/digital data, images, sound, compression and encryption

## Goal
The learner explains analogue-to-digital conversion, bitmapped vs vector graphics, digital sound representation and MIDI, and data compression and encryption.

## Syllabus items taught here
- 4.5.6.1 - Analogue and digital data; analogue-to-digital conversion
- 4.5.6.4 - Bitmapped and vector graphics
- 4.5.6.7 - Digital representation of sound, and MIDI
- 4.5.6.9 - Data compression and encryption

## How to teach this
Ask the learner what a microphone actually captures (a smoothly varying signal) and what a computer needs instead (a sequence of discrete numbers) -- and how one becomes the other. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.5.6.1 Analogue and digital data; analogue-to-digital conversion
**Analogue** data varies smoothly and continuously (e.g. a sound wave's air pressure, a dimmer switch's brightness); **digital** data is represented as discrete values (binary numbers). **Analogue-to-digital conversion (ADC)** samples the analogue signal at regular intervals, measuring (and rounding, or **quantising**, to the nearest representable value) its level at each sample point, and stores the sequence of measured values digitally. Higher **sample rate** (samples per second) and higher **resolution** (bits per sample, giving finer quantisation) both give a more accurate digital representation of the original analogue signal, but need more storage.

#### 4.5.6.4 Bitmapped and vector graphics
**Bitmapped (raster) graphics** store an image as a grid of individually coloured **pixels**; each pixel's colour is stored using a fixed number of bits (its **colour depth**). Scaling a bitmap image up loses quality (**pixelation**) because there is no more detail to draw on, only the existing pixels enlarged. **Vector graphics** instead store an image as a set of mathematical shapes/paths (lines, curves, fills) with properties like start/end points, colour and thickness; a vector image can be scaled to any size without losing quality, since the shapes are recalculated/redrawn at the new size, but it is less suited to photographic/highly detailed images (which have no simple underlying shapes to describe).

#### 4.5.6.7 Digital representation of sound, and MIDI
**Digital sound** is captured by sampling an analogue sound wave's amplitude at regular intervals (as in ADC, above); the sample rate and bit resolution together determine sound quality and file size, just as with images. **MIDI (Musical Instrument Digital Interface)** takes a fundamentally different approach: rather than storing sampled audio, it stores **instructions** describing a performance -- which note, how loud, how long, on which instrument -- to be played back by a synthesiser. This makes MIDI files far smaller than sampled audio of the same music, and easily editable (individual notes can be changed), but the actual sound produced depends entirely on the playback device/synthesiser used, unlike a sampled recording which always sounds the same.

#### 4.5.6.9 Data compression and encryption
**Data compression** reduces the size of stored/transmitted data. **Lossless compression** (e.g. run-length encoding, RLE, which replaces runs of repeated values with a count and the value, e.g. "AAAAABBBCC" becomes "5A3B2C") can be perfectly reversed to recover the exact original data; **lossy compression** discards some information judged less noticeable (used for photos, audio, video) to achieve much greater size reduction, but the original cannot be perfectly recovered. **Encryption** scrambles data using an algorithm and a **key**, so it is unreadable without the correct key to reverse (decrypt) it, protecting confidentiality if data is intercepted or stolen; it does not reduce the size of data (encryption and compression solve different problems, and if both are wanted, data is normally compressed before it is encrypted).

## Explicitly not here
This is the last data-representation stage; S20 begins computer systems.

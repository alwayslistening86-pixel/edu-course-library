# S10_Bioelectricity_and_Medical_Instrumentation - Test: Bioelectricity and Medical Instrumentation

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why an instrumentation (differential) amplifier, rather than a simple single-ended amplifier, is used for ECG measurement, referring specifically to mains interference. [3 marks]
2. A biosignal has an EEG-band frequency content up to 100 Hz. An engineer samples it at 150 Hz. Explain, using the Nyquist-Shannon theorem, why this sampling rate is inadequate, and state a suitable minimum sampling rate. [3 marks]
3. Which filter type(s) would be appropriate to remove baseline wander (very low frequency drift from breathing/electrode motion) from an ECG trace while preserving the QRS complex? Choose every correct option.
   A. A high-pass filter with a low cutoff (e.g. ~0.5 Hz)
   B. A low-pass filter with a cutoff of 1 Hz
   C. A notch filter at 50/60 Hz
   D. A low-pass filter with a cutoff of around 150 Hz
4. A recorded ECG signal has a signal power of 4.0 mW and a noise power of 0.02 mW. Calculate the SNR in dB. [2 marks]
5. An amplifier design has differential gain 500. If a CMRR of at least 80 dB is required, calculate the maximum common-mode gain permitted. [3 marks]

## Answer key (for the tutor only)
1. [3] B1 mains (50/60 Hz) interference is picked up roughly equally by both electrodes, so it is a common-mode signal; B1 a differential amplifier amplifies only the difference between the two electrode signals, rejecting the common-mode interference while amplifying the genuine (differential) cardiac signal; B1 a single-ended amplifier would amplify the interference along with the signal, since it has no way to distinguish common from differential components.
2. [3] B1 the Nyquist rate requires sampling faster than twice the highest frequency present, i.e. > 200 Hz here, so 150 Hz is below this and will cause aliasing; B1 aliased high-frequency content folds back and appears indistinguishable from genuine low-frequency content in the sampled signal, corrupting it; B1 a suitable rate is any value clearly above 200 Hz (e.g. 250-500 Hz), ideally with an anti-aliasing filter applied before sampling.
3. Correct: A, D (exactly these options, no others)
4. [2] M1 SNR(dB) = 10 log10(4.0/0.02); A1 = 23.0 dB.
5. [3] M1 80 = 20 log10(500/Acm); M1 500/Acm = 10^(80/20) = 10000; A1 Acm = 500/10000 = 0.0500.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Bioelectricity_and_Medical_Instrumentation` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Biophotonics_Signal_Processing_and_Biomedical_Component_Design.

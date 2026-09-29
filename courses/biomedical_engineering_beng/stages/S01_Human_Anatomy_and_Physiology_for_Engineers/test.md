# S01_Human_Anatomy_and_Physiology_for_Engineers - Test: Human Anatomy and Physiology for Engineers

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why the resting membrane potential and the action potential are relevant to a biomedical engineer designing an ECG amplifier, referring to amplitude and timescale. [3 marks]
2. A patient has systolic pressure 130 mmHg and diastolic pressure 85 mmHg. Calculate the pulse pressure and the mean arterial pressure. [3 marks]
3. Which of the following are synovial joints? Choose every correct option.
   A. hip
   B. skull sutures
   C. knee
   D. elbow
4. Minute ventilation is tidal volume x respiratory rate. A patient breathes at 14 breaths/min with tidal volume 480 mL. A ventilator engineer needs to deliver this same minute ventilation at a slower rate of 10 breaths/min. Find the new tidal volume required. [3 marks]
5. Give the negative-feedback loop structure (three named components) that a bioengineer would use as an analogy when designing a closed-loop insulin pump, and match each to its physiological equivalent. [3 marks]

## Answer key (for the tutor only)
1. [3] B1 the AP is a ~1 ms, roughly 100 mV depolarisation event, so the amplifier needs a bandwidth that captures signals changing on a millisecond timescale; B1 the extracellular signal reaching skin electrodes is millivolts, far smaller than the intracellular AP, so high gain and low noise are both needed; B1 knowing the physiological origin lets the engineer distinguish real cardiac signal from electrical noise or motion artefact.
2. [3] M1 pulse pressure = 130 - 85 = 45 mmHg; M1 MAP = diastolic + (1/3)(systolic - diastolic); A1 = 100.0 mmHg.
3. Correct: A, C, D (exactly these options, no others)
4. [3] M1 minute ventilation = 480 x 14 = 6720 mL/min; M1 new tidal volume = 6720/10; A1 672 mL.
5. [3] B1 sensor (continuous glucose monitor / physiological receptor); B1 controller (pump algorithm / control centre); B1 effector (insulin delivery / physiological effector organ), acting to oppose the deviation from target blood glucose.

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Human_Anatomy_and_Physiology_for_Engineers` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Mathematical_and_Statistical_Methods_for_Bioengineering.

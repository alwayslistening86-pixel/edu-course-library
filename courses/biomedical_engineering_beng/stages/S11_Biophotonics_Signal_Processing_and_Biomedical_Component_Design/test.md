# S11_Biophotonics_Signal_Processing_and_Biomedical_Component_Design - Test: Biophotonics, Signal Processing and Biomedical Component Design

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Using the base-10 Beer-Lambert law A = epsilon c L, a solution of a single absorbing species has epsilon = 150 L/(mol cm) at a given wavelength, path length L = 1.0 cm, and measured absorbance A = 0.45. Calculate the concentration c. [3 marks]
2. Explain, in terms of the Beer-Lambert law and haemoglobin's absorption spectrum, why pulse oximetry uses two specific wavelengths (red ~660 nm and infrared ~940 nm) rather than just one. [4 marks]
3. Which of the following are genuine reasons a clinician might choose ultrasound over CT for a given imaging task, based on this stage? Choose every correct option.
   A. Ultrasound uses no ionising radiation
   B. Ultrasound gives real-time imaging
   C. Ultrasound penetrates bone and air-filled structures better than CT
   D. Ultrasound generally has lower equipment/running cost than CT
4. A chest CT scan delivers an effective dose of 7 mSv, compared with a chest X-ray's 0.02 mSv. Calculate how many chest X-rays would deliver the same effective dose as one such CT scan, and briefly state the dose-related engineering/clinical principle this comparison illustrates. [3 marks]
5. A photoplethysmogram's cardiac pulsatile component has frequency content up to about 5 Hz. State the minimum sampling rate to satisfy the Nyquist criterion, and explain in one sentence why a moving-average filter might still be applied even after correct sampling. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 A = epsilon c L => c = A/(epsilon L); A1 c = 0.45/(150x1.0); A1 = 0.0030 mol/L (= 3.00 mmol/L).
2. [4] B1 oxygenated (HbO2) and deoxygenated (Hb) haemoglobin have different molar absorptivities, and the difference between them is large at red but small at infrared wavelengths; B1 measuring at a single wavelength alone cannot separate the contribution of blood oxygenation from other factors (e.g. total blood volume/path length changes) affecting absorbance; B1 using the ratio of absorbance changes at two wavelengths (R, BP-3) cancels out path-length-dependent factors common to both, leaving a quantity that varies specifically (and can be calibrated) against blood oxygen saturation; B1 red is chosen because Hb/HbO2 differ strongly there, giving the measurement good sensitivity to oxygenation changes.
3. Correct: A, B, D (exactly these options, no others)
4. [3] M1 ratio = 7/0.02; A1 = 350 X-rays; B1 illustrates the ALARA principle (as low as reasonably achievable) -- because CT delivers substantially more dose, imaging modality and protocol should be chosen/optimised to use no more radiation dose than needed to answer the clinical question.
5. [3] B1 minimum sampling rate > 2 x 5 = 10 Hz (Nyquist rate; a practical design would sample well above this for margin); B2 a moving-average filter is applied to smooth out remaining higher-frequency noise (e.g. motion artefact, electronic noise) that lies within the sampled bandwidth and was not removed by anti-aliasing filtering before sampling, at the cost of some signal delay and loss of fine detail.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Biophotonics_Signal_Processing_and_Biomedical_Component_Design` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Biomaterials_II_Drug_Delivery_and_Regenerative_Medicine.

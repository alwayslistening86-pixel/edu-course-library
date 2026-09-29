# S10_Bioelectricity_and_Medical_Instrumentation - Lesson: Bioelectricity and Medical Instrumentation

## Goal
The learner explains how the heart's and muscles' electrical activity is detected at the skin, designs a biopotential amplifier's key parameters, and applies sampling theory and basic filtering to a biomedical signal.

## Syllabus items taught here
- MI-1 - From cellular action potential to the surface ECG
- MI-2 - Biopotential electrodes
- MI-3 - Instrumentation amplifiers and common-mode rejection
- MI-4 - Frequency content of ECG, EMG and EEG
- MI-5 - The Nyquist-Shannon sampling theorem applied to biosignals
- MI-6 - Basic filtering and signal-to-noise ratio

## How to teach this
Ask: the heart's electrical signal at the cell is around 100 mV, but a standard ECG electrode on the skin picks up only about 1 mV -- where did the other 99% go, and what does an ECG amplifier's design have to do about it? Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### MI-1 From cellular action potential to the surface ECG
**From action potential to surface ECG**: as a wave of depolarisation spreads through cardiac muscle (triggered by the sinoatrial node, then travelling through the atria, the atrioventricular node, and the ventricles via the bundle of His and Purkinje fibres), the net electrical dipole this creates is detectable, greatly attenuated by the resistive/capacitive path through tissue, at electrodes on the skin -- typically only about 1 mV, versus the ~100 mV transmembrane action potential (S01, AP-6) itself. The classic ECG waveform (P wave = atrial depolarisation, QRS complex = ventricular depolarisation, T wave = ventricular repolarisation) is this attenuated, filtered signature of the underlying cellular electrical events.

#### MI-2 Biopotential electrodes
**Biopotential electrodes**: surface Ag/AgCl electrodes form a stable electrode-skin electrochemical interface (via a conductive gel), converting ionic current in the body to electronic current in the measurement circuit; the electrode-skin interface itself behaves electrically like a resistor and capacitor in parallel, contributing both a DC offset and frequency-dependent impedance the amplifier design must tolerate. Poor electrode contact (dry gel, poor skin prep) raises this impedance and is the single most common cause of noisy real ECG/EMG traces.

#### MI-3 Instrumentation amplifiers and common-mode rejection
**Instrumentation amplifiers and common-mode rejection**: a biopotential amplifier is built around a differential (instrumentation) amplifier that amplifies the small difference between two electrodes while rejecting signals common to both -- critically, mains interference (50/60 Hz) picked up equally by both electrodes (a common-mode signal) is rejected, while the genuine biosignal (a differential signal between the two electrode sites) is amplified. Common-mode rejection ratio (CMRR), usually quoted in dB, CMRR(dB) = 20 log10(differential gain / common-mode gain), quantifies how well this works; a driven-right-leg circuit actively cancels common-mode interference further in real ECG instrumentation.

#### MI-4 Frequency content of ECG, EMG and EEG
**Frequency content of biosignals**: ECG's clinically relevant content is roughly 0.05-150 Hz (with the QRS complex itself needing up to ~100 Hz to preserve its shape for diagnosis); EMG (muscle electrical activity) spans roughly 10 Hz-500 Hz; EEG (brain electrical activity, even smaller amplitude, tens of microvolts) is dominated by frequencies below about 40-100 Hz, further divided into named clinical bands (delta <4 Hz, theta 4-8 Hz, alpha 8-13 Hz, beta 13-30 Hz). Each signal's known bandwidth directly sets the amplifier and filter design (below) needed to capture it faithfully without excess noise bandwidth.

#### MI-5 The Nyquist-Shannon sampling theorem applied to biosignals
**The Nyquist-Shannon sampling theorem**: to reconstruct a continuous signal from samples without aliasing, the sampling frequency f_s must exceed twice the highest frequency component present in the signal (f_s > 2 f_max, the Nyquist rate); an anti-aliasing low-pass filter is applied before sampling to remove content above f_s/2 that would otherwise fold back (alias) into the sampled signal's frequency range and be indistinguishable from genuine low-frequency content. Clinical ECG is typically sampled at 250-1000 Hz to comfortably exceed the Nyquist rate for its ~150 Hz bandwidth with practical margin.

#### MI-6 Basic filtering and signal-to-noise ratio
**Basic filtering for biosignals**: a low-pass filter attenuates frequencies above a cutoff (removing high-frequency noise/EMG contamination from an ECG trace); a high-pass filter attenuates frequencies below a cutoff (removing baseline wander from breathing or electrode motion, typically below ~0.5 Hz for ECG); a notch (band-stop) filter removes a narrow band around a specific frequency (removing 50/60 Hz mains interference specifically, while leaving nearby frequencies largely intact). Signal-to-noise ratio (SNR), commonly expressed in decibels, SNR(dB) = 10 log10(signal power / noise power) [equivalently 20 log10(signal amplitude / noise amplitude)], quantifies how much a given filtering/amplification design has improved (or left) the usable signal quality.

## Explicitly not here
Detailed analogue circuit design (specific op-amp topologies, component-level filter design) and digital-signal-processing implementation in code are out of scope; this stage teaches the physiological-signal and systems-level instrumentation theory (bandwidth, sampling, CMRR, SNR) that any medical-instrumentation circuit design must satisfy.

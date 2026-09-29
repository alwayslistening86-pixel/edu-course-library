# S11_Biophotonics_Signal_Processing_and_Biomedical_Component_Design - Lesson: Biophotonics, Signal Processing and Biomedical Component Design

## Goal
The learner applies the Beer-Lambert law to optical biosensing (pulse oximetry as the worked case), extends digital sampling/filtering concepts to broader biomedical signal processing, and surveys medical imaging modalities and radiation dose concepts at an overview level.

## Syllabus items taught here
- BP-1 - Light-tissue interaction: absorption and scattering
- BP-2 - The Beer-Lambert law
- BP-3 - Pulse oximetry as a worked biophotonics application
- BP-4 - Sampling and filtering extended to the photoplethysmogram
- BP-5 - Medical imaging modalities overview: X-ray/CT, ultrasound, MRI
- BP-6 - Radiation dose concepts and the ALARA principle

## How to teach this
Ask how a small clip-on finger sensor can report both heart rate and blood oxygen saturation using nothing but two LEDs and a light detector -- pulse oximetry is this stage's central worked example. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### BP-1 Light-tissue interaction: absorption and scattering
**Light-tissue interaction**: light passing through tissue is attenuated by absorption (energy converted to heat or re-emitted at a different wavelength, wavelength- and chromophore-dependent) and scattering (direction changed by tissue microstructure, generally more significant at shorter wavelengths). Different tissue chromophores (haemoglobin, melanin, water) have distinct absorption spectra as a function of wavelength, which is the basis for selecting specific wavelengths to target a specific chromophore optically -- the working principle behind pulse oximetry, near-infrared spectroscopy and many optical biosensors.

#### BP-2 The Beer-Lambert law
**The Beer-Lambert law**: for light of intensity I0 passing through an absorbing medium of thickness L and molar absorptivity (extinction coefficient) epsilon at concentration c, the transmitted intensity is I = I0 e^(-epsilon c L), or equivalently absorbance A = log10(I0/I) = epsilon c L (base-10 form, the more common engineering convention). Absorbance is additive for multiple absorbing species at the same wavelength (A_total = sum of each species' epsilon_i c_i L), the principle exploited by pulse oximetry to distinguish oxygenated from deoxygenated haemoglobin.

#### BP-3 Pulse oximetry as a worked biophotonics application
**Pulse oximetry (worked application)**: oxygenated haemoglobin (HbO2) and deoxygenated haemoglobin (Hb) have different molar absorptivities at red (~660 nm) and infrared (~940 nm) wavelengths -- Hb absorbs red light more strongly than HbO2, while both absorb infrared light more similarly. A pulse oximeter shines both wavelengths through a fingertip, measures the pulsatile (arterial-blood-only) component of transmitted light at each wavelength, and computes a ratio R = (AC_red/DC_red)/(AC_ir/DC_ir); R is empirically calibrated against known blood oxygen saturation SpO2 values, since the Beer-Lambert law's ideal predictions are modified in practice by scattering and finger geometry.

#### BP-4 Sampling and filtering extended to the photoplethysmogram
**Sampling and filtering, extended to broader biosignals**: the Nyquist/anti-aliasing principles of S10 apply equally to a pulse oximeter's photoplethysmogram (PPG) waveform (pulsatile blood-volume signal, low frequency, roughly 0.5-5 Hz for the cardiac component) and to any other digitised physiological waveform; a moving-average filter (a simple low-pass filter that replaces each sample with the average of itself and its neighbours) is a common, easily implemented way to smooth noisy biosignal data at the cost of some loss of high-frequency detail and a small time delay.

#### BP-5 Medical imaging modalities overview: X-ray/CT, ultrasound, MRI
**Medical imaging modalities, overview**: X-ray/CT imaging uses ionising radiation attenuated differently by tissues of different density (bone attenuates strongly, soft tissue weakly), reconstructed (for CT) from many angular projections into a cross-sectional image; ultrasound imaging uses high-frequency sound reflected at tissue interfaces of differing acoustic impedance, non-ionising and real-time but limited in penetration through bone/air; MRI uses strong magnetic fields and radiofrequency pulses to exploit hydrogen nuclei's magnetic resonance, non-ionising, with excellent soft-tissue contrast but slower acquisition and higher equipment cost. Modality choice in practice trades off radiation dose, contrast, resolution, speed and cost against the specific clinical question.

#### BP-6 Radiation dose concepts and the ALARA principle
**Radiation dose concepts, overview**: absorbed dose (energy absorbed per unit mass, unit gray, Gy = J/kg) is scaled by a radiation-weighting factor to give equivalent dose (unit sievert, Sv), and further by tissue-weighting factors summed across exposed organs to give effective dose (also Sv), the standard quantity used to compare and limit radiation exposure risk across different imaging procedures and body regions; a typical chest X-ray delivers an effective dose of the order of 0.02 mSv, a typical CT scan of the order of several mSv to tens of mSv depending on the body region and protocol -- several hundred times more than a single X-ray, a key clinical/engineering justification-and-optimisation consideration (the ALARA -- as low as reasonably achievable -- principle) whenever ionising-radiation imaging is specified.

## Explicitly not here
Full image-reconstruction mathematics (CT filtered back-projection, MRI k-space and pulse-sequence physics) and digital-signal-processing code implementation (FFT algorithms in software) are out of scope; this stage teaches the optical/imaging physics principles and dose concepts at the level a biomedical engineer needs to specify, select between, or interface with such systems.

# S12_Biomaterials_II_Drug_Delivery_and_Regenerative_Medicine - Lesson: Biomaterials II: Drug Delivery and Regenerative Medicine

## Goal
The learner analyses controlled drug-release kinetics from a biodegradable polymer delivery system, distinguishes diffusion-controlled from degradation-controlled release, and relates biomaterial choice to regenerative-medicine design goals.

## Syllabus items taught here
- BIO2-1 - Diffusion-controlled (Higuchi) drug release
- BIO2-2 - Degradation-controlled drug release from biodegradable polymers
- BIO2-3 - First-order drug-release approximation
- BIO2-4 - Biodegradable polymer selection for regenerative medicine
- BIO2-5 - Regenerative medicine design goals
- BIO2-6 - Comparing zero-order, first-order and square-root release profiles

## How to teach this
Ask: a drug-eluting polymer implant needs to release its drug at a steady, predictable rate for months -- what could possibly go wrong with a simple 'load the drug into the polymer and let it diffuse out' design? The answer motivates the release-kinetics models in this stage. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### BIO2-1 Diffusion-controlled (Higuchi) drug release
**Diffusion-controlled release**: for a drug dissolved/dispersed in a non-degrading (or slowly degrading) polymer matrix, release is governed by Fickian diffusion (S01, AP-7; S09, CB-2) through the polymer; the Higuchi model, a standard simplified result for this geometry, gives cumulative drug released Q(t) proportional to root(t) (square-root-of-time kinetics) for early-time release from a planar matrix, meaning the release rate (dQ/dt, proportional to 1/root(t)) is fastest immediately after implantation and steadily slows -- a "burst then taper" profile that is often clinically undesirable if a steady, zero-order rate is wanted instead.

#### BIO2-2 Degradation-controlled drug release from biodegradable polymers
**Degradation-controlled (erosion-controlled) release**: for a biodegradable polymer matrix (e.g. PLGA) where the drug is released mainly as the polymer itself breaks down, release can be engineered closer to zero-order (constant rate) by matching the drug-loading/geometry to the polymer's degradation profile, since new drug is exposed to the surrounding fluid at a rate set by degradation rather than by diffusion through an intact matrix. PLGA (poly(lactic-co-glycolic acid)) degrades by hydrolysis of its ester bonds; its degradation rate (and hence, indirectly, drug release rate) can be tuned by the lactic:glycolic acid ratio and polymer molecular weight -- a real, widely used design lever in controlled-release device engineering.

#### BIO2-3 First-order drug-release approximation
**First-order release approximation (worked)**: for many practical delivery systems, especially where diffusion through a reservoir-type device with a rate-limiting membrane dominates, cumulative release approximates first-order kinetics, mathematically the same exponential form met repeatedly already in this course (S02, MM-1; S06, BM2-6): the amount remaining in the device M(t) = M0 e^(-kt), so the fraction released is 1 - e^(-kt), and the release half-life is ln(2)/k -- letting a delivery-device designer reuse the same half-life/rate-constant calculation and reasoning as a pharmacokinetic clearance problem.

#### BIO2-4 Biodegradable polymer selection for regenerative medicine
**Biodegradable polymer selection for regenerative medicine**: alongside PLGA, other biodegradable polymers used in tissue engineering and drug delivery include polycaprolactone (PCL, slower-degrading, good mechanical properties, useful where a longer-lasting scaffold is needed) and natural polymers such as collagen, gelatin and chitosan (good biocompatibility and cell-interaction properties, but generally weaker mechanically and faster-degrading than the synthetic options). Selecting a biodegradable material is therefore, as in S07, a multi-criteria trade-off between mechanical performance, degradation timescale and biological interaction, not a single "best" material.

#### BIO2-5 Regenerative medicine design goals
**Regenerative medicine design goals**: a regenerative-medicine construct (a scaffold, possibly combined with cells and/or growth factors, i.e. a "tissue-engineered" product) aims to support and guide the body's own tissue-regeneration process rather than simply replace lost tissue with an inert substitute; success criteria include appropriate initial mechanical support (S07, BIO1-4), a degradation rate matched to new-tissue formation (this stage), and often controlled, localised delivery of growth factors or other bioactive molecules using the drug-release principles above -- so this stage's release-kinetics tools apply directly to regenerative-medicine scaffold design, not only to conventional pharmaceutical delivery devices.

#### BIO2-6 Comparing zero-order, first-order and square-root release profiles
**Zero-order versus first-order versus square-root release, compared**: a zero-order profile releases drug at a constant rate (dQ/dt = constant) -- generally the clinically preferred profile for maintaining a steady therapeutic drug concentration; a first-order profile (BIO2-3) releases proportionally to the amount remaining, so the rate falls over time; a square-root-of-time (Higuchi, diffusion-controlled, BIO2-1) profile releases fastest at the start and slows progressively. Recognising which kinetic model a measured release-rate-versus-time data set matches (e.g. by checking whether cumulative release is linear in t, in ln(remaining), or in root(t)) is the practical, testable engineering skill this stage builds towards.

## Explicitly not here
Detailed polymer synthesis chemistry, full Fickian partial-differential-equation solutions for arbitrary geometries, and in-vivo pharmacokinetic/pharmacodynamic modelling beyond the one-compartment case (S08) are out of scope; this stage teaches the standard simplified release-kinetics models used for engineering design and interpretation of release data.

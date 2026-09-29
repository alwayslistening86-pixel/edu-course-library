# S06_Biomechanics_II_Mechanics_of_Biological_Tissue - Lesson: Biomechanics II: Mechanics of Biological Tissue

## Goal
The learner applies stress-strain and viscoelastic concepts specifically to bone, tendon/ligament and cartilage, and analyses implant-bone load sharing including stress shielding and implant fatigue.

## Syllabus items taught here
- BM2-1 - Anisotropic and rate-dependent mechanical behaviour of bone
- BM2-2 - Tendon and ligament as viscoelastic materials
- BM2-3 - Cartilage as a biphasic (fluid + solid) material
- BM2-4 - Stress shielding at the implant-bone interface
- BM2-5 - Implant fatigue design
- BM2-6 - Quantified stress relaxation of soft tissue

## How to teach this
Ask why a hip implant made of a very strong, very stiff metal can still cause the surrounding bone to weaken and eventually fail over years -- the counter-intuitive answer (stress shielding) motivates this whole stage. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### BM2-1 Anisotropic and rate-dependent mechanical behaviour of bone
**Mechanical anisotropy and rate-dependence of bone**: cortical bone is anisotropic (stronger and stiffer along its long/longitudinal axis, the direction of habitual loading, than transverse to it) and its apparent stiffness increases with strain rate (bone tested at a fast loading rate, e.g. impact, appears stiffer and stronger than the same bone tested slowly). Typical longitudinal values: Young's modulus ~17-20 GPa, ultimate tensile strength ~130-150 MPa, ultimate compressive strength ~170-200 MPa (bone is notably stronger in compression than tension) -- values used directly in the S03 stress = E x strain relationship, now applied to a real anisotropic tissue rather than an idealised isotropic material.

#### BM2-2 Tendon and ligament as viscoelastic materials
**Tendon and ligament as viscoelastic materials**: tendon and ligament are dense, mostly type-I-collagen connective tissue exhibiting creep (increasing strain under sustained constant load) and stress relaxation (decreasing stress under sustained constant strain, as the tissue's viscous component allows internal rearrangement). Their stress-strain curve under moderate loading rate is non-linear: an initial low-stiffness "toe region" as crimped collagen fibres straighten, then a stiffer, roughly linear region as the straightened fibres bear load directly, before yield and failure -- unlike bone's simpler near-linear elastic region.

#### BM2-3 Cartilage as a biphasic (fluid + solid) material
**Cartilage as a biphasic material**: articular cartilage is modelled as biphasic -- a solid collagen-proteoglycan matrix phase plus an interstitial fluid phase. Under a sudden load, initial stiffness is dominated by fluid pressurisation (fluid cannot escape instantly, so it carries much of the load); under sustained load, fluid gradually exudes and load transfers to the solid matrix, which is far less stiff, so cartilage creeps substantially under prolonged static loading. This fluid-load-support mechanism is also central to cartilage's low-friction lubrication function at a synovial joint.

#### BM2-4 Stress shielding at the implant-bone interface
**Stress shielding**: when a stiff implant (e.g. Ti-6Al-4V, E ~ 110 GPa) shares load with much more compliant surrounding bone (E ~ 18 GPa) in parallel (e.g. a femoral hip stem inside the femoral canal), the stiffer implant carries a disproportionate share of the load (for two materials of the same strain, stress is proportional to stiffness, sigma = E x epsilon, so equal strain gives roughly (110/18) times more stress carried by the implant per unit area, weighted by their relative cross-sections). Bone that is chronically under-loaded relative to its physiological baseline remodels itself to lower density and strength (per Wolff's law, S01), a process called stress shielding that can loosen the implant over years -- one reason lower-modulus implant materials or porous/compliant implant designs are actively researched.

#### BM2-5 Implant fatigue design
**Implant fatigue design**: because implants are cyclically loaded of order 10^6 times per year (S03), implant design targets a specified fatigue life at physiological loads with a safety factor, using S-N data for the implant material and accounting for stress concentrations at geometric features (e.g. the modular neck-stem junction in some hip designs, a documented real-world fatigue failure site). Surface treatments (e.g. shot peening, inducing beneficial residual compressive stress) and avoiding sharp internal corners in the design are standard mitigations.

#### BM2-6 Quantified stress relaxation of soft tissue
**Soft-tissue creep and stress relaxation, quantified**: a simple linear viscoelastic (standard linear solid) description gives stress relaxation as sigma(t) = sigma_infinity + (sigma_0 - sigma_infinity) e^(-t/tau), where tau is a characteristic relaxation time constant, sigma_0 the instantaneous stress and sigma_infinity the long-term equilibrium stress -- mathematically the same exponential-decay form as the first-order pharmacokinetic model in S02 (MM-1), reinforcing that a single mathematical tool (first-order exponential decay/relaxation) recurs across very different biomedical engineering contexts.

## Explicitly not here
Poroelastic/biphasic constitutive equations in full mathematical detail, and finite-element implant stress analysis, are out of scope; this stage teaches the physical concepts and simple closed-form calculations that motivate and underlie that more advanced modelling.

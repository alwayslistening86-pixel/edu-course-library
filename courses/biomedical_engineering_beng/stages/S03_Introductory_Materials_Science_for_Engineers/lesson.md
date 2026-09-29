# S03_Introductory_Materials_Science_for_Engineers - Lesson: Introductory Materials Science for Engineers

## Goal
The learner relates atomic/molecular structure to bulk mechanical behaviour, reads and interprets a stress-strain curve, and classifies engineering materials by class and mechanical property, as the foundation for biomaterials.

## Syllabus items taught here
- MS-1 - Atomic bonding and its link to material class
- MS-2 - Stress, strain and Hooke's law
- MS-3 - The stress-strain curve: yield, UTS, ductile vs brittle behaviour
- MS-4 - Resilience and toughness from the stress-strain curve
- MS-5 - Fatigue and fracture under cyclic loading
- MS-6 - Comparing metal, ceramic, polymer and composite material classes
- MS-7 - Viscoelasticity introduced: creep and stress relaxation

## How to teach this
Show a stress-strain curve with no labels and ask what physical event on the specimen corresponds to each turning point on the graph -- then build the vocabulary to answer precisely. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### MS-1 Atomic bonding and its link to material class
**Bonding and structure**: metallic bonding (delocalised electrons, ductile, good electrical/thermal conductors -- e.g. titanium and cobalt-chrome implant alloys), ionic and covalent bonding (ceramics: stiff, hard, brittle, e.g. alumina and hydroxyapatite), and covalent chains with weaker secondary (van der Waals/hydrogen) bonds between them (polymers: flexible, lower stiffness, e.g. UHMWPE, PEEK, PLA). Composites combine two material classes (e.g. carbon-fibre-reinforced polymer, or bone itself: collagen + hydroxyapatite) to get properties neither constituent has alone.

#### MS-2 Stress, strain and Hooke's law
**Stress and strain**: engineering stress sigma = F/A0 (force over original cross-sectional area, units Pa = N/m^2); engineering strain epsilon = (L - L0)/L0 = delta-L/L0 (dimensionless, often given as %). In the elastic (linear) region, stress and strain are proportional: sigma = E x epsilon (Hooke's law), where E is the Young's modulus, the material's stiffness. Typical values: cortical bone E ~ 17-20 GPa, titanium alloy Ti-6Al-4V E ~ 110 GPa, UHMWPE E ~ 1 GPa, collagen E ~ 1-2 GPa -- the wide spread across tissue and implant materials drives the "stress shielding" problem revisited in S06.

#### MS-3 The stress-strain curve: yield, UTS, ductile vs brittle behaviour
**The stress-strain curve**: the linear elastic region (Hooke's law, fully recoverable deformation) ends at the yield point (yield strength, sigma_y), beyond which plastic (permanent) deformation occurs; the curve typically rises to the ultimate tensile strength (UTS, the maximum stress the material sustains) before necking and fracture at the fracture stress/strain. Ductile materials (most metals) show substantial plastic strain before fracture; brittle materials (ceramics, and ceramic-like ones such as bone in certain loading modes) fracture with little or no plastic deformation, at or near the yield point.

#### MS-4 Resilience and toughness from the stress-strain curve
**Elastic properties from the curve**: the area under the elastic (linear) part of the stress-strain curve up to yield is the resilience (energy absorbed elastically per unit volume, (1/2) sigma_y epsilon_y); the total area under the whole curve to fracture is the toughness (total energy absorbed before fracture). A material can be strong (high UTS) but not tough (fractures with little plastic deformation, e.g. many ceramics) or tough but not especially strong (large plastic region, e.g. many metals) -- both matter differently for, say, a brittle bone cement versus a ductile hip stem.

#### MS-5 Fatigue and fracture under cyclic loading
**Fatigue and fracture**: cyclic loading below the static yield strength can still cause failure after many cycles (fatigue), because microscopic cracks initiate (often at a stress concentration -- a hole, notch or surface defect) and grow a little on each cycle until the remaining cross-section fails suddenly. An S-N curve (stress amplitude S against number of cycles to failure N, log scale) characterises a material's fatigue life; some metals (notably steel) show a fatigue limit below which fatigue failure effectively never occurs, while most non-ferrous metals and polymers do not, and must instead be designed for a finite fatigue life. Orthopaedic implants are cyclically loaded roughly a million times a year by walking alone, making fatigue design (not static strength) usually the governing constraint.

#### MS-6 Comparing metal, ceramic, polymer and composite material classes
**Material classes for engineering, compared**: metals -- high stiffness and strength, ductile, generally good fatigue resistance, but corrosion and wear-debris concerns in the body; ceramics -- very high stiffness and hardness, excellent wear resistance and biocompatibility, but brittle (low fracture toughness, sensitive to flaws); polymers -- low stiffness, high compliance, easy to process into complex shapes, but generally lower strength and prone to creep; composites -- engineered to combine the strengths of two classes (e.g. glass/carbon fibres in a polymer matrix for stiffness-to-weight, or bone's own collagen-hydroxyapatite composite structure). Choice of material class is the first decision in any biomaterial selection problem (S07).

#### MS-7 Viscoelasticity introduced: creep and stress relaxation
**Viscoelasticity, introduced**: unlike a purely elastic (Hookean) solid, many biological and polymeric materials show time-dependent mechanical behaviour: creep (increasing strain under constant stress) and stress relaxation (decreasing stress under constant strain), because the material's response is part elastic (instantaneous) and part viscous (time-dependent, flow-like). This behaviour, revisited quantitatively for tendon, ligament and cartilage in S06, means a single Young's modulus is an incomplete description of soft tissue.

## Explicitly not here
Detailed crystallography, phase diagrams, processing/manufacturing routes and full fracture mechanics (stress-intensity factors) are out of scope; this stage builds the stress-strain vocabulary and material-class comparison that S06/S07 apply to bone, soft tissue and implants specifically.

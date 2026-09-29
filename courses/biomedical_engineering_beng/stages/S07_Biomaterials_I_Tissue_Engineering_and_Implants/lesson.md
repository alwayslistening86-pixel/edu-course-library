# S07_Biomaterials_I_Tissue_Engineering_and_Implants - Lesson: Biomaterials I: Tissue Engineering and Implants

## Goal
The learner classifies biomaterials by class and biological response, selects appropriate implant/scaffold materials against a design case, and describes surface modification and sterilisation as engineering considerations.

## Syllabus items taught here
- BIO1-1 - Bioinert, bioactive and bioresorbable material response
- BIO1-2 - Metallic implant materials
- BIO1-3 - Ceramic and polymeric implant materials
- BIO1-4 - Scaffold design for tissue engineering
- BIO1-5 - Implant surface modification
- BIO1-6 - Sterilisation methods and their material constraints

## How to teach this
Ask: if a material is 'biocompatible', does that mean the body ignores it completely? Use the answer (almost never -- there is always some host response) to introduce the spectrum from bioinert to bioactive to resorbable. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### BIO1-1 Bioinert, bioactive and bioresorbable material response
**Defining biomaterial response**: bioinert materials (e.g. alumina, titanium's native oxide layer) provoke minimal host response and are simply encapsulated by fibrous tissue; bioactive materials (e.g. bioactive glass, hydroxyapatite coatings) form a direct chemical bond with living bone; bioresorbable/biodegradable materials (e.g. PLA, PGA and their copolymer PLGA) are gradually broken down and replaced by the body's own tissue, so no permanent implant remains. The right category depends on the application: a permanent joint replacement wants bioinert or bioactive fixation; a temporary fracture-fixation plate or a tissue-engineering scaffold may deliberately want bioresorbable behaviour matched to the tissue's healing timescale.

#### BIO1-2 Metallic implant materials
**Metallic implant materials**: stainless steel (316L, cheap, used for temporary fixation), cobalt-chromium alloys (very high wear resistance, used for the bearing surfaces of joint replacements) and titanium alloys (Ti-6Al-4V; lower stiffness than steel/CoCr, excellent corrosion resistance and biocompatibility via a stable, self-healing oxide layer, and good osseointegration) are the three main classes. Titanium's relatively lower modulus (still far above bone's) is one motivation for porous/lattice titanium implant designs that reduce effective stiffness further, mitigating stress shielding (S06).

#### BIO1-3 Ceramic and polymeric implant materials
**Ceramic and polymeric implant materials**: alumina and zirconia ceramics give extremely low wear rates as femoral-head/acetabular bearing surfaces in hip replacements but are brittle and can fracture catastrophically under impact or malpositioning; hydroxyapatite (chemically similar to bone mineral) is used as a bioactive coating to promote bone ingrowth. Ultra-high-molecular-weight polyethylene (UHMWPE) is the standard bearing-surface polymer (e.g. the acetabular liner in a hip replacement), chosen for low friction and wear resistance against a metal or ceramic counterface, though wear debris particles can themselves provoke an inflammatory osteolytic response -- a key implant-longevity failure mode.

#### BIO1-4 Scaffold design for tissue engineering
**Scaffold design for tissue engineering**: a tissue-engineering scaffold provides a temporary 3D structure for cells to attach, proliferate and form new tissue, and should be biocompatible, have interconnected porosity (typically pore size in the range of roughly 100-500 micrometres for bone tissue engineering, to allow cell infiltration, nutrient/waste diffusion and eventual vascularisation) and degrade at a rate matched to the rate of new tissue formation, so mechanical support is not lost before the regenerating tissue can bear load itself. Common scaffold materials include biodegradable polymers (PLGA), bioceramics (hydroxyapatite, tricalcium phosphate) and natural polymers (collagen, chitosan).

#### BIO1-5 Implant surface modification
**Surface modification**: implant surfaces are engineered independently of the bulk material -- e.g. grit-blasting or plasma-spraying to increase surface roughness (promoting mechanical interlock and osseointegration for a cementless implant), hydroxyapatite coating (promoting a bioactive bond), or surface treatments to reduce ion release and improve corrosion resistance. This separates the bulk mechanical requirement (handled by material and geometry selection, S03/S06) from the surface biological-interaction requirement, letting each be optimised largely independently.

#### BIO1-6 Sterilisation methods and their material constraints
**Sterilisation methods and their material constraints**: autoclaving (pressurised steam, ~121-134 degC) is effective and cheap but can degrade heat-sensitive polymers; ethylene oxide (EtO) gas sterilises at low temperature (suitable for polymers and electronics) but requires a lengthy aeration period to remove toxic residue; gamma irradiation sterilises effectively and penetrates packaging, but can alter polymer properties (e.g. gamma-irradiated UHMWPE historically suffered oxidative embrittlement over shelf life, a real, documented implant-material lesson that drove the development of highly cross-linked, vitamin-E-stabilised UHMWPE formulations). The chosen sterilisation method is therefore a real materials-selection constraint, not an afterthought.

## Explicitly not here
Detailed cell-culture protocols, molecular-level scaffold chemistry synthesis routes and regulatory sterility-assurance-level (SAL) validation testing are out of scope; this stage teaches the engineering material-selection logic and stays theory/design-only, matching the library's convention for hands-on laboratory work.

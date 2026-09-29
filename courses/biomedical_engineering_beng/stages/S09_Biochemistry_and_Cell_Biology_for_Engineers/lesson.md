# S09_Biochemistry_and_Cell_Biology_for_Engineers - Lesson: Biochemistry and Cell Biology for Engineers

## Goal
The learner describes cell structure, membrane transport, protein/enzyme function and basic reaction kinetics at the level a bioengineer needs to design cell-contacting devices, drug-delivery systems and tissue-engineering scaffolds.

## Syllabus items taught here
- CB-1 - Cell structure relevant to engineering
- CB-2 - Membrane transport mechanisms
- CB-3 - Proteins and enzymes
- CB-4 - Michaelis-Menten enzyme kinetics
- CB-5 - DNA and the central dogma, briefly
- CB-6 - Extracellular matrix and mechanotransduction

## How to teach this
Ask: an implanted drug-delivery device releases its drug at a perfectly steady rate in a beaker of saline in the lab, but a much less predictable rate in the body -- what is different biochemically about the environment inside the body that the lab test missed? Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### CB-1 Cell structure relevant to engineering
**Cell structure relevant to engineering**: the plasma membrane (a phospholipid bilayer with embedded proteins) separates the cell's interior from its environment and controls what crosses it; key organelles include the nucleus (genetic material, DNA), mitochondria (ATP/energy production), and the endoplasmic reticulum/Golgi apparatus (protein and lipid synthesis and processing). For a bioengineer, the plasma membrane is the interface every implant surface, drug carrier or biosensor ultimately interacts with.

#### CB-2 Membrane transport mechanisms
**Membrane transport**: passive diffusion moves molecules down a concentration gradient with no energy cost (rate proportional to concentration difference and membrane permeability, per Fick's law, S01 AP-7); facilitated diffusion uses a specific membrane protein channel or carrier, still passive but selective and saturable; active transport (e.g. the Na+/K+ pump) moves molecules against their concentration gradient, consuming ATP. Drug delivery across a cell membrane or the blood-brain barrier depends on which of these mechanisms is available for a given molecule's size and charge, a key constraint on drug-delivery-device design.

#### CB-3 Proteins and enzymes
**Proteins and enzymes**: proteins are folded chains of amino acids whose 3D shape (determined by the amino acid sequence) gives them their function -- structural (collagen), transport (haemoglobin), or catalytic (enzymes). Enzymes lower the activation energy of a specific biochemical reaction without being consumed, are highly substrate-specific (a "lock and key" or induced-fit model), and their activity is sensitive to temperature and pH -- both practical constraints on any device or biomaterial designed to preserve enzyme or protein function (e.g. a biosensor using an immobilised enzyme, or a drug-delivery vehicle carrying a therapeutic protein).

#### CB-4 Michaelis-Menten enzyme kinetics
**Michaelis-Menten enzyme kinetics**: reaction rate v = Vmax [S] / (Km + [S]), where [S] is substrate concentration, Vmax the maximum rate at saturating substrate, and Km the substrate concentration at half-maximal rate (a measure of the enzyme's affinity for its substrate -- a lower Km means higher affinity). At low [S] (<< Km), v is approximately first-order in [S] (v ~ (Vmax/Km)[S]); at high [S] (>> Km), v approaches Vmax and becomes independent of [S] (zero-order, saturated) -- the same saturation behaviour seen in many biosensor and drug-delivery release kinetics.

#### CB-5 DNA and the central dogma, briefly
**DNA and the central dogma, briefly**: DNA (a double helix of nucleotide base pairs, A-T and C-G) encodes genes, which are transcribed into messenger RNA and translated into proteins (DNA -> RNA -> protein, the "central dogma"). A bioengineer meets this most directly in biosensor design (e.g. detecting a specific DNA/RNA sequence via complementary base-pair hybridisation) and in understanding why a cell's protein-expression programme -- not just its physical environment -- governs its response to a biomaterial or scaffold.

#### CB-6 Extracellular matrix and mechanotransduction
**Extracellular matrix and cell signalling, for tissue engineering**: cells embedded in tissue are surrounded by an extracellular matrix (ECM) -- structural proteins (collagen, elastin) and proteoglycans that provide mechanical support and also chemical/mechanical signals cells sense and respond to (mechanotransduction: cells alter behaviour in response to the stiffness and mechanical loading of their surroundings). This is why a tissue-engineering scaffold's mechanical properties (S07, BIO1-4) are not only a structural requirement but also a biochemical signalling cue that influences how seeded cells differentiate and behave.

## Explicitly not here
Detailed biochemical pathway maps, genetic engineering/recombinant DNA techniques and wet-lab cell culture protocols are out of scope; this stage teaches the cell/molecular vocabulary and kinetics a device- and materials-focused bioengineer needs, not molecular biology as a subject in its own right.

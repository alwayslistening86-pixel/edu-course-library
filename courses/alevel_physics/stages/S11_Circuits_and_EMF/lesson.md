# S11_Circuits_and_EMF - Lesson: Circuits, potential dividers, emf and internal resistance

## Goal
The learner applies the rules for series and parallel circuits, conservation of charge and energy, potential dividers (including with sensors), emf and internal resistance, and carries out required practical 6.

## Syllabus items taught here
- 3.5.1.4 - Circuits
- 3.5.1.5 - Potential divider
- 3.5.1.6 - Electromotive force and internal resistance
- RP6 - Required practical 6: emf and internal resistance of cells

## How to teach this
Ask why car headlights dim when the starter motor turns. Teach from the physics outwards: state the principle, derive or justify the equation, then do a worked example with units and sensible significant figures. Use AQA's data and formulae booklet values (e.g. g = 9.81 N kg^-1, e = 1.60 x 10^-19 C, h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m s^-1). Every numerical answer here was computed when the course was built.

#### 3.5.1.4 Circuits
Series: R_T = R1 + R2 + ...; same current; pds add. Parallel: 1/R_T = 1/R1 + 1/R2 + ...; same pd; currents add. Current is conserved at junctions (conservation of charge) and the sum of emfs round a loop equals the sum of pds (conservation of energy). *Example:* 6 Ω in series with (3 Ω parallel with 6 Ω): R_T = 6 + 2 = 8 Ω. Cells in series: emfs add; identical cells in parallel: the emf of one cell.

#### 3.5.1.5 Potential divider
A potential divider splits a supply voltage in the ratio of the resistances: V_out = V_in x R2/(R1 + R2). With a thermistor or LDR as one resistor, the output varies with temperature or light, for sensor circuits (e.g. an LDR in the bottom position gives a high output in the dark if the LDR's resistance rises in darkness). A potentiometer (variable resistor as a divider) gives a variable output from 0 to V_in.

#### 3.5.1.6 Electromotive force and internal resistance
The emf ε is the energy transferred per unit charge by the source; the terminal pd V is less when current flows because of the internal resistance r: ε = I(R + r) = V + Ir. Lost volts = Ir. *Example:* a 9.0 V battery with r = 1.5 Ω supplies a 12 Ω lamp: I = 9.0/13.5 = 0.667 A, V = 8.0 V.

#### RP6 Required practical 6: emf and internal resistance of cells
**Method:** connect the cell to a variable resistor with an ammeter in series and a voltmeter across the cell; include a protective resistor; vary R and record V and I (open the switch between readings so the cell doesn't warm up and change r). **Analysis:** V = -rI + ε: plot V against I: gradient = -r, y-intercept = ε.

## Explicitly not here
Capacitors in circuits are S16.

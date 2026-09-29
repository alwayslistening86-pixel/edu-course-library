# S10_Open_Economy_Macroeconomics - Lesson: Open economy macroeconomics

## Goal
The learner uses the balance of payments identity, explains purchasing power parity and interest rate parity, applies the Mundell-Fleming model under fixed and floating exchange rates, and states the impossible trinity.

## Syllabus items taught here
- D217-31 - The balance of payments identity
- D217-32 - Purchasing power parity and interest rate parity
- D217-33 - The Mundell-Fleming model
- D217-34 - The impossible trinity

## How to teach this
Ask why a country with a fixed exchange rate cannot simultaneously run an independent monetary policy and allow free capital movement. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-31 The balance of payments identity
The balance of payments records a country's transactions with the rest of the world: the current account (trade in goods/services, income, transfers) plus the capital and financial accounts (asset transactions, reserve changes) sum to (approximately) zero by accounting construction -- a current account deficit must be financed by a financial account surplus (net capital inflow) of matching size. A persistent current account deficit therefore implies the country is a net borrower from, or is selling assets to, the rest of the world.

#### D217-32 Purchasing power parity and interest rate parity
Purchasing power parity (PPP): in the long run, exchange rates adjust so that a basket of goods costs the same in any currency, e/f = P_domestic/P_foreign; if domestic inflation exceeds foreign inflation, PPP predicts the domestic currency depreciates by roughly the inflation differential. Interest rate parity: in the absence of arbitrage, the interest differential between two countries should equal the expected rate of currency depreciation/appreciation, so capital doesn't systematically flow one way for a risk-free profit. *Example:* UK interest rate 5%, US rate 2%: uncovered interest parity predicts the pound is expected to depreciate against the dollar by about 3% over the relevant period, offsetting the interest advantage.

#### D217-33 The Mundell-Fleming model
The Mundell-Fleming model extends IS-LM to an open economy with capital mobility. Under floating exchange rates: expansionary fiscal policy raises r, attracting capital inflow, appreciating the currency, which crowds out net exports -- so fiscal policy is weakened (or, with perfect capital mobility, fully offset); expansionary monetary policy lowers r, causing capital outflow and depreciation, which boosts net exports -- so monetary policy is strengthened. Under a fixed exchange rate (with the central bank committed to defending the peg): fiscal policy is strengthened (the central bank must expand the money supply to prevent the interest-rate-driven appreciation, reinforcing the expansion), while monetary policy loses its independent power (any attempt to change the money supply is undone by the need to defend the peg).

#### D217-34 The impossible trinity
The impossible trinity (trilemma): a country cannot simultaneously have a fixed exchange rate, free capital mobility and independent monetary policy -- it must give up (at most) two of the three. A fixed rate with free capital flows requires monetary policy to be devoted to defending the peg (as in D217-33); floating exchange rates allow independent monetary policy alongside free capital flows (the exchange rate absorbs the pressure instead); capital controls allow a fixed rate with independent monetary policy by preventing arbitrage flows.

## Explicitly not here
Statistical methods (probability and inference) begin in S11.

# FA_S11_Introduction_to_Consolidated_Financial_Statements - Lesson: Introduction to consolidated financial statements

## Goal
The learner explains why and when consolidated financial statements are prepared, calculates goodwill on acquisition and non-controlling interest for a simple subsidiary, and distinguishes a subsidiary from an associate.

## Syllabus items taught here
- FA.H1 - Subsidiaries
- FA.H2 - Associates

## How to teach this
Ask: 'A parent company owns 80% of a subsidiary. Does the group's statement of financial position show 80% of the subsidiary's assets, or all of them?' Use the answer to introduce consolidation. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.H1 Subsidiaries
**Subsidiaries**: where a parent has **control** over another entity (usually, but not only, through owning more than 50% of its voting shares), the group must prepare **consolidated financial statements** combining the parent and subsidiary as if they were a single economic entity - adding together 100% of the subsidiary's assets, liabilities, income and expenses (not just the parent's ownership percentage), and then showing any portion owned by other shareholders as **non-controlling interest (NCI)**, both in the statement of financial position (within equity) and in the statement of profit or loss (a share of profit). On acquisition, **goodwill** = consideration transferred + NCI (at acquisition) - fair value of the subsidiary's identifiable net assets acquired; positive goodwill is recognised as an intangible asset (tested for impairment, not amortised). *Worked example*: a parent acquires 80% of a subsidiary for £340,000 cash consideration. At acquisition, the subsidiary's identifiable net assets have a fair value of £360,000, and NCI is measured at its proportionate share of those net assets: NCI = 360,000 x 20% = £{360000 * 0.20:,.0f}. Goodwill = 340,000 + {360000 * 0.20:,.0f} - 360,000 = £{340000 + 360000 * 0.20 - 360000:,.0f}.

#### FA.H2 Associates
**Associates** (IAS 28): where an investor has **significant influence** (but not control) over another entity - commonly presumed from holding 20%-50% of its voting shares, evidenced by, e.g., board representation or participation in policy decisions - the investment is not consolidated line by line. Instead, the **equity method** is used: the investment is initially recognised at cost, then adjusted each period for the investor's share of the associate's profit or loss (added to the carrying amount, and to group profit) and any dividends received (deducted from the carrying amount, not double-counted as income). *Worked example*: an investor buys a 30% stake in an associate for £90,000. In the following year, the associate makes a profit of £50,000 and pays no dividend: the investor's share of profit = 50,000 x 30% = £{50000 * 0.30:,.0f}, added to group profit and to the investment's carrying amount, giving a year-end carrying amount of 90,000 + {50000 * 0.30:,.0f} = £{90000 + 50000 * 0.30:,.0f}.

## Explicitly not here
Interpreting group or single-entity financial statements through ratios is FA_S12.

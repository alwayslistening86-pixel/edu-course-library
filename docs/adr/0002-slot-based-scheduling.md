# ADR 0002 — Time is counted in session slots, never dates

Status: accepted (recorded retrospectively from `docs/history/DESIGN_NOTES.md`)

## Decision
Time is counted in session slots, never dates.

## Why
A learner can move faster or slower than any plan; dates imply false precision and need a calendar integration. Capacity is a rate (`sessions_per_week`) used only for rough projections; review `due_at_slot` and planning use slots.

## Consequences
Honest framing, no calendar state. Cost: five sessions in a day look like five weeks to the scheduler (accepted). Opt-in `exam_date` planning (L-12) is the only planned exception and stores no schedule.

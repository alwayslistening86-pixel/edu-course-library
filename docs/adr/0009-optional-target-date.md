# ADR 0009 — An optional, learner-stated target date (amends ADR 0002)

Status: accepted (owner delegated; recommended option taken)

## Context
ADR 0002 keeps all scheduling in session slots, never dates, so the system cannot imply false precision. But a learner with a real exam date reasonably wants to know whether the work fits before it, and "roughly N weeks" cannot answer that.

## Decision
A learner may give **one optional `target` date per course** (`plan_target.py`). It is the only calendar date stored anywhere. The planner compares estimated remaining slots (`plan_estimate.py`) with the slots the learner's own stated `sessions_per_week` would provide before that date and reports `on_track` / `tight` / `short` / `expired` with the options that would close a shortfall. Nothing is scheduled on a calendar and no date is promised; the tutor never asks for a date unprompted.

## Consequences
- ADR 0002's slot model is unchanged for scheduling, review and the plan; only the feasibility comparison reads a date.
- A past target is reported as expired and ignored, never silently acted on; the learner clears or resets it.
- Estimates are rough (default 3 slots per remaining stage + 10% review, overridable per course) and labelled as such.
- Consent class *progress*: a `limited` learner still keeps their target; `revoked` stores nothing.

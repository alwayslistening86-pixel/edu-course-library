"""
Evaluation harness for the generic-tutor plugin (Phase 3, A-01).

Offline by default: cases, scoring and reporting need no model. A model-in-the-loop run uses the
`claude` CLI as a backend (`python -m evals run --backend claude`), is manual/nightly only and never part
of PR CI. Reference answers never depend on a human marker: they come from construction (synthetic
learner responses derived from a known-correct solution) or from deterministic oracles (see README.md).
"""

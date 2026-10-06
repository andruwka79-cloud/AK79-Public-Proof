# What Failed

Public Proof v1 intentionally includes failures.

## Benchmark fixture defect

A generalized test fixture initially stored a mutable reference to observed state. Later recovery could make an earlier historical observation appear to contain future state.

Action:
- result was not accepted;
- fixture was corrected to snapshot observed state;
- both sides were rerun.

## Live AK-79 manifest-binding defect

The live ingress referenced a stale W04 manifest filename.

Action:
- current manifest was independently identified;
- binding was repaired;
- rollback copy preserved;
- live path was rerun.

## Model protocol noncompliance

A deterministic QA path unnecessarily passed through a local language model after mandatory tests had already passed.

The model returned JSON that did not satisfy the action protocol.

Action:
- failure preserved;
- no blind replay;
- deterministic QA path used deterministic FSM instead.

## Generation-1 AK-79 incremental-reuse failure

IR01 passed.

IR02 setup branch encountered ambiguous readback after the setup effect.

The frozen runner had not applied the same UNKNOWN -> reconcile discipline to its own setup write.

Action:
- no blind replay;
- remote branch was independently reconciled;
- cleanup was performed;
- Generation 1 remained frozen negative evidence.

## Generation-1 Temporal failure

Temporal failed before external benchmark effects because workflow sandbox validation rejected a module-level path-resolution behavior.

Action:
- failure preserved;
- Generation 1 was not edited in place;
- Generation 2 used a new frozen implementation.

## Generation-2 hypothesis kill

Both sides were remediated and frozen before external execution.

The AK-79 / Temporal AST burden ratio was 82.3055%.

The preregistered kill threshold was 80% on either primary burden metric.

Action:
- hypothesis killed;
- no unnecessary Generation-2 external effects were launched.

This is the intended behavior of the protocol.

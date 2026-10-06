# Methodology

AK-79 Public Proof uses a falsification-first approach.

## Core rules

1. Preregister before execution.
2. Freeze task class, expected world state, definitions of done, metrics, and kill criteria.
3. Preserve negative evidence.
4. Treat UNKNOWN as UNKNOWN until independent readback resolves it.
5. Never blind replay an external write solely because acknowledgement was lost.
6. Distinguish task identity from attempt identity.
7. Require terminal truth to be independently reconstructable.
8. Separate internal QA from external verification.
9. Do not change a frozen generation after seeing its result.
10. If a preregistered kill condition is already satisfied, stop rather than run unnecessary external effects.

## Why this matters

Tool-using agents can fail in a dangerous way: the external effect may have happened even when the client observes timeout or lost acknowledgement.

A retry can then duplicate the effect.

The benchmark therefore focuses on observable world state rather than trusting local success/error labels.

## Visible test families

Critical ambiguity:
- effect happened, acknowledgement lost;
- cross-provider continuation after UNKNOWN;
- acknowledgement lost plus provider switch.

Generalized semantics:
- unique create;
- append-once with marker;
- compare-and-set versioned update;
- partial two-step effect.

Incremental-reuse public test classes:
- local atomic file write;
- GitHub content create;
- GitHub ref create.

The final hidden holdout is not published in Public Proof v1.

## Independent internal QA

AK-79 uses a separate W04 QA lane to check frozen artifacts and deterministic validators.

W04 is still internal.

W04 PASS is evidence of internal discipline, not external certification.

# Interim Results

All results below are VERIFIED_INTERNAL unless stated otherwise.

## 1. Critical ambiguity preflight

Visible vectors: V05, V07, V13.

AK-79 reference: 3/3 PASS.
Temporal real SDK implementation: 3/3 PASS.
Unintended duplicate effects: 0 / 0.

Finding: explicit Temporal reconciliation can correctly handle these ambiguity cases. This weakened the original AK-79 differentiation claim.

## 2. Generalized reconciliation

Effect semantics: unique create, append-once, versioned compare-and-set, partial two-step effect.

AK-79 reference: 4/4 PASS.
Temporal reusable implementation: 4/4 PASS.
Unintended duplicate effects: 0 / 0.

Finding: reusable reconciliation across effect classes is not uniquely an AK-79 capability.

## 3. Live AK-79 path

The live AK-79 task identity -> execution fabric -> deterministic QA -> durable terminal receipt path reached FINISH with zero protocol errors after remediation of two internal defects.

This proves an internal live path.

It does not prove broad production readiness.

## 4. Real GitHub/CI visible preflight

Both live AK-79 and Temporal completed the tested GitHub/CI scenario with:

- one push attempt;
- zero duplicate push attempts;
- remote SHA matched;
- successful CI;
- no blind replay.

Finding: reliability parity on the tested visible task.

## 5. One-call packaging

AK-79 later reached one-command repeatability.

Single-class runner structural comparison:

AK-79:
- 1754 AST nodes
- 9449 bytes

Temporal:
- 975 AST nodes
- 5913 bytes

Finding: one-call parity achieved, packaging advantage not proven.

## 6. Incremental reuse

Frozen Generation-2 structural accounting:

AK-79:
- 1735 AST nodes
- 8821 bytes

Temporal:
- 2108 AST nodes
- 11626 bytes

AK-79 / Temporal AST ratio:
0.823055028462998

AK-79 / Temporal byte ratio:
0.7587304317908137

The preregistered kill rule stated that the hypothesis is killed if AK-79 reaches 80% or more of Temporal on either primary burden metric.

The AST ratio crossed that threshold.

Verdict:
KILLED UNDER FROZEN ACCOUNTING.

Generation-2 external effects were not run because they could not reverse the already-triggered code-burden kill condition.

## Current product status

Runtime superiority: NOT PROVEN.

Generic reconciliation moat: FALSIFIED / NARROWED.

Single-class packaging advantage: NOT PROVEN.

Large marginal integration-code advantage: KILLED.

External-effect integrity verification thesis: CANDIDATE / UNPROVEN.

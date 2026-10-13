# AK-79 Public Proof v1

AK-79 is an experimental AI execution and verification system built by a single founder.

This repository is not a claim that AK-79 is production-proven, externally certified, or superior to Temporal. It is a public proof package showing how AK-79 tests its own claims, preserves negative evidence, and stops experiments when preregistered kill conditions fire.

## What this release proves

Results below are reported by the author from internal runs. The machine-readable artifacts behind them are not part of this repository, so they cannot be reproduced from here. Only the V13 scenario has a runnable check in this repository (harness and tests).

- Critical ambiguity preflight: AK-79 reference 3/3, real Temporal SDK 3/3.
- Generalized reconciliation preflight: AK-79 reference 4/4, real Temporal SDK 4/4.
- Live AK-79 task identity -> execution fabric -> deterministic QA -> terminal receipt path: verified internally.
- Real GitHub/CI visible preflight: reliability parity between live AK-79 and Temporal on the tested task.
- One-call packaging parity: achieved.
- Single-class code-burden advantage for AK-79: not proven.
- Large marginal integration-code advantage: killed under the frozen preregistered accounting rule.

See docs/RESULTS.md and docs/WHAT_FAILED.md.

## What this release does not prove

- No external certification.
- No production claim.
- No claim that AK-79 beats Temporal.
- No final hidden holdout result.
- No proven commercial moat.
- No proven willingness to pay.
- No claim that total project cost was USD 20.

See docs/CLAIMS_BOUNDARY.md.

## Why publish negative results?

The purpose of Public Proof v1 is falsification, not marketing theater.

A benchmark that only publishes wins is weak evidence. This repository publishes where Temporal matched AK-79, where AK-79 failed, where the benchmark fixture itself was wrong, and where AK-79's own preregistered kill threshold terminated a favored hypothesis.

## Reproducible public harness

The small harness in harness/ is intentionally not the private AK-79 runtime. It is a public, standard-library demonstration of the external-effect ambiguity problem:

1. an effect commits;
2. acknowledgement is lost;
3. local state becomes UNKNOWN;
4. the system independently reads remote state;
5. no blind replay occurs;
6. terminal truth is reconstructed.

Run:

    python -m unittest discover -s tests -v

GitHub Actions runs the same test on every push.

## Repository map

- docs/METHODOLOGY.md — falsification rules.
- docs/RESULTS.md — public-safe interim results.
- docs/WHAT_FAILED.md — preserved negative evidence.
- docs/FOUNDER_STORY.md — founder-reported origin story with claim boundaries.
- docs/CLAIMS_BOUNDARY.md — what may and may not be claimed.
- benchmark/visible_vectors.json — public visible vector subset.
- results/public_results_v1.json — machine-readable public result snapshot.
- harness/ambiguity_harness.py — small public demonstration harness.
- tests/test_ambiguity_harness.py — deterministic tests.

## Founder story, carefully stated

Founder-reported chronology: AK-79 started from zero with ChatGPT Plus on a phone; a single personal laptop was added later; the concentrated build period was a little over one month.

This chronology is not independently audited in this release.

ChatGPT Plus is currently priced at USD 20/month by OpenAI. That is one subscription price, not the total economic cost of AK-79.

Temporal announced a USD 550M Series E at a USD 12.55B valuation in September 2026. That fact is used only as context for the scale of the incumbent, not as an apples-to-apples cost comparison.

Official sources:
- OpenAI Help Center: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
- Temporal announcement: https://temporal.io/news/temporal-raises-550m-at-a-12-55b-valuation

## Current thesis

The runtime-moat thesis was materially weakened.

The next candidate thesis is narrower: External-Effect Integrity Verification — independently reconstructing whether a tool-using agent duplicated, lost, partially applied, or falsely reported an external side effect under ambiguous failure.

That thesis is candidate / unproven.

## Version

AK-79 Public Proof v1
Date: 2026-10-06 (v1.0.1: verifier hardened, statuses restated, CI pinned)

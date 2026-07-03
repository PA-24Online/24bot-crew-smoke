# Review — issue #1: `add(2,3)` returns -1 instead of 5

**Verdict (advisory): LGTM.** The change correctly and minimally resolves the issue.
No security, data-safety, or migration hazards. Merge gate is the дирижёр's call.

## What changed (diff vs. `main`)

- `calculator.py:9` — `return a - b` → `return a + b`. One-line operator fix,
  exactly what the Teamlead's plan specified (`product_paths: ["calculator.py"]`).
- `tests/test_calculator.py` appears in the branch diff because it is new vs. `main`,
  but it was authored by the **oracle** step (commit `27c0375`), not the Implementer.
  `git log -- tests/test_calculator.py` shows no Implementer commit — the red oracle
  is **intact**.

## Correctness

- Solves the reported bug: `add(2, 3)` now returns `5`. Confirmed by running the suite.
- `python -m pytest tests/test_calculator.py -q` → **4 passed** (was red on base).
- Full `tests/` dir (incl. the tester's verify-leg file) → **6 passed**.
- The fix is the operator itself, so it satisfies the oracle's commutativity,
  identity, and negative-operand assertions rather than special-casing the repro.

## Scope & discipline

- Implementer stayed within `product_paths` (`calculator.py` only). ✅
- No test files were edited or deleted by the Implementer. ✅
- No out-of-scope, config, or dependency changes. ✅
- Untracked `tests/test_calculator_verify.py` belongs to the tester's verify leg
  (uncommitted); it is not an Implementer edit and is not a red flag.

## Strengths

- Change is idiomatic, matches surrounding style, and leaves the type hints intact.
- Behaviour is corrected at the root (the operator), not patched around the failing input.

## Nits / risks

- None material. Python ints are arbitrary-precision, so no overflow concern.
- No non-int input validation, but the signature is typed `int` and the issue does not
  ask for it — out of scope for this fix.

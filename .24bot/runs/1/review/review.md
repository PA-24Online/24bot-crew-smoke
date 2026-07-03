# Review — issue #1: `add(2,3)` returns -1 instead of 5

**Verdict: advisory — LGTM.** The change correctly and minimally resolves the reported bug.

## Diff (branch `24bot/issue-1` vs `main`)

- `calculator.py:9` — `return a - b` → `return a + b`. One-line fix, exactly the
  root cause named in the issue and the Teamlead's plan.
- `tests/test_add.py` — the Oracle's red repro, added intact.

## Correctness

- Solves the issue: `add(2, 3) == 5` (was `-1`). Verified `python -m pytest -q` → **5 passed**.
- Regression coverage is meaningful: the Tester's cases (commutativity, zero,
  negatives, large) would all fail under the subtraction bug, so they genuinely
  pin the fix rather than merely re-asserting the new code.

## Scope & integrity

- Stayed within `product_paths` (`calculator.py` only) — no out-of-scope edits.
- Tester's test file untouched; the implementer did not weaken or edit it.
- No security, data-safety, or migration surface (pure arithmetic function).

## Nits (non-blocking)

- Untracked `tests/test_add_verify.py` (verify-leg black-box assertions) sits in
  the worktree but is **not committed**, so it will not land on merge. If that
  coverage is meant to be durable, it needs to be committed; if it's a throwaway
  verify artifact, fine as-is. Flagging so the merge gate isn't surprised.

## Strengths

- Truly minimal diff; comment cruft (`# BUG:`) removed rather than left stale.
- Clear, well-documented regression test authored by the Oracle/Tester leg.

Merge decision remains policy/human — this verdict is advisory only.

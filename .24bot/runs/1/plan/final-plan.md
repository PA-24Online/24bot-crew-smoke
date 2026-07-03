# Final Plan — issue #1: `add(2, 3)` returns -1 instead of 5

## 1. Definition of done
Red test `tests/test_calculator.py::AddTests::test_add_returns_sum_for_positive_integers`
(asserts `add(2, 3) == 5`) passes, with no other tests broken.
Command: `python3 -m unittest tests.test_calculator`.

## 2. Root cause
`calculator.py` line 8: `add` returns `a - b` (planted bug) instead of `a + b`.

## 3. Steps (ordered)
1. In `calculator.py`, change the body of `add` from `return a - b` to `return a + b`.
   Drop/adjust the now-stale `# BUG:` comment.
2. Run `python3 -m unittest tests.test_calculator` — expect green.

## 4. Path ownership split
- product_paths: `calculator.py` — the only file the Implementer edits.
- test_paths: `tests/test_calculator.py` — read-only during implement.

## 5. Risk
Low. Single-line arithmetic fix, fully covered by the red test. No API or signature change.

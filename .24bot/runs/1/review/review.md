# Review - issue #1

Findings: none.

The branch fixes the reported bug by changing `calculator.add` from subtraction to addition. The implementer commit touches only `calculator.py`, matching the planned `product_paths`; the regression test in `tests/test_calculator.py` was added by the oracle commit and was not modified by the implementer.

Verification run:

```text
python3 -m unittest tests.test_calculator
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Residual risk is low. The fix preserves the function signature and directly covers the reported `add(2, 3) == 5` behavior.

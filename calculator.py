"""Fixture product code with a planted bug: ``add`` subtracts instead of adding.

The E2E bug flow drives the crew to reproduce this with a failing test, fix it,
and merge — landing the regression test on the default branch.
"""


def add(a: int, b: int) -> int:
    return a - b  # BUG: should be a + b

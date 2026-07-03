"""Regression test pinning the reported bug (issue #1).

``calculator.add`` must add its operands; the planted bug subtracts them, so
``add(2, 3)`` returns ``-1`` instead of ``5``. This test is red on the current
base and becomes the durable regression coverage once the bug is fixed.
"""

from calculator import add


def test_add_2_3_returns_5():
    # The exact case from the issue: add(2, 3) should be 5, not -1.
    assert add(2, 3) == 5


def test_add_is_commutative_and_correct():
    assert add(3, 2) == 5
    assert add(0, 0) == 0
    assert add(-4, 10) == 6
    assert add(100, 1) == 101

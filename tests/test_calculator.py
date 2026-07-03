"""Regression coverage for issue #1: ``calculator.add`` must add, not subtract.

Red oracle for the bug "add(2,3) returns -1 instead of 5". These are black-box
assertions against the public ``add`` API — they fail on the planted bug
(``a - b``) and pass once the behaviour is corrected to ``a + b``.
"""

from calculator import add


def test_add_two_and_three_returns_five():
    # The exact repro from the issue: add(2, 3) should be 5, not -1.
    assert add(2, 3) == 5


def test_add_is_commutative():
    # Subtraction is not commutative; addition is. Pins the operator.
    assert add(2, 3) == add(3, 2)


def test_add_with_zero_is_identity():
    assert add(0, 7) == 7
    assert add(7, 0) == 7


def test_add_negative_operands():
    assert add(-4, -6) == -10
    assert add(10, -3) == 7

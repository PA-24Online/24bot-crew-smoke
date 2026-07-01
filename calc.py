"""A tiny calculator (smoke fixture)."""


def add(a: int, b: int) -> int:
    # BUG: subtracts instead of adding — add(2, 3) returns -1, expected 5.
    return a - b


def mul(a: int, b: int) -> int:
    return a * b

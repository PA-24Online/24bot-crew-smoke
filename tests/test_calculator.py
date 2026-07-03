import unittest

from calculator import add


class AddTests(unittest.TestCase):
    def test_add_returns_sum_for_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

import unittest
from square import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0, "Incorrect multy with zero in area in square.")

    def test_square_mul(self):
        res = area(7)
        self.assertEqual(res, 49, "Incorrect multy square in area in square.")

    def test_inc_mul_1(self):
        try:
            res = area('7')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in square.")

    def test_inc_mul_2(self):
        try:
            res = area(-7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in square.")

    def test_zero_sum(self):
        res = perimeter(0)
        self.assertEqual(res, 0, "Incorrect sum with zero in perimeter in square.")

    def test_square_sum(self):
        res = perimeter(7)
        self.assertEqual(res, 28, "Incorrect sum with 4 same numbers in perimeter in square.")

    def test_inc_sum_1(self):
        try:
            res = area('7')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in square.")

    def test_inc_sum_2(self):
        try:
            res = area(-7)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in square.")

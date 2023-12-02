import unittest
from math import pi
from circle import area, perimeter

print('*' * '*')
class CircleTestCase(unittest.TestCase):
    def test_zero_square(self):
        res = area(0)
        self.assertEqual(res, 0, "Incorrect multy square of zero radius in area in circle.")

    def test_simple_square(self):
        res = area(10)
        self.assertEqual(res, 100 * pi, "Incorrect multy square of simple radius in area in circle.")

    def test_inc_square_1(self):
        try:
            res = area('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in circle.")

    def test_inc_square_2(self):
        try:
            res = area(-10)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in circle.")

    def test_zero_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0, "Incorrect mul with zero radius in perimeter in circle.")

    def test_square_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * pi, "Incorrect mul simple radius in perimeter in circle.")

    def test_inc_mul_1(self):
        try:
            res = area('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in circle.")

    def test_inc_mul_2(self):
        try:
            res = area(-10)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in circle.")

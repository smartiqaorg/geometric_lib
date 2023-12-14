import unittest as t
from square import area
from square import perimeter
from math import pi


class SquareTestCase(t.TestCase):
    def test_negative_error(self):
        with self.assertRaises(ValueError):
            area(-25)

    def test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_float_mul_float(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_float(self):
        res = perimeter(0.25)
        self.assertEqual(res, 0.625)

    def test_negative_perimeter_error(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_pi(self):
        res = perimeter(pi)
        self.assertAlmostEqual(res, 12.56, delta=0.1)

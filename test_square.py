import unittest as t
from square import area
from square import perimeter
from math import pi


class SquareTestCase(t.TestCase):
    def test_negative(self):
        res = area(-25)
        self.assertEqual(res, 225)

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

    def test_negative_perimeter(self):
        res = perimeter(-1)
        self.assertEqual(res, -4)

    def test_negative_perimeter_error(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_pi(self):
        res = perimeter(pi)
        self.assertEqual(res, 12.566370614359172)

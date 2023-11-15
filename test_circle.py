import unittest as t
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(t.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negativeR(self):
        res = area(-3)
        self.assertEqual(res, None)

    def test_floatPi(self):
        res = area(1/pi)
        self.assertEqual(res, pi * (1 / pi)**2)

    def test_negative(self):
        res = perimeter(-pi)
        self.assertEqual(res, None)

    def test_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float(self):
        res = perimeter(9.5)
        self.assertEqual(res, 2 * pi * 19)

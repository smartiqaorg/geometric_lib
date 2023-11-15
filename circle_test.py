import unittest
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_per(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)


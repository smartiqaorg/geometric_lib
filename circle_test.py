import unittest
import math
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_rectangle_mul_1(self):
        res = area(3)
        self.assertEqual(res, 9 * math.pi)

    def test_rectangle_mul_2(self):
        res = area(2)
        self.assertEqual(res, 4 * math.pi)

    def test_rectangle_per_1(self):
        res = perimeter(4)
        self.assertEqual(res, 8 * math.pi)

    def test_rectangle_per_2(self):
        res = perimeter(8)
        self.assertEqual(res, 16 * math.pi)

    def test_rectangle_per_3(self):
        res = perimeter(12)
        self.assertEqual(res, 24 * math.pi)

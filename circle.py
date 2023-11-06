import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337)
        self.assertEqual(res, 5615813.638184853)

    def test_zero_perimeter_case(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = perimeter(1337)
        self.assertEqual(res, 8400.618755699106)


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


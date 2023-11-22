import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):

    def test_area1(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_perimeter1(self):
        res = perimeter(5)
        self.assertEqual(res, math.pi * 2 * 5)

    def test_area2(self):
        res = area(18)
        self.assertEqual(res, math.pi * 18 * 18)

    def test_perimeter2(self):
        res = perimeter(15)
        self.assertEqual(res, math.pi * 2 * 15)

    def test_area3(self):
        res = area(28)
        self.assertEqual(res, math.pi * 28 * 28)

    def test_perimeter3(self):
        res = perimeter(71)
        self.assertEqual(res, math.pi * 2 * 71)

if __name__ == "__main__":
    unittest.ma

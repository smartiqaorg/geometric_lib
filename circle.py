import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):

    def test_area1(self):
        res = area(10)
        self.assertEqual(res, 314.15)

    def test_perimeter1(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41)

    def test_area2(self):
        res = area(18)
        self.assertEqual(res, 1017.87)

    def test_perimeter2(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24)

    def test_area3(self):
        res = area(28)
        self.assertEqual(res, 2463)

    def test_perimeter3(self):
        res = perimeter(-71)
        self.assertEqual(res, "error")

if __name__ == "__main__":
    unittest.ma

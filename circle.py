import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):

    def test_area1(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_perimeter1(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_area2(self):
        res = area(18)
        self.assertEqual(res, 1017.8760197630929)

    def test_perimeter2(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24777960769379)

    def test_area3(self):
        res = area(28)
        self.assertEqual(res, 2463.0086404143976)

    def test_perimeter3(self):
        res = perimeter(-71)
        self.assertEqual(res, "error")

if __name__ == "__main__":
    unittest.ma

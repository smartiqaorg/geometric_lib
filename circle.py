import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_square_mul1(self):
        res1 = area(0)
        self.assertAlmostEqual(res1, 0, delta=0.01)

    def test_square_mul2(self):
        res2 = area(1)
        self.assertAlmostEqual(res2, 3.14, delta=0.01)

    def test_square_mul3(self):
        with self.assertRaises(Exception):
            area(-7)

    def test_square_mul4(self):
        res4 = area(10)
        self.assertAlmostEqual(res4, 314.15, delta=0.01)

    def test_square_mul5(self):
        res5 = area(20)
        self.assertAlmostEqual(res5, 1256.63, delta=0.01)

    def test_perimeter_mul1(self):
        res1 = perimeter(0)
        self.assertAlmostEqual(res1, 0, delta=0.01)

    def test_perimeter_mul2(self):
        res2 = perimeter(1)
        self.assertAlmostEqual(res2, 6.28, delta=0.01)

    def test_perimeter_mul3(self):
        res3 = perimeter(5)
        self.assertAlmostEqual(res3, 31.42, delta=0.01)

    def test_perimeter_mul4(self):
        with self.assertRaises(Exception):
            perimeter(-7)

    def test_perimeter_mul5(self):
        res5 = perimeter(25.25)
        self.assertAlmostEqual(res5, 158.65, delta=0.01)
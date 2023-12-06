import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_square_mul(self):
        res1 = area(0)
        self.assertEqual(res1, 0)

        res2 = area(1)
        self.assertEqual(res2, 3.141592653589793)

        res3 = area(-5)
        self.assertEqual(res3, "error")

        res4 = area(100.248)
        self.assertEqual(res4, 31571.942752030554)

        res5 = area(25)
        self.assertEqual(res5, 1963.4954084936207)

    def test_perimeter_mul(self):
        res1 = perimeter(0)
        self.assertEqual(res1, 0)

        res2 = perimeter(1)
        self.assertEqual(res2, 6.283185307179586)

        res3 = perimeter(5)
        self.assertEqual(res3, 31.41592653589793)

        res4 = perimeter(-100)
        self.assertEqual(res4, "error")

        res5 = perimeter(25.25)
        self.assertEqual(res5, 158.65042900628455)
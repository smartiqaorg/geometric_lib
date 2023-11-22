from square import *
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_a(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_mul_a(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_p(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_mul_p(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

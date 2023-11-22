from triangle import *
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_mul_a(self):
        res = area(0,10)
        self.assertEqual(res, 0)

    def test_mul_five_a(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_zero_mul_zero_p(self):
        res = perimeter(0,10,0)
        self.assertEqual(res, 10)

    def test_mul_mul_five_p(self):
        res = perimeter(10, 10,5)
        self.assertEqual(res, 25)

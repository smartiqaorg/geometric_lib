from rectangle import *
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_zero_a(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_mul_five_a(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_zero_zero_p(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_mul_mul_p(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

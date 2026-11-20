from circle import *
import unittest
import math


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_zero_add(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_add(self):
        res = perimeter(1)
        self.assertEqual(res, math.pi * 2)
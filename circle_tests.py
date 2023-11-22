import unittest
from circle import *


class circleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(6)
        self.assertEqual(res, 113.09733552923255)
        
    def test_minus_area(self):
        res = area(-4)
        self.assertEquale(res, "r > 0")

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)
        
    def test_minus_perimeter(self):
        res = perimeter(-5)
        self.assertEqual(res, "r > 0")

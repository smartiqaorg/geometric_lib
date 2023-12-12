import unittest
from circle import *


class circleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(6)
        self.assertAlmostEqual(res, 113.1, delta=0.1)
        
    def test_minus_area(self):
        with self.assertRaises(Exception):
            area(-6)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.4, delta=0.1)
        
    def test_minus_perimeter(self):
        with self.assertRaises(Exception):
            perimeter(-5)

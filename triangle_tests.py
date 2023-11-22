import unittest
from triangle import *


class triangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0,0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5, 3);
        self.assertEqual(res, 7.5)

    def test_float_area(self):
        res = area(5.1, 4.76)
        self.assertEqual(res, 12.137999999999998)
        
    def test_minus_area(self):
        res = area(-5, 1)
        self.assertEqual(res, "base > 0")
        
    def test_minus_area(self):
        res = area(5, -1)
        self.assertEqual(res, "height > 0")

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(5, 7, 10)
        self.assertEqual(res, 22)

    def test_float_perimeter(self):
        res = perimeter(5.45, 1.21, 8.35)
        self.assertEqual(res, 15.01)
    
    def test_minus_perimeter(self):
        res = perimeter(-9, 10, 4)
        self.asseptEqual(res, "side > 0")
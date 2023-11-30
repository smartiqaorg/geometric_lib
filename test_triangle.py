import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    
    def test_zero_area(self):
        
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        
        res = area(-10, -20)
        self.assertRaises(res, Exception)

    def test_float_area(self):
        
        res = area(228.228, 1337.1919)
        self.assertAlmostEqual(res, 782.70995, delta=0.1)

    def test_zero_perim(self):
        
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        
        res = area(-10, -20, -30)
        self.assertRaises(res, Exception)

    def test_float_perim(self):
        
        res = perimeter(228.228, 1919.1919, 777.1337)
        self.assertAlmostEqual(res, 2924.5536, delta=0.1)

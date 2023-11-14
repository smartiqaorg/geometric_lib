import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    
    def test_zero_area(self):
        
        res = area(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        
        res = area(228.1337)
        self.assertAlmostEqual(res, 52044.98507569, delta=0.1)

    def test_zero_perim(self):
        
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float_perim(self):
        
        res = perimeter(228.1337)
        self.assertAlmostEqual(res, 912.5348, delta=0.1)

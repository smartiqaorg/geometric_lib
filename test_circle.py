import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    
    def test_zero_area(self):
        
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        
        self.assertRaises(ExpectedException, area(-10))
        
    def test_float_area(self):
        
        res = area(1337.420)
        self.assertAlmostEqual(res, 5619342.45223919, delta=0.1)

    def test_zero_perim(self):
        
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        
        self.assertRaises(ExpectedException, perimeter(-10))

    def test_float_perim(self):
        
        res = perimeter(1337.420)
        self.assertAlmostEqual(res, 8403.257693528, delta=0.1)

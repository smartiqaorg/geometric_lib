import unittest
import math
from circle import area, perimeter

class CircleleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
    
    def test_zero1_mul(self):
       res = area(2)
       self.assertEqual(res, math.pi * 4)

    def test_nefative_number_area_mul(self):
       res = area(-4)
       self.assertEqual(res, 0)  

    def test_perimeter_zero_mul(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

    def test_perimeter_1_mul(self):
       res = perimeter(5)
       self.assertEqual(res, math.pi * 10)

    def test_negative_number_perimeter_1_mul(self):
       res = perimeter(-5)
       self.assertEqual(res, 0)
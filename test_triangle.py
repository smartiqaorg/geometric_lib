import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
       res = area(0, 45)
       self.assertEqual(res, 0)
    
    def test_area_1_mul(self):
       res = area(4, 11)
       self.assertEqual(res, 22)
       
    def test_negative_number_area_mul(self):
       res = area(-4, 13)
       self.assertEqual(res, 0)  

    def test_perimeter_zero_mul(self):
       res = perimeter(0, 13, 15)
       self.assertEqual(res, 0)

    def test_perimeter_1_mul(self):
       res = perimeter(5, 6, 7)
       self.assertEqual(res, 18)

    def test_nefative_number_perimeter_mul(self):
       res = perimeter(2, 6, 20)
       self.assertEqual(res, 0)
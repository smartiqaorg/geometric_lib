import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_nefative_number_area_mul(self):
       res = area(-4)
       self.assertEqual(res, 0)       
    
    def test_area_1_mul(self):
       res = area(4)
       self.assertEqual(res, 16)

    def test_perimeter_zero_mul(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

    def test_perimeter_1_mul(self):
       res = perimeter(5)
       self.assertEqual(res, 20)

    def test_negative_number_perimeter_1_mul(self):
       res = perimeter(-5)
       self.assertEqual(res, 0)
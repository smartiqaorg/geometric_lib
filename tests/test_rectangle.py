from rectangle import *
import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
   
    def test_zero_add(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_add(self):
        res = perimeter(6, 9)
        self.assertEqual(res, 30)

    
    

       

from triangle import *
import unittest


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
   
    def test_zero_add(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_add(self):
        res = perimeter(5, 4, 3)
        self.assertEqual(res, 12)
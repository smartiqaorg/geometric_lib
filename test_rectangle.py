import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = area(420.024, 1337.22869)
        self.assertAlmostEqual(res, 561668.143, delta=0.1)

    def test_negative_area(self):
        
        res = area(-10, -10)
        self.assertRaises(res, ExpectedException)

    def test_zero_perim(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_same_numbers_perim(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_perimeter(self):
        
        res = perimeter(-10, -10)
        self.assertRaises(res, ExpectedException)

    def test_float_perim(self):
        res = perimeter(420.024, 1337.22869)
        self.assertAlmostEqual(res, 3514.50538, delta=0.1)

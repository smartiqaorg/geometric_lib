import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5.0, 2.5), 12.5, 'wrong answer')
        self.assertEqual(area(10, 10), 100, 'wrong answer')

        res = area(1000000000000000000000000000, 1000000000000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000000000000000000000, 'wrong answer')

    def test_area_strings(self):
        self.assertRaises(Exception, area, 2, 'a')
        self.assertRaises(Exception, area, 'a', 2)
        self.assertRaises(Exception, area, 'a', 'b')

    def test_area_negative(self):
        self.assertRaises(Exception, area, 2, -1)
        self.assertRaises(Exception, area, -1, 2)
        self.assertRaises(Exception, area, -2, -3)

    def test_area_zero_mul(self):
        self.assertRaises(Exception, area, 10, 0)
        self.assertRaises(Exception, area, 0, 0)

    def test_area_objects(self):
        self.assertRaises(Exception, area, enumerate, 2)
        self.assertRaises(Exception, area, range, 2)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5.0, 2.5), 15, 'wrong answer')
        self.assertEqual(perimeter(10, 10), 40, 'wrong answer')

        res = perimeter(1000000000000000000000000000, 1000000000000000000000000000)
        self.assertEqual(res, 4000000000000000000000000000, 'wrong answer')

    def test_perimeter_strings(self):
        self.assertRaises(Exception, perimeter, 2, 'a')
        self.assertRaises(Exception, perimeter, 'a', 2)
        self.assertRaises(Exception, perimeter, 'a', 'b')

    def test_perimeter_negative(self):
        self.assertRaises(Exception, perimeter, 2, -1)
        self.assertRaises(Exception, perimeter, -1, 2)
        self.assertRaises(Exception, perimeter, -2, -3)

    def test_perimeter_zero_mul(self):
        self.assertRaises(Exception, perimeter, 10, 0)
        self.assertRaises(Exception, perimeter, 0, 0)

    def test_perimeter_objects(self):
        self.assertRaises(Exception, perimeter, enumerate, 2)
        self.assertRaises(Exception, perimeter, range, 2)


    

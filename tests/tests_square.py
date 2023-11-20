import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5.0), 25.0, 'wrong answer')
        self.assertEqual(area(10), 100, 'wrong answer')

        res = area(1000000000000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000000000000000000000, 'wrong answer')

    def test_area_strings(self):
        self.assertRaises(Exception, area, 'a')
        self.assertRaises(Exception, area, '12345')

    def test_area_not_positive(self):
        self.assertRaises(Exception, area, -10)
        self.assertRaises(Exception, area, -5)
        self.assertRaises(Exception, area, 0)

    def test_area_objects(self):
        self.assertRaises(Exception, area, enumerate)
        self.assertRaises(Exception, area, range)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5.0), 20.0, 'wrong answer')
        self.assertEqual(perimeter(10), 40, 'wrong answer')

        res = perimeter(1000000000000000000000000000)
        self.assertEqual(res, 4000000000000000000000000000, 'wrong answer')

    def test_perimeter_strings(self):
        self.assertRaises(Exception, perimeter, 'a')
        self.assertRaises(Exception, perimeter, '12345')

    def test_perimeter_not_positive(self):
        self.assertRaises(Exception, perimeter, -1) 
        self.assertRaises(Exception, perimeter, -5)
        self.assertRaises(Exception, perimeter, 0)

    def test_perimeter_objects(self):
        self.assertRaises(Exception, perimeter, enumerate)
        self.assertRaises(Exception, perimeter, range)


    

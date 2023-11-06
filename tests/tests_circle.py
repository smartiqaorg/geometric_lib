import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(area(5.0), 78.5398, places=3, msg='wrong answer')
        self.assertAlmostEqual(area(10), 314.1592, places=3, msg='wrong answer')
        self.assertAlmostEqual(area(0), 0, places=3, msg='wrong answer')

    def test_area_strings(self):
        self.assertRaises(Exception, area, 'a')
        self.assertRaises(Exception, area, '12345')

    def test_area_negative(self):
        self.assertRaises(Exception, area, -10)
        self.assertRaises(Exception, area, -5)

    def test_area_objects(self):
        self.assertRaises(Exception, area, enumerate)
        self.assertRaises(Exception, area, range)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(5.0), 31.4159, places=3, msg='wrong answer')
        self.assertAlmostEqual(perimeter(10), 62.8318, places=3, msg='wrong answer')
        self.assertAlmostEqual(perimeter(0), 0, places=3, msg='wrong answer')

    def test_perimeter_strings(self):
        self.assertRaises(Exception, perimeter, 'a')
        self.assertRaises(Exception, perimeter, '12345')

    def test_perimeter_negative(self):
        self.assertRaises(Exception, perimeter, -1) 
        self.assertRaises(Exception, perimeter, -5)

    def test_perimeter_objects(self):
        self.assertRaises(Exception, perimeter, enumerate)
        self.assertRaises(Exception, perimeter, range)


    

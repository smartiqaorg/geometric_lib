import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(area(5.0), 78.5398, places=3, msg='wrong answer')
        self.assertAlmostEqual(area(10), 314.1592, places=3, msg='wrong answer')
        self.assertAlmostEqual(area(0), 0, places=3, msg='wrong answer')

    def test_area_strings(self):
        self.assertEqual(Exception, area, 'a')
        self.assertEqual(Exception, area, '12345')

    def test_area_negative(self):
        self.assertEqual(Exception, area, -10)
        self.assertEqual(Exception, area, -5)

    def test_area_objects(self):
        self.assertRaises(Exception, area, enumerate)
        self.assertRaises(Exception, area, range)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5.0), 31.4159, 'wrong answer')
        self.assertEqual(perimeter(10), 62.8318, 'wrong answer')
        self.assertEqual(perimeter(0), 0, 'wrong answer')

    def test_perimeter_strings(self):
        self.assertRaises(Exception, perimeter, 'a')
        self.assertRaises(Exception, perimeter, '12345')

    def test_perimeter_negative(self):
        self.assertRaises(Exception, perimeter, -1) 
        self.assertRaises(Exception, perimeter, -5)

    def test_perimeter_objects(self):
        self.assertRaises(Exception, perimeter, enumerate)
        self.assertRaises(Exception, perimeter, range)


    

import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5.0, 2.5), 6.25, 'wrong answer')
        self.assertEqual(area(10, 10), 50.0, 'wrong answer')

        res = area(1000000000000000000000000000, 1000000000000000000000000000)
        self.assertEqual(res, 500000000000000000000000000000000000000000000000000000.0, 'wrong answer')

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
        self.assertEqual(perimeter(3.0, 4.0, 5.0), 12.0, 'wrong answer')
        self.assertEqual(perimeter(10, 10, 10), 30, 'wrong answer')

        res = perimeter(1000000000000000000000000000, 1000000000000000000000000000, 1000000000000000000000000000)
        self.assertEqual(res, 3000000000000000000000000000, 'wrong answer')

    def test_perimeter_incorrect(self):
        self.assertNotEqual(perimeter(1.0, 1.0, 20.0), 22.0, msg="such triangle isn't exists")
        self.assertNotEqual(perimeter(0, 1.0, 1.0), 2.0,  msg="such triangle isn't exists")
        self.assertNotEqual(perimeter(1.0, 5.0, 100.0), 106.0, msg="such triangle isn't exists")


    def test_perimeter_strings(self):
        self.assertRaises(Exception, perimeter, 2, 'a', 'b')
        self.assertRaises(Exception, perimeter, 'a', 2, 'b')
        self.assertRaises(Exception, perimeter, 'a', 'b', 'c')

    def test_perimeter_negative(self):
        self.assertRaises(Exception, perimeter, 2, -1, -3)
        self.assertRaises(Exception, perimeter, -1, 2, 1)
        self.assertRaises(Exception, perimeter, -2, -3, -10)

    def test_perimeter_zero_mul(self):
        self.assertRaises(Exception, perimeter, 10, 0, 2)
        self.assertRaises(Exception, perimeter, 0, 0, 0)

    def test_perimeter_objects(self):
        self.assertRaises(Exception, perimeter, enumerate, map, range)
        self.assertRaises(Exception, perimeter, range, 2, 1)


    

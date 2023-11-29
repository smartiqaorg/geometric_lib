import unittest
from circle import *
import math
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), math.pi * 3 * 3)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), math.pi)
    def test_values(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -1)

    def test_types(self):
        self.assertRaises(TypeError, area, 'one')
        self.assertRaises(TypeError, area, [1, 2])

class PerimetrTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 2 * math.pi * 3)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 2 * math.pi)

    def test_values(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -1)

    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'one')
        self.assertRaises(TypeError, perimeter, [1, 2])

from rectangle import *
import unittest
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 3), 2 * 3)
        self.assertEqual(area(0, 0), 0)
    def test_values(self):
        self.assertRaises(ValueError, area, -2, 2)
        self.assertRaises(ValueError, area, -3, -3)
    def test_types(self):
        self.assertRaises(TypeError, area, 'one', 2)
        self.assertRaises(TypeError, area, 'abc', 'def')
        self.assertRaises(TypeError, area, [1, 2], [3, 4])

class PerimetrTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), (2 + 3) * 2)
        self.assertEqual(perimeter(0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, area, -2, 2)
        self.assertRaises(ValueError, area, -3, -3)

    def test_types(self):
        self.assertRaises(TypeError, area, 'one', 2)
        self.assertRaises(TypeError, area, 'abc', 'def')
        self.assertRaises(TypeError, area, [1, 2], [3, 4])
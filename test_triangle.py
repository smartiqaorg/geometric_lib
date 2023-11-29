from triangle import *
import unittest
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 2), (4 * 2) / 2)
        self.assertEqual(area(0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, area, -2, 2)
        self.assertRaises(ValueError, area, -3, -3)

    def test_types(self):
        self.assertRaises(TypeError, area, 'one', 2)
        self.assertRaises(TypeError, area, 'abc', 'def')
        self.assertRaises(TypeError, area, [1, 2], [3, 4])

class PerimetrTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(perimeter(1, 2, 3), 1 + 2 + 3)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, perimeter, -2, 2, -1)
        self.assertRaises(ValueError, perimeter, -3, -3, 2)

    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'one', 2, [1])
        self.assertRaises(TypeError, perimeter, 'abc', 'def', 23)
        self.assertRaises(TypeError, perimeter, [1, 2], [3, 4], 'abc')
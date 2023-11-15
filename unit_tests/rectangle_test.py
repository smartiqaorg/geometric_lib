import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_wrong_type_area(self):
        self.assertEqual(area("5", "4"),20)
        self.assertEqual(area("7", "3"),21)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5, 4)
        self.assertRaises(ValueError, area, "-5", "4")
    def test_area(self):
        self.assertEqual(area(5, 4),20)
        self.assertEqual(area(7, 3),21)
    def test_zero_area(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area("0", "5"), 0)

    def test_wrong_type_perimeter(self):
        self.assertEqual(perimeter("5", "4"),18)
        self.assertEqual(perimeter("7", "3"),20)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5, 4)
        self.assertRaises(ValueError, perimeter, "-5", "4")
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 4),18)
        self.assertEqual(perimeter(7, 3),20)
    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 5), 0)
        self.assertEqual(perimeter("0", "5"), 0)
    
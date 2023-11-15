import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_wrong_type_area(self):
        self.assertEqual(area("5", "4"),10)
        self.assertEqual(area("7", "3"),10.5)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5, 4)
        self.assertRaises(ValueError, area, "-5", "4")
    def test_area(self):
        self.assertEqual(area(5, 4),10)
        self.assertEqual(area(7, 3),10.5)
    def test_zero_area(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area("0", "5"), 0)

    def test_wrong_type_perimeter(self):
        self.assertEqual(perimeter("2", "3", "4"),9)
        self.assertEqual(perimeter("6", "3", "6"),15)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5, 4, 1)
        self.assertRaises(ValueError, perimeter, "-5", "4", "1")
    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4),9)
        self.assertEqual(perimeter(6, 3, 6),15)
    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 5, 2), 0)
        self.assertEqual(perimeter("0", "5", "2"), 0)

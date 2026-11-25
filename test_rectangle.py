import unittest
import rectangle


class RectangleTests(unittest.TestCase):
    def test_area(self):
        result = rectangle.area(3, 5)
        self.assertEqual(result, 15)

    def test_perimeter(self):
        result = rectangle.perimeter(3, 5)
        self.assertEqual(result, 16)

    def test_area_with_zero_side(self):
        result = rectangle.area(10, 0)
        self.assertEqual(result, 0)
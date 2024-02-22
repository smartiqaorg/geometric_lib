import unittest

from rectangle import area, perimeter


class RectangleTest(unittest.TestCase):
    def test_area_correct(self):
        self.assertAlmostEqual(area(8, 9), 72)
        self.assertAlmostEqual(area(3, 7), 21)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -2, 89)

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, -2, "str")

    def test_perimeter_correct(self):
        self.assertAlmostEqual(perimeter(9.4, 8), 34.8)
        self.assertAlmostEqual(perimeter(10, 12), 44)

    def test_perimeter_value_error(self):
        self.assertRaises(ValueError, perimeter, -6, 84)

    def test_area_type_error(self):
        self.assertRaises(TypeError, perimeter, -6, "str")


if __name__ == '__main__':
    unittest.main()
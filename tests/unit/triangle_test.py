import unittest

from triangle import area, perimeter


class TriangleTest(unittest.TestCase):
    def test_area_correct(self):
        self.assertAlmostEqual(area(8, 4), 16)
        self.assertAlmostEqual(area(3, 10), 15)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -2, 2)

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, 2, "str")

    def test_perimeter_correct(self):
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(perimeter(10, 12, 18), 40)

    def tests_perimeter_value_error(self):
        self.assertRaises(ValueError, perimeter, -8, 8, 9)

    def tests_perimeter_type_error(self):
        self.assertRaises(TypeError, perimeter, "str", 8, 8)


if __name__ == '__main__':
    unittest.main()
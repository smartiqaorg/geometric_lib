import unittest

from square import area, perimeter


class SquareTest(unittest.TestCase):
    def test_area_correct(self):
        self.assertAlmostEqual(area(5), 25)
        self.assertAlmostEqual(area(3), 9)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -6.2)

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, "str")

    def test_perimeter_correct(self):
        self.assertAlmostEqual(perimeter(3), 12)
        self.assertAlmostEqual(perimeter(10), 40)

    def test_area_value_error(self):
        self.assertRaises(ValueError, perimeter, -5.5)

    def test_area_type_error(self):
        self.assertRaises(TypeError, perimeter, "str")


if __name__ == '__main__':
    unittest.main()
import unittest
import math

import square
import rectangle

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(3), 9)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(3), 12)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(0.5), 2.0)

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(2, 4), 8)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(1.5, 2), 3.0)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 4), 12)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_square_case(self):
        self.assertEqual(rectangle.perimeter(5, 5), 20)

    def test_diag_pythagorean(self):
        self.assertAlmostEqual(rectangle.diag(3, 4), 5.0)

    def test_diag_zero_side(self):
        self.assertAlmostEqual(rectangle.diag(0, 7), 7.0)

    def test_diag_unit_square(self):
        self.assertAlmostEqual(rectangle.diag(1, 1), math.sqrt(2))

if __name__ == "__main__":
    unittest.main()

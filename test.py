import unittest
import math

import square
import rectangle
import circle
import triangle

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

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_single(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 6 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)

class TriangleTestCase(unittest.TestCase):
    def test_is_triangle_valid(self):
        self.assertTrue(triangle.is_triangle(3, 4, 5))

    def test_is_triangle_equilateral(self):
        self.assertTrue(triangle.is_triangle(2, 2, 2))

    def test_is_triangle_degenerate(self):
        self.assertFalse(triangle.is_triangle(1, 2, 3))

    def test_is_triangle_too_long_side(self):
        self.assertFalse(triangle.is_triangle(1, 1, 5))

    def test_is_triangle_zero_side(self):
        self.assertFalse(triangle.is_triangle(0, 4, 4))

    def test_area(self):
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6.0)

    def test_area_equilateral(self):
        self.assertAlmostEqual(triangle.area(2, 2, 2), math.sqrt(3))

    def test_area_degenerate(self):
        self.assertEqual(triangle.area(1, 2, 3), 0)

    def test_area_nonexistent_triangle(self):
        self.assertEqual(triangle.area(1, 1, 5), 0)

    def test_perimeter(self):
        self.assertEqual(triangle.perimiter(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimiter(0.5, 0.5, 0.5), 1.5)

if __name__ == "__main__":
    unittest.main()

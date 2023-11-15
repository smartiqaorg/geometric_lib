import unittest

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestGeometricLib(unittest.TestCase):
    # Test cases
    def setUp(self):
        self.circle_area_cases = [
            (0, 0),
            (1, 3.141592653589793),
            (2.5, 19.634954084936208),
            (0.001, 3.1415926535897933e-06),
        ]

        self.circle_perimeter_cases = [
            (0, 0),
            (1, 6.283185307179586),
            (2.5, 15.707963267948966),
            (0.001, 0.006283185307179587),
        ]

        self.square_area_cases = [
            (0, 0),
            (1, 1),
            (2.5, 6.25),
            (0.001, 1e-06),
        ]

        self.square_perimeter_cases = [
            (0, 0),
            (1, 4),
            (2.5, 10.0),
            (0.001, 0.004),
        ]

        self.rectangle_area_cases = [
            ((0, 0), 0),
            ((1, 2), 2),
            ((2.5, 5.0), 12.5),
            ((0.001, 1000), 1),
        ]

        self.rectangle_perimeter_cases = [
            ((0, 0), 0),
            ((1, 2), 6),
            ((2.5, 5.0), 15.0),
            ((0.001, 1000), 2000.002),
        ]

        self.triangle_area_cases = [
            ((0, 0), 0),
            ((1, 2), 1),
            ((2.5, 5), 6.25),
            ((0.001, 1000), 0.5),
        ]

        self.triangle_perimeter_cases = [
            ((0, 0, 0), 0),
            ((1, 2, 3), 6),
            ((2.5, 5.0, 7.5), 15.0),
            ((0.001, 1000, 10), 1010.001),
        ]

    # Circle tests
    def test_circle_area(self):
        for radius, expected_area in self.circle_area_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle_area(radius), expected_area)

    def test_circle_perimeter(self):
        for radius, expected_perimeter in self.circle_perimeter_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle_perimeter(radius), expected_perimeter)

    # Square tests
    def test_square_area(self):
        for side, expected in self.square_area_cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(square_area(side), expected)

    def test_square_perimeter(self):
        for side, expected_perimeter in self.square_perimeter_cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(square_perimeter(side), expected_perimeter)

    # Rectangle tests
    def test_rectangle_area(self):
        for (length, width), expected in self.rectangle_area_cases:
            with self.subTest(length=length, width=width):
                self.assertAlmostEqual(rectangle_area(length, width), expected)

    def test_rectangle_perimeter(self):
        for (length, width), expected_perimeter in self.rectangle_perimeter_cases:
            with self.subTest(length=length, width=width):
                self.assertAlmostEqual(rectangle_perimeter(length, width), expected_perimeter)

    # Triangle tests
    def test_triangle_area(self):
        for (base, height), expected in self.triangle_area_cases:
            with self.subTest(base=base, height=height):
                self.assertAlmostEqual(triangle_area(base, height), expected)

    def test_triangle_perimeter(self):
        for (side1, side2, side3), expected in self.triangle_perimeter_cases:
            with self.subTest(side1=side1, side2=side2, side3=side3):
                self.assertAlmostEqual(triangle_perimeter(side1, side2, side3), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
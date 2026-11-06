import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [
            (10, 5, 25.0), (3, 4, 6.0), (8, 5, 20.0), (1, 1, 0.5),
            (0, 5, 0.0), (5, 0, 0.0), (20, 10, 100.0), (15, 4, 30.0),
            (7, 2, 7.0), (100, 50, 2500.0), (1000, 10, 5000.0),
        ]
        for a, h, expected in cases:
            with self.subTest(a=a, h=h):
                self.assertEqual(triangle.area(a, h), expected)

    def test_perimeter_numbers(self):
        cases = [
            (6, 8, 10, 24), (9, 12, 15, 36), (10, 24, 26, 60),
            (16, 30, 34, 80), (18, 24, 30, 72), (15, 20, 25, 60),
            (10, 10, 12, 32), (10, 10, 16, 36), (5, 5, 6, 16),
            (13, 14, 15, 42), (13, 13, 10, 36), (3, 4, 5, 12), (7, 24, 25, 56),
        ]
        for a, b, c, expected in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.perimeter(a, b, c), expected)

    def test_area_decimal(self):
        cases = [
            (1.5, 2.0, 1.5, 1.5e-12), (0.6, 0.8, 0.24, 2.4e-13),
            (0.5, 1.2, 0.3, 3e-13), (2.5, 6.0, 7.5, 7.5e-12),
            (3.5, 12.0, 21.0, 2.1e-11), (6.0, 8.0, 24.0, 2.4e-11),
            (0.09, 0.12, 0.0054, 5.4e-15), (0.03, 0.04, 0.0006, 6e-16),
        ]
        for a, h, expected, delta in cases:
            with self.subTest(a=a, h=h):
                self.assertAlmostEqual(triangle.area(a, h), expected, delta=delta)

    def test_perimeter_decimal(self):
        cases = [
            (0.09, 0.12, 0.15, 0.36, 3.6e-14), (0.3, 0.4, 0.5, 1.2, 1.2e-12),
            (1.5, 2.0, 2.5, 6.0, 6e-12), (0.5, 1.2, 1.3, 3.0, 3e-12),
            (2.5, 6.0, 6.5, 15.0, 1.5e-11), (3.5, 12.0, 12.5, 28.0, 2.8e-11),
            (6.0, 8.0, 10.0, 24.0, 2.4e-11), (30, 40, 50, 120.0, 1.2e-10),
        ]
        for a, b, c, expected, delta in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertAlmostEqual(triangle.perimeter(a, b, c), expected, delta=delta)


if __name__ == "__main__":
    unittest.main()
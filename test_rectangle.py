import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [
            (2, 6, 12), (8, 3, 24), (0, 7, 0), (5, 5, 25), (1, 10, 10), 
            (10, 1, 10), (9, 9, 81), (6, 7, 42), (12, 12, 144), (25, 4, 100),
            (50, 20, 1000), (2, 500, 1000), (11, 11, 121), (13, 5, 65), 
            (17, 3, 51), (20, 30, 600), (101, 102, 10302), (2, 2, 4), 
            (5, 0, 0), (0, 0, 0),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.area(a, b), expected)

    def test_perimeter_numbers(self):
        cases = [
            (2, 6, 16), (8, 3, 22), (0, 7, 14), (5, 5, 20), (1, 10, 22), 
            (10, 1, 22), (9, 9, 36), (6, 7, 26), (12, 12, 48), (25, 4, 58),
            (50, 20, 140), (2, 500, 1004), (11, 11, 44), (13, 5, 36), 
            (17, 3, 40), (20, 30, 100), (101, 102, 406), (2, 2, 8), 
            (5, 0, 10), (0, 0, 0),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.perimeter(a, b), expected)

    def test_area_decimal(self):
        cases = [
            (0.3, 0.4, 0.12, 1e-14),
            (0.002, 500, 1.0, 1e-12),
            (500, 0.002, 1.0, 1e-12),
            (0.5, 0.5, 0.25, 2.5e-13),
            (1.5, 3.5, 5.25, 5.25e-12),
            (10.5, 10.5, 110.25, 1.1025e-10),
            (250.5, 4, 1002.0, 1.002e-09),
        ]
        for a, b, expected, delta in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(rectangle.area(a, b), expected, delta=delta)

    def test_perimeter_decimal(self):
        cases = [
            (0.3, 0.4, 1.4, 1.4e-12),
            (0.002, 500, 1000.004, 1.000004e-09),
            (500, 0.002, 1000.004, 1.000004e-09),
            (0.5, 0.5, 2.0, 2e-13),
            (1.5, 3.5, 10.0, 1e-11),
            (10.5, 10.5, 42.0, 4.2e-11),
            (250.5, 4, 509.0, 5.09e-10),
        ]
        for a, b, expected, delta in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(rectangle.perimeter(a, b), expected, delta=delta)


if __name__ == "__main__":
    unittest.main()
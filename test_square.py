import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [(3, 9), (0, 0), (2, 4), (6, 36), (8, 64), (9, 81), (11, 121), (12, 144), (20, 400), (25, 625), (50, 2500), (100, 10000), (1000, 1000000), (2000, 4000000)]
        for a, expected in cases:
            with self.subTest(a=a):
                self.assertEqual(square.area(a), expected)

    def test_perimeter_numbers(self):
        cases = [(3, 12), (0, 0), (2, 8), (6, 24), (8, 32), (9, 36), (11, 44), (12, 48), (20, 80), (25, 100), (50, 200), (100, 400), (1000, 4000), (2000, 8000)]
        for a, expected in cases:
            with self.subTest(a=a):
                self.assertEqual(square.perimeter(a), expected)

    def test_area_decimal(self):
        cases = [(0.3, 0.09, 9e-15), (0.05, 0.0025, 2.5e-15), (0.5, 0.25, 2.5e-14), (1.5, 2.25, 2.25e-12), (3.5, 12.25, 1.225e-11), (10.5, 110.25, 1.1025e-10), (500.5, 250500.25, 2.5050025e-07)]
        for a, expected, delta in cases:
            with self.subTest(a=a):
                self.assertAlmostEqual(square.area(a), expected, delta=delta)

    def test_perimeter_decimal(self):
        cases = [(0.3, 1.2, 1.2e-13), (0.05, 0.2, 2e-14), (0.5, 2.0, 2e-13), (1.5, 6.0, 6e-13), (3.5, 14.0, 1.4e-12), (10.5, 42.0, 4.2e-12), (500.5, 2002.0, 2.002e-09)]
        for a, expected, delta in cases:
            with self.subTest(a=a):
                self.assertAlmostEqual(square.perimeter(a), expected, delta=delta)


if __name__ == "__main__":
    unittest.main()
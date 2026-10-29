import unittest

import square

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

if __name__ == "__main__":
    unittest.main()

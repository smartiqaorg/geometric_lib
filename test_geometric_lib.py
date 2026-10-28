
import math
import unittest

import circle
import square


class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle.area(5), 25 * math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(5), 10 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)


class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)


if __name__ == "__main__":
    unittest.main()

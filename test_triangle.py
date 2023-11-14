import unittest
from triangle import area, perimeter
class TestTriangleFunctions(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(0, 2), 0)
        self.assertEqual(area(2, 0), 0)

    def test_area_rand(self):
        self.assertAlmostEqual(area(1, 2), 1)
        self.assertAlmostEqual(area(2, 1), 1)
        self.assertAlmostEqual(area(3, 4), 6)
        self.assertAlmostEqual(area(4, 3), 6)

    def test_area_values(self):
        with self.assertRaises(ValueError):
            area(-1, -1)
        with self.assertRaises(ValueError):
            area(-1, 5)
        with self.assertRaises(ValueError):
            area(5, -1)

    def test_perimeter_rand(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(3, 3, 3), 9)

    def test_is_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(10, 1, 2)

    def test_perimeter_values(self):
        with self.assertRaises(ValueError):
            perimeter(-1, -1, -1)
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 3)
        with self.assertRaises(ValueError):
            perimeter(2, 4, -1)
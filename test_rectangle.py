import unittest
from rectangle import area, perimeter
class TestRectangleFunctions(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_rand(self):
        self.assertAlmostEqual(area(2, 3), 6)
        self.assertAlmostEqual(area(1326, 25464), 33765264)

    def test_area_values(self):
        with self.assertRaises(ValueError):
            area(-1, -1)
        with self.assertRaises(ValueError):
            area(-1, 3)
        with self.assertRaises(ValueError):
            area(2, -1)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_rand(self):
        self.assertAlmostEqual(perimeter(2, 3), 10)
        self.assertAlmostEqual(perimeter(12, 4), 32)

    def test_perimeter_values(self):
        with self.assertRaises(ValueError):
            area(-1, -1)
        with self.assertRaises(ValueError):
            area(-1, 2)
        with self.assertRaises(ValueError):
            area(4, -1)

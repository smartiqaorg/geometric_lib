import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_norm(self):
        res = area(4, 5)
        self.assertEqual(res, 10.0)

    def test_triangle_area_neNorm(self):
        with self.assertRaises(ValueError):
            area(4, -6)

    def test_triangle_area_real(self):
        res = area(4.5, 5.5)
        self.assertAlmostEqual(res, 12.375)

    def test_triangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_norm(self):
        res = perimeter(4, 5, 6)
        self.assertEqual(res, 15)

    def test_triangle_perimeter_neNorm(self):
        with self.assertRaises(ValueError):
            perimeter(4, 5, -6)

    def test_triangle_perimeter_real(self):
        res = perimeter(4.5, 5.5, 6.5)
        self.assertAlmostEqual(res, 16.5)

    def test_triangle_perimeter_zero(self):
        res = perimeter(4, 0, 4.5)
        self.assertAlmostEqual(res, 8.5)


if __name__ == '__main__':
    unittest.main()

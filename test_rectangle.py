import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_norm(self):
        res = area(4, 5)
        self.assertEqual(res, 20)

    def test_rectangle_area_neNorm(self):
        with self.assertRaises(ValueError):
            area(4, -6)

    def test_rectangle_area_real(self):
        res = area(4.5, 5.5)
        self.assertAlmostEqual(res, 24.75)

    def test_rectangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_norm(self):
        res = perimeter(4, 5)
        self.assertEqual(res, 18)

    def test_rectangle_perimeter_neNorm(self):
        with self.assertRaises(ValueError):
            perimeter(4, -5)

    def test_rectangle_perimeter_real(self):
        res = perimeter(4.5, 5.5)
        self.assertAlmostEqual(res, 20.0)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(4, 0)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()

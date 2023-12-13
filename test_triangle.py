import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_dobri(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)

    def test_triangle_area_zloy(self):
        res = area(5, -7)
        self.assertEqual(res, 'The base and height cannot be negative')

    def test_triangle_area_real(self):
        res = area(5.5, 7.7)
        self.assertEqual(res, 21.175)

    def test_triangle_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_dobri(self):
        res = perimeter(5, 6, 7)
        self.assertEqual(res, 18)

    def test_triangle_perimeter_zloy(self):
        res = perimeter(5, -6, 7)
        self.assertEqual(res, 'The base and height cannot be negative')

    def test_triangle_perimeter_real(self):
        res = perimeter(5.5, 6.6, 7)
        self.assertEqual(res, 19.1)

    def test_triangle_perimeter_zero(self):
        res = perimeter(5, 0, 5.5)
        self.assertEqual(res, 10.5)


if __name__ == '__main__':
    unittest.main()

import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_dobri(self):
        res = area(4, 6)
        self.assertEqual(res, 24)

    def test_rectangle_area_zloy(self):
        res = area(4, -6)
        self.assertEqual(res, 'The sides of the rectangle cannot be negative')

    def test_rectangle_area_real(self):
        res = area(4.4, 6.6)
        self.assertEqual(res, 29.04)

    def test_rectangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_dobri(self):
        res = perimeter(4, 6)
        self.assertEqual(res, 20)

    def test_rectangle_perimeter_zloy(self):
        res = perimeter(4, -6)
        self.assertEqual(res, 'The sides of the rectangle cannot be negative')

    def test_rectangle_perimeter_real(self):
        res = perimeter(4.4, 6.6)
        self.assertEqual(res, 22.0)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(4, 0)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()

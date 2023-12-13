import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_dobri(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_circle_area_zloy(self):
        res = area(-5)
        self.assertEqual(res, 'The radius cannot be negative')

    def test_circle_area_real(self):
        res = area(6.5)
        self.assertEqual(res, 132.73228961416876)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_dobri(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_circle_perimeter_zloy(self):
        res = perimeter(-5)
        self.assertEqual(res, 'The radius cannot be negative')

    def test_circle_perimeter_real(self):
        res = perimeter(6.5)
        self.assertEqual(res, 40.840704496667314)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()

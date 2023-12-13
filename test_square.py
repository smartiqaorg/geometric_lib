import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_dobri(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_square_area_zloy(self):
        res = area(-3)
        self.assertEqual(res, 'The side of the square cannot be negative')

    def test_square_area_real(self):
        res = area(3.5)
        self.assertEqual(res, 12.25)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_dobri(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_perimeter_zloy(self):
        res = perimeter(-3)
        self.assertEqual(res,'The side of the square cannot be negative')

    def test_square_perimeter_real(self):
        res = perimeter(3.5)
        self.assertEqual(res, 14)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()

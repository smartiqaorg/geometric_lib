import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_norm(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_square_area_neNorm(self):
        res = area(-4)
        self.assertEqual(res, 'the side of the square cannot be negative')

    def test_square_area_real(self):
        res = area(4.5)
        self.assertEqual(res, 20.25)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_norm(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_square_perimeter_neNorm(self):
        res = perimeter(-4)
        self.assertEqual(res,'the side of the square cannot be negative')

    def test_square_perimeter_real(self):
        res = perimeter(4.5)
        self.assertEqual(res, 18.0)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()

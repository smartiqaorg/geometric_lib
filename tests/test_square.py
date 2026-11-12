import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_unit_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_typical_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_typical_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)


if __name__ == '__main__':
    unittest.main()
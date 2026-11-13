import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_typical_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
        
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_typical_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 10)


if __name__ == '__main__':
    unittest.main()
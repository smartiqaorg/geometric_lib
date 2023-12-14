import unittest

from triangle import area, perimeter


class TriangleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(8, 4), 16)
        self.assertAlmostEqual(area(3, 10), 15)
        self.assertAlmostEqual(area(-2, 2), 2)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(perimeter(10, 12, 18), 40)
        self.assertAlmostEqual(perimeter(-8, 8, 9), 25)


if __name__ == '__main__':
    unittest.main()
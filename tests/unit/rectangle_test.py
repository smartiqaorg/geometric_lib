import unittest

from rectangle import area, perimeter


class RectangleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(8, 9), 72)
        self.assertAlmostEqual(area(3, 7), 21)
        self.assertAlmostEqual(area(2, 89), 178)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(9.4, 8), 34.8)
        self.assertAlmostEqual(perimeter(10, 12), 44)
        self.assertAlmostEqual(perimeter(6, 84), 180)


if __name__ == '__main__':
    unittest.main()
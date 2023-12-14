import unittest

from square import area, perimeter


class SquareTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 25)
        self.assertAlmostEqual(area(3), 9)
        self.assertAlmostEqual(area(-6.2), 38.44)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 12)
        self.assertAlmostEqual(perimeter(10), 40)
        self.assertAlmostEqual(perimeter(-5.5), 22)


if __name__ == '__main__':
    unittest.main()
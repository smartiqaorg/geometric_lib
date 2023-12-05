import unittest

import square
from square import area, perimeter


class SquareTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3), 9)
        self.assertAlmostEqual(area(-99), 9801)
        self.assertAlmostEqual(area(16.77), 281.2329)
        self.assertAlmostEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 12)
        self.assertAlmostEqual(perimeter(-99), -396)
        self.assertAlmostEqual(perimeter(16.77), 67.08)
        self.assertAlmostEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()
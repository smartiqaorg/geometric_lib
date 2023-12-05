import unittest

import triangle
from triangle import area, perimeter


class TriangleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3, 6), 9)
        self.assertAlmostEqual(area(-7, 12), -42)
        self.assertAlmostEqual(area(3.5, 6.8), 11.9)
        self.assertAlmostEqual(area(12.1, 8), 48.4)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(perimeter(-12, 4, 8), 0)
        self.assertAlmostEqual(perimeter(0, 98, 0), 98)
        self.assertAlmostEqual(perimeter(9.766, 16, 9.01),34.775999999999996 )

if __name__ == '__main__':
    unittest.main()

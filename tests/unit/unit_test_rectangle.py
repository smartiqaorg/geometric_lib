import unittest
from rectangle import area, perimeter


class RectangleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5, -7), -35)
        self.assertAlmostEqual(area(8, 13.5), 108)
        self.assertAlmostEqual(area(1, 3), 3)
        self.assertAlmostEqual(area(0, 89), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5, -7), -4)
        self.assertAlmostEqual(perimeter(8, 13.5), 43)
        self.assertAlmostEqual(perimeter(1, 3), 8)
        self.assertAlmostEqual(perimeter(0, 89), 178)


if __name__ == '__main__':
    unittest.main()

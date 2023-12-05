import unittest

import circle
from circle import area, perimeter


class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(8), 201.06192982974676)
        self.assertAlmostEqual(area(9.31), 272.30099900181426)
        self.assertAlmostEqual(area(-15), 706.8583470577034)
        self.assertAlmostEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(8), 50.26548245743669)
        self.assertAlmostEqual(perimeter(9.31), 58.49645520984195)
        self.assertAlmostEqual(perimeter(-15),-94.24777960769379 )
        self.assertAlmostEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()

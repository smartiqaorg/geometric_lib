import math
import unittest
from circle import perimeter, area

class TestCircle(unittest.TestCase):

    def testcircleperimeter(self):
        radius = 10
        expectedperimeter = 2 * math.pi * radius
        self.assertAlmostEqual(perimeter(radius), expectedperimeter, places=2)

    def testcirclearea(self):
        radius = 5
        expectedarea = math.pi * radius ** 2
        self.assertAlmostEqual(area(radius), expectedarea, places=7)

if __name__ == 'main':
    unittest.main()
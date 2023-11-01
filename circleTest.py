import unittest
import math
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_first_area(self):
        Areares = area(10)
        self.assertEqual(Areares, 100*math.pi )

    def test_second_area(self):
        Areares = area(1)
        self.assertEqual(Areares, 1*math.pi)

    def test_third_area(self):
        Areares = area(100, )
        self.assertEqual(Areares, 10000*math.pi)

    def test_first_per(self):
        PerimeterRes = perimeter(10)
        self.assertEqual(PerimeterRes, 20*math.pi)

    def test_second_per(self):
        PerimeterRes = perimeter(3)
        self.assertEqual(PerimeterRes, 6*math.pi)

    def test_third_per(self):
        PerimeterRes = perimeter(101)
        self.assertEqual(PerimeterRes, 202*math.pi)


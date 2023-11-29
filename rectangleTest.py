import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_first_mul(self):
        Areares = area(10, 10)
        self.assertEqual(Areares, 100)

    def test_second_mul(self):
        Areares = area(1, 11)
        self.assertEqual(Areares, 11)

    def test_third_mul(self):
        Areares = area(100, 0)
        self.assertEqual(Areares, 0)

    def test_first_per(self):
        PerimeterRes = perimeter(10, 11)
        self.assertEqual(PerimeterRes, 42)

    def test_second_per(self):
        PerimeterRes = perimeter(1, 2)
        self.assertEqual(PerimeterRes, 6)

    def test_third_per(self):
        PerimeterRes = perimeter(100, 1)
        self.assertEqual(PerimeterRes, 202)

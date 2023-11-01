import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    def test_first_area(self):
        Areares = area(10, 10)
        self.assertEqual(Areares, 50)

    def test_second_area(self):
        Areares = area(1, 2)
        self.assertEqual(Areares, 1)

    def test_third_area(self):
        Areares = area(100, 14)
        self.assertEqual(Areares, 700)

    def test_first_per(self):
        PerimeterRes = perimeter(10, 14,10)
        self.assertEqual(PerimeterRes, 34)

    def test_second_per(self):
        PerimeterRes = perimeter(3, 4,5)
        self.assertEqual(PerimeterRes, 12)

    def test_third_per(self):
        PerimeterRes = perimeter(100, 50,90)
        self.assertEqual(PerimeterRes, 240)


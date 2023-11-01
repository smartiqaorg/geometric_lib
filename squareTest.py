import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_first_area(self):
        Areares = area(10)
        self.assertEqual(Areares, 100)

    def test_second_area(self):
        Areares = area(1, )
        self.assertEqual(Areares, 1)

    def test_third_area(self):
        Areares = area(100, )
        self.assertEqual(Areares, 10000)

    def test_first_per(self):
        PerimeterRes = perimeter(10)
        self.assertEqual(PerimeterRes, 40)

    def test_second_per(self):
        PerimeterRes = perimeter(3)
        self.assertEqual(PerimeterRes, 12)

    def test_third_per(self):
        PerimeterRes = perimeter(101)
        self.assertEqual(PerimeterRes, 404)


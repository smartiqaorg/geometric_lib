import unittest
import circle
import math
import square
import triangle
import rectangle


class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi * (1 ** 2), "area1_FAIL")

    def test_area_2(self):
        res = circle.area(2)
        self.assertEqual(res, math.pi * (2 ** 2), "area2_FAIL")

    def test_area_3(self):
        res = circle.area(3)
        self.assertEqual(res, math.pi * (3 ** 2), "area3_FAIL")

    def test_area_4(self):
        res = circle.area(4)
        self.assertEqual(res, math.pi * (4 ** 2), "area4_FAIL")

    def test_area_5(self):
        res = circle.area(5)
        self.assertEqual(res, math.pi * (5 ** 2), "area5_FAIL")

    def test_per_1(self):
        res = circle.perimeter(1)
        self.assertEqual(res, 2 * math.pi * 1)

    def test_per_2(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 2 * math.pi * 2)

    def test_per_3(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 2 * math.pi * 3)

    def test_per_4(self):
        res = circle.perimeter(4)
        self.assertEqual(res, 2 * math.pi * 4)

    def test_per_5(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

class SquaretestCase(unittest.TestCase):

    def test_per_1(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4 * 1)

    def test_per_2(self):
        res = square.perimeter(2)
        self.assertEqual(res, 4 * 2)

    def test_per_3(self):
        res = square.perimeter(3)
        self.assertEqual(res, 4 * 3)

    def test_per_4(self):
        res = square.perimeter(4)
        self.assertEqual(res, 4 * 4)

    def test_per_5(self):
        res = square.perimeter(5)
        self.assertEqual(res, 4 * 5)

    def test_area_1(self):
        res = square.area(1)
        self.assertEqual(res, 1 * 1)

    def test_area_2(self):
        res = square.area(2)
        self.assertEqual(res, 2 * 2)

    def test_area_3(self):
        res = square.area(3)
        self.assertEqual(res, 3 * 3)

    def test_area_4(self):
        res = square.area(4)
        self.assertEqual(res, 4 * 4)

    def test_area_5(self):
        res = square.area(5)
        self.assertEqual(res, 5 * 5)

class trianlgeTestCase(unittest.TestCase):

    def test_per_1(self):
        res = triangle.perimeter(2,2,3)
        self.assertEqual(res, 2 + 2 + 3)

    def test_per_2(self):
        res = triangle.perimeter(4,5,6)
        self.assertEqual(res, 4 + 5 + 6)

    def test_per_3(self):
        res = triangle.perimeter(7, 6, 5)
        self.assertEqual(res, 5 + 6 + 7)

    def test_per_4(self):
        res = triangle.perimeter(4, 4, 4)
        self.assertEqual(res, 12)

    def test_per_5(self):
        res = triangle.perimeter(10, 4, 4)
        self.assertEqual(res, 18)

    def test_area_1(self):
        res = triangle.area(1, 4)
        self.assertEqual(res, 2)

    def test_area_2(self):
        res = triangle.area(2, 4)
        self.assertEqual(res, 4)

    def test_area_3(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_area_4(self):
        res = triangle.area(3, 5)
        self.assertEqual(res, 7.5)

    def test_area_5(self):
        res = triangle.area(5, 5)
        self.assertEqual(res, 12.5)

class RectangleTestCase(unittest.TestCase):
    def test_mul_0(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_mul_1(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_mul_2(self):
        res = rectangle.area(20, 20)
        self.assertEqual(res, 400)

    def test_mul_3(self):
        res = rectangle.area(30, 30)
        self.assertEqual(res, 900)


    def test_perimetr_1(self):
        res = rectangle.perimeter(5, 1)
        self.assertEqual(res, 2 * (5 + 1))

    def test_perimetr_2(self):
        res = rectangle.perimeter(50, 1)
        self.assertEqual(res, 2 * (50 + 1))

    def test_perimetr_3(self):
        res = rectangle.perimeter(50, 10)
        self.assertEqual(res, 2 * (50 + 10))

    def test_perimetr_4(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 2 * (0 + 0))

    def test_perimetr_5(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 2 * (1 + 1))
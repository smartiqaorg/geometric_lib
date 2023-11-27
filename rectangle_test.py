import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(5, 0)
       self.assertEqual(res, 0)
       
    def test_rectangle_mul_1(self):
       res = area(100, 5)
       self.assertEqual(res, 500)

    def test_rectangle_mul_2(self):
       res = area(10, 2)
       self.assertEqual(res, 20)

    def test_rectangle_per_1(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_rectangle_per_2(self):
        res = perimeter(1, 2)
        self.assertEqual(res, 6)

    def test_rectangle_per_3(self):
        res = perimeter(3, 8)
        self.assertEqual(res, 22)



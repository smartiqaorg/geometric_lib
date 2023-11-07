import unittest
import Rectangle
import triangle
import square
import circle
import math

class MyTestCase(unittest.TestCase):

    def test_Rectangle_area(self):
        test_data = ((1, 2, 2), (7, 9, 63),(3,10,30),(0,5,"ERROR"),(-1,7,"ERROR"))
        for a, b, s in test_data:
            res = Rectangle.area(a, b)
            self.assertEqual(res, s)

    def test_Rectangle_perimetr(self):
        test_data = ((1, 2, 6), (7, 9, 32), (3, 10, 26), (0, 5,"ERROR"), (-1, 7,"ERROR"))
        for a, b, p in test_data:
            res = Rectangle.perimeter(a, b)
            self.assertEqual(res, p)

    def test_square_area(self):
        test_data = ((1, 1), (7, 49),(30, 900),(0,"ERROR"),(-1,"ERROR"))
        for a, s in test_data:
            res = square.area(a)
            self.assertEqual(res, s)

    def test_square_perimetr(self):
        test_data = ((1, 4), (7, 28), (30, 120), (0, "ERROR"), (-1, "ERROR"))
        for a, p in test_data:
            res = square.perimeter(a)
            self.assertEqual(res, p)

    def test_triangle_area(self):
        test_data = ((1, 2, 1), (7, 8, 28),(3,10,15),(0,5,"ERROR"),(-1,7,"ERROR"))
        for a, h, s in test_data:
            res = triangle.area(a, h)
            self.assertEqual(res, s)

    def test_triangle_perimetr(self):
        test_data = ((1, 1, 1, 3), (7, 9, 8, 24), (30, 15, 20, 65), (0, 5, 10,"ERROR"), (-1, 7,8,"ERROR"),(3, 2,1,"ERROR"))
        for a, b, c,p in test_data:
            res = triangle.perimeter(a, b,c)
            self.assertEqual(res, p)

    def test_circle_area(self):
        test_data = ((1, 1*1*math.pi), (7, 7*7*math.pi), (30, 30*30*math.pi), (0,"ERROR"), (-1,"ERROR"))
        for a, s in test_data:
            res = circle.area(a)
            self.assertEqual(res, s)

    def test_circle_perimetr(self):
        test_data = ((1, 1*2*math.pi), (7, 7*2*math.pi), (30, 30*2*math.pi), (0,"ERROR"), (-1,"ERROR"))
        for a, p in test_data:
            res = circle.perimeter(a)
            self.assertEqual(res, p)

if __name__ == '__main__':
    unittest.main()

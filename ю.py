import unittest
import math
import circle
import rectangle
import square
import triangle

class MyTestCase(unittest.TestCase):
    def test_circle_area(self):
        c = ((1, 1*math.pi), (0, 0), (-1, "ERROR"))
        for n, s in c:
            res = circle.area(n)
            self.assertEqual(res, s)

    def test_circle_perimeter(self):
        c = ((1, 2*math.pi), (-1, "ERROR"), (0, 0))
        for n, s in c:
            res = circle.perimeter(n)
            self.assertEqual(res, s)

    def test_rectangle_area(self):
        c = ((1, 2, 2), (0, 0, 0), (-1, 3, "ERROR"))
        for n, m, s in c:
            res = rectangle.area(n, m)
            self.assertEqual(res, s)

    def test_rectangle_perimeter(self):
        c = ((1, 2, 6), (0, 0, 0), (-1, 3, "ERROR"))
        for n, m, s in c:
            res = rectangle.perimeter(n, m)
            self.assertEqual(res, s)

    def test_square_area(self):
        c = ((1, 1), (0, 0), (-1, "ERROR"))
        for n, s in c:
            res = square.area(n)
            self.assertEqual(res, s)

    def test_square_perimeter(self):
        c = ((1, 4), (0, 0), (-1, "ERROR"))
        for n, s in c:
            res = square.perimeter(n)
            self.assertEqual(res, s)

    def test_triangle_area(self):
        c = ((1, 2, 1), (0, 0, 0), (-1, 3, "ERROR"))
        for n, m, s in c:
            res = triangle.area(n, m)
            self.assertEqual(res, s)

    def test_triangle_perimeter(self):
        c = ((1, 2, 2, 5), (0, 0, 0, 0), (-1, 3, -2, "ERROR"))
        for n, m, k, s in c:
            res = triangle.perimeter(n, m, k)
            self.assertEqual(res, s)

if __name__ == '__main__':
    unittest.main()

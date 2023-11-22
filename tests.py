import unittest
import rectangle
import triangle
import square
import circle
import math

class CircleTestCase(unittest.TestCase):
   def test_circle_area(self):
        test_ci_ar=((0, "error"),(7, 49*math.pi),(-3, "error"))
        for a, s in test_ci_ar:
            res=circle.area(a)
            self.assertEqual(res, s)
       
   def test_circle_perimeter(self):
        test_ci_pe=((0, "error"),(7, 14*math.pi),(-3, "error"))
        for a, s in test_ci_pe:
            res=circle.perimeter(a)
            self.assertEqual(res, s)

class SquareTestCase(unittest.TestCase):
   def test_square_area(self):
        test_sq_ar=((0, "error"),(7, 49),(-3, "error"))
        for a, s in test_sq_ar:
            res=square.area(a)
            self.assertEqual(res, s)
       
   def test_square_perimeter(self):
        test_sq_pe=((0, "error"),(7, 28),(-3, "error"))
        for a, s in test_sq_pe:
            res=square.perimeter(a)
            self.assertEqual(res, s)
            
class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area(self):
        test_re_ar = ((0, 1, "error"),(7, 13, 91),(-3, -8, "error"))
        for a, b, s in test_re_ar:
            res=rectangle.area(a, b)
            self.assertEqual(res, s)
       
   def test_rectangle_perimeter(self):
        test_re_pe = ((0, 1, "error"),(7, 13, 40),(-3, -8, "error"))
        for a, b, s in test_re_pe:
            res=rectangle.perimeter(a, b)
            self.assertEqual(res, s)
            
class TriangleTestCase(unittest.TestCase):
   def test_triangle_area(self):
        test_tr_ar=((0, 1, "error"),(7, 12, 42),(-3, -8, "error"))
        for a, b, s in test_tr_ar:
            res=triangle.area(a, b)
            self.assertEqual(res, s)
       
   def test_triangle_perimeter(self):
        test_tr_pe=((0, 0, 0, "error"),(7, 13, 19, 39),(-3, -8, -13, "error"))
        for a, b, c, s in test_tr_pe:
            res=triangle.perimeter(a, b, c)
            self.assertEqual(res, s)

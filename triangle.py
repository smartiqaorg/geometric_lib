import unittest

def area(a, h):
    '''Принимает числа a и h, возвращает ah/2 - площадь треугольника
    При вызове функции print(area(25, 6,72)) выведет 84 - площадь треугольника со стороной основания a=25 и высотой, опущенной на эту сторону, h=6,72'''
    if (a>0) and (h>0):
        return a * h / 2
    else:
        return "error"

def perimeter(a, b, c):
    '''Принимает числа a, b и c, возвращает a + b + c - периметр треугольника
    При вызове функции print(perimeter(25, 24, 7)) выведет 56 - периметр треугольника со сторонами a=25, b=24 и c=7'''
    if (a>0) and (b>0) and (c>0):
        return a + b + c
    else:
        return "error"

class TriangleTestCase(unittest.TestCase):
   def test_triangle_area(self):
        test_tr_ar=((0, 1, "error"),(7, 12, 42),(-3, -8, "error"))
        for a, b, s in test_tr_ar:
            res=area(a, b)
            self.assertEqual(res, s)
       
   def test_triangle_perimeter(self):
        test_tr_pe=((0, 0, 0, "error"),(7, 13, 19, 39),(-3, -8, -13, "error"))
        for a, b, c, s in test_tr_pe:
            res=perimeter(a, b, c)
            self.assertEqual(res, s)

import unittest

def area(a, b):
    '''Принимает числа a и b, возвращает ab - площадь прямоугольника
    При вызове функции print(area(1, 2)) выведет 2 - площадь прямоугольника со сторонами a=1 и b=2'''
    if (a>0) and (b>0):
        return a * b
    else:
        return "error"
    
def perimeter(a, b):
    '''Принимает числа a и b, возвращает 2a + 2b - периметр прямоугольника'''
    '''При вызове функции print(perimeter(1, 2)) выведет 6 - периметр прямоугольника со сторонами a=1 и b=2'''
    if (a>0) and (b>0):
        return 2*(a + b)
    else:
        return "error"

class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area(self):
        test_re_ar = ((0, 1, "error"),(7, 13, 91),(-3, -8, "error"))
        for a, b, s in test_re_ar:
            res=area(a, b)
            self.assertEqual(res, s)
       
   def test_rectangle_perimeter(self):
        test_re_pe = ((0, 1, "error"),(7, 13, 40),(-3, -8, "error"))
        for a, b, s in test_re_pe:
            res=perimeter(a, b)
            self.assertEqual(res, s)

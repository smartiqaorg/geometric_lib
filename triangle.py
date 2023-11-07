import unittest

def area(a, h):
    '''
    Принимает числа a(сторона треугольника) и h(высота треугольника, проведённая к этой стороне)
    Возвращает площадь треугольника a * h / 2
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
    Принимает числа a, b, c(стороны треугольника)
    Возвращает периметр a + b + c
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
       res = area(10, 4)
       self.assertEqual(res, 20.0)
    def test_triangle_perimetr(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)


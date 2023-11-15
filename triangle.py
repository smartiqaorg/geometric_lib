def area(a, h):
    '''Принимает числа a и h (сторона и высота, перпендикулярная стороне, соотвественно), возвращает площадь треугольника'''
    return a * h / 2
def perimeter(a, b, c):
    '''Принимает числа a, b и c (три стороны треугольника), возвращает периметр треугольника'''
    return a + b + c
import unittest
class CircleTestCase(unittest.TestCase):

    def test_zero_area(self):

        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perim(self):

        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

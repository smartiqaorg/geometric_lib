import unittest
def area(a, h):
    return a * h / 2
# принимает на вход значения стороны треугольника, которой проведена высота, и высоты, выводит площадь треугольника

def perimeter(a, b, c): 
    return a + b + c 
# принимает на вход значения всех сторон треугольника, выводит периметр треугольника


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_per(self):
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 20)

    def test_triangle_per(self):
        res = perimeter(15, 15, 15)
        self.assertEqual(res, 45)
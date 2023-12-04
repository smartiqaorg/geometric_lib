import unittest

def area(a, h): 
    """
        Возвращает площадь треугольника со стороной a и высотой h
        Параметры:
            а (int) : сторона треугольника
            h (int) : высота h
    """
    return a * h / 2 

def perimeter(a, b, c): 
    """
        Возвращает периметр треугольника со сторонами a, b, c
        Параметры:
            a (int) : сторона треугольника
            b (int) : сторона треугольника
            c (int) : сторона треугольника
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10, 8)
        self.assertEqual(res, 40)

    def test_int_perimeter(self):
        res = perimeter(10, 10, 12)
        self.assertEqual(res, 32)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)
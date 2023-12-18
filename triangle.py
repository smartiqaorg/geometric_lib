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
    def test_int_perimeter(self):
        res = perimeter(10, 10, 12)
        self.assertEqual(res, 32)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("abc")

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("abc")
    
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5, 1, -2)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-2.5, 1)

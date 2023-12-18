import unittest

def area(a, b): 
    """
        Возвращает площадь прямоугольника со стороной a и стороной b
        Параметры:
            а (int) : сторона 
            b (int) : сторона прямоугольника
    """
    return a * b

def perimeter(a, b): 
    """
        Возвращает периметр прямоугольника со стороной a и стороной b
        Параметры:
            а (int) : сторона прямоугольника
            b (int) : сторона прямоугольника
    """
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10, 20)
        self.assertEqual(res, 200)

    def test_int_perimeter(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_float_area(self):
        res = area(2.5, 3.5)
        self.assertEqual(res, 8.75)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("abc", 2)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("abc", 2)
    
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5, -10)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-2.5, -10)

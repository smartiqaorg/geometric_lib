import math
import unittest

def area(r):
    """
        Возвращает площадь круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return math.pi * r * r

def perimeter(r):
    """
        Возвращает периметр круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.159, 3)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.832, 3)

    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.635, 3)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 15.708, 3)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("abc")

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("abc")
    
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-2)
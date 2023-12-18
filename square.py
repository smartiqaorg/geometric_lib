import unittest

def area(a):
    """
        Возвращает площадь квадрата со стороной a
        Параметры:
            а (int) : сторона квадрата
    """
    return a * a

def perimeter(a):
    """
        Возвращает периметр квадрата со стороной a
        Параметры:
            а (int) : сторона квадрата
    """
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)

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

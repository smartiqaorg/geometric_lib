def area(a, b):
    ''' принимает значение а,b. а возвращает площадь прямоугольника со сторонами а и b'''
    return a * b

def perimeter(a, b):
    ''' принимает значение а,b. а возвращает периметр прямоугольника со сторонами а и b'''
    return 2 * (a + b)

import unittest


class MyTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)


import unittest

class TriangleTestCase(unittest.TestCase):
    # тесты для функции area()
    def test_zero_mul(self):
        res = area(0, 100)
        self.assertEqual(res, 0)

    def test_int_mul(self):
        res = area(12, 20)
        self.assertEqual(res, 120)

    def test_minus_mul(self):
        res = area(-5, -10.00)
        self.assertEqual(res, -1, "длина > 0")

    def test_mater_mul(self):
        res = area(2.9, 12.8)
        self.assertEqual(res, 18.56)

    def test_mater2_mul(self):
        res = area(4.9, 3)
        self.assertEqual(res, 7.35)
        
    def test_mater3_mul(self):
        res = area(3.5, 3.9)
        self.assertEqual(res, 6.825)


    #тесты для функции perimeter()
    def test_int_perimeter_mul(self):
        res = perimeter(3, 15, 5)
        self.assertEqual(res, 23)
    
    def test_minus_perimeter_mul(self):
        res = perimeter(-3, 16, 7)
        self.assertEqual(res, -1, "длина > 0")

    def test_mater_perimeter_mul(self):
        res = perimeter(3.1, 15.8, 5.1)
        self.assertEqual(res, 24)
    
    def test_mater2_perimeter_mul(self):
        res = perimeter(3.1, 15.8, 50)
        self.assertEqual(res, 68.9)



def area(a, h):
    '''
    Возвращает площадь треугольника.

        Принимает:
                a (int): первое десятичное число в 10 система счисления, длина основания
                h (int): второе десятичное число в 10 система счисления, длина высоты

        Возвращаемое значение:
                площадь треугольника
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает 3 числа a,b,c и возвращает сумму этих чисел/периметр треугольника'''
    return a + b + c

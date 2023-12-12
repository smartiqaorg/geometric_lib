import unittest

class RectangleTestCase(unittest.TestCase):
    # тесты для функции area()
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_int_area_mul(self):
        res = area(34, 12)
        self.assertEqual(res, 408)

    def test_mater_mul(self):
        res = area(15.5, 3.5)
        self.assertEqual(res, 54.25)

    def test_mater2_mul(self):
        res = area(5.45, 5.88)
        self.assertEqual(res, 32.046)
    
    def test_mater3_mul(self):
        res = area(1.6, 6)
        self.assertEqual(res, 9.6)

    def test_long_long_numb_mul(self):
        res = area(1000000000000000000, 5000000000000000000)
        self.assertEqual(res, 5000000000000000000000000000000000000)
        
    def test_minus_mul(self):
        res = area(-14, 5)
        self.assertEqual(res, -1, "площадь > 0")



    #тесты для функции perimeter()
    def test_int_perimeter_mul(self):
        res = perimeter(6, 5)
        self.assertEqual(res, 22)

    def test_mater_perimeter_mul(self):
        res = perimeter(6, 5.9)
        self.assertEqual(res, 23.8)

    def test_mater2_perimeter_mul(self):
        res = perimeter(1.6, 14.8300)
        self.assertEqual(res, 32.86)
    
    def test_mater3_perimeter_mul(self):
        res = perimeter(1, 0.00004225)
        self.assertEqual(res, 2.0000845)

    def test_minus_perimeter_mul(self):
        res = perimeter(-1, -10)
        self.assertEqual(res, -1, "периметр > 0")
    
    def test_minus2_perimeter_mul(self):
        res = perimeter(-2, 100)
        self.assertEqual(res, -1, "сторона > 0")




def area(a, b):
    '''Принимает 2 числа а,b и возвращает результат умножения а на b.
    Это является площадью квадрата/прямоугольника'''
    return a * b 

def perimeter(a, b):
    '''Принимает 2 числа а,b и возвращает периметр фигуры'''
    return 2*(a + b)

import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a и b (числа)

        Параметры:
            a : длинна одной стороны (число)
            b : длинна другой стороны (число)

        Возвращаемое значение (число):
            произведение а и b, то есть площадь прямоугольника
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает  периметр прямоугольника со сторонами a, b (числа)

        Парметры:
            a - длина одной стороны (число)
            b- длина другой стороны (число)

        Возвращаемое значение (число):
            удвоенная сумма а и b
    '''
    return 2*(a + b)

class RectangleTestCase(unittest.TestCase):
    def test_mul_0(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_mul_1(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_mul_2(self):
        res = area(20, 20)
        self.assertEqual(res, 400)

    def test_mul_3(self):
        res = area(30, 30)
        self.assertEqual(res, 900)


    def test_perimetr_1(self):
        res = perimeter(5, 1)
        self.assertEqual(res, 2 * (5 + 1))

    def test_perimetr_2(self):
        res = perimeter(50, 1)
        self.assertEqual(res, 2 * (50 + 1))

    def test_perimetr_3(self):
        res = perimeter(50, 10)
        self.assertEqual(res, 2 * (50 + 10))

    def test_perimetr_4(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 2 * (0 + 0))

    def test_perimetr_5(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 2 * (1 + 1))


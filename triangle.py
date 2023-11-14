import unittest
def area(a, h):
    '''
    возвращает площадь треугольника с длиной одной из сторон a, и длины высоты, которая к ней проведена, h.

        Парметры:
            a - длина одной из сторон (число)
            h - длина высоты, которая проведена к указанной стороне. (число)

        Возвращаемое значение:
            Полупроизведение высоты на эту сторону, то есть площадь треугольника.
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника со сторонами a, b, c (числа)

        Входные данные:
            a - длина первой стороны (число)
            b - длина второй стороны (число)
            c - длина третьей стороны (число)

        Возвращаемое значение (число): сумма a, b, c.
    '''
    return a + b + c

class trianlgeTestCase(unittest.TestCase):

    def test_per_1(self):
        res = perimeter(2,2,3)
        self.assertEqual(res, 2 + 2 + 3)

    def test_per_2(self):
        res = perimeter(4,5,6)
        self.assertEqual(res, 4 + 5 + 6)

    def test_per_3(self):
        res = perimeter(7, 6, 5)
        self.assertEqual(res, 5 + 6 + 7)

    def test_per_4(self):
        res = perimeter(4, 4, 4)
        self.assertEqual(res, 12)

    def test_per_5(self):
        res = perimeter(10, 4, 4)
        self.assertEqual(res, 18)

    def test_area_1(self):
        res = area(1, 4)
        self.assertEqual(res, 2)

    def test_area_2(self):
        res = area(2, 4)
        self.assertEqual(res, 4)

    def test_area_3(self):
        res = area(3, 4)
        self.assertEqual(res, 6)

    def test_area_4(self):
        res = area(3, 5)
        self.assertEqual(res, 7.5)

    def test_area_5(self):
        res = area(5, 5)
        self.assertEqual(res, 12.5)
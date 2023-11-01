import unittest
class RectangleTestCase(unittest.TestCase):
    def test_zero_ab(self):
        resarea = area(0,0)
        resperimetr = perimeter(0,0)
        self.assertEqual(resarea, 0)
        self.assertEqual(resperimetr, 0)
    def test_single_ab(self):
        resarea = area(1,1)
        resperimetr = perimeter(1,1)
        self.assertEqual(resarea, 1)
        self.assertEqual(resperimetr, 4)
    def test_examplefromdeclaration_ab(self):
        resarea = area(4,4)
        resperimetr = perimeter(4,4)
        self.assertEqual(resarea, 16)
        self.assertEqual(resperimetr, 16)

def area(a, b):
    '''
    Принимает числа а и b - стороны прямоугольника
    Возвращает площадь прямоугольника
    Пример: a=4, b=4, area(4,4)=16
    '''
    return a * b

def perimeter(a, b):
    '''
    Принимает числа а и b - стороны прямоугольника
    Возвращает периметр прямоугольника
    Пример: a=4, b=4, perimeter(4,4)=16
    '''
    return 2 * (a + b)

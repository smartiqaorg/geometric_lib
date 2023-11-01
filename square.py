import unittest
class RectangleTestCase(unittest.TestCase):
    def test_zero_xab(self):
        resarea = area(0)
        resperimetr = perimeter(0)
        self.assertEqual(resarea, 0)
        self.assertEqual(resperimetr, 0)
    def test_single_ab(self):
        resarea = area(1)
        resperimetr = perimeter(1)
        self.assertEqual(resarea, 1)
        self.assertEqual(resperimetr, 4)
    def test_examplefromdeclaration_ab(self):
        resarea = area(4)
        resperimetr = perimeter(4)
        self.assertEqual(resarea, 16)
        self.assertEqual(resperimetr, 16)
def area(a):
    '''
    Принимает число a - сторона квадрата
    Возвращает площадь квадрата
    Пример: a=4, area(4)=16
    '''
    return a * a
def perimeter(a):
    '''
    Принимает число a - сторона квадрата
    Возвращает периметр квадрата
    Пример: a=4, perimeter(4)=16
    '''
    return 4 * a
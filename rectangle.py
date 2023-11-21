import unittest

class RectangleTestCase(unittest.TestCase):
    def test_area_0(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_area_1(self):
        res = area(15, 5)
        self.assertNotEqual(res, (15 * 5) + 1)

    @unittest.expectedFailure
    def test_area_2(self):
        res = area('12', '123')
        self.assertEqual(res, TypeError)

    def test_area_3(self):
       res = area(50, 50)
       self.assertEqual(res, 50*50)

    def test_perimeter_0(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(1000, 500)
        self.assertEqual(res, (1000+500) * 2)

def area(a, b):
    '''
    Функция принимает на вход числа a, b - стороны прямоугольника и возвращает площадь Прямоугольника

    Вход: 3 4 Выход: 12
    ''' 
    return a * b 

def perimeter(a, b):
    '''
    Функция принимает на вход числа a, b - стороны прямоугольника и возвращает периметр Прямоугольника
    
    Вход: 2 5 Выход: 14
    ''' 
    return (a + b) * 2 
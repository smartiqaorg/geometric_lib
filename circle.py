import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_area_0(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(100)
        self.assertNotEqual(res, 100*100*3,14)

    @unittest.expectedFailure
    def test_area_2(self):
        res = area('1')
        self.assertEqual(res, TypeError)

    def test_area_3(self):
       res = area(50)
       self.assertEqual(res, 50*50*math.pi)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(10000)
        self.assertEqual(res, 2*math.pi*10000)

def area(r):
    '''
    Функция возвращает площадь Круга

    Функция принимает на вход число r - радиус круга. 
    Также задействуя доп. библиотеку math используется число Pi.

    Вход: 2 Выход: 12,56
    ''' 
    return math.pi * r * r


def perimeter(r):
    '''
    Функция возвращает периметр Круга

    Функция принимает на вход число r - радиус круга. 
    Так же задействуя доп. библиотеку math используется число Pi.
    
    Вход: 3 Выход: 18,84
    ''' 
    return 2 * math.pi * r


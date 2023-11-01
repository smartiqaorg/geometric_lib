import unittest
class RectangleTestCase(unittest.TestCase):
    def test_zero_r(self):
        resarea = area(0)
        resperimetr = perimeter(0)
        self.assertEqual(resarea, 0)
        self.assertEqual(resperimetr, 0)
    def test_single_к(self):
        resarea = area(1)
        resperimetr = perimeter(1)
        self.assertEqual(resarea, 3.141592653589793)
        self.assertEqual(resperimetr, 6.283185307179586)
    def test_examplefromdeclaration_к(self):
        resarea = area(4)
        resperimetr = perimeter(4)
        self.assertEqual(resarea, 50.26548245743669)
        self.assertEqual(resperimetr, 25.132741228718345)
import math
def area(r):
    '''
    Принимает число r - радиус круга
    Возвращает площадь круга
    Пример: r=4, area(4)=50.26548245743669
    '''
    return math.pi * r * r
def perimeter(r):
    '''
    Принимает число r - радиус круга
    Возвращает периметр круга
    Пример: r=4, perimeter(4)=25.132741228718345
    '''
    return 2 * math.pi * r
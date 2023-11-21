import math
import unittest

class TestTriangleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1,2), 1)
        self.assertEqual(area(math.sqrt(2),math.sqrt(2)), 1)
        self.assertEqual(area(-14,-12), 0)
    def test_perimetr():
        self.assertEqual(perimeter(1,3,3), 7)
        self.assertEqual(perimeter(1,10,100), 0)
        self.assertEqual(perimeter(-3,1,1), 0)


def area(a, h):
    '''Возвращает численное значение площади треугольника со стороной a и высотой h'''
    return a * h / 2 

def perimeter(a, b, c):
    '''Возвращает численное значение периметра треугольника со сторонами a,b,c'''
    return a + b + c 

if __name__ == '__main__':
    unittest.main()

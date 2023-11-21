import math
import unittest

class TestRectangleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1,1), 1)
        self.assertEqual(area(2/3,3/2), 1)
        self.assertEqual(area(1000000,1/7), 1000000/7)
        self.assertEqual(area(-1,-1), 0)
    def test_perimetr():
        self.assertEqual(perimeter(1,1), 4)
        self.assertEqual(perimeter(2/3,3/2), 13/3)
        self.assertEqual(perimeter(1000000,1/7), 1400002/7)
        self.assertEqual(perimeter(-1,-1), 0)


def area(a, b):
    '''Возвращает численное значение площади прямоугольника с длиннами a,b'''
    return a * b 

def perimeter(a, b):
    '''Возвращает численное значение периметра прямоугольника с длиннами a,b'''
    return 2*(a + b) 

if __name__ == '__main__':
    unittest.main()

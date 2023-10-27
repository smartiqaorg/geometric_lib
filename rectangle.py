import unittest
…
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

def area(a,b):
    return a * b
'''
Принимает числа а и b - стороны прямоугольника
Возвращает площадь прямоугольника
Пример: a=4, b=4, area(4,4)=16
'''
def perimeter(a,b):
'''
Принимает числа а и b - стороны прямоугольника
Возвращает периметр прямоугольника
Пример: a=4, b=4, perimeter(4,4)=8
'''
    return (a+b)*2

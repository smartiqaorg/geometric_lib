
import unittest


def area(a, b):
    return a*b
'''Функция нахождения площади прямоугольника: принимает два числа a и b, возвращает произведение a и b'''
def perimeter(a, b):
    return 2*a + 2*b
'''Функция нахождения периметра прямоугольника: принимает два числа a, b, возвращает сумму произведений чисел a и 2, b и 2'''


class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area(self):
       test_data = ((1,1,1), (2,2,4), (3,3,9),(0,2,0),(2,0,0))
       for x,y,s in test_data:
          res = area(x, y)
          self.assertEqual(res, s)
       
   def test_rectangle_perimetr(self):
      test_data = ((1,1,4), (10,1,22), (3,3,12),(2,3,10),(3,2,10))
      for x,y,s in test_data:
         res = perimeter(x, y)
         self.assertEqual(res, s)


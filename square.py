
import unittest

def area(a):
    return a * a
'''Функция нахождения плошади квадрата: принимает число a, возвращает квадрат числа a'''

def perimeter(a):
    return 4 * a
'''Функция нахождения периметра квадрата: принимает число a, возвращает произведение a и 4'''


class SquareTestCase(unittest.TestCase):
   def test_square_area(self):
       test_data = ((1,1), (2,4), (3,9), (0,0))
       for x,s in test_data:
          res = area(x)
          self.assertEqual(res, s)
       
   def test_square_perimetr(self):
      test_data = ((1,4), (10,40), (3,12),(2,8),(0,0))
      for x,s in test_data:
         res = perimeter(x)
         self.assertEqual(res, s)

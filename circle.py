import math
import unittest

def area(r):
    return math.pi * r * r
'''Функция нахождения площади круга: принимает число r, возвращает произведение квадрата r и числа пи'''

def perimeter(r):
    return 2 * math.pi * r
'''Функция нахождения периметра круга: возвращает удвоенное произведение числа пи и r'''


class CircleTestCase(unittest.TestCase):
   def test_circle_area(self):
       test_data = ((1,1*math.pi), (2,4*math.pi), (3,9*math.pi), (0,0))
       for x,s in test_data:
          res = area(x)
          self.assertEqual(res, s)
       
   def test_circle_perimetr(self):
      test_data = ((1,2*math.pi), (10,20*math.pi), (3,6*math.pi),(0,0))
      for x,s in test_data:
         res = perimeter(x)
         self.assertEqual(res, s)

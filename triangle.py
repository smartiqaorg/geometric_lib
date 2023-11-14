
import unittest
import math

def area(a, b, c):
    return (a*b*math.sin(c))/2
'''Функция нахождения плошади треугольника: принимает число a, b - стороны треугольника, и c - угол между этими сторонами, возвращает половину произведения a, b и синуса угла c'''
def perimeter(a, b, c):
    return a + b + c
'''Функция нахождения периметра треугольника: принимает числа a, b, c - стороны треугольника, возвращает сумму a, b, c'''

class TriangleTestCase(unittest.TestCase):
   def test_triangle_area(self):
       test_data = ((3,4,math.pi/2,6),)
       for x,y,c,s in test_data:
          res = area(x, y, c)
          self.assertEqual(res, s)
       
   def test_triangle_perimetr(self):
      test_data = ((1,1,1,3), (3,4,5,12))
      for x,y,c,s in test_data:
         res = perimeter(x, y, c)
         self.assertEqual(res, s)

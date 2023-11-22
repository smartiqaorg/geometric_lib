import math
import unittest
def area(r):
    return math.pi * r ** 2
# Принимает значение радиуса окружности r и возвращает площадь круга с таким радиусом 

def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(area(0), 0);
        self.assertEqual(perimeter(0), 0);
    def test2(self):
        self.assertEqual(area(1), math.pi);
        self.assertEqual(perimeter(1), 2 * math.pi);
    def test3(self):
        self.assertEqual(area(1000), 1000000 * math.pi);
        self.assertEqual(perimeter(1000), 2000 * math.pi);
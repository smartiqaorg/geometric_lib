import unittest
def area(a, h): 
    return a * h / 2 
# Принимает сторону и высоту к ней треугольника a и h и возвращает его площадь
def perimeter(a, b, c): 
    return a + b + c 
# Принимает три стороны треугольника a,b,c и возвращает его периметр
class TriangleTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(area(0, 0), 0);
        self.assertEqual(perimeter(0, 0, 0), 0);
    def test2(self):
        self.assertEqual(area(1, 1), 0.5);
        self.assertEqual(perimeter(1, 1, 1), 3);
    def test3(self):
        self.assertEqual(area(100, 2), 100);
        self.assertEqual(perimeter(100, 100, 1), 201);
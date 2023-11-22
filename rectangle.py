import unittest
def area(a, b):
	return a * b
# Принимает стороны a и b прямоугольника и возвращает его площадь
def perimeter(a, b):
	return 2 * (a + b)
# Принимает стороны a и b прямоугольника и вовзращает его периметр
class RectangleTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(area(0, 0), 0);
        self.assertEqual(perimeter(0, 0), 0);
    def test2(self):
        self.assertEqual(area(1, 1), 1);
        self.assertEqual(perimeter(1, 1), 4);
    def test3(self):
        self.assertEqual(area(100, 29), 2900);
        self.assertEqual(perimeter(100, 29), 258);
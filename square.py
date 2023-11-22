import unittest
def area(a):
    return a * a
#  Принимает Значение стороны a квадрата и возвращает его площадь

def perimeter(a):
    return 4 * a
#  Принимает Значение стороны a квадрата и возвращает его периметр
class SquareTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(area(0), 0);
        self.assertEqual(perimeter(0), 0);
    def test2(self):
        self.assertEqual(area(1), 1);
        self.assertEqual(perimeter(1), 4);
    def test3(self):
        self.assertEqual(area(100), 10000);
        self.assertEqual(perimeter(100), 400);
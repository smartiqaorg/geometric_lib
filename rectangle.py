import unittest

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 12) # successful test
        self.assertEqual(area(2, 3), 5) # fail test
        self.assertEqual(area('string', 4), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 2), 14) # successful test
        self.assertEqual(perimeter(10, 2), 62)  # fail test
        self.assertEqual(perimeter('string', 3), 'fail')  # fail test

def area(a, b):
    return a * b
    # принимает два числа a и b - стороны прямоугольника
    # возвращает площадь прямоугольника со сторонами a и b
def perimeter(a, b):
    return a * 2 + b * 2
    # принимает два числа a и b - стороны прямоугольника
    # возвращает периметр прямоугольника со сторонами a и b

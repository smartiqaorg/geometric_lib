import unittest

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 12) # successful test
        self.assertEqual(area(2, 3), 5) # fail test
        self.assertEqual(area('string', 4), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 2, 3), 10) # successful test
        self.assertEqual(perimeter(10, 2, 1), 62)  # fail test
        self.assertEqual(perimeter('string', 3, 1), 'fail')  # fail test

def area(a, h):
    return a * h / 2
    # принимает два числа a - длинна основания треугольника и b - высоту треугольника
    # возвращает площадь треугольника с основанием a и высотой h
def perimeter(a, b, c):
    return a + b + c
    # принимает три числа a, b и c - стороны треугольника
    # возвращает периметр треугольника со сторонами a, b и c

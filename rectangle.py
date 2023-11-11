import unittest

def area(a, b):
    """
    Вычисляет площадь прямоугольника на основе длин его сторон.
	
	Параметры:
		    a (float): длина прямоугольника.
		    b (float): ширина прямоугольника.
	Возвращаемое значение:
		    float: площадь прямоугольника, вычисляемая по формуле a * b.
    """
    return a * b 

def perimeter(a, b): 
    """
    Вычисляет периметр прямоугольника на основе длин его сторон.
	
	Параметры:
		    a (float): длина прямоугольника.
		    b (float): ширина прямоугольника.
	Возвращаемое значение:
		    float: периметр прямоугольника, вычисляемый по формуле 2*(a + b).
    """
    return 2*(a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_per(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

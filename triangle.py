import unittest
def area(a, h):
    """
    Вычисляет площадь треугольника на основе его основания и высоты.
	
	Параметры:
		    a (float): длина основания треугольника.
                    h (float): высота треугольника (перпендикулярно основанию).
	Возвращаемое значение:
		    float: площадь треугольника, вычисляемая по формуле (a * h)/2.
    """
    return a * h / 2 

def perimeter(a, b, c): 
    """
    Вычисляет периметр треугольника на основе длин его сторон.
	
	Параметры:
		    a (float): длина первой стороны треугольника.
                    b (float): длина второй стороны треугольника.
                    c (float): длина третьей стороны треугольника.
	Возвращаемое значение:
		    float: периметр треугольника, вычисляемый по формуле a + b + c.
    """
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = area(10,10)
        self.assertEqual(res, 50)

    def test_zero_per(self):
        res = perimeter(10,0,50)
        self.assertEqual(res, 60)

    def test_triangle_per(self):
        res = perimeter(29,11,88)
        self.assertEqual(res, 128)
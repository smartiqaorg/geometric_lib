import math
import unittest
def area(r):
    """
    Вычисляет площадь круга на основе его радиуса.
	
	Параметры:
		    r (float): радиус круга.
	Возвращаемое значение:
		    float: площадь круга, вычисляемая по формуле math.pi * r * r.
    """
    return math.pi * r * r

def perimeter(r):
    """
    Вычисляет периметр круга на основе его радиуса.

	Параметры:
		    r (float): радиус круга.
        Возвращаемое значение:
		    float: периметр круга, вычисляемый по формуле 2 * math.pi * r.
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_per(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
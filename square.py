import unittest
def area(a):
    """
    Вычисляет площадь квадрата по длине его стороны.
	
	Параметры:
		    a (float): длина стороны квадрата.
	Возвращаемое значение:
		    float: Площадь квадрата, вычисляемая по формуле a * a.
    """
    return a * a

def perimeter(a):
    """
    Вычисляет периметр квадрата по длине его стороны.
	
	Параметры:
		    a (float): длина стороны квадрата.
	Возвращаемое значение:
		    float: Периметр квадрата, вычисляемый по формуле 4 * a.
    """
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
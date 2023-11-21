import math
import unittest

class TestCircleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1), math.pi)
        self.assertEqual(area(2/3), 4/9*math.pi)
        self.assertEqual(area(1/math.sqrt(math.pi)), 1)
        self.assertEqual(area(-1), 0)
    def test_perimetr():
        self.assertEqual(perimeter(1), 2*math.pi)
        self.assertEqual(perimeter(2/3), 4/3*math.pi)
        self.assertEqual(perimeter(1/math.pi), 2)
        self.assertEqual(perimeter(-1), 0)

def area(r):
    '''Принимает число r-радиус окуржности, возвращает численное значение площади круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r-радиус окуржности, возвращает численное значение периметра круга'''
    return 2 * math.pi * r

if __name__ == '__main__':
    unittest.main()

import math
import unittest

class TestCircleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2/3), 4/9)
        self.assertEqual(area(10000/7), 100000000/49)
        self.assertEqual(area(math.sqrt(3)), 3)
        self.assertEqual(area(-1), 0)
    def test_perimetr():
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2/3), 4/3)
        self.assertEqual(perimeter(10000/7), 40000/7)
        self.assertEqual(perimeter(math.sqrt(3)), math.sqrt(48))
        self.assertEqual(perimeter(-1), 0)


def area(a):
    '''Возвращает численное значение площади квадарата со сторонной a'''
    return a * a


def perimeter(a):
    '''Возвращает численное значение периметра квадарата со сторонной a'''
    return 4 * a

if __name__ == '__main__':
    unittest.main()

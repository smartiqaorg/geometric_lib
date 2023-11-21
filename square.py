import unittest

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25) # successful test
        self.assertEqual(area(2), 6) # fail test
        self.assertEqual(area('string'), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20) # successful test
        self.assertEqual(perimeter(10), 62)  # fail test
        self.assertEqual(perimeter('string'), 'fail')  # fail test

def area(a):
    return a * a
    # принимает число a - сторону квадрата
    # возвращает площадь квадрата со стороной a

def perimeter(a):
    return 4 * a
    # принимает число a - сторону квадрата
    # возвращает периметр квадрата со стороной a

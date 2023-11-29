def area(a,b):
    return a*b

def perimeter(a,b):
    return 2*a+2*b


import unittest

class TestArea(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(area(-1, 4), -4)


class TestPerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(-2, 4), 4)
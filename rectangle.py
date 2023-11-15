def area(a, b):
	''' Принимает два числа, обозначающих стороны прямоугольника и перемножает их, получая площадь''' 
	return a * b
def perimeter(a, b):
	''' Принимает два числа, обозначающих стороны прямоугольника, затем складывает их и умножает на два, таким образом получаем периметр''' 
	return 2*(a + b)

import unittest

class RectangleTestCase(unittest.TestCase):
    def test_one_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_two_area(self):
        res = area(5, 25)
        self.assertEqual(res, 125)

    def test_three_area(self):
        res = area(14, 196)
        self.assertEqual(res, 2744)

    def test_four_area(self):
        res = area(21, 21)
        self.assertEqual(res, 441)

    def test_five_area(self):
        res = area(7262, 9146)
        self.assertEqual(res, 66418252)

    def test_one_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_two_perimeter(self):
        res = perimeter(5, 44)
        self.assertEqual(res, 98)

    def test_three_perimeter(self):
        res = perimeter(267, 823)
        self.assertEqual(res, 2180)

    def test_four_perimeter(self):
        res = perimeter(13, 422)
        self.assertEqual(res, 870)

    def test_five_perimeter(self):
        res = perimeter(3874, 7263)
        self.assertEqual(res, 22274)

if __name__ == '__main__':
    unittest.main()

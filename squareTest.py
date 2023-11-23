import unittest
from square import area
from square import perimeter

class SquareTests(unittest.TestCase):
    def test_area_regular(self):
        ans = area(5)
        self.assertEqual(25, ans)
        ans = area(30)
        self.assertEqual(900, ans)
        ans = area(100)
        self.assertEqual(10000, ans)

    def test_area_big_number(self):
        ans = area(10 ** 5)
        self.assertEqual(10 ** 10, ans)
        ans = area(30000)
        self.assertEqual(900000000, ans)
        ans = area(1337228)
        self.assertEqual(1337228 ** 2, ans)

    def test_area_wrong_answers(self):
        ans = area(-1)
        self.assertEqual(ValueError, ans)
        ans = area('239')
        self.assertEqual(TypeError, ans)
        ans = area(-0)
        self.assertEqual(0, ans)

    def test_perimeter_regular(self):
        ans = perimeter(5)
        self.assertEqual(20, ans)
        ans = perimeter(30)
        self.assertEqual(120, ans)
        ans = perimeter(100)
        self.assertEqual(400, ans)

    def test_perimeter_big_number(self):
        ans = perimeter(10 ** 5)
        self.assertEqual(400000, ans)
        ans = perimeter(20000)
        self.assertEqual(80000, ans)
        ans = perimeter(1337228)
        self.assertEqual(1337228 * 4, ans)

    def test_perimeter_wrong_answers(self):
        ans = perimeter(-1)
        self.assertEqual(ValueError, ans)
        ans = perimeter('239')
        self.assertEqual(TypeError, ans)
        ans = perimeter(-0)
        self.assertEqual(0, ans)

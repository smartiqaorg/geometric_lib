import unittest
from triangle import area
from triangle import perimeter

class TriangleTests(unittest.TestCase):
    def test_area_regular(self):
        ans = area(5, 7)
        self.assertEqual(17.5, ans)
        ans = area(30, 2)
        self.assertEqual(30, ans)
        ans = area(100, 1)
        self.assertEqual(50, ans)

    def test_area_big_number(self):
        ans = area(10 ** 5, 7 ** 7)
        self.assertEqual(41177150000.0, ans)
        ans = area(10000, 20000)
        self.assertEqual(100000000.0, ans)
        ans = area(1337228, 2281337)
        self.assertEqual(1525333856918.0, ans)

    def test_area_wrong_answers(self):
        ans = area(-1, 11)
        self.assertEqual(ValueError, ans)
        ans = area('239', 'moment')
        self.assertEqual(TypeError, ans)
        ans = area(-0, 0)
        self.assertEqual(0, ans)

    def test_perimeter_regular(self):
        ans = perimeter(5, 7, 9)
        self.assertEqual(21, ans)
        ans = perimeter(30, 2, 30)
        self.assertEqual(62, ans)
        ans = perimeter(100, 17, 89)
        self.assertEqual(206, ans)

    def test_perimeter_big_number(self):
        ans = perimeter(10 ** 5, 7 ** 7, 3 ** 3)
        self.assertEqual(923570, ans)
        ans = perimeter(10000, 20000, 40000)
        self.assertEqual(70000, ans)
        ans = perimeter(1337228, 2281337, 20232320)
        self.assertEqual(23850885, ans)

    def test_perimeter_wrong_answers(self):
        ans = perimeter(-1, 11, 17)
        self.assertEqual(ValueError, ans)
        ans = perimeter('239', 'moment', [1337, 228])
        self.assertEqual(TypeError, ans)
        ans = perimeter(-0, 0, 00)
        self.assertEqual(0, ans)

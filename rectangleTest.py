import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTests(unittest.TestCase):
    def test_area_regular(self):
        ans = area(5, 7)
        self.assertEqual(35, ans)
        ans = area(30, 2)
        self.assertEqual(60, ans)
        ans = area(100, 1)
        self.assertEqual(100, ans)

    def test_area_big_number(self):
        ans = area(10 ** 5, 7 ** 7)
        self.assertEqual(823_543_000_00, ans)
        ans = area(10000, 20000)
        self.assertEqual(200000000, ans)
        ans = area(1337228, 2281337)
        self.assertEqual(3050667713836, ans)

    def test_area_wrong_answers(self):
        ans = area(-1, 11)
        self.assertEqual(ValueError, ans)
        ans = area('239', 'moment')
        self.assertEqual(TypeError, ans)
        ans = area(-0, 0)
        self.assertEqual(0, ans)

    def test_perimeter_regular(self):
        ans = perimeter(5, 7)
        self.assertEqual(24, ans)
        ans = perimeter(30, 2)
        self.assertEqual(64, ans)
        ans = perimeter(100, 1)
        self.assertEqual(202, ans)

    def test_perimeter_big_number(self):
        ans = perimeter(10 ** 5, 7 ** 7)
        self.assertEqual(1847086, ans)
        ans = perimeter(10000, 20000)
        self.assertEqual(60000, ans)
        ans = perimeter(1337228, 2281337)
        self.assertEqual(7237130, ans)

    def test_perimeter_wrong_answers(self):
        ans = perimeter(-1, 11)
        self.assertEqual(ValueError, ans)
        ans = perimeter('239', 'moment')
        self.assertEqual(TypeError, ans)
        ans = perimeter(-0, 0)
        self.assertEqual(0, ans)

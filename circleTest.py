import unittest
import math
from circle import area
from circle import perimeter

class CircleTests(unittest.TestCase):
    def test_area_regular(self):
        ans = area(5)
        self.assertEqual(math.pi * 25, ans )
        ans = area(3)
        self.assertEqual(math.pi * 9, ans)
        ans = area(100)
        self.assertEqual(math.pi * 10000, ans)

    def test_area_big_numbers(self):
        ans = area(10 ** 9)
        self.assertEqual(math.pi * (10 ** 18), ans)
        ans = area(10 ** 24)
        self.assertEqual(math.pi * (10 ** 48), ans)
        ans = area(10 ** 12)
        self.assertEqual(math.pi * (10 ** 24), ans)

    def test_area_wrong_answers(self):
        ans = area(-2)
        self.assertEqual(ValueError, ans)
        ans = area('100')
        self.assertEqual(TypeError, ans)
        ans = area(-0)
        self.assertEqual(0, ans)

    def test_perimeter_regular(self):
        ans = perimeter(5)
        self.assertEqual(10 * math.pi, ans)
        ans = perimeter(95)
        self.assertEqual(190 * math.pi, ans)
        ans = perimeter(228)
        self.assertEqual(456 * math.pi, ans)

    def test_perimeter_big_numbers(self):
        ans = perimeter(10 ** 9)
        self.assertEqual(2 * 10 ** 9 * math.pi, ans)
        ans = perimeter(100000000000000000)
        self.assertEqual(200000000000000000 * math.pi, ans)
        ans = perimeter(10 ** 24)
        self.assertEqual(10 ** 24 * 2 * math.pi, ans)

    def test_perimeter_wrong_answers(self):
        ans = perimeter(-1)
        self.assertEqual(ValueError, ans)
        ans = perimeter('-17')
        self.assertEqual(TypeError, ans)
        ans = perimeter(-0)
        self.assertEqual(0, ans)

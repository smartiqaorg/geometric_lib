import unittest as t
from triangle import area
from triangle import perimeter


class TriangleTestCase(t.TestCase):
    def test_positive_mul_positive(self):
        res = area(3, 2)
        self.assertEqual(res, 3)

    def test_negative_mul_negative(self):
        with self.assertRaises(ValueError):
            area(-1, -1)

    def test_float_mul_x(self):
        res = area(1.75, 4)
        self.assertEqual(res, 3.5)

    def test_posx3_error(self):
        with self.assertRaises(ValueError):
            perimeter(2, 3, 4)

    def test_triple_one(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(12, 15, -19)


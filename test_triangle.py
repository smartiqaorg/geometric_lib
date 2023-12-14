import unittest as t
from triangle import area
from triangle import perimeter


class TriangleTestCase(t.TestCase):
    def test_positive_mul_positive(self):
        res = area(3, 2)
        self.assertEqual(res, 3)

    def test_negative_mul_negative(self):
        res = area(-1, -1)
        self.assertEqual(res, 0.5)

    def test_negative_mul_negative_error(self):
        with self.assertEqual(ValueError):
            area(-1, -1)

    def test_float_mul_x(self):
        res = area(1.75, 4)
        self.assertEqual(res, 3.5)

    def test_posx3(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_posx3_error(self):
        with self.assertEqual(ValueError):
            area(2, 3, 4)

    def test_negative_mul_negative_error(self):
        with self.assertEqual(ValueError):
            area(-1, -1)

    def test_triple_one(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_negative_perimeter(self):
        res = perimeter(12, 15, -19)
        self.assertEqual(res, 8)

    def test_negative_perimeter_error(self):
        with self.assertEqual(ValueError):
            area(12, 15, -19)


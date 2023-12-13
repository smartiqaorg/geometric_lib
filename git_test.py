import unittest
import circle
import rectangle
import triangle
import square
import math

class RectangleTestCase(unittest.TestCase):
    def testa_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def testa_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    def testp_zero_nul(self):
        res = rectangle.perimeter(0, 10)
        self.assertEqual(res, 20)

class CircleTestCase (unittest.TestCase):
    def testa_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def testa_pi_mul (self):
        res = circle.area(math.pi)
        self.assertEqual(res, math.pi**3)

    def testp_zero_mul(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def testp_pi_mul(self):
        res = circle.perimeter(math.pi)
        self.assertEqual(res, 2*math.pi**2)

class TriangleTestCase(unittest.TestCase):
    def testa_zero1_mul(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def testa_zero2_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def testa_standart_mul(self):
        res = triangle.area(10 ,10)
        self.assertEqual(res, 50)

    def testp_zero1_mul(self):
        res = triangle.perimeter(0, 10, 10)
        self.assertEqual(res, 20)

    def testp_zero2_mul(self):
        res = triangle.perimeter(10, 0, 10)
        self.assertEqual(res, 20)

    def testp_zero3_mul(self):
        res = triangle.perimeter(10, 10, 0)
        self.assertEqual(res, 20)

    def testp_standart_mul(self):
        res = triangle.perimeter(10, 10, 10)
        self.assertEqual(res, 30)

class SquareTestCase(unittest.TestCase):
    def testa_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def testa_standert_mul(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def testp_zero_mul(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def testp_standart_mul(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)


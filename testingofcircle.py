import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_standart_input_circle_area(self):
        value = area(2)
        self.assertEqual(value, 4 * math.pi)

    def test_standart_input_circle_perimeter(self):
        value = perimeter(2)
        self.assertEqual(value, 4 * math.pi)


    def test_standart_input_circle_area(self):
        value = area(404)
        self.assertEqual(value, 404 * 404 * math.pi)

    def test_standart_input_circle_perimeter(self):
        value = perimeter(404)
        self.assertEqual(value, 808 * math.pi)


    def test_zero_input_circle_area(self):
        value = area(0)
        self.assertEqual(value, 0)

    def test_zero_input_circle_perimeter(self):
        value = perimeter(0)
        self.assertEqual(value, 0)

        
    def test_negative_input_circle_area(self):
        try:
            value = area(-404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")

    def test_negative_input_circle_perimeter(self):
        try:
            value = perimeter(-404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")


    def test_string_input_circle_area(self):
        try:
            value = area('hello')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: string value")

    def test_string_input_circle_perimeter(self):
        try:
            value = perimeter('hello')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrcet input: string value")


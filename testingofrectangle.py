import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_standart_input_rectangle_area(self):
        value = area(2, 7)
        self.assertEqual(value, 14)

    def test_standart_input_rectangle_perimeter(self):
        value = perimeter(2, 7)
        self.assertEqual(value, 18)


    def test_standart_input_rectangle_area(self):
        value = area(404, 100)
        self.assertEqual(value, 40400)

    def test_standart_input_rectangle_perimeter(self):
        value = perimeter(404, 100)
        self.assertEqual(value, 1008)


    def test_zero_input_rectangle_area(self):
        value = area(0, 0)
        self.assertEqual(value, 0)

    def test_zero_input_rectangle_perimeter(self):
        value = perimeter(0, 0)
        self.assertEqual(value, 0)

        
    def test_negative_input_rectangle_area(self):
        try:
            value = area(-404, 404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")

    def test_negative_input_rectangle_perimeter(self):
        try:
            value = perimeter(-404, 404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")


    def test_string_input_rectangle_area(self):
        try:
            value = area('hello', 'world')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: string value")

    def test_string_input_rectangle_perimeter(self):
        try:
            value = perimeter('hello', 'world')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrcet input: string value")

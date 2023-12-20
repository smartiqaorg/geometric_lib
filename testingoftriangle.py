import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_standart_input_triangle_area(self):
        value = area(3, 6)
        self.assertEqual(value, 9)

    def test_standart_input_triangle_perimeter(self):
        value = perimeter(3, 4, 5)
        self.assertEqual(value, 12)


    def test_standart_input_triangle_area(self):
        value = area(404, 100)
        self.assertEqual(value, 20200)

    def test_standart_input_triangle_perimeter(self):
        value = perimeter(404, 100, 505)
        self.assertEqual(value, 1009)


    def test_zero_input_triangle_area(self):
        value = area(0, 4)
        self.assertEqual(value, 0)

    def test_zero_input_triangle_perimeter(self):
        value = perimeter(0, 0, 0)
        self.assertEqual(value, 0)

        
    def test_negative_input_triangle_area(self):
        try:
            value = area(-404, 5)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")

    def test_negative_input_triangle_perimeter(self):
        try:
            value = perimeter(-404, 3, 100)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")


    def test_string_input_triangle_area(self):
        try:
            value = area('hello', 'world')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: string value")

    def test_string_input_triangle_perimeter(self):
        try:
            value = perimeter('hello', 'world', '!!!')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrcet input: string value")

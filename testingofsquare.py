import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_standart_input_square_area(self):
        value = area(5)
        self.assertEqual(value, 25)

    def test_standart_input_square_perimeter(self):
        value = perimeter(5)
        self.assertEqual(value, 20)


    def test_standart_input_square_area(self):
        value = area(100)
        self.assertEqual(value, 10000)

    def test_standart_input_square_perimeter(self):
        value = perimeter(100)
        self.assertEqual(value, 400)


    def test_zero_input_square_area(self):
        value = area(0)
        self.assertEqual(value, 0)

    def test_zero_input_square_perimeter(self):
        value = perimeter(0)
        self.assertEqual(value, 0)

        
    def test_negative_input_square_area(self):
        try:
            value = area(-404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")

    def test_negative_input_square_perimeter(self):
        try:
            value = perimeter(-404)
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: negative value")


    def test_string_input_square_area(self):
        try:
            value = area('hello')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrect input: string value")

    def test_string_input_square_perimeter(self):
        try:
            value = perimeter('hello')
        except Exception as e:
            value = e.__class__
        self.assertEqual(value, TypeError, "Incorrcet input: string value")

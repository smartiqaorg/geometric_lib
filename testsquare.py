import unittest
from square import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_square_area(self):
        data = area(10)
        self.assertEqual(data , 100)

    def test_zero_square_area(self):
        data = area(0)
        self.assertEqual(data , 0)

    def test_string_square_area(self):
        try:
            data = area('2')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : string")

    def test_negative_square_area(self):
        try:
            data = area(-7)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Incorrcet input : negative")

    def test_string_and_int_square_area(self):
        with self.assertRaises(TypeError):
            area("10", 2)

    def test_not_all_elem_square_area(self):
        with self.assertRaises(TypeError):
            area()

    def test_normaly_square_perimeter(self):
        data = perimeter(10)
        self.assertEqual(data , 40)

    def test_zero_square_perimeter(self):
        data = perimeter(0)
        self.assertEqual(data , 0)

    def test_string_square_perimeter(self):
        try:
            data = perimeter('2')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : string")

    def test_negative_square_perimeter(self):
        try:
            data = perimeter(-7)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Incorrcet input : negative")

    def test_string_and_int_square_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("10", 2)

    def test_not_all_elem_square_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter()



import unittest
from rectangle import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_rectangle_area(self):
        data = area(10 , 5)
        self.assertEqual(data , 50)

    def test_zero_rectangle_area(self):
        data = area(0 , 20)
        self.assertEqual(data , 0)

    def test_string_rectangle_area(self):
        try:
            data = area('10' , "2")
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : string")

    def test_negative_rectangle_area(self):
        try:
            data = area(-10 , 2)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : negative")

    def test_string_and_int_rectangle_area(self):
        try:
            data = area("10" , 2)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : cannot calculate string and int")

    def test_not_all_elem_rectangle_area(self):
        try:
            data = area(5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : not all elements")




    def test_normaly_rectangle_perimeter(self):
        data = perimeter(10 , 2)
        self.assertEqual(data , 24)

    def test_zero_rectangle_perimeter(self):
        data = perimeter(0 , 0)
        self.assertEqual(data , 0)

    def test_string_rectangle_perimeter(self):
        try:
            data = perimeter('10', '2')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Incorrcet input : string")

    def test_negative_rectangle_perimeter(self):
        try:
            data = perimeter(-10, 2)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Incorrcet input : negative")

    def test_string_and_int_rectangle_perimeter(self):
        try:
            data = perimeter("10" , 2)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : cannot calculate string and int")

    def test_not_all_elem_rectangle_perimeter(self):
        try:
            data = perimeter(5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : not all elements")





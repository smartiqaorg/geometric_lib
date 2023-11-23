
import unittest
import circle, rectangle, square, triangle

class RectangleTestCase(unittest.TestCase):
    '''
    The class performs testing function from 'rectangle.py'.
    It contains functions that test the function of finding the perimeter and area.
    There are 3 tests for each function.
    '''

    def test_rectangle_area_1(self):
        res = rectangle.area(0, 244)
        self.assertEqual(res, 0)

    def test_rectangle_area_2(self):
        with self.assertRaises(ValueError) as context:
            rectangle.area(-6, 2355)

        expected_error_message = 'ERROR: Wrong format in input data.'
        self.assertIn(expected_error_message, str(context.exception))

    def test_rectangle_area_3(self):
        res = rectangle.area(31, 23)
        self.assertEqual(res, 713)

    def test_rectangles_perimeter_1(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_rectangles_perimeter_2(self):
        res = rectangle.perimeter(13, 244)
        self.assertEqual(res, 514)

    def test_rectangles_perimeter_3(self):
        res = rectangle.perimeter(31, 23)
        self.assertEqual(res, 108)


class SquareTestCase(unittest.TestCase):
    '''
    The class performs testing function from 'square.py'.
    It contains functions that test the function of finding the perimeter and area.
    There are 3 tests for each function.
    '''

    def test_squares_area_1(self):
        res = square.area(13)
        self.assertEqual(res, 169)

    def test_squares_area_2(self):
        res = square.area(100.5)
        self.assertEqual(res, 10100.25)

    def test_squares_area_3(self):
        res = square.area(31)
        self.assertEqual(res, 961)

    def test_squares_perimeter_1(self):
        with self.assertRaises(ValueError) as context:
            square.perimeter(-13)
        expected_error_message = 'ERROR: Wrong format in input data.'
        self.assertIn(expected_error_message, str(context.exception))

    def test_squares_perimeter_2(self):
        res = square.perimeter(31)
        self.assertEqual(res, 124)

    def test_squares_perimeter_3(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)

class TriangleTestCase(unittest.TestCase):
    '''
    The class performs testing function from 'triangle.py'.
    It contains functions that test the function of finding the perimeter and area.
    There are 3 tests for each function.
    '''

    def test_triangles_area_1(self):
        with self.assertRaises(ValueError) as context:
            triangle.area(-100, -50)
        expected_error_message = 'ERROR: Wrong format in input data.'
        self.assertIn(expected_error_message, str(context.exception))


    def test_triangles_area_2(self):
        res = triangle.area(3, 14)
        self.assertEqual(res, 21)

    def test_triangles_area_3(self):
        res = triangle.area(45, 5)
        self.assertEqual(res, 112.5)

    def test_triangles_perimeter_1(self):
        with self.assertRaises(ValueError) as context:
            triangle.perimeter(100, 1, 1)
        expected_error_message = 'ERROR: Wrong format in input data.'
        self.assertIn(expected_error_message, str(context.exception))

    def test_triangles_perimeter_2(self):
        res = triangle.perimeter(23, 24, 14)
        self.assertEqual(res, 61)

    def test_triangles_perimeter_3(self):
        res = triangle.perimeter(45, 45, 4)
        self.assertEqual(res, 94)

class CircleTestCase(unittest.TestCase):
    '''
    The class performs testing function from 'circle.py'.
    It contains functions that test the function of finding the perimeter and area.
    There are 3 tests for each function.
    '''

    def test_circles_area_1(self):
        res = circle.area(50)
        self.assertEqual(res, 7853.981633974483)

    def test_circles_area_2(self):
        with self.assertRaises(ValueError) as context:
            circle.area(-2)
        expected_error_message = 'ERROR: Wrong format in input data.'
        self.assertIn(expected_error_message, str(context.exception))

    def test_circles_area_3(self):
        res = circle.area(44)
        self.assertEqual(res, 6082.123377349839)

    def test_circles_perimeter_1(self):
        res = circle.perimeter(50)
        self.assertEqual(res, 314.1592653589793)

    def test_circles_perimeter_2(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_circles_perimeter_3(self):
        res = circle.perimeter(4)
        self.assertEqual(res, 25.132741228718345)


import unittest
import square
import circle
import rectangle
import triangle
import math

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        radius = 0
        with self.assertRaises(ValueError):
            result = circle.area(radius)

    def test_area_negative(self):
        radius = -2
        with self.assertRaises(ValueError):
            result = circle.area(radius)
    
    def test_area_positive(self):
        radius = 1
        expectedResult = 3.1415
        result = circle.area(radius)
        self.assertEqual(expectedResult, result)


    def test_perimeter_zero(self):
        radius = 0
        with self.assertRaises(ValueError):
            result = circle.perimeter(radius)

    def test_perimeter_negative(self):
        radius = -2
        with self.assertRaises(ValueError):
            result = circle.perimeter(radius)

    def test_perimeter_positive(self):
        radius = 2
        expectedResult = 12.566
        result = circle.perimeter(radius)
        self.assertEqual(expectedResult, result)



class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        a = 0
        with self.assertRaises(ValueError):
            result = square.area(a)

    def test_area_negative(self):
        a = -2
        with self.assertRaises(ValueError):
            result = square.area(a)
    
    def test_area_positive(self):
        a = 5
        expectedResult = 25
        result = square.area(a)
        self.assertEqual(expectedResult, result)


    def test_perimeter_zero(self):
        a = 0
        with self.assertRaises(ValueError):
            result = square.perimeter(a)

    def test_perimeter_negative(self):
        a = -2
        with self.assertRaises(ValueError):
            result = square.perimeter(a)

    def test_perimeter_positive(self):
        a = 6
        expectedResult = 24
        result = square.perimeter(a)
        self.assertEqual(expectedResult, result)




class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        a = 0
        b = 5
        with self.assertRaises(ValueError):
            result = rectangle.area(a, b)

    def test_area_negative(self):
        a = -2
        b = -4
        with self.assertRaises(ValueError):
            result = rectangle.area(a, b)
    
    def test_area_positive(self):
        a = 5
        b = 1
        expectedResult = 5
        result = rectangle.area(a, b)
        self.assertEqual(expectedResult, result)


    def test_perimeter_zero(self):
        a = 0
        b = 5
        with self.assertRaises(ValueError):
            result = rectangle.perimeter(a, b)

    def test_perimeter_negative(self):
        a = -2
        b = 3
        with self.assertRaises(ValueError):
            result = rectangle.perimeter(a, b)

    def test_perimeter_positive(self):
        a = 6
        b = 4
        expectedResult = 20
        result = rectangle.perimeter(a, b)
        self.assertEqual(expectedResult, result)



class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        s = 0
        h = 5
        with self.assertRaises(ValueError):
            result = triangle.area(s, h)

    def test_area_negative(self):
        s = 22
        h = -4
        with self.assertRaises(ValueError):
            result = triangle.area(s, h)
    
    def test_area_positive(self):
        s = 5
        h = 10
        expectedResult = 25
        result = triangle.area(s, h)
        self.assertEqual(expectedResult, result)


    def test_perimeter_zero(self):
        a = 0
        b = 5
        c = 4
        with self.assertRaises(ValueError):
            result = triangle.perimeter(a, b, c)

    def test_perimeter_negative(self):
        a = -2
        b = 3
        c = -2
        with self.assertRaises(ValueError):
            result = triangle.perimeter(a, b, c)

    def test_perimeter_positive(self):
        a = 6
        b = 4
        c = 5
        expectedResult = 15
        result = triangle.perimeter(a, b, c)
        self.assertEqual(expectedResult, result)
    
    def test_perimeter_impossibleTriangle(self):
        a = 6
        b = 2
        c = 3
        with self.assertRaises(ValueError):
            result = triangle.perimeter(a, b, c)
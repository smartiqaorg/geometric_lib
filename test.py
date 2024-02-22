import unittest
import rectangle, circle, square, triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0,0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = rectangle.area(10,10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0,0)
        self.assertEqual(res, 0)

    def test_zero_one_perimeter(self):
        res = rectangle.perimeter(0,1)
        self.assertEqual(res, 2)

    def test_square_perimeter(self):
        res = rectangle.perimeter(10,10)
        self.assertEqual(res, 40)
    def test_minus_perimeter(self):
        self.assertRaises(ValueError, rectangle.perimeter, -2, 2)
    def test_simbol_perimeter(self):
        self.assertRaises(ValueError, rectangle.perimeter, "w", 2)
    def test_minus_area(self):
        self.assertRaises(ValueError, rectangle.area, -2, 2)
    def test_simbol_area(self):
        self.assertRaises(ValueError, rectangle.area, "w", 2)


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = circle.area(153)
        self.assertEqual(res, 73541.54242788347)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = circle.perimeter(153)
        self.assertEqual(res, 961.3273519984767)
    def test_minus_perimeter(self):
        self.assertRaises(ValueError, circle.perimeter, -2, 2)
    def test_simbol_perimeter(self):
        self.assertRaises(ValueError, circle.perimeter, "w", 2)
    def test_minus_area(self):
        self.assertRaises(ValueError, circle.area, -2, 2)
    def test_simbol_area(self):
        self.assertRaises(ValueError, circle.area, "w", 2)


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = square.area(153)
        self.assertEqual(res, 23409)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = square.perimeter(153)
        self.assertEqual(res, 612)
    def test_minus_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, -2)
    def test_simbol_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, "w")
    def test_minus_area(self):
        self.assertRaises(ValueError, square.area, -2)
    def test_simbol_area(self):
        self.assertRaises(ValueError, square.area, "w") 


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_height_zero_area(self):
        res = triangle.area(153, 0)
        self.assertEqual(res, 0)

    def test_side_zero_area(self):
        res = triangle.area(0, 153)
        self.assertEqual(res, 0)

    def test_area(self):
        res = triangle.area(153, 93)
        self.assertEqual(res, 7114.5)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0,0,0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = triangle.perimeter(153, 153, 153)
        self.assertEqual(res, 459)
    def test_minus_perimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, -2, 2, 2)
    def test_simbol_perimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, "w", 2, 2)
    def test_minus_area(self):
        self.assertRaises(ValueError, triangle.area, -2, 2)
    def test_simbol_area(self):
        self.assertRaises(ValueError, triangle.area, "w", 2)

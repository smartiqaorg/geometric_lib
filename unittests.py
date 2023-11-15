import unittest
import circle
import rectangle
import square
import triangle

class RectangletestsCase(unittest.TestCase):
    def test_rectangle_area(self):
        res = rectangle.area(6,0) # zero
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(1, 2)  # integers
        self.assertEqual(res, 2)
        res = rectangle.area(3, "q")  # string
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(-2, 3)  # negative integer
        self.assertEqual(res, "Invalid input")


    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(9, 0)  # zero
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(1, 3)  # integers
        self.assertEqual(res, 4)
        res = rectangle.perimeter(3, "q")  # string
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(-2, 3)  # negative integer
        self.assertEqual(res, "Invalid input")


class TriangletestsCase(unittest.TestCase):
    def test_triangle_area(self):
        res = triangle.area(9, 0)  # zero
        self.assertEqual(res, "Invalid input")
        res = triangle.area(2, 1)  # integers
        self.assertEqual(res, 1)
        res = triangle.area(2, "q")  # string
        self.assertEqual(res, "Invalid input")
        res = triangle.area(2, -1)  # negative integer
        self.assertEqual(res, "Invalid input")


    def test_triangle_perimetr(self):
        res = triangle.perimetr(1, 0, 3)  # zero
        self.assertEqual(res, "Invalid input")
        res = triangle.perimetr(2, 1,3)  # integers
        self.assertEqual(res, 6)
        res = triangle.perimetr(2, "q", 3)  # string
        self.assertEqual(res, "Invalid input")
        res = triangle.perimetr(2, -1, 4)  # negative integer
        self.assertEqual(res, "Invalid input")


class SquaretestsCase(unittest.TestCase):
    def test_square_area(self):
        res = square.area(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = square.area(2)  # integers
        self.assertEqual(res, 4)
        res = square.area("q")  # string
        self.assertEqual(res, "Invalid input")
        res = square.area(-1)  # negative integer
        self.assertEqual(res, "Invalid input")


    def test_square_perimeter(self):
        res = square.perimeter(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(2)  # integers
        self.assertEqual(res, 8)
        res = square.perimeter("q")  # string
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(-1)  # negative integer
        self.assertEqual(res, "Invalid input")


class CircletestsCase(unittest.TestCase):
    def test_circle_area(self):
        res = circle.area(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = circle.area(2)  # integers
        self.assertEqual(res, 12.56)
        res = circle.area("q")  # string
        self.assertEqual(res, "Invalid input")
        res = circle.area(-1)  # negative integer
        self.assertEqual(res, "Invalid input")


    def test_circle_perimeter(self):
        res = circle.perimeter(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(2)  # integers
        self.assertEqual(res, 12.56)
        res = circle.perimeter("q")  # string
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(-1)  # negative integer
        self.assertEqual(res, "Invalid input")


if __name__ == '__main__':
    unittest.main()
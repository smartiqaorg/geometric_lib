import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337, 228)
        self.assertEqual(res, 152418)

    def test_zero_perimeter_case(self):
        res = perimeter(0, 10, 10)
        self.assertEqual(res, 20)
        res = perimeter(10, 0, 10)
        self.assertEqual(res, 20)
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 20)
        res = perimeter(0, 0, 10)
        self.assertEqual(res, 10)
        res = perimeter(0, 10, 0)
        self.assertEqual(res, 10)
        res = perimeter(10, 0, 0)
        self.assertEqual(res, 10)

    def test_general_perimeter_case(self):
        res = perimeter(1337, 228, 131)
        self.assertEqual(res, 1696)


def area(a, h):
<<<<<<< Updated upstream
=======
    """
    Возвращает площадь треугольника с передаваемыми высотой и основанием.

                Параметры:
                        a (float): основание треугольника
                        h (float): высота треугольника

                Возвращаемое значение:
                        a * h / 2 (float): площадь треугольника
    """
>>>>>>> Stashed changes
    return a * h / 2


def perimeter(a, b, c):
<<<<<<< Updated upstream
    return a + b + c
=======
    """
    Возвращает периметр треугольника с передаваемыми сторонами.

                Параметры:
                        a (float): первая сторона треугольника
                        b (float): вторая сторона треугольника
                        c (float): третья сторона треугольника

                Возвращаемое значение:
                        a + b + c (float): периметр треугольника
        """
    return a + b + c
>>>>>>> Stashed changes

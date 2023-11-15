import unittest
import circle
import rectangle
import square
import trinagle

'''
    За основу берем цифру, равную трем
       (С трех удобней всего начинать),
    Приплюсуем сперва восемьсот сорок два
         И умножим на семьдесят пять.

    Разделив результат на шестьсот пятьдесят
        (Ничего в этом трудного нет),
     Вычтем сто без пяти и получим почти
        Безошибочно точный ответ.

    Суть же метода, мной примененного тут,
       Объяснить я подробней готов,
     Если есть у вас пара свободных минут
        И хотя бы крупица мозгов.'''


class CircleTest(unittest.TestCase):
    def test_area_some_values(self):
        self.assertEqual(circle.area(10), 314.1592653589793)
        self.assertEqual(circle.area(1), 3.141592653589793)
        self.assertAlmostEquals(circle.perimeter(11), 2 * circle.math.pi * 11)
        self.assertAlmostEquals(circle.area(1e10), 3.1415926535897933e+20)
        self.assertEquals(circle.perimeter(1), circle.math.pi * 2 * 1)
        self.assertEquals(circle.perimeter(6), circle.math.pi * 2 * 6)

    def test_area_negative_numbers(self):
        self.assertRaises(Exception, circle.area(-1), -1)
        self.assertRaises(Exception, circle.area(-10), -10)
        self.assertRaises(Exception, circle.area(-2), -2)

    def test_per_overcome_values(self):
        self.assertAlmostEquals(circle.perimeter(1e10), 2 * 1e10 * circle.math.pi)
        self.assertAlmostEquals(circle.perimeter(1e16), 2 * 1e16 * circle.math.pi)
        self.assertAlmostEquals(circle.perimeter(1e18), 2 * 1e18 * circle.math.pi)
        self.assertAlmostEquals(circle.perimeter(1e19), 2 * 1e19 * circle.math.pi)


class RectangleTest(unittest.TestCase):
    def test_area_some_values(self):
        self.assertEqual(rectangle.area(2, 4), 2 * 4)
        self.assertEqual(rectangle.area(1, 4), 4 * 1)
        self.assertEqual(rectangle.area(3.1, 4), 3.1 * 4)

        self.assertEqual(rectangle.perimeter(2, 4), 2 * (2 + 4))
        self.assertEqual(rectangle.perimeter(1, 4), 2 * (1 + 4))
        self.assertEqual(rectangle.perimeter(17, 42), 2 * (17 + 42))

    def test_area_zero_values(self):
        self.assertRaises(Exception, rectangle.area(2, 0), 0)
        self.assertRaises(Exception, rectangle.area(0, 4), 0)
        self.assertRaises(Exception, rectangle.area(-1, 0), 0)

        self.assertRaises(Exception, rectangle.perimeter(-2, 24), 0)
        self.assertRaises(Exception, rectangle.perimeter(6, -4), 0)
        self.assertRaises(Exception, rectangle.perimeter(-1, 5), 0)

    def test_area_overcome_values(self):
        self.assertEqual(rectangle.area(1e10, 1e5), 1e15)
        self.assertEqual(rectangle.area(1921378, 4), 4 * 1921378)
        self.assertEqual(rectangle.area(3.19324786, 7298437), 3.19324786 * 7298437)

        self.assertEqual(rectangle.perimeter(1e10, 1e5), 2 * (1e10 + 1e5))
        self.assertEqual(rectangle.perimeter(1921378, 4), 2 * (4 + 1921378))
        self.assertEqual(rectangle.perimeter(3.19324786, 7298437), 2 * (3.19324786 + 7298437))


class SqareTest(unittest.TestCase):
    def test_area_some_values(self):
        self.assertEqual(square.area(1), 1 * 1)
        self.assertEqual(square.area(3.1), 3.1 * 3.1)
        self.assertEqual(square.area(4), 4 * 4)

        self.assertEqual(square.perimeter(10), 4 * 10)
        self.assertEqual(square.perimeter(1123), 4 * 1123)
        self.assertEqual(square.perimeter(73), 4 * 73)
        self.assertEqual(square.perimeter(1), 4 * 1)

    def test_area_zero_values(self):
        self.assertRaises(Exception, square.area(41 - 41), 0)
        self.assertRaises(Exception, square.area(0), 0)

    def test_area_overcome_values(self):
        self.assertEqual(square.area(1e8), 1e8 * 1e8)
        self.assertEqual(square.area(3.19187236), 3.19187236 * 3.19187236)
        self.assertEqual(square.area(4e24), 4e24 * 4e24)

        self.assertEqual(square.perimeter(129137761063), 4 * 129137761063)
        self.assertEqual(square.perimeter(110129837423), 4 * 110129837423)
        self.assertEqual(square.perimeter(73e3), 4 * 73e3)


class TrinagleTest(unittest.TestCase):
    def test_area_some_values(self):
        self.assertEqual(trinagle.area(1, 1), 1 * 1 / 2)
        self.assertEqual(trinagle.area(3.1, 5.2), (5.2 * 3.1) / 2)
        self.assertEqual(trinagle.area(4, 2), 4)

        self.assertEqual(trinagle.perimeter(3, 4, 5), 3 + 4 + 5)
        self.assertEqual(trinagle.perimeter(11, 12, 5), 11 + 12 + 5)
        self.assertEqual(trinagle.perimeter(73, 74, 75), 73 + 74 + 75)

    def test_area_zero_values(self):
        self.assertRaises(Exception, trinagle.area(41, 0), 0)
        self.assertRaises(Exception, trinagle.area(0, 24), 0)
        self.assertRaises(Exception, trinagle.area(41, 0), 0)
        self.assertRaises(Exception, trinagle.area(41, 0), 0)
        self.assertRaises(Exception, trinagle.area(0, 0), 0)

    def test_area_overcome_values(self):
        self.assertEqual(trinagle.area(1e8, 192750371), (1e8 * 192750371) / 2)
        self.assertEqual(trinagle.area(3.19187236, 78348), (3.19187236 * 78348) / 2)
        self.assertEqual(trinagle.area(4e24, 253), (4e24 * 253) / 2)

        self.assertEqual(trinagle.perimeter(129137761063, 12710723198273, 21987361036),
                         12710723198273 + 21987361036 + 129137761063)
        self.assertEqual(trinagle.perimeter(110129837423, 1, 2), 110129837423 + 1 + 2)
        self.assertEqual(trinagle.perimeter(73e3, 4, 3), 4 + 3 + 73e3)


if __name__ == '__main__':
    unittest.main()

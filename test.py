import unittest
import rectangle, circle, square, triangle

class RectangleTestCase(unittest.TestCase):
    '''
    тесты для поиска периметра и площади rectangle
    '''
    def test_zero_area(self):
        '''
        проверка на нулевые стороны
        '''
        res = rectangle.area(0,0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_square_area(self):
        '''
        тест если он квадрат
        '''
        res = rectangle.area(10,10)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        '''
        тест если a и b нули
        '''
        res = rectangle.perimeter(0,0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_zero_one_perimeter(self):
        '''
        тест где одна сторона 0 другая 1
        '''
        res = rectangle.perimeter(0,1)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 2)

    def test_square_perimeter(self):
        '''
        тест на квадрат
        '''
        res = rectangle.perimeter(10,10)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 40)


class CircleTestCase(unittest.TestCase):
    '''
    тесты для поиска периметра и площади circle
    '''
    def test_zero_area(self):
        '''
        тест если нулевой радиус
        '''
        res = circle.area(0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        проверка округления
        '''
        res = circle.area(153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 73541.54242788347)

    def test_zero_perimeter(self):
        '''
        проверка на нулевой радиус
        '''
        res = circle.perimeter(0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_perimeter(self):
        '''
        проверка округления
        '''
        res = circle.perimeter(153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 961.3273519984767)


class SquareTestCase(unittest.TestCase):
    '''
    тесты для поиска периметра и площади square
    '''
    def test_zero_area(self):
        '''
        тест на 0
        '''
        res = square.area(0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        тест на правильность умножения
        '''
        res = square.area(153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 23409)

    def test_zero_perimeter(self):
        '''
        тест если 0
        '''
        res = square.perimeter(0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_perimeter(self):
        '''
        тест на правильность умножения функции
        '''
        res = square.perimeter(153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 612)


class TriangleTestCase(unittest.TestCase):
    '''
    тесты для поиска периметра и площади triangle
    '''
    def test_zero_area(self):
        '''
        тест если 0
        '''
        res = triangle.area(0, 0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_height_zero_area(self):
        '''
        тест если высота нулевая
        '''
        res = triangle.area(153, 0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_side_zero_area(self):
        '''
        тест если сторона нулевая
        '''
        res = triangle.area(0, 153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        проверка умножения и округления ф-ции
        '''
        res = triangle.area(153, 93)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 7114.5)

    def test_zero_perimeter(self):
        '''
        тест если все нули
        '''
        res = triangle.perimeter(0,0,0)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 0)

    def test_one_zero_perimeter(self):
        '''
        тест если 2 нуля
        '''
        res1 = triangle.perimeter(153,0,0)
        res2 = triangle.perimeter(0, 153, 0)
        res3 = triangle.perimeter(0, 0, 153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res1, 153)
        self.assertEqual(res2, 153)
        self.assertEqual(res3, 153)

    def test_perimeter(self):
        '''
        тест проверка на периметр
        '''
        res = triangle.perimeter(153, 153, 153)
        '''
        сравнение результата с подсчитанным в ручную ответом
        '''
        self.assertEqual(res, 459)
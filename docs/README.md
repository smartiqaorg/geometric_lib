# Документация проекта

## Файлы в geometric lib
1)Circle.py

    import math ''' импортировали библиотеку'''
    def area(r):
        ''' принимает число r, возвращает площадь окружности'''
        return math.pi * r * r 


    def perimeter(r):
        '''принимает число r , возвращает периметр'''
        return 2 * math.pi * r 

В данном коде используется библиотека math для вычисления площади и периметра окружности на основе радиуса r.

Функция area(r) принимает радиус r и возвращает площадь окружности, используя формулу math.pi * r * r.
Функция perimeter(r) также принимает радиус r и возвращает периметр окружности, используя формулу 2 * math.pi * r.
Эти функции позволяют вычислить площадь и периметр окружности на основе заданного радиуса и могут быть использованы для решения задач, связанных с окружностями.
    
Пример вызова:

Вычисление площади и периметра окружности с радиусом 5

    radius = 5
    circle_area = area(radius)
    circle_perimeter = perimeter(radius)

    print("Площадь окружности:", circle_area)
    print("Периметр окружности:", circle_perimeter)

2)Square.py

    def area(a):
        '''принимает число a , возвращает площадь квадрата'''
        return a * a


    def perimeter(a):
        '''принимает число a , возвращает периметр квадрата '''
        return 4 * a
    
Этот код содержит две функции для вычисления площади и периметра квадрата на основе длины его стороны a.
Функция area(a) принимает длину стороны квадрата a и возвращает его площадь, используя формулу a * a.
Функция perimeter(a) также принимает длину стороны a и возвращает периметр квадрата, используя формулу 4 * a.
Эти функции могут быть использованы для вычисления площади и периметра квадрата при заданной длине его стороны и помогут решать задачи, связанные с квадратами.
    
Пример вызова:

    side_length = 6
    square_area = area(side_length)
    square_perimeter = perimeter(side_length)

    print("Площадь квадрата:", square_area)
    print("Периметр квадрата:", square_perimeter)

3)Rectangle.py

    def area(a, b):
        '''принимает числа a и b, возвращает площадь прямоугольника '''
        return a * b


        def perimeter(a, b):
        '''принимает числа a и b , возвращает периметр прямоугольника'''
        return 2*(a + b)

Этот код содержит две функции для вычисления площади и периметра прямоугольника на основе его сторон a и b.
Функция area(a, b) принимает длины сторон прямоугольника a и b и возвращает его площадь, используя формулу a * b.
Функция perimeter(a, b) также принимает длины сторон a и b и возвращает периметр прямоугольника, используя формулу 2 * (a + b).
Эти функции позволяют вычислить площадь и периметр прямоугольника при заданных длинах его сторон и могут быть использованы для решения задач, связанных с прямоугольниками.
    
    
Пример вызова:

    length = 5  # Длина
    width = 3   # Ширина

    rectangle_area = area(length, width)
    rectangle_perimeter = perimeter(length, width)

    print("Площадь прямоугольника:", rectangle_area)
    print("Периметр прямоугольника:", rectangle_perimeter)

4)triangle.py

    def area(a, h):
        ''' принимает a и h , возвращает площадь треугольника'''
        return a * h / 2

    def perimeter(a, b, c):
        '''принимает a,b,c , возвращает периметр треугольника'''
        return a + b + c
Этот код содержит две функции для вычисления площади и периметра треугольника на основе его сторон и высоты.
Функция area(a, h) принимает длину основания треугольника a и его высоту h и возвращает площадь треугольника, используя формулу a * h / 2.
Функция perimeter(a, b, c) принимает длины всех трех сторон треугольника a, b и c и возвращает его периметр, используя формулу a + b + c.
Эти функции могут быть использованы для вычисления площади и периметра треугольника при заданных параметрах и помогут решать задачи, связанные с треугольниками.
    
Пример вызова:
Вычисление площади треугольника с основанием a = 6 и высотой h = 4:
    
    area_result = area(6, 4)
    print("Площадь треугольника:", area_result)
    

# История изменений проекта:
1)Добавление комментариев в triangle.py 

    ea3eacabdfd99b8eb60bf25590e4b6d5400b04cb  Style : add comments in triangle.
    
2)Добавление комментариев в rectangle.py 

    62cf1fcaf693d01aac7874fae895bda677961e68 Style : add comments in rectangle.py

3)Добавление комментариев в square.py

    43edeea0ea86515282f29736ad86c8b70e03b950 Style: add comments in square.py

4)Добавление комментариев в circle.py

    d68901e0688deb6e9f2ad29d065a48ed6ccda9cd Style:add new comment in circle.py

## Unit-tests
1)Тесты для rectangle.py
    
    import unittest
    from rectangle import area
    from rectangle import perimeter

    class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5, 2)
        self.assertEqual(res, 10)

    def test_2_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5, 2)
    
        self.assertEqual(str(context.exception), "Invalid value")

    def test_1_perimeter(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_2_perimeter(self):
        res = perimeter(2, 0)
        self.assertEqual(res, 4)

    if __name__ == '__main__':
        unittest.main()


2)Тесты для square.py

    import unittest
    from square import area
    from square import perimeter
    class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_2_area(self):
        res = area(2)
        self.assertEqual(res, 4)
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5)

        self.assertEqual(str(context.exception), "Invalid value")
    
    
    def test_4_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5.5)

        self.assertEqual(str(context.exception), "Invalid value")



    def test_1_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_2_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    if __name__ == '__main__':
        unittest.main()

3)Тесты для triangle.py

    import unittest
    from triangle import area
    from triangle import perimeter
    class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5,2)
        self.assertEqual(res, 5)

    def test_2_area(self):
        res = area(13,4)
        self.assertEqual(res, 26)
    
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-3, 4)
    
        self.assertEqual(str(context.exception), "Invalid value")

    def test_1_perimeter(self):
        res = perimeter(3,4,1)
        self.assertEqual(res, 8)

    def test_2_perimeter(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    if __name__ == '__main__':
        unittest.main()

4)Тесты для circle.py

    import unittest
    import math
    from circle import area
    from circle import perimeter
    class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5)
        self.assertEqual(res, math.pi * 25)

    def test_2_area(self):
        res = area(13)
        self.assertEqual(res, math.pi * 169)
    
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-13)
    
        self.assertEqual(str(context.exception), "Invalid value")

    def test_1_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, math.pi * 6)

    def test_2_perimeter(self):
        res = perimeter(30)
        self.assertEqual(res, math.pi * 60)

    if __name__ == '__main__':
        unittest.main()


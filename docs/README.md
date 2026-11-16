
# General solution
Implemented functions to find areas and perimeters of different geometric shapes using next math formulas
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions description

## Area

- Circle:

    Возвращает значение площади круга с заданным радиусом

    Параметры:

    r (float): радиус круга

    Возвращаемое значение:

    circle_area (float): площадь круга с радиусом r

    Пример вызова:

        `area(6.7)`

- Rectangle:

    Возвращает значение площади прямоугольника с заданными сторонами

    Параметры:

    a (float): первая сторона
    b (float): вторая сторона

    Возвращаемое значение:

    rectangle_area (float): площадь прямоугольника со сторонами a и b

    Пример вызова:

        `area(5.0, 3.0)`

- Square:

    Возвращает значение площади квадрата с заданной стороной

    Параметры:

    a (float): сторона квадрата

    Возвращаемое значение:

    square_area (float): площадь квадрата со стороной a

    Пример вызова:

        `area(4.0)`

- Triangle:

    Возвращает значение площади треугольника с заданной стороной и с заданной высотой

    Параметры:

    a (float): сторона треугольника
    h (float): высота треугольника

    Возвращаемое значение:

    triangle_area (float): высота треугольника со стороной a и высотой h

    Пример вызова:

        `area(6.0, 4.0)`
## Perimeter

- Circle:

    Возвращает значение длины окружности с заданным радиусом

    Параметры:

    r (float): радиус круга

    Возвращаемое значение:

    circle_perimeter (float): длина окружности с радиусом r

    Пример вызова:

        `perimeter(6.7)`

- Rectangle:

    Возвращает значение периметра прямоугольника с заданными сторонами

    Параметры:

    a (float): первая сторона
    b (float): вторая сторона

    Возвращаемое значение:

    rectangle_perimeter (float): периметр прямоугольника со сторонами a и b

    Пример вызова:

        `perimeter(5.0, 3.0)`

- Square:

    Возвращает значение периметра квадрата с заданной стороной

    Параметры:

    a (float): сторона квадрата

    Возвращаемое значение:

    square_perimeter (float): периметр квадрата со стороной a

    Пример вызова:

        `perimeter(4.0)`

- Triangle:

    Возвращает значение периметра треугольника с заданными сторонами

    Параметры:

    a (float): первая сторона
    b (float): вторая сторона
    c (float): третья сторона

    Возвращаемое значение:

    triangle_perimeter (float): периметр треугольника со сторонами a, b и c

    Пример вызова:

        `perimeter(3.0, 4.0, 5.0)`

# Commit history
- commit fa852e3a2e895a1d3289549d906852d9a134882a "made comments"
- commit 971677d9ee94b3721aa3ca4029723c12770e72a6 "added new file rectangle.py"
- commit fdaed39d53d9701e03594fbd8099eeeb05959cbc "created new file triangle.py and fixed perimeter function in rectangle.py"

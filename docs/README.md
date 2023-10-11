# Документация проекта
## Общее описание
В этом проекте представлены функции, вычисляющие периметр и площадь для геометрических фигур: треугольника, квадрата, прямоугольника и окружности.

## Треугольник

### Вычисление площади треугольника
Функция принимает два числа, значение a - сторона треугольника, h - высота треугольника.

Так как Python является языком с динамической типизацией данных, значение а и h могут быть типа ***int*** или ***float***, в зависимости от входных данных.

Функция возвращает площадь треугольника.
 
    def area(a, h):
        return a * h / 2

**Пример вызова:**

    def area(a, h): 
            return a * h / 2 


    print("Enter the side lengths and heights of the triangle")

    a, h = float(input()), float(input())

    print(area(a, h))

***input:***
    
    6.74
    8.5
***output:***

    28.645

### Вычисление периметра треугольника
Функция Принимает три числа, равные длинам сторон треугольника, а возвращает площадь треугольника.
 
    def perimeter(a, h):
        return a * h / 2

**Пример вызова:**

    def perimeter(a, b, c):
        return a + b + c 


    print("Enter the lengths of the sides of the triangle")

    a, b, c = int(input()), int(input()), int(input())

    print(perimeter(a, b, c))

***input:***
    
    3
    4
    5
***output:***

    12

## Квадрат
### Вычисление площади квадрата
Функция принимает одно значение, равное длинне стороны квадрата, возвращает площадь квадрата.

**Пример вызова:**

    def area(a): 
            return a * a


    print("Enter the length of the side of the square")

    a = float(input())

    print(area(a))

***input:***
    
    6

***output:***

    36

### Вычисление периметра квадрата
Функция принимает одно значение, равное длинне стороны квадрата, возвращает периметр квадрата.

**Пример вызова:**

    def perimeter(a): 
            return 4 * a


    print("Enter the length of the side of the square")

    a = float(input())

    print(perimeter(a))

***input:***
    
    6

***output:***

    24

## Прямоугольник

### Вычисление площади прямоугольника
Функция принимает два значения, равные двум сторонам прямоугольника, возвращает его площадь.

    def area(a, b):
        return a * b 


    print("Enter the lengths of the sides of the rectangle")

    a, b = int(input()), int(input())

    print(area(a, b))

***input***

    2
    5

***output***

    10

### Вычисление периметра прямоугольника
Функция принимает два значения, равные двум сторонам прямоугольника, возвращает его периметр.

    def perimeter(a, b):
        return (a + b) * 2


    print("Enter the lengths of the sides of the rectangle")

    a, b = int(input()), int(input())

    print(perimeter(a, b))

***input***

    10
    4

***output***

    28

## Окружность

### Вычисление площади окружности
Функция принимает одно значение - радиус окружности, возвращает ее площадь.
Также из бибиолетки **math** берется значение числа ₶.

    import math


    def area(r):
        return math.pi * r * r


    print("Enter the radius of the circle")

    r = int(input())

    print(area(r))

***input***

    6

***output***
 
    113.09733552923255


### Вычисление периметра окружности
Функция принимает одно значение - радиус окружности, возвращает ее периметр.
Также из бибиолетки **math** берется значение числа ₶.

    import math


    def perimeter(r):
        return 2 * math.pi * r

    print("Enter the radius of the circle")

    r = int(input())

    print(perimeter(r))


***input***

    6

***output***

    37.69911184307752


## История изменений проекта
    #Добавлены комментарии в файл cicle.py
    af8de7434b8a0ed15a8335e7da36afe868a56e36 style:added description to the file circle.py
    
    #Добавлены комментарии в файл rectangle.py
    a9961f2e50a3bd93fc8729c9682235fad1dc3ec7 style:added description to the file rectangle.py
    
    #Добавлены комментарии в файл square.py
    a1d8cb613f0ee5b8c89da2de42fe85882b87e0d7 style:added description to the file square.py
    
    #Добавлены комментарии в файл triangle.py
    cb1a1dd7b6c775d9ef5bd8d0c0cb26bc34c6db6b style:added description to the file triangle.py
